# BLE Provisioning Flow

## GATT services
- **Device Info**: name, firmware version, device ID.
- **Provisioning**: LoRaWAN keys, mesh settings, region.
- **Whitelist**: list management, add/remove.
- **Prompt**: toot-prompt upload.

## Flow
1) User holds button B to enable BLE provisioning for 2 minutes.
2) App connects, reads Device Info, and verifies device ID.
3) App writes provisioning config (region, LoRaWAN join mode).
4) Device validates and stores config in NVS.
5) App confirms completion and disconnects.

## Error recovery
- If write fails, device discards partial config and restores previous state.
- If session times out, device closes BLE and logs the event.

## Safe-mode UX
- Safe-mode is entered by holding A+B during boot.
- BLE provisioning remains available in safe-mode.
- Prompts and DIY peripherals are disabled in safe-mode.
