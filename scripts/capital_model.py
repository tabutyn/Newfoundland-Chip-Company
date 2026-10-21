#!/usr/bin/env python3
"""Summarize explicit startup assumptions; optional inflation sensitivity.

No network, packages, credentials, or file writes. Values are planning inputs,
not quotations or forecasts. Run from any working directory with Python 3.
"""

import argparse
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path


def inflation_rate(value):
    try:
        rate = Decimal(value)
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError("Inflation must be a decimal, such as 0.025") from exc
    if not rate.is_finite() or not Decimal("-0.5") <= rate <= Decimal("0.5"):
        raise argparse.ArgumentTypeError("Use a finite annual rate from -0.5 to 0.5")
    return rate


def money(value):
    return f"C${value:,.2f}M"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--year", type=int, default=2026, help="Price-level year; default 2026")
    parser.add_argument("--inflation", type=inflation_rate, default=None,
                        help="Required with a future year; e.g. 0.025 for an illustrative 2.5%%")
    args = parser.parse_args()
    data_path = Path(__file__).resolve().parents[1] / "finance" / "assumptions.json"
    data = json.loads(data_path.read_text(encoding="utf-8"), parse_float=Decimal)
    base_year = data["price_basis_year"]
    if not base_year <= args.year <= 2100:
        parser.error(f"Year must be between {base_year} and 2100")
    if args.year != base_year and args.inflation is None:
        parser.error("Supply an explicit --inflation assumption with a future year")
    rate = args.inflation if args.inflation is not None else Decimal("0")
    factor = (Decimal("1") + rate) ** (args.year - base_year)
    totals = [Decimal("0"), Decimal("0")]
    print(f"Newfoundland Computers — original {base_year} CAD startup assumptions")
    print("These are gross cash envelopes, not factory quotes or forecasts.\n")
    if args.year != base_year:
        print(f"Illustrative {args.year} price level at {rate:.2%}/year: factor {factor:.4f}\n")
    for company in data["initial_companies"]:
        calculated = [sum((v[i] for v in company["costs_cad_m"].values()), Decimal("0"))
                      for i in (0, 1)]
        if calculated != company["total_cad_m"]:
            raise ValueError(f"Budget categories do not match stated total for {company['id']}")
        if any(v[0] < 0 or v[1] < v[0] for v in company["costs_cad_m"].values()):
            raise ValueError(f"Invalid budget range for {company['id']}")
        adjusted = [v * factor for v in calculated]
        totals = [totals[i] + adjusted[i] for i in (0, 1)]
        first = company["first_paid_customer_months"]
        print(f"{company['name']}: {money(adjusted[0])}–{money(adjusted[1])}")
        print(f"  First paid customer target: {first[0]}–{first[1]} months after funding")
    print(f"\nCombined four-company initial envelopes: {money(totals[0])}–{money(totals[1])}")
    shared = [Decimal(str(v)) * factor for v in data["shared_feasibility"]["total_cad_m"]]
    print(f"Separate shared feasibility: {money(shared[0])}–{money(shared[1])}")
    print("Do not add feasibility spending twice if it is already in a company budget.")
    print("No uncommitted grants or prospective revenue deducted. First revenue is not profitability.")
    print("Later-stage envelopes are deliberately not totalled: their scopes overlap.")


if __name__ == "__main__":
    main()
