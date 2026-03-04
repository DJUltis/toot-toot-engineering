# Schematic Refinement Notes

## Purpose
Translate the block-level schematic into a pin-level wiring plan.

## Required inputs
- Finalized pin map (`CompanionID/docs/pin-map.md`).
- XIAO ESP32-S3 Sense pinout.
- SX1262 module pinout.
- ST7735S TFT pinout.

## Refinement steps
1) Assign SPI pins and verify no conflicts with boot pins.
2) Map SX1262 DIO/BUSY pins to interrupt-capable GPIOs.
3) Map TFT control pins and backlight PWM to valid GPIOs.
4) Add button circuits with pull-ups and optional RC debounce.
5) Add I2C header with proper pull-ups.
6) Add battery sense divider and ADC mapping.

## Installation notes
- No software installation required.
- Use a schematic tool of choice (KiCad recommended if needed).
