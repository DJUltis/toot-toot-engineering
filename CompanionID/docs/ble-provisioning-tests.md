# BLE Provisioning Tests

## Scope
Validate provisioning flow, timeouts, and recovery paths using a simple BLE test client.

## Test cases
1) **Happy path**: connect, write config, verify stored values, disconnect.
2) **Timeout**: connect, idle past 2 minutes, ensure BLE closes cleanly.
3) **Partial write**: write region only, disconnect, confirm rollback.
4) **Invalid key**: send malformed LoRaWAN keys, expect rejection.
5) **Safe-mode**: enter safe-mode, verify provisioning still works.

## Tooling
- Mobile app prototype or BLE test client (nRF Connect).

## Installation notes
- Install nRF Connect (mobile) or a BLE client of choice.
- No firmware install required beyond the CompanionID test build.
