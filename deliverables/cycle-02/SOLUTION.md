# SOLUTION (cycle-02)

## Summary
Built a desktop configurator that edits K10 TTDB navigator settings, previews list/detail themes, and exports JSON configuration files.

## Primary artifacts
- `deliverables/cycle-02/k10_ttdb_configurator.py`
- `deliverables/cycle-02/assets/k10_nav_config.json`

## How to run
```bash
python3 deliverables/cycle-02/k10_ttdb_configurator.py
```

## What it does
- Edit navigation settings such as wrap columns and list/detail line counts.
- Adjust theme colors with live list/detail previews.
- Load and save JSON config files.

## Config schema (export)
- `storage.ttdb_path`: path on K10 SD card (default `/ttdb_dice_k10.md`)
- `navigation.wrap_cols`: text wrap columns for detail view
- `navigation.max_body_chars`: preview body limit
- `navigation.list_window`: number of list rows visible
- `navigation.detail_lines`: number of detail lines visible
- `theme.background`, `theme.text`, `theme.muted`, `theme.accent`, `theme.accent2`, `theme.select`
