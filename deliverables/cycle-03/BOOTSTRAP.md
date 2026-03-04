# BOOTSTRAP (cycle-03)

## Prompt interpretation
Cycle-03 executes all prompts together: deliver a firmware skeleton with a minimal test harness for radio arbitration, produce a pin map for the XIAO ESP32-S3 Sense, validate power and payload constraints against datasheets, refine the schematic with pin mapping guidance, and define BLE provisioning tests plus prompt engine fuzz cases (including installation steps where needed).

## Inputs
- `deliverables/cycle-02/BOOTSTRAP.md`
- `CompanionID/ESP32_RND_OUTLINE.md`
- `CompanionID/docs/requirements.md`
- `CompanionID/docs/architecture.md`
- `CompanionID/docs/ux-buttons.md`
- `CompanionID/docs/protocols.md`
- `CompanionID/docs/security.md`
- `CompanionID/docs/radio-arbitration.md`
- `CompanionID/docs/message-spec.md`
- `CompanionID/docs/power-budget.md`
- `CompanionID/docs/prompt-engine.md`
- `CompanionID/docs/pairing-key-exchange.md`
- `CompanionID/docs/ble-provisioning.md`
- `CompanionID/hardware/schematic/SCHEMATIC.md`
- `CompanionID/hardware/bom/BOM.md`
- `CompanionID/roadmap.md`

## Proposed team composition
- Bootstrap (this step)
- Storyteller
- Orchestrator
- Core worker
- Reviewer
- Delivery packager
- Retrospective

## High-level objectives for cycle-03
- Produce a firmware skeleton and minimal arbiter test harness.
- Create a pin map and schematic refinement notes for wiring.
- Validate power and payload assumptions against datasheets.
- Define BLE provisioning test plan and prompt fuzzing plan.

## Recommended plan adjustments
- Add installation/setup notes to firmware and test plan docs.
- Include pin map and schematic refinement as explicit deliverables.

## Risks and questions
- Actual pin availability may require rework once XIAO pin map is finalized.
- Datasheet current draw may be higher than estimates, reducing battery life.

## Suggested next-cycle prompts (choose one)
1) "Cycle-04: Build a hardware prototype wiring guide and validate pin map on a breadboard."
2) "Cycle-04: Implement BLE provisioning in firmware with automated test scripts."
3) "Cycle-04: Create a minimal prompt-engine emulator and integration tests."

## Retrospective (cycle-03)
### What to change next cycle
- Require pin-map validation against official pinout before wiring tasks.
- Add a minimal build config (`platformio.ini`) when firmware skeletons are introduced.
- Define a standard test harness tool (Python + pytest or embedded Unity) for repeatability.

### Offer to implement
I can apply these recommendations and reset `PLAN.md` with the next-cycle prompt once you choose one of the options below.

### Next-cycle prompt options (choose one)
1) "Cycle-04: Validate the XIAO ESP32-S3 Sense pin map and add a platformio.ini with build instructions."
2) "Cycle-04: Implement a basic radio arbiter test harness and timing measurement plan."
3) "Cycle-04: Prototype BLE provisioning interactions and automate disconnect recovery tests."
