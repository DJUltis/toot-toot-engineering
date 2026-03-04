# Pin Map (Draft)

## Target board
Seeed Studio XIAO ESP32-S3 Sense.

## Pin assignments (proposed)
Note: confirm against official pinout before wiring.

### SPI (shared)
- SCK: GPIO6
- MOSI: GPIO7
- MISO: GPIO8

### SX1262 (LoRa)
- CS: GPIO3
- RESET: GPIO2
- DIO1: GPIO4
- BUSY: GPIO5

### ST7735S TFT
- CS: GPIO9
- DC: GPIO10
- RST: GPIO11
- BL (PWM): GPIO12

### Buttons
- Button A: GPIO13
- Button B: GPIO14
- Button C: GPIO15
- Button D: GPIO16

### I2C DIY
- SDA: GPIO17
- SCL: GPIO18

### Power sense
- VBAT_SENSE: GPIO1 (ADC)

## Notes
- If any pins are unavailable, prioritize radio pins first, then display, then buttons.
- Confirm pin availability for XIAO ESP32-S3 Sense before PCB layout.
