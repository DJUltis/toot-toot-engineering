# CompanionID Schematic Draft

## Blocks
- **MCU**: Seeed Studio XIAO ESP32-S3 Sense.
- **Radio**: SX1262 module via SPI (shared bus).
- **Display**: 0.96" TFT SPI, IC ST7735S.
- **Power**: USB-C LiPo charger module + 1-cell LiPo.
- **Buttons**: 4 tactile switches with pull-ups.
- **DIY Port**: I2C (SDA/SCL), GPIO, 3.3V, GND.

## Key connections
- SPI bus shared between SX1262 and ST7735S.
  - MOSI/MISO/SCK from XIAO.
  - Separate CS lines for radio and display.
  - Separate reset lines.
- Radio DIO pins to GPIO interrupts.
- Buttons to GPIO with internal pull-ups; optional RC debounce.
- Display backlight via PWM GPIO.
- I2C port with 4.7k pull-ups on SDA/SCL.

## Power notes
- LiPo charger provides 3.3V rail or feeds XIAO VIN.
- Battery voltage sense to ADC for fuel gauge.
- Power switch or load switch optional for peripherals.
