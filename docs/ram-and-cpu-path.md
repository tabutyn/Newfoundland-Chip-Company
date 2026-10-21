# From assembled computers to locally fabricated RAM and CPUs

**Planning basis:** 21 October 2026. This is a proposed capability ladder through 2056, with conditional review windows. It does not predict which memory technology, process node or customer market will be competitive in thirty years.

Newfoundland can build useful computers before it manufactures their silicon. The long-term goal becomes more achievable when each step produces a useful product, a trained team or measured manufacturing knowledge. Progress in computer products and progress in fabrication should be tracked separately: a successful local computer does not prove a local chip process, and a working test chip does not prove a useful computer business.

## 1. Define the milestones honestly

| Review window | Milestone | What may accurately be claimed |
| --- | --- | --- |
| 2026–2031 | Assemble, test and support computers or instruments using purchased chips | Local assembly and support; local board design if performed locally |
| 2028–2036 | Develop FPGA logic, firmware and customer-specific computing systems | Local hardware design running on externally manufactured programmable silicon |
| 2028–2036 | Fabricate a locally designed ASIC, CPU or SRAM test circuit through an outside foundry | Local chip design; wafer fabrication elsewhere, with packaging/test locations disclosed |
| 2031–2046 | Establish a qualified local pilot and fabricate small SRAM or specialty logic | Local device fabrication on specified wafers, with measured capability and limits |
| 2036–2056 | Qualify repeatable local specialty production and complete customer products | Commercial local fabrication only for the qualified process and products |
| 2046–2056 | Assess a dedicated DRAM manufacturing partnership | A separate investment decision; success is conditional and can be declined |

These windows overlap and follow the [roadmap](roadmap.md). They do not remove the development time following each funding decision. Several branches can remain commercially useful without advancing to the next stage.

## 2. Ship useful computers first

The first product should solve a customer problem: for example, an industrial controller or instrument whose reliability, interfaces and support justify its price. These are discovery candidates, not verified market opportunities. Use purchased processors, memory, storage and power components while learning board manufacture, assembly, test, repair and customer support.

The Chip Company owns system architecture, board design, firmware and software integration. The Foundry's early integration unit or qualified outside contractors handle assembly and production testing. Custom enclosures, PCB fabrication and specialist compliance work may remain outsourced. A product needs a maintained bill of materials, approved replacements, programming/calibration records, field diagnostics and an update/support plan.

Assembling a DIMM from purchased packaged DRAM is memory-module manufacturing. It does not manufacture the DRAM dies. That distinction should appear in product provenance and project reporting.

## 3. Learn chip design without buying a fab

An FPGA allows the Chip Company to demonstrate its digital architecture, interfaces and software before committing to a custom chip. It can also remain the final product if volumes do not justify an ASIC. Passing FPGA tests does not prove ASIC timing, power, analog behavior, physical implementation or production yield.

For a first ASIC, select a small function with a paying customer and an affordable verification and test plan. Use a supported external process, its PDK and licensed libraries. CMC's advertised MPW and packaging services are one Canadian access route to investigate; availability, pricing and commercial eligibility require confirmation. [CMC MPW services](https://www.cmc.ca/fab/)

A small CPU can use an open instruction-set architecture such as RISC-V. The ISA is a specification, not a finished processor. Core implementation, peripherals, debug, memory interfaces, firmware and validation remain substantial work, and third-party implementation IP may have separate fees and licences. [RISC-V FAQ](https://riscv.org/about/faq/)

Budget multiple validation steps: simulation and verification, physical-design sign-off, fabricated samples, packaging, laboratory characterization, a possible re-spin and customer qualification. A packaged chip becomes useful only when its board, boot software, programming tools and application operate together.

## 4. Choose SRAM as an early local memory milestone

SRAM and DRAM are both random-access memory, but their circuits and manufacturing needs differ. A conventional SRAM cell stores state in a powered transistor circuit; a manufacturer datasheet provides a concrete six-transistor example. DRAM uses transistor/capacitor cells and refresh. [SRAM example](https://ww1.microchip.com/downloads/en/DeviceDoc/doc7791.pdf) · [Micron DRAM overview](https://www.micron.com/products/memory/dram-components/ddr5-sdram)

A credible first local RAM objective is a modest SRAM array with documented capacity, voltage, access time, operating conditions, test coverage and yield. Begin with test structures and small circuits, then demonstrate repeatability across lots. The team must distinguish one functioning cell, one working die, a qualified device and sustained production.

The local Foundry needs a controlled process and usable PDK; the Chip Company supplies design and test expertise. The Wafer Company supplies substrates only after acceptance, while Nanomachines supports qualified tools and automation. Imported wafers, process equipment or packaging can remain part of this local fabrication milestone.

An open PDK cannot simply be installed as a manufacturing recipe. SKY130's public documentation, for example, marks its open release experimental and warns against assuming production readiness. The selected local process requires its own device characterization, rules, supported design flow and qualification. [SKY130 status](https://skywater-pdk.readthedocs.io/en/main/)

## 5. Separate a research demonstration from a production business

Fabrication needs more than lithography: deposition, pattern transfer, thermal steps, doping, cleaning, inspection, metrology and integrated process control must work together. A laboratory coating tool or mask aligner can support valuable training and research. It does not establish a full CMOS or DRAM line.

Exposure-tool resolution, overlay accuracy and a marketed process-node name are different quantities. Do not infer a chip's capability from a stepper specification alone. Select equipment against a complete process and customer acceptance requirements; see [Nanomachines](../companies/02-nanomachines.md).

The initial **C$10.5–29M** across the four proposed startups funds defined service/design scopes. It does not purchase four factories. The separate **C$50–200M** pilot and **C$1–3B** specialty-fab envelopes are original, low-confidence screening assumptions with different scopes. Commercial operation additionally requires reproducible yield, reliability, enough paid demand, maintainable equipment and funded operating losses during ramp. See the [Foundry plan](../companies/04-foundry.md); these overlapping stages are not an additive total.

## 6. Treat DRAM as a separate strategic decision

By the later review windows, assess whether a specialist memory partner, customer commitments, intellectual-property rights and utilities make dedicated DRAM attractive. Compare cost per good bit, qualification time and continued process investment with buying memory from established suppliers. A small SRAM achievement alone cannot answer those questions.

The **C$15–40B+** advanced-DRAM scenario is an original screening allowance outside the baseline, not a price guarantee. For scale, Micron's 2022 Idaho announcement alone proposed approximately **US$15B** for a leading-edge memory fab beside an established R&D operation. Preserve its historical date, currency and scope when comparing it. [Micron announcement](https://investors.micron.com/news/press-release/2022/Micron-to-Invest-15-Billion-in-New-Idaho-Fab-Bringing-Leading-Edge-Memory-Manufacturing-to-the-US-09-01-2022/default.aspx)

The 2056 outcome should be assessed through saleable products, retained capability, external revenue and reliable employment. Successful local design, equipment, wafer services, assembly, test and specialty fabrication would create a substantial computer industry even if a dedicated DRAM proposal fails its investment gate.
