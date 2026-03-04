# Pin Map (Validated)

## Status
Validation pending; requires official XIAO ESP32-S3 Sense pinout before wiring.

## Pin assignments
Use the same assignments as `CompanionID/docs/pin-map.md`, but confirm each GPIO is:
- not a strapping pin conflict,
- available on the board edge,
- compatible with SPI/I2C use.

## Validation steps
- Capture the official pinout reference (PDF or datasheet).
- Confirm SPI pins for shared radio + display.
- Confirm DIO/BUSY pins map to interrupt-capable GPIOs.
- Confirm PWM-capable pin for display backlight.
- Confirm ADC pin for battery sense.
- Confirm button pins do not conflict with boot or USB functions.
