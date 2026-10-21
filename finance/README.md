# Capital model and estimate basis

**All Newfoundland estimates are original screening assumptions in constant 2026 CAD.** They are not current market quotations, a valuation, a financing offer, or a bankable feasibility study. The low/high cases represent different scopes and staffing choices, not statistically estimated confidence bounds. Actual needs could exceed the high case.

The editable numerical source is [assumptions.json](assumptions.json). Detailed work packages and commercial reasoning are in the four [company plans](../README.md#four-companies).

## 1. Initial company financing

Millions of Canadian dollars:

| Company | CapEx | Operating and development spending | Working capital | Contingency | Gross initial cash |
| --- | ---: | ---: | ---: | ---: | ---: |
| Wafer Company | 0.40–1.00 | 1.00–2.40 | 0.30–0.70 | 0.30–0.90 | **2.00–5.00** |
| Nanomachines | 0.35–1.05 | 1.15–2.75 | 0.20–0.50 | 0.30–0.70 | **2.00–5.00** |
| Chip Company | 0.08–0.25 | 1.12–2.95 | 0.10–0.30 | 0.20–0.50 | **1.50–4.00** |
| Foundry startup services | 1.60–5.00 | 1.50–4.70 | 0.70–1.80 | 1.20–3.50 | **5.00–15.00** |
| **Four-company arithmetic** | **2.43–7.30** | **4.77–12.80** | **1.30–3.30** | **2.00–5.60** | **10.50–29.00** |

“CapEx” means initial capital equipment and fit-out. “Operating” includes staff, contractors, overhead and development work during the stated runway. “Working capital” means inventory, receivables, spares or a separately identified operating cash buffer; a detailed model must prevent double-counting those buffers with operating runway. “Contingency” is an unallocated reserve and is not automatically profit or spare scope.

These are 18–24 month staffed startup envelopes. They do not fund mines, smelters, an electronic-grade refinery, a wafer fab, an advanced CPU, a DRAM product family, or a production lithography stepper. Founder discovery can begin with a much smaller budget. Stage funding is released when a viable scope and team exist; this is not a recommendation to raise the total immediately.

### What is and is not in the estimates

The initial plans assume leased or contracted facilities and services. Equipment installation and modest fit-out are included in broad allowances, not priced by a vendor. Initial staffing is ramped, especially in the low case. Import duties, shipping, insurance, sales cycles and taxes need explicit treatment in the next budget revision; current broad allowances are not a tax or customs calculation. Recoverable tax timing, financing fees, interest, customer deposits, and exchange exposure are not separately modelled. No land acquisition, major utility extension, or full regulatory application is presumed funded by the startup envelope.

The base model credits **zero uncommitted grants, tax credits, deposits or revenue**. A financing source changes who supplies cash; it does not erase the cost of the project. Repayable support also creates future cash obligations.

## 2. Shared feasibility program

An optional **C$0.25–0.75M over 6–12 months** would pay for customer discovery, technical leadership, independent evidence, resource screening, and initial feasibility work. See [first 90 days](../docs/first-90-days.md). It is separate from the C$10.5–29M arithmetic. If a company has already paid for part of this work, reconcile that overlap rather than count it twice. No shared institution or funding has been established.

## 3. Larger stages

| Possible investment | Screening envelope, CAD2026 | Time from funding/authorization | Boundary |
| --- | ---: | --- | --- |
| Wafer finishing/reclaim | C$15–50M | 2–5 years | Selected service/product range |
| Crystal growth and prime-wafer expansion | C$100–500M | 5–10 years | Specialty program; scale remains to be specified |
| Integrated mine-to-refining-to-wafer program | C$1–5B+ | 10–20+ years | Multiple industrial capabilities and partners |
| One R&D deposition platform | C$8–25M | 3–5 years | Research equipment, not a production stepper |
| Qualified specialty equipment platform | C$30–100M+ | 5–10 years | One product family and its support system |
| Lithography feasibility/demonstrators | C$2–10M | 2–3 years | Does not fund a commercial lithography business |
| Qualified niche ASIC | C$5–20M additional | 2–4 years | A particular product program and qualification |
| Several products or more capable CPU/SoC | C$25–100M+ additional | 4–8 years | A chosen product portfolio; no desktop CPU parity assumed |
| Limited microfabrication pilot | C$50–200M | 4–8 years | Narrow process family; full CMOS not presumed |
| Specialty 150/200 mm fab | C$1–3B | 6–10 years | Rough screening scope; requires process and site engineering |
| Advanced DRAM partnership | C$15–40B+ | 8–15+ years | Separate optional program; excluded from baseline |

**Do not sum this table.** Some stages replace others or reuse their assets, some occur in parallel, and others never happen. Full stepper development is unpriced. Long-term working capital, refresh cycles, technology licenses, ramp losses, financing and infrastructure could materially enlarge a selected program. “+” means there is no meaningful established upper bound. A complete 30-year investment total would be invented before product, process, capacity, and ownership choices exist.

The commercial fab range has especially low confidence. A small specialty facility is not a scaled-down leading-edge DRAM plant; no linear cost-per-wafer extrapolation is justified. Historical primary-source benchmarks are recorded in [research](../research/README.md), retaining their original currency, date and scope.

## 4. Calculations

The startup cash rule is:

`Gross initial financing = equipment/fit-out + operating/development runway + working capital + contingency`

Once contracts and timing exist, build a monthly cash model:

`Closing cash = opening cash + financing received + cash collected - operating payments - capital payments - tax/interest/debt payments`

Financing must cover the lowest cumulative cash point and a separately justified minimum cash reserve. Booked sales are not cash collected. The initial aggregate is deliberately simple because there are no validated sales or construction schedules.

For unit economics, use the appropriate unit:

| Business | Contribution measure | Critical sensitivity |
| --- | --- | --- |
| Wafer services | Net price minus landed wafer, analysis, handling, rejection and freight cost | Rejection rate, customer qualification, inventory turnover |
| Equipment | Selling price minus parts, build labour, installation, warranty and field support | Rework, service travel, utilization of engineers |
| Chip services/products | Project or chip revenue minus direct engineering or landed tested-chip cost | Billable utilization, re-spins, volume, package/test cost |
| Foundry/test | Service or wafer revenue minus variable processing/test cost | Tool utilization, yield, downtime, fixed overhead |

For a chip, compute saleable devices from wafers, gross dies per wafer, electrical yield, packaging yield and final-test yield. Then add mask/NRE amortization and fixed-cost allocation separately. For a wafer fab, avoid treating wafer starts, completed wafers and accepted shipments as interchangeable units.

Illustrative break-even volume is `fixed annual cash cost / contribution per accepted unit`. It omits capital recovery unless explicitly added. A positive contribution margin does not establish that a business recovers its development spending or debt.

## 5. Inflation and foreign currency

Keep the baseline in constant 2026 dollars so scope changes can be compared. An illustrative nominal amount is:

`Nominal amount in year Y = CAD2026 amount × (1 + assumed annual inflation)^(Y - 2026)`

At an **assumed**, not forecast, 2.5% per year, the 2056 multiplier is about 2.10. Specialized equipment, labour, exchange rates and technology prices can behave very differently. This generic multiplier is not a replacement for updated bids.

```bash
python3 scripts/capital_model.py
python3 scripts/capital_model.py --year 2056 --inflation 0.025
```

The script runs from any directory, checks that category totals match the stated initial envelopes, and prints only the four-company sum plus the separate feasibility scope. It intentionally does not total optional later stages.

For a foreign quotation, store the source currency and amount, date, validity, freight/tax scope, an explicitly sourced exchange-rate date, and the resulting CAD amount. This version does not convert the international industrial benchmarks.

## 6. What the next finance revision needs

Replace top-down allowances with a work-breakdown structure, actual headcount ramp and compensation assumptions, facilities bids, commercial tool/PDK access, signed customer milestones, payment terms, import and tax treatment, insurance, capex payment schedules, and a downside case. Keep subsidy applications and awards separate. Obtain independent industrial and finance review before using the model to commit capital.
