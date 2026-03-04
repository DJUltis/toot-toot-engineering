# BLE Provisioning Prototype

## Goal
Define a minimal working prototype to validate provisioning flow and data storage.

## Prototype steps
1) Enable BLE provisioning on button hold.
2) Advertise a provisioning service with Device Info and Config characteristics.
3) Accept config write for region and LoRaWAN join mode.
4) Persist to NVS and respond with success status.
5) Disconnect and disable BLE after completion.

## Minimal data model
- `region` (enum)
- `lorawan_join` (enum: OTAA/ABP)
- `device_name` (string, optional)

## Installation notes
- Use nRF Connect (mobile) or a BLE test client.
- No custom app required for the prototype phase.
