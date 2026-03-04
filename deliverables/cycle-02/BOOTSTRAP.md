# BOOTSTRAP (cycle-02)

## Prompt interpretation
Cycle-02 executes all prior prompt candidates: define radio arbitration timing and message formats with test vectors, build a per-mode power budget and draft hardware schematic/BOM, specify pairing key exchange with BLE provisioning flow (including safe-mode UX), and formalize the toot-prompt engine (validation, versioning, rollback).

## Inputs
- `deliverables/cycle-01/BOOTSTRAP.md`
- `CompanionID/ESP32_RND_OUTLINE.md`
- `CompanionID/docs/requirements.md`
- `CompanionID/docs/architecture.md`
- `CompanionID/docs/ux-buttons.md`
- `CompanionID/docs/protocols.md`
- `CompanionID/docs/security.md`
- `CompanionID/roadmap.md`

## Proposed team composition
- Bootstrap (this step)
- Storyteller
- Orchestrator
- Core worker
- Reviewer
- Delivery packager
- Retrospective

## High-level objectives for cycle-02
- Produce concrete radio arbitration timing and message formats with test vectors.
- Produce a per-mode power budget and hardware draft (schematic + BOM).
- Define pairing key exchange and BLE provisioning + safe-mode UX.
- Formalize the prompt engine (toot-prompts) with validation and rollback.

## Recommended plan adjustments
- Add explicit deliverables for radio arbitration and message spec.
- Include hardware draft outputs under `CompanionID/hardware/`.
- Add prompt engine doc with validation and rollback behavior.

## Risks and questions
- Radio arbitration timing may conflict with regional duty-cycle limits.
- Power budget depends on display brightness and radio listen windows.
- BLE provisioning must handle interrupted sessions gracefully.

## Suggested next-cycle prompts (choose one)
1) "Cycle-03: Build firmware skeleton with state machines and a minimal test harness for radio arbitration."
2) "Cycle-03: Prototype hardware wiring and update BOM with real part availability and cost ranges."
3) "Cycle-03: Implement a prompt-engine emulator and define acceptance tests for prompt safety."

## Retrospective (cycle-02)
### What to change next cycle
- Add a validation step that checks current draw and payload sizes against real part datasheets.
- Introduce a dedicated "pin map" deliverable before any PCB layout work.
- Expand test planning earlier, especially for BLE disconnect recovery and prompt validation fuzzing.

### Offer to implement
I can apply these recommendations and reset `PLAN.md` with the next-cycle prompt once you choose one of the options below.

### Next-cycle prompt options (choose one)
1) "Cycle-03: Produce a firmware skeleton with state machines, radio arbiter tests, and a pin map for the XIAO ESP32-S3 Sense."
2) "Cycle-03: Validate power budget and payload sizes against datasheets, then refine the schematic with pin mapping."
3) "Cycle-03: Build a BLE provisioning prototype plan with disconnect recovery tests and prompt engine fuzz cases."
