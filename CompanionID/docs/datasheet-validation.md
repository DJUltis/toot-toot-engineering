# Datasheet Validation Plan

## Goal
Verify power budget and payload limits against actual part datasheets for XIAO ESP32-S3 Sense, SX1262, and ST7735S display.

## Power validation checklist
- XIAO ESP32-S3 Sense active current at 240 MHz and 80 MHz.
- XIAO deep-sleep current with RTC memory retention.
- SX1262 RX/TX currents at target TX power.
- ST7735S display current at low/medium/high brightness.
- USB-C charger quiescent current.

## Payload validation checklist
- LoRaWAN max payload by region and data rate.
- Meshtastic typical frame size and overhead.
- Ed25519 signature size impact on payload budget.

## Procedure
1) Capture datasheet values and cite page numbers.
2) Update `CompanionID/docs/power-budget.md` with measured or datasheet values.
3) Update `CompanionID/docs/message-spec.md` if payload limits require truncation.

## Installation notes
- No software installation required; only datasheets and a spreadsheet.
- If bench measurements are performed, use a USB power meter or inline current meter.
