# Prompt Engine Fuzz Tests

## Scope
Validate prompt parsing, schema enforcement, and rollback behavior under malformed inputs.

## Fuzz cases
1) Oversized payloads (513-2048 bytes).
2) Invalid UTF-8 sequences.
3) Unsupported verbs (e.g., `set_radio_power`).
4) Missing required fields.
5) Repeated prompt_id with different payload hash.
6) Rapid prompt bursts (10 in 2 seconds).

## Expected behavior
- Reject invalid prompts without applying.
- Log a validation failure event.
- Trigger rollback only if a prompt was applied and later fails.

## Tooling
- Simple script to send randomized payloads over BLE or mesh.

## Installation notes
- If using Python for fuzzing:
  - Install Python 3.10+.
  - `pip install bleak` (BLE) or use an existing mesh injection tool.
