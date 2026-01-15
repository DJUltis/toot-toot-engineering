# ANIMATION (Cycle 02)

## Outputs
- `banner-16x9.html` (16:9 cinematic banner)
- `banner-3x1.html` (3:1 cinematic banner)
- `banner.css`, `banner.js`, `banner-data.js` (shared assets)
- `hero-16x9.ppm` and `hero-3x1.ppm` (still frames)
- `assets/toot-toot-logo.png` (logo bug)

## How it works
The HTML files render the STL via a lightweight canvas renderer in JavaScript. The model rotates slowly with soft shading and a gradient background to emulate a cinematic turntable.

## Notes
- The animation is runtime-rendered in the browser. If MP4/GIF exports are needed, record the canvas or use a screen capture tool.
- PPM hero frames are provided as ASCII stills; convert them to PNG using an image tool if desired.
