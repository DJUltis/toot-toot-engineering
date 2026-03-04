# CompanionID Firmware Skeleton

## Tooling
Preferred setup: PlatformIO with VS Code.

## Installation (PlatformIO)
1) Install VS Code.
2) Install the "PlatformIO IDE" extension.
3) Open the repo folder and allow PlatformIO to initialize.
4) Select the XIAO ESP32-S3 target board in `platformio.ini` (to be added).

## Structure
- `platformio.ini`: PlatformIO build configuration.
- `src/main.cpp`: main application entry and task scheduler stub.
- Future: `app/`, `services/`, `drivers/`, `protocols/`.

## Build/run
```
pio run
pio run -t upload
```
