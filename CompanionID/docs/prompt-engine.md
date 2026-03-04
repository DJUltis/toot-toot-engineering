# Prompt Engine (Toot-Prompts)

## Purpose
Allow the owner to add or modify behaviors in a controlled, reversible way, without destabilizing core functions.

## Prompt lifecycle
1) Receive prompt via BLE or mesh.
2) Validate against schema and safety rules.
3) Stage prompt as a draft with a new `prompt_id`.
4) Apply on next idle cycle or by explicit user confirmation.
5) Log applied version and checksum.

## Data model
- `prompt_id` (u32)
- `version` (u16)
- `hash` (u64, truncated SHA-256)
- `source` (ble/mesh)
- `payload` (UTF-8, max 512 bytes)
- `status` (staged/applied/rolled_back)

## Validation rules
- Max payload length: 512 bytes.
- No network keys or secrets allowed in payload.
- Allowed verbs: set_mode, add_timer, add_notification, add_game, add_hook.
- Reject if payload fails to parse or contains unsupported verbs.

## Rollback behavior
- Maintain the last 3 applied prompt versions.
- On failure, revert to last known good version and enter safe-mode indicator.
- Rollback requires no user action but logs an event.

## Safety constraints
- Prompts cannot change radio arbitration policy or security settings.
- Prompts cannot enable peripherals without physical confirmation.
- Prompts are disabled when safe-mode is active.
