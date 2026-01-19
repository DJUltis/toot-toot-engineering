# CompanionID Architecture

## System overview
CompanionID is built as a modular firmware stack on an ESP32-class MCU with a shared LoRa radio, BLE for mobile provisioning, and optional Wi-Fi for updates. Core services expose a stable message bus for pairing, whitelist sync, idle modes, and peripheral data.

## Hardware blocks
- MCU: ESP32-S3 or ESP32-C6.
- LoRa radio: SX1262 (shared for Meshtastic and LoRaWAN).
- Power: LiPo + charger + fuel gauge (optional).
- UX: 2-4 buttons, LED (or small OLED), optional buzzer.
- DIY port: I2C + GPIO + 3.3V rail.

## Firmware layers
1) **HAL/Drivers**: GPIO, I2C, SPI, radio, BLE, power management.
2) **Core services**: pairing, whitelist manager, message router, scheduler, radio arbiter.
3) **Protocols**: Meshtastic, LoRaWAN, BLE GATT.
4) **Features**: idle modes, prompt engine, peripheral host, diagnostics.
5) **UX**: button state machine, LED/buzzer feedback patterns.

## Data flow
- Pairing flow enters a "Meet" state via button combo.
- Devices exchange IDs and capabilities via local radio channel.
- Whitelist manager stores peer info and keys in NVS.
- Message router signs and routes updates to the appropriate protocol.
- Prompt updates arrive over BLE or mesh, are validated, and then staged for apply.

## State machines (high-level)
- **Idle**: low-power, periodic beacon and content cycle.
- **Meet**: time-bounded pairing window; accepts one candidate at a time.
- **Active**: high-frequency updates (short duration) after user action.
- **DIY**: peripheral detected; driver loads from manifest.
- **Safe mode**: boot with prompts and peripherals disabled.

## Power states
- **Deep sleep**: wake on button or scheduled radio check-in.
- **Listen window**: short radio receive burst for mesh updates.
- **Active**: pairing, provisioning, or DIY interaction.

## Storage
- NVS: device keys, whitelist, user settings.
- Flash log: rolling event log (pairings, updates, idle events).

## OTA and update flow
- Signed firmware bundles.
- Staged update over BLE or Wi-Fi; apply on next boot.
