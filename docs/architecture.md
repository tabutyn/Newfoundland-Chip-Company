# Industrial architecture

**Status:** Proposed system design, 21 October 2026. Interface requirements below are a framework for contracts and technical work; numerical specifications must come from the selected product and customer.

## 1. Keep four companies, with independent business cases

The original four-company structure covers materials, equipment, design, and manufacturing. Its main economic risk is circular dependence: a wafer company needs the foundry, the foundry needs the chip company, and the equipment company needs all three. That creates four speculative customers instead of external demand.

The proposed architecture breaks this dependence. Each company must qualify for customers outside the local group. It may initially import inputs or outsource manufacturing. Internal transactions use written specifications, market comparisons, and transfer prices that allow the economics of each company to be assessed independently.

| Function | Responsible proposed company | Initial outside dependency | Local capability to consider later |
| --- | --- | --- | --- |
| Geological resource assessment and source traceability | Wafer Company, using qualified mineral specialists | Accredited analytical laboratories and specialist process trials | A qualified local feedstock, only if competitive |
| Electronic-grade polysilicon and single-crystal substrates | Wafer Company | Established qualified suppliers | Selected finishing, crystal growth, and eventually refining |
| Vacuum, deposition, handling, and equipment controls | Nanomachines | OEM parts, calibration, specialist materials | Service, a narrow tool platform, and qualified subsystems |
| Chip architecture, RTL, verification, physical design | Chip Company | EDA tools, licensed IP, foundry PDK and external fabrication | A growing design and verification team |
| Process integration, cleanroom operation, yield | Foundry | External process-transfer partner and equipment vendors | A specific pilot or specialty process |
| Photomasks and mask inspection | Foundry procurement with Chip Company sign-off | Qualified mask supplier | Remains an external service unless a separate case emerges |
| Wafer probe, dicing, die assembly, packaging, final test | Foundry and qualified outsourced assembly/test partners | Specialist packaging and reliability houses | In-house steps justified by volume and margin |
| Board design, firmware, operating software, customer product | Chip Company | Components, PCB manufacture, software ecosystems | Locally designed systems and selected CPUs |
| Board/module/computer assembly, test, repair | Foundry's integration unit or contract partners | External packaged chips and components | Local production and field support |
| Financing, site infrastructure, community agreements | Each legal business; shared coordination as needed | Investors, lenders, utilities, municipalities, rights holders | Commercial agreements rather than assumed access |

Each company can be independently owned, financed, relocated, or discontinued without revoking the open plans. A future jointly owned facility needs explicit ownership and access agreements; the repository itself owns no industrial assets.

## 2. Define interfaces before purchasing assets

### Wafer Company to Foundry or external customer

A wafer catalogue must define material, diameter, crystal orientation, dopant type, resistivity range and uniformity, thickness and total thickness variation, bow/warp, surface finish, particles, metal contamination, defect specifications, packaging, and certificate of analysis. Grade must distinguish prime device wafers, monitor/test wafers, and reclaimed wafers. The customer approves incoming inspection methods, sampling, lot genealogy, and change notification.

The initial ambition is silicon, not silicone. Boron-doped p-type silicon is one possible specification. A customer's chosen process may require a different substrate. Industry manufacturing descriptions provide the technical context; this list is a proposed purchasing interface, not a complete wafer standard. See the [Wafer Company plan](../companies/01-wafer-company.md) and its sources.

### Nanomachines to a manufacturing customer

A purchase specification must identify the application and substrate, process uniformity and repeatability, contamination limits, throughput, uptime, consumables, utilities, exhaust and abatement interface, calibration, safety review, training, documentation, spares, and service response. Acceptance requires installation qualification and agreed process demonstrations on the customer's material. A successful laboratory demonstration does not constitute a production warranty.

Nanomachines should be free to sell to other sectors and existing laboratories. The Foundry should be free to buy a proven outside tool when that best meets its process needs.

### Chip Company to Foundry

Select an actual supported process before physical design. The package of deliverables includes a versioned PDK, design rules, device models, standard-cell and memory libraries with usable licenses, DRC/LVS reports, extraction and timing results, corner coverage, manufacturability review, layout database, mask conventions, test structures, and wafer/package test plans. Responsibility for each sign-off and re-spin must be written down.

An open source PDK can be useful for education and prototyping, but its exact release and permitted production use must be checked. The [SKY130 documentation](https://skywater-pdk.readthedocs.io/en/main/) explicitly describes the open release as experimental and unsuitable for production settings. Do not infer production qualification from a public repository or from a nominal process-node label.

### Foundry to packaging, test, and systems

Manufacturing output is a traceable lot with measured electrical results, wafer maps, known-good-die criteria where applicable, handling requirements, package requirements, test coverage, reliability evidence, and disposition of failures. System assembly also needs PCB/BOM revisions, firmware provenance, programming and calibration steps, component authenticity controls, repair procedures, and customer acceptance records.

This is how an internally fabricated die becomes a usable product. A cleanroom alone does not supply these capabilities.

## 3. Use outside manufacturing while building local competence

The Chip Company can send approved designs to an external foundry and obtain packaging/test services. CMC describes commercial-foundry MPW and dedicated runs with packaging support, making it a relevant access route to investigate rather than a promised partnership. [CMC MPW services](https://www.cmc.ca/fab/).

The same principle applies elsewhere: use imported qualified wafers to test the equipment business; use existing deposition tools to qualify a material; use an external lab for impurity analysis. The purpose is to isolate technical uncertainty so the outcome of one experiment can be understood.

## 4. Site architecture

Do not require the mine, chemical refining plant, precision equipment workshop, design office, and cleanroom to share one site. Their infrastructure, workforce, environmental footprint, and logistics needs differ. Grey River is a proposed feedstock investigation area, not a selected fab location.

Compare sites using [local feasibility](local-feasibility.md). For a fab, power quality, reliable water and waste treatment, maintainability, workforce, transport, and the cost of downtime may dominate proximity to quartz. A shared campus is an option only after these requirements are quantified.

## 5. Track capability and value creation

For each shipped product, record where it was designed, where its silicon wafer originated, where devices were fabricated, where it was packaged and tested, and where the system was assembled. Report Newfoundland payroll, supplier spending, retained IP rights, export revenue, recurring customer orders, and paid apprenticeships separately. Do not double-count intercompany sales as new external revenue.

Examples of honest product descriptions are “designed and assembled in Newfoundland using imported chips” and “devices fabricated in Newfoundland on imported wafers.” A later product may meet more of the local-manufacturing goals, but the label should follow the evidence.

## 6. Architecture decisions to revisit

- Which first customer problem gives each company a defensible reason to exist?
- Is the wafer opportunity distribution, reclaimed test wafers, specialty prime wafers, crystal growth, polysilicon, or crucible quartz? These are different businesses.
- Does an industrial customer need a custom chip at all, or does an available microcontroller/FPGA solve the problem better?
- Which packaging and test work can be profitable at realistic regional and export volumes?
- What process can an experienced partner transfer, and what customers will buy that output?
- What ownership, publication, and manufacturing rights can actually be obtained?

Record substantial changes using the [decision template](../templates/decision-record.md). Preserve rejected alternatives and the evidence that caused the rejection.
