# SOLUTION (cycle-01)

## Summary
Implemented a K10 Arduino TTDB navigator that reads a compact Dice TTDB from the K10 micro SD card and provides list/detail browsing with buttons and tilt gestures. Included a K10-ready TTDB sample.

## Primary artifacts
- `deliverables/cycle-01/k10_ttdb_navigator.ino`
- `deliverables/cycle-01/assets/ttdb_dice_k10.md`

## Usage
1. Copy `deliverables/cycle-01/assets/ttdb_dice_k10.md` to the SD card root as `ttdb_dice_k10.md`.
2. Open `deliverables/cycle-01/k10_ttdb_navigator.ino` in the Arduino IDE.
3. Select the Unihiker K10 board profile and upload.

## Controls
- `Button A`: previous record.
- `Button B`: next record.
- `Button A+B`: toggle list/detail view.
- Tilt left/right: rapid record stepping.
- Tilt forward/back: scroll within detail view.

## Notes
- The sketch uses `SD.begin()` plus `k10.initSDFile()` and expects the TTDB file at `/ttdb_dice_k10.md`.
- The screen palette matches the dark, accented styling from `ttdb_navigator.py`.
