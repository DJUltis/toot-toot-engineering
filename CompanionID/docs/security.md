# CompanionID Security

## Identity and keys
- Each device has a unique keypair generated at provisioning.
- Device ID is derived from the public key hash.
- Keys stored in NVS with readout disabled where possible.
- Optional derived session keys per peer for short-lived encryption.

## Pairing and whitelist
- Meet mode uses a short-lived pairing window.
- Devices exchange signed Meet messages, challenge-response, and confirm user action.
- Whitelist entries include device ID, public key, and last-seen timestamp.
- Pairing window uses a 5-minute TTL with cooldown to deter spam.

## Message integrity
- All whitelist messages are signed.
- Optional encryption for sensitive payloads (future cycle).
- Reject messages with stale nonce or repeated sequence values.

## OTA updates
- Firmware images are signed and verified before apply.
- Rollback protection via version monotonic counter.

## Threat model summary
- Mitigate spoofed devices via signature verification.
- Mitigate replay attacks via nonce/sequence in messages.
- Rate-limit pairing attempts to prevent battery drain.
- Safe-mode boot allows recovery from faulty prompts or peripherals.
