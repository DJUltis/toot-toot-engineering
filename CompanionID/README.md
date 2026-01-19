# CompanionID

CompanionID is a small ESP32-based companion device that forms trusted micro-communities via mesh and low-power radios, provides calm idle utilities, and supports DIY peripherals. This folder is the working project space for the multi-cycle build.

## Goals
- Trusted "Meet" pairing and a local whitelist for private updates.
- Idle modes that are useful and companionable (timers, games, transit updates).
- Multi-protocol connectivity: Meshtastic, LoRaWAN, and BLE mobile app.
- A simple DIY expansion interface for peripherals.
- Growth via toot-prompts without losing stability or user trust.

## Scope (cycle-01)
- Convert the R&D outline into full requirements and architecture docs.
- Define UX, button mapping, and pairing flows.
- Define connectivity, message types, and security model.
- Produce a multi-cycle roadmap.

## Key docs
- `ESP32_RND_OUTLINE.md`
- `docs/requirements.md`
- `docs/architecture.md`
- `docs/ux-buttons.md`
- `docs/protocols.md`
- `docs/security.md`
- `roadmap.md`

## Project principles
- Pairing is deliberate and opt-in.
- Idle behavior is calm, not intrusive.
- DIY peripherals are easy and safe.
- Connectivity prioritizes local trust over remote services.
