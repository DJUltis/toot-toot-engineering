# CompanionID Protocols

## Priority model
1) BLE (mobile provisioning and local control)
2) Meshtastic (peer mesh updates)
3) LoRaWAN (wide-area updates)

## Meshtastic integration
- Use Meshtastic protobuf message frames.
- Advertise device ID and capabilities during Meet mode.
- Primary use: local trusted updates with low latency.

## LoRaWAN integration
- Use OTAA or ABP depending on provisioning.
- Payloads are minimized; use for periodic status or alerts.
- Conflicts with Meshtastic are scheduled via a radio arbiter.

## BLE GATT
- Services:
  - Device Info
  - Provisioning (network keys, device name)
  - Whitelist management
  - Prompt channel (toot-prompt input)
- Connection policy: short-lived; disconnect on inactivity.

## Message types (initial)
- `MEET_REQUEST`: pairing initiation
- `MEET_ACCEPT`: pairing acceptance with key exchange
- `STATUS_UPDATE`: battery, idle mode state
- `PING`: request for status
- `PROMPT_UPDATE`: prompt payload for new behavior

## Radio arbitration
- Time-slice radio access between Meshtastic and LoRaWAN.
- Prefer Meshtastic during active Meet and whitelist sync.
- Prefer LoRaWAN during scheduled check-ins.
