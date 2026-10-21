# Initial work backlog

These are proposed tasks, not assigned work or evidence of commitments. Every owner is **unassigned** until a person agrees to take it. Start with the tasks that change a funding or product decision; several can proceed in parallel. Use the [templates](../templates/company-plan.md) and [contribution guide](../CONTRIBUTING.md), and relate investment decisions to [roadmap gates G0–G5](roadmap.md).

## Blocker 1 — Accountable people and evidence that customers will pay

| ID | Task | Owner role, unassigned | Deliverable / acceptance | Dependency |
| --- | --- | --- | --- | --- |
| B01 | Recruit business and technical leads | Project convenor | A role roster for each company with an agreed accountable founder and experienced reviewer, or an explicit vacancy; no implied appointments | None |
| B02 | Define the memory and computer milestones | Memory/process engineer | A reviewed capability table separating module assembly, externally fabricated designs, embedded SRAM, standalone memory and DRAM; acceptance criteria state where fabrication occurs | None |
| B03 | Test the wafer company's first offer | Materials sales lead | At least ten relevant buyer interviews, written acceptance requirements, delivered-cost alternatives and two credible paid-pilot prospects, or a stop decision | None |
| B04 | Test equipment-service demand | Equipment commercial lead | At least ten relevant buyer interviews, supported tool families, service geography and two credible paid-pilot prospects; quantify travel/support constraints | None |
| B05 | Test chip-design and FPGA demand | Semiconductor commercial lead | At least ten relevant buyer interviews, one narrow offer, accessible implementation path and two credible paid-pilot prospects | B02 |
| B06 | Test foundry/test/module demand | Test and packaging commercial lead | At least ten relevant buyer interviews comparing local test/assembly with outside providers; two credible paid-pilot prospects and clear exclusions | B02 |

## Blocker 2 — The local material and facility premises are unverified

| ID | Task | Owner role, unassigned | Deliverable / acceptance | Dependency |
| --- | --- | --- | --- | --- |
| B07 | Resolve the Grey River claim and access rights | Qualified geoscientist | Dated source/location record distinguishing quartz occurrence from resource/reserve; tenure and sampling-access status; remaining gaps | None |
| B08 | Design a representative feedstock study | Geoscientist and analytical specialist | Authorized sampling plan, independent laboratory scope, customer impurity requirements and cost comparison against imported inputs; no suitability claim before results | B03, B07 |
| B09 | Verify existing local equipment and facilities | Facilities engineer | Current asset/access inventory with condition, owner, availability, restrictions and written access status; flag historical web listings | B01 |
| B10 | Screen sites and utility service | Industrial facilities lead | Shortlist matched to proposed process demand; power quality/capacity, water, waste, freight and expansion gaps; distinguish enquiry from firm utility commitment | Relevant B03–B06, B09 |
| B11 | Map permitting and community work | Environmental and community lead | Scope-specific approvals pathway, rights/community engagement plan, studies, lead-time assumptions and accountable professional reviewers | B07 or B10, as applicable |

## Blocker 3 — A product must have a lawful and supportable delivery path

| ID | Task | Owner role, unassigned | Deliverable / acceptance | Dependency |
| --- | --- | --- | --- | --- |
| B12 | Map process, design and publication rights | IP counsel with technical lead | Rights matrix for proposed IP, PDKs, software, process transfer and tool changes; permitted MIT contributions separated from third-party restrictions | Relevant B03–B06 |
| B13 | Compare suppliers and international partners | Procurement and partnerships lead | At least two feasible routes per critical input where available; lead time, support, import/export requirements and single-source risks; no implied agreements | Relevant B03–B06, B12 |
| B14 | Cost workforce and training | Operations and workforce lead | Staged roles and hiring-cost assumptions validated by practitioner input; training/access proposals and a plan for experienced supervision | B01, B09, B13 |
| B15 | Build offer-specific unit economics | Finance lead with delivery engineer | Price, direct cost, fixed cost, yield/rework, warranty, cash collection and break-even sensitivity for each chosen offer; no duplicated costs | Relevant B03–B06, B13, B14 |

## Blocker 4 — Release capital only for a bounded, reviewable next step

| ID | Task | Owner role, unassigned | Deliverable / acceptance | Dependency |
| --- | --- | --- | --- | --- |
| B16 | Replace rough budgets with quoted scopes | Project estimator | Dated CapEx, runway, working-capital and contingency model; supplier quotes where possible; exclusions and overlapping stages resolved; repository summaries agree | B15; B10–B14 as applicable |
| B17 | Test the financing structure | Business-development and finance lead | Sources-and-uses case, equity/debt/grant assumptions, cash-timing downside and funder criteria; unapproved support contributes zero committed cash | B15, B16 |
| B18 | Scope paid pilots and obtain an investment decision | Each company founder | Pilot deliverables, price, acceptance, rights and payment terms; G0 decision record approving a bounded scope, more discovery or a stop | B01; relevant customer task; B12–B17 for the selected scope |
| B19 | Specify an affordable computer demonstrator | Chip systems engineer | FPGA or standard-component design brief with testable function, cost ceiling, procurement route and honest local-content label; fabrication claims match actual work | B02, B05, B12, B13 |
| B20 | Publish the first evidence review | Repository maintainer and independent reviewer | Decision records identify changed assumptions, results, failed premises, budget revisions and next owners; no gate advances without its evidence | B01 and the completed tasks being reviewed |

Dependencies identify required inputs, not an obligation to fund every task. For example, discovery can stop a manufacturing branch before site studies, and a service startup need not wait for a computer demonstrator. Company plans may set stronger customer targets than the minimum G0 threshold.

Keep completed task evidence in a focused pull request or decision record. Do not publish confidential interviews, private contact details, restricted designs or quotations without permission. A task listed here does not imply that outreach, spending or a commercial commitment has already occurred.
