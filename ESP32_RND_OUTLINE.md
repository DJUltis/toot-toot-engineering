# ESP32 Multi-Protocol Companion Device - R&D Outline

## Scope summary
Small ESP32-based hardware device with multiple connectivity options (Meshtastic, mobile app, LoRaWAN), physical buttons for core functions, and a DIY prototyping interface.

Core functions:
1) "Meet" other units to whitelist and send/receive updates within the list.
2) Idle functions: companion games, utility timers, transit updates, etc.
3) DIY peripheral platform for simple add-ons.
4) Dynamic interaction with the owner using toot-prompts for feature growth.

---

## Proposed repository file system
```
/
  README.md
  docs/
    overview.md
    requirements.md
    ux-buttons.md
    protocols.md
    security.md
    power.md
    manufacturing.md
    compliance.md
    threat-model.md
    user-guides/
  hardware/
    schematic/
    pcb/
    bom/
    mechanical/
    enclosure/
  firmware/
    platformio.ini
    src/
      main.cpp
      app/
      services/
      drivers/
      protocols/
      storage/
    include/
    test/
  mobile/
    app/
    common/
  cloud/
    api/
    functions/
  tools/
    flashing/
    provisioning/
    logging/
  assets/
    ui/
    branding/
  manufacturing/
    test-jigs/
    instructions/
  release/
  archive/
```

---

## R&D outline

### 1) Hardware definition
- MCU: ESP32-S3 or ESP32-C6 (evaluate BLE, Wi-Fi, RAM/flash needs).
- Radios: Meshtastic (LoRa via SX1262), LoRaWAN stack (same radio), BLE for mobile app.
- Power: LiPo + charger, deep sleep, wake-on-button, wake-on-radio.
- Buttons: 2-4 physical buttons + optional long-press combos.
- I/O for DIY: I2C/GPIO header, 3.3V rail, simple expansion port.
- UX: LED or small OLED for status; buzzer optional.

### 2) Connectivity and protocol plan
- Meshtastic: leverage existing protobuf messaging and node discovery.
- LoRaWAN: separate network join credentials, optional cloud integration.
- Mobile app: BLE GATT for provisioning, whitelist management, prompts.
- Conflict model: priority and fallback (BLE > LoRaWAN > Meshtastic).

### 3) "Meet" and whitelist flow
- Meet mode: button combo enters pairing; exchange device IDs + capabilities.
- Whitelist: stored locally with TTL + manual delete.
- Sync: periodic status updates, low-power beacons, user-approved joins.
- Abuse controls: rate limiting, signed messages, optional PIN entry.

### 4) Idle functions and content engine
- Core idle modes: egg timer, simple games, transit info sync.
- Content engine: lightweight scheduler with plugin-style modules.
- Local storage: ring buffer for events, settings in NVS.

### 5) DIY peripherals
- Standardized peripheral class: I2C sensors, simple GPIO triggers.
- Peripheral manifest: ID, power budget, data schema, update interval.
- Safety: max current, brownout detection, periph sandbox.

### 6) Toot-prompt interaction
- Prompt interface: BLE + optional cloud sync.
- Prompt parser: convert textual prompts into configuration or task bundles.
- Versioning: store changes as reversible diffs with audit log.

### 7) Firmware architecture
- Event loop: task scheduler + radio queue + UX handler.
- Protocol adapters: Meshtastic, LoRaWAN, BLE.
- Storage: NVS for config, flash for logs.
- OTA: Wi-Fi or BLE staging, signed updates.

### 8) Mobile app outline
- Provisioning: set device name, network keys, whitelist.
- Control: idle mode settings, logs, prompt creation.
- Sync: cloud optional, direct BLE always available.

### 9) Security model
- Device identity: unique keypair per unit.
- Pairing: ephemeral challenge during meet mode.
- Message signing: signed updates for whitelist members.
- Factory reset: physical button sequence.

### 10) Power, reliability, and test
- Power budget targets per mode.
- Battery life estimates by usage profile.
- Integration tests: radio interoperability, pairing, OTA.
- Field testing: mesh density, LoRaWAN coverage, BLE range.

### 11) Risks and unknowns
- Dual use of LoRa radio for Meshtastic + LoRaWAN.
- App provisioning UX complexity.
- Regulatory constraints for RF regions.
- Firmware complexity vs. battery life.

---

## Early milestones (suggested)
1) Breadboard proof: ESP32 + SX1262 + two buttons + LED status.
2) Mesh pairing demo: whitelist handshake + local status update.
3) BLE provisioning demo: mobile app sets name + whitelist.
4) Idle mode module: egg timer + buzzer + screen.
5) DIY header: I2C sensor reporting via mesh.
