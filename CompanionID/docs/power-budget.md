# Power Budget

## Assumptions
- Battery: 600 mAh LiPo.
- MCU deep sleep: 80 uA.
- MCU active (no radio): 35 mA.
- LoRa RX: 12 mA.
- LoRa TX (14 dBm): 120 mA.
- BLE active: 20 mA.
- TFT display (low brightness): 15 mA.
- Regulator overhead: 10%.

## Modes and duty cycles
### Idle (target 7+ days)
- Deep sleep: 95% of time.
- Mesh RX windows: 4 x 1.5s per minute (10%).
- Display off: 100%.
- BLE off.

Estimated average current:
- Sleep: 0.08 mA * 0.95 = 0.076 mA
- Mesh RX: 12 mA * 0.10 = 1.2 mA
- Overhead: 10% => 1.4 mA average

Estimated battery life: 600 mAh / 1.4 mA = ~17.8 days

### Meet mode (short bursts)
- Active + LoRa RX/TX: 100% for up to 5 minutes.
- Average current estimate: 60 mA.
- Energy cost per meet: 60 mA * 0.083 h = 5 mAh.

### Active interaction (display on)
- MCU active, display on, BLE active.
- Average current: 35 + 15 + 20 = 70 mA (plus 10% overhead).

### DIY peripheral
- Add 10-30 mA depending on peripheral.
- Limit peripheral rail to 100 mA total.

## Budget notes
- The idle target relies on short RX windows and minimal display usage.
- Higher LoRa TX power or longer RX windows will reduce battery life.
- Display brightness should be capped in firmware to preserve targets.
