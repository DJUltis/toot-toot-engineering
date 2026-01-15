# SVG_ENGINEER

## SVG strengths
- Vector layering supports dense industrial detail without raster artifacts.
- SMIL or CSS animations can create looping motion with minimal overhead.
- Symbols and `<use>` enable reuse for gears, bolts, pipes, and plaques.

## SVG constraints
- Overuse of filters/blur can hurt performance; keep filter count low.
- Large path counts can bloat file size; reuse symbols and simplify shapes.
- SMIL support is strong in modern browsers but should be kept simple.

## Proposed structure
- Root `viewBox` sized for a wide cinematic ratio (e.g., 1600x600).
- Layer groups: `bg-hall`, `mid-gears`, `mid-press`, `fg-text`, `fx-glow`.
- Define gradients and reusable symbols in `<defs>`.

## Animation plan (storyboard note)
- Molten streams: slow vertical translate + subtle opacity shimmer (6–10s loop).
- Gears: rotate using CSS keyframes at staggered speeds (20–60s loop).
- Memory plates: brief glow pulse synced to gear rotation (8–12s loop).
- Furnace light: low-frequency flicker using opacity modulation (5–7s loop).

## Performance guidance
- Prefer simple shapes and strokes; limit filter usage to a single glow.
- Use `vector-effect="non-scaling-stroke"` only when needed to keep strokes consistent.
- Keep animation durations long for calm motion and lower CPU usage.

## Logo integration
- Embed a small Toot Toot Engineering logo as a companion mark near the foreground plaque, or include as a discrete corner stamp. Use `toot-toot-logo.svg` as a reference.

## Deliverable expectation
- Primary animated mural at `deliverables/cycle-01/assets/time-foundry.svg` with inline CSS animations.
