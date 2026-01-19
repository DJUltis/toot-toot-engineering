# CompanionID Requirements

## Functional requirements
- FR-01: Support intentional pairing ("Meet") with another CompanionID using physical buttons.
- FR-02: Maintain a local whitelist of trusted nodes with add/remove actions.
- FR-03: Send and receive status updates only from whitelisted nodes.
- FR-04: Provide at least three idle modes (timer, simple game, info sync).
- FR-05: Expose a DIY peripheral interface for basic I2C/GPIO devices.
- FR-06: Provide BLE-based mobile app provisioning and configuration.
- FR-07: Support Meshtastic mesh messaging.
- FR-08: Support LoRaWAN for wide-area updates when provisioned.
- FR-09: Provide local storage of settings and a small event log.
- FR-10: Provide a "toot-prompt" interface for adding new behaviors or configurations.
- FR-11: Provide a radio arbitration policy for shared LoRa access (Meshtastic and LoRaWAN).
- FR-12: Provide a pairing confirmation step on both devices (visual or audio).
- FR-13: Support a two-button fallback UX for minimal hardware builds.
- FR-14: Provide a safe-mode boot (buttons held) to disable peripherals and prompts.

## Non-functional requirements
- NFR-01: Battery life target of at least 7 days in idle with periodic check-ins.
- NFR-02: Pairing and whitelist changes require explicit user action.
- NFR-03: All messages between whitelisted nodes are signed.
- NFR-04: Device must remain usable without cloud access.
- NFR-05: Firmware updates are authenticated (signed OTA).
- NFR-06: Design for low-latency local BLE control within 10 meters.
- NFR-07: Idle power draw target under 1.0 mA average (with scheduled wake).
- NFR-08: Cold boot to usable state within 5 seconds.
- NFR-09: Core functions remain usable without a screen (LED-only variant).

## Constraints
- C-01: Single LoRa radio shared between Meshtastic and LoRaWAN.
- C-02: Operate within regional RF compliance limits.
- C-03: Use an ESP32 variant with BLE and adequate RAM/flash.
- C-04: Buttons must support one-handed use and glove-friendly actuation.
- C-05: External peripherals must be 3.3V logic compatible.
