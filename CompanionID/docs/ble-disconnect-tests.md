# BLE Disconnect Recovery Tests

## Goal
Verify the device recovers gracefully from BLE disconnects during provisioning.

## Test cases
1) Disconnect during Device Info read; device should keep BLE active until timeout.
2) Disconnect during config write; device should rollback to previous config.
3) Disconnect immediately after config write; device should persist if checksum passes.
4) Reconnect within 30 seconds; device should resume provisioning.
5) Reconnect after timeout; device should require a new provisioning session.

## Success criteria
- No partial or corrupted config stored.
- Clean log entries for all disconnect events.

## Installation notes
- Use nRF Connect or a BLE test app with manual disconnect control.
