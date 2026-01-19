# BOOTSTRAP (cycle-01)

## Prompt interpretation
We are starting a multi-cycle project to design and build "CompanionID" from the `CompanionID/` folder. The immediate goal is to turn the existing R&D outline into a complete, actionable plan spanning hardware, firmware, mobile app, and UX, then iterate through cycles to produce working artifacts and documentation for a small ESP32-based device with Meshtastic, LoRaWAN, and mobile connectivity, physical buttons, and DIY peripheral support.

## Inputs
- `README.md` (cycle-01 prompt source)
- `CompanionID/ESP32_RND_OUTLINE.md` (seed R&D outline)

## Proposed team composition
- Bootstrap (this step)
- Storyteller: sharpen product narrative and user story for CompanionID
- Orchestrator: formalize plan, roles, and logging for this cycle
- Core worker: produce the primary CompanionID artifacts (specs, architecture, and initial implementation plan)
- Reviewer: validate feasibility, gaps, and test needs
- Delivery packager: assemble final cycle deliverables and release notes
- Retrospective: improve the process and propose next-cycle changes

## High-level objectives for cycle-01
- Convert the R&D outline into a complete multi-discipline specification.
- Define the core device UX (button map, idle modes, pairing flow).
- Define the connectivity architecture (Meshtastic, LoRaWAN, BLE) and security model.
- Produce a structured repo layout for CompanionID with initial docs and stubs.

## Recommended plan adjustments
- Add `CompanionID/ESP32_RND_OUTLINE.md` to the Inputs list in `PLAN.md` for cycle-01.
- Ensure a dedicated `CompanionID/README.md` is created during Core worker step to scope the project inside the folder.
- Emphasize a "multi-cycle roadmap" output in cycle-01 so later cycles can execute it.

## Risks and questions
- Dual use of a single LoRa radio for Meshtastic and LoRaWAN needs a clear concurrency and scheduling plan.
- Mobile provisioning requirements (BLE + optional cloud) may define early UX constraints.
- Regional RF compliance and certification need early consideration for hardware selection.

## Suggested next-cycle prompts (choose one)
1) "Refine CompanionID by building a full firmware architecture skeleton and message spec for Meet/Whitelist, with test vectors."
2) "Advance CompanionID by producing a complete hardware schematic + BOM draft and enclosure concept, including power budget."
3) "Advance CompanionID by designing the mobile app UX flows and BLE provisioning spec, plus a minimal prototype plan."

## Retrospective (cycle-01)
### What to change next cycle
- Add a dedicated "power budget" step before hardware commitments.
- Include a radio arbitration decision record to de-risk Meshtastic + LoRaWAN sharing.
- Define a minimal test plan earlier, alongside specs.

### Offer to implement
I can apply these recommendations and reset `PLAN.md` with the next-cycle prompt once you choose one of the options below.

### Next-cycle prompt options (choose one)
1) "Cycle-02: Specify radio arbitration timing (slots, guard times, backoff), finalize Meet/Whitelist message formats, and draft test vectors."
2) "Cycle-02: Build a per-mode power budget with duty-cycle assumptions, then draft the hardware schematic and BOM to meet it."
3) "Cycle-02: Define the pairing key exchange format and BLE provisioning flow, plus error recovery and safe-mode UX."
