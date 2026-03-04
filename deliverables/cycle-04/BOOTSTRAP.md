# BOOTSTRAP (cycle-04)

## Prompt interpretation
Cycle-04 executes all options together: validate the XIAO ESP32-S3 Sense pin map and add a `platformio.ini` build config, define a radio arbiter test harness and timing measurement plan, and prototype BLE provisioning interactions with automated disconnect recovery tests.

## Inputs
- `deliverables/cycle-03/BOOTSTRAP.md`
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
- `CompanionID/docs/pin-map.md`
- `CompanionID/docs/datasheet-validation.md`
- `CompanionID/docs/schematic-refinement.md`
- `CompanionID/docs/ble-provisioning-tests.md`
- `CompanionID/docs/prompt-fuzz-tests.md`
- `CompanionID/firmware/README.md`
- `CompanionID/firmware/src/main.cpp`
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

## High-level objectives for cycle-04
- Validate the pin map and produce a validated pin mapping file.
- Add a minimal `platformio.ini` for firmware builds.
- Define a radio arbiter timing test harness plan.
- Define BLE provisioning prototype steps and automated disconnect tests.

## Recommended plan adjustments
- Include a validated pin map deliverable distinct from the draft.
- Add explicit test harness documentation with measurement guidance.

## Risks and questions
- Pin validation needs an authoritative pinout reference.
- PlatformIO board configuration may need custom settings for the XIAO S3 Sense.

## Suggested next-cycle prompts (choose one)
1) "Cycle-05: Implement the radio arbiter test harness with timing instrumentation."
2) "Cycle-05: Validate BLE provisioning on hardware and document edge cases."
3) "Cycle-05: Begin integrating the display and buttons into the firmware skeleton."

## Retrospective (cycle-04)
### What to change next cycle
- Require pinout validation evidence (reference link or captured table) before declaring pin map complete.
- Add a minimal firmware build verification step once `platformio.ini` exists.
- Expand BLE tests to include repeated reconnect attempts and throughput limits.

### Offer to implement
I can apply these recommendations and reset `PLAN.md` with the next-cycle prompt once you choose one of the options below.

### Next-cycle prompt options (choose one)
1) "Cycle-05: Verify pin map against official XIAO ESP32-S3 Sense pinout and update the schematic accordingly."
2) "Cycle-05: Implement a minimal firmware build and add arbiter timing instrumentation."
3) "Cycle-05: Build a BLE provisioning test harness with automated reconnect and timeout scenarios."
