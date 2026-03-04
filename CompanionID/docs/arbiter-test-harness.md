# Radio Arbiter Test Harness

## Goal
Measure radio slot timing accuracy and verify arbitration policy behavior under load.

## Test harness outline
- Implement a scheduler stub that emits GPIO pulses at slot boundaries.
- Log timestamps to serial for each slot start/stop.
- Inject synthetic mesh/LoRa queues to trigger preemption rules.

## Measurements
- Slot start jitter (target < 20 ms).
- Guard time adherence (target >= 150 ms).
- Preemption latency (Meet mode should preempt within one slot).

## Tooling
- Logic analyzer or oscilloscope for GPIO timing.
- Serial logger for timestamp capture.

## Installation notes
- Install PlatformIO (see `CompanionID/firmware/README.md`).
- If using a logic analyzer, install the vendor capture software.
