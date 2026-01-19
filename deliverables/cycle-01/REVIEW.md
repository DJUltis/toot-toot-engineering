# REVIEW (cycle-01)

## Findings (ordered by severity)
1) **Protocol concurrency risk**: Shared LoRa radio for Meshtastic and LoRaWAN now has a policy, but still lacks concrete timing parameters and a conflict test plan. (See `CompanionID/docs/protocols.md`)
2) **Power budget gap**: Targets are defined, but no per-mode power budget or estimated duty cycle exists. (See `CompanionID/docs/requirements.md`)
3) **Security detail gap**: Pairing and replay protections are outlined, but key exchange format and nonce/sequence encoding need specification. (See `CompanionID/docs/security.md`)
4) **UX validation**: Two-button fallback is defined, but needs confirmation against hardware constraints and LED-only UX. (See `CompanionID/docs/ux-buttons.md`)

## Tests and validation gaps
- No integration test plan for mesh pairing + whitelist sync.
- No BLE provisioning flow validation or error recovery strategy.
- No LoRaWAN join retry/backoff parameters defined.

## Overall status
Acceptable for cycle-01 documentation, but the above gaps should be addressed in cycle-02 before hardware commitments.
