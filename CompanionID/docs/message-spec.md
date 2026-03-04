# Message Specification

## Transport
- Used across Meshtastic and LoRaWAN payloads.
- Payloads should remain under 128 bytes when possible.

## Common header (all messages)
- `version` (1 byte): protocol version.
- `msg_type` (1 byte): enum.
- `device_id` (8 bytes): first 8 bytes of public key hash.
- `seq` (4 bytes): monotonic counter per peer.
- `nonce` (8 bytes): random per message.
- `ttl` (2 bytes): seconds to live.

## Message types
### MEET_REQUEST (0x01)
- `caps` (2 bytes): capability bitfield.
- `ephemeral_pub` (32 bytes): X25519 public key.

### MEET_ACCEPT (0x02)
- `caps` (2 bytes)
- `ephemeral_pub` (32 bytes)
- `confirm` (1 byte): 0x01 for accepted.

### STATUS_UPDATE (0x03)
- `battery_pct` (1 byte)
- `mode` (1 byte): idle/meet/active/diy.
- `signal` (1 byte): RSSI bucket.

### PING (0x04)
- no extra fields

### PROMPT_UPDATE (0x05)
- `prompt_id` (4 bytes)
- `prompt_hash` (8 bytes)
- `payload_len` (2 bytes)
- `payload` (variable, UTF-8)

## Signing
- Sign `header + payload` using Ed25519.
- `signature` appended (64 bytes) where transport permits.
- For LoRaWAN uplinks where size is constrained, send signature only for high-trust messages (Meet/Whitelist).

## Test vectors (illustrative)
### MEET_REQUEST
- version: 0x01
- msg_type: 0x01
- device_id: 0xA1A2A3A4A5A6A7A8
- seq: 0x0000002A
- nonce: 0x0102030405060708
- ttl: 0x012C (300s)
- caps: 0x0007
- ephemeral_pub: 0xE0...E1 (32 bytes)

### STATUS_UPDATE
- version: 0x01
- msg_type: 0x03
- device_id: 0xB1B2B3B4B5B6B7B8
- seq: 0x00000010
- nonce: 0x1112131415161718
- ttl: 0x003C (60s)
- battery_pct: 0x64
- mode: 0x00
- signal: 0x03
