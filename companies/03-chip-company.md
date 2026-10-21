# Newfoundland Chip Company

**Status:** proposed company; open concept plan, not an incorporated business or a funded project.  
**Planning basis:** 21 October 2026; all original estimates in constant 2026 Canadian dollars.  
**Mission:** design useful processors, memory circuits and computing products in Newfoundland, earn export revenue, and build the design capability that a future local foundry can serve.

## 1. Start with a business that can earn money before a local fab exists

The recommended first business is a small **fabless design and engineering company**: it designs chips but buys wafer fabrication from an established foundry. Begin with paid FPGA, digital-design, verification, embedded-computing and test-development projects. Develop a narrow proprietary or openly licensed product only after a customer identifies a costly problem and pays for a feasibility phase.

Potential customer segments to investigate are ocean instrumentation, industrial sensing, robotics, energy monitoring and long-life embedded systems. These are hypotheses, not evidence of customers or sufficient demand. Seek customers outside Newfoundland from the first year. A local address alone is not a competitive advantage; lower customer integration cost, dependable support, product lifetime and a measurable technical benefit must justify buying.

CMC Microsystems already advertises multi-project-wafer (MPW), dedicated fabrication and packaging services through commercial foundries. An MPW shares a wafer run across designs, allowing a prototype without financing an entire fab. Request current commercial access terms, pricing, export requirements and delivery dates; none is assumed in this plan. [C01: CMC MPW services](https://www.cmc.ca/fab/)

## 2. Define the products precisely

| Product or capability | What it means | Proposed position |
| --- | --- | --- |
| FPGA implementation | A design running on an already manufactured programmable chip | First paid prototypes and customer demonstrations |
| ASIC | An application-specific integrated circuit; a product category, not a design program | A small customer-funded controller or interface after prototype validation |
| CPU | A processor architecture implemented as circuits, with software and verification | Start with a small embedded processor or licensed core; a competitive desktop CPU is a separate large program |
| SRAM | Static memory, often used inside a chip; a common cell uses six transistors and retains state while powered without DRAM-style refresh | First meaningful memory-design milestone: a small SRAM test macro or qualified SRAM integrated in an ASIC |
| DRAM | Dense dynamic memory based on transistor/capacitor cells and refresh | Separate process, IP and manufacturing partnership; not obtained merely by sending an SRAM or CPU layout to a general CMOS line |
| DIMM or memory module | A circuit board populated with packaged memory chips and supporting components | Can be designed and assembled locally using imported chips; label this honestly as module assembly |
| Complete computer | Processor, memory, board, power, interconnects, enclosure, firmware and software | A system product can precede local chip fabrication by many years |

For a concrete commercial example of six-transistor SRAM cells, see [C05: Microchip-hosted AT65609EHW datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/doc7791.pdf). Micron describes DDR5 as DRAM and identifies its transistor/capacitor memory cells. [C04: Micron DDR5 technical overview](https://www.micron.com/products/memory/dram-components/ddr5-sdram)

The design flow uses electronic-design-automation software (EDA/CAD), a foundry process-design kit (PDK), circuit libraries, verification, physical design, fabrication sign-off and a test plan. Each process has its own rules and device models. Moving a design to Newfoundland Foundry would require an approved PDK and requalification; ownership of the layout does not make it portable to any equipment line.

RISC-V is a useful candidate for an open processor instruction set. Its specification is not a finished CPU: a core, peripherals, memory interfaces, physical implementation and software still need to be built or licensed. RISC-V International explicitly distinguishes its free ISA from other implementation IP that may carry fees. [C02: RISC-V FAQ](https://riscv.org/about/faq/)

## 3. Capital, staffing and time

These are original, broad planning assumptions, not quotations or a valuation. The low case uses a narrow scope, a ramped team and outside specialists; the high case funds more verification, paid tools and a larger first design. No grant, customer deposit or revenue is deducted from the required cash.

| Stage | Cash required for that stage | Time from that stage's authorization | Deliverable and gate |
| --- | ---: | --- | --- |
| First financing: engineering and prototype business | **C$1.5–4.0M** | 18–24 months of funded work; first paid service delivery targeted at 6–12 months | Paying customers, FPGA prototype and one small MPW design if justified |
| Qualified niche ASIC product | **C$5–20M additional** | 2–4 years for product development and qualification; may overlap service activity | Repeatable production, test coverage, accepted customer product, funded inventory and support |
| Several products or a more capable CPU/SoC | **C$25–100M+ additional** | 4–8 years from a specific product program | Only proceed with proven distribution, technical advantage and finance for multiple revisions |
| Discrete DRAM or a competitive high-end CPU | **Not budgeted in the baseline** | Partner- and process-dependent | Commission a separate business and technology-transfer case; no 2056 competitiveness promise |

The first service sale, a working prototype, qualified production and profitability are different milestones. A prototype can fail and require another wafer run. Calendar targets in the wider 2026–2056 roadmap move if a gate is delayed. The table is not a 30-year funding total and alternative product paths should not be added together mechanically.

### First financing breakdown

| Use of cash over 18–24 months | Low, C$M | High, C$M | Classification |
| --- | ---: | ---: | --- |
| Ramped payroll, contractors and benefits | 0.85 | 2.10 | Operating expense |
| Workstations, FPGA boards and lab instruments | 0.08 | 0.25 | Capital expenditure |
| EDA/cloud access and engineering subscriptions | 0.04 | 0.15 | Operating expense |
| MPW fabrication, packaging, evaluation and revision reserve | 0.15 | 0.50 | Development expense |
| Sales, travel, insurance, accounting and IP contracts | 0.08 | 0.20 | Operating expense |
| Customer receivables and initial inventory cash buffer | 0.10 | 0.30 | Working capital |
| Unallocated contingency | 0.20 | 0.50 | Reserve |
| **Total first financing** | **1.50** | **4.00** | **Gross cash need** |

Start with a founder/business lead, an experienced chip-design lead, digital/verification engineers and a firmware/test engineer. Use specialist physical-design and analog contractors where economical. A ramp to roughly 6–10 people by the end of this stage is a staffing hypothesis; the low-case payroll assumes fewer people for much of the period. Recruit at least one person who has personally delivered working silicon to customers. The initial team is not large enough to develop a contemporary general-purpose CPU, DRAM process and commercial EDA stack simultaneously.

## 4. How the business earns revenue

Use paid discovery, fixed-scope engineering milestones, integration support and recurring product sales. Contract terms must identify acceptance criteria, change control, IP ownership, rights to publish and liability. Open reference designs can attract adopters while paid engineering, customization, tested hardware, support and manufacturing coordination create revenue.

**Illustrative service economics, assumptions only:** a C$150,000 project requiring 900 engineering hours at a fully loaded direct cost of C$90/hour, plus C$15,000 of tools and outside services, has C$96,000 of direct cost and C$54,000 of gross contribution (36%). It still has to cover non-project staff, sales, rent, idle time, warranty and taxes. Do not count the same engineering payroll again when constructing overhead.

**Illustrative product economics, assumptions only:** selling 100,000 chips at C$12 with a fully landed and tested variable cost of C$4 produces C$800,000 of gross contribution before ongoing fixed costs. Recovering C$5M of development spending would require at least 625,000 such sales before fixed operating costs or finance charges. This is a sensitivity example, not a sales forecast. Die size, wafer price, yield, packaging, test time, scrap, returns and customer volume must replace these invented inputs.

A useful early success can be a profitable engineering company. Productizing an ASIC is optional until customer volume supports the development cost.

## 5. Design and release gates

| Gate | Evidence required | Pause or stop when |
| --- | --- | --- |
| Service launch | At least two unrelated prospective buyers with explicit problems; one paid engagement or a credible contracted path to one | Interviews produce enthusiasm but no paid need |
| FPGA prototype | Customer acceptance against written performance, power and interface requirements | The customer can buy an existing part that solves the problem more cheaply |
| MPW commitment | Approved PDK/tool versions; licensed IP; verification plan; DRC/LVS/sign-off; package/test plan; revision cash | Tool/PDK access, required IP or testability is unresolved |
| Production commitment | Measured silicon results across required conditions; reliability qualification; production supply and test agreements; volume case | Prototype success is treated as evidence of production yield or lifetime |
| Local-foundry migration | Foundry-supported PDK, qualified devices, packaging/test path, accepted customer samples and a second-source strategy | Migration would sacrifice customer reliability just to meet a local-content target |

Open tools and PDKs help learning, but availability does not establish production readiness. As retrieved for this plan, the open SKY130 documentation calls its release experimental and says it is not intended for production use. Obtain the actual foundry's written supported flow before committing a commercial product. [C03: SKY130 current-status documentation](https://skywater-pdk.readthedocs.io/en/main/)

## 6. Responsibilities inside the four-company landscape

The Chip Company owns product requirements, architecture, design verification, firmware, reference boards and customer support. Newfoundland Foundry can initially provide board/module assembly coordination, test and selected packaging services; outside specialists provide services that neither company has qualified. Newfoundland Nanomachines can supply test automation and later qualified process equipment. Newfoundland Wafer Company can become a substrate supplier only against the foundry's acceptance specification.

The companies should negotiate ordinary contracts with one another and retain external suppliers and customers. None should need all four to succeed before its first invoice. The Chip Company must not become the only assumed customer underwriting a billion-dollar fab.

## 7. First 90 days and first year

**First 90 days:** appoint the business and silicon leads; interview at least 20 potential paying customers across three segments; document competing products and reasons to buy; ask for commercial EDA/PDK/MPW/packaging quotations; scope one paid FPGA project; select one demonstrator whose entire test strategy is affordable. Record the evidence and revise the budget before hiring the full team.

**Months 4–12:** deliver the first paid projects, measure project contribution and repeat business, publish an original open reference design where customer contracts permit, and build a reproducible verification flow. Authorize a tape-out only after the gate above. If service sales do not support continued hiring, narrow the offering or stop product development before committing further fabrication cash.

## 8. What a credible 2056 outcome looks like

A meaningful outcome is a Newfoundland-based company exporting chip designs and embedded systems, with some designs fabricated locally and others through international partners. A small functional SRAM array fabricated in Newfoundland would count as a locally fabricated RAM-chip milestone. It would not establish competitive commodity DRAM density, cost or scale. Keep that distinction visible in every roadmap revision.

Original material in this plan follows the repository's MIT licence. Third-party PDKs, CPU cores, EDA software, standards, patents and customer information retain their own terms; link to them instead of copying restricted material into this repository.
