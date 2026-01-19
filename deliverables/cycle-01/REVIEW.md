# REVIEW (cycle-01)

## Findings (ordered by severity)
1) **Protocol concurrency risk**: Shared LoRa radio for Meshtastic and LoRaWAN lacks a concrete arbitration algorithm and timing model. This is a major integration risk. A scheduling policy and test plan are required. (See `CompanionID/docs/protocols.md`)
2) **Security detail gap**: Pairing flow does not yet define nonce/sequence formats, key exchange method, or replay protection specifics. This is required for implementation. (See `CompanionID/docs/security.md`)
3) **Power budget missing**: Battery life targets are stated, but no power budget or sleep strategy exists. This can derail feasibility. (See `CompanionID/docs/requirements.md`)
4) **UX confirmation**: The three-button mapping is proposed but not validated against two-button hardware fallback or an OLED-less variant. Needs a fallback matrix. (See `CompanionID/docs/ux-buttons.md`)

## Tests and validation gaps
- No integration test plan for mesh pairing + whitelist sync.
- No BLE provisioning flow validation or error recovery strategy.
- No LoRaWAN join retry/backoff parameters defined.

## Overall status
Acceptable for cycle-01 documentation, but the above gaps should be addressed in cycle-02 before hardware commitments.
