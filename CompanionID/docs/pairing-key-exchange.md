# Pairing Key Exchange

## Identity
- Long-term identity: Ed25519 keypair per device.
- Device ID: first 8 bytes of SHA-256(public key).

## Meet handshake (X25519 + HKDF)
1) **MEET_REQUEST**:
   - Includes device ID, caps, and ephemeral X25519 public key.
   - Signed with Ed25519.
2) **MEET_ACCEPT**:
   - Includes device ID, caps, and ephemeral X25519 public key.
   - Signed with Ed25519.
3) **Shared secret**:
   - Both sides compute ECDH(X25519) and derive session keys using HKDF-SHA256.
4) **Confirm**:
   - Each side sends a short confirm message encrypted with the derived session key.

## Replay protection
- `seq` must increase per peer; reject stale values.
- `nonce` must be unique within a rolling window (store last 32 nonces per peer).

## Key usage
- Session key used for encrypting sensitive Meet/Whitelist messages.
- Long-term keys used only for signatures.

## Failure handling
- If confirm fails, discard session keys and leave Meet mode.
- Re-enter Meet only after a 30-second cooldown.
