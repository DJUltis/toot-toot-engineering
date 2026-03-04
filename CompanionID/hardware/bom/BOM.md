# CompanionID BOM Draft

## Core components
- Seeed Studio XIAO ESP32-S3 Sense (pre-soldered).
- SX1262 LoRa module (SPI).
- 0.96" TFT SPI display (ST7735S controller).
- USB-C LiPo charger module (1-cell, 500-1000 mA).
- LiPo battery 600 mAh (3.7V).

## Buttons and passives
- 4x tactile switches (through-hole or SMD).
- 4x 10k pull-up resistors (if not using internal pull-ups).
- 2x 4.7k I2C pull-up resistors.
- 1x 0.1 uF decoupling per power rail.

## Connectors
- 1x I2C/GPIO header (4-6 pins).
- 1x battery connector (JST-PH 2-pin).

## Optional
- Piezo buzzer (3.3V).
- Power switch or load switch IC for peripherals.
