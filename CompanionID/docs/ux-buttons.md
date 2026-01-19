# CompanionID UX and Buttons

## Button model
Assume 3 buttons: A, B, C. (Can scale to 2 or 4 if needed.)

## Core actions
- **Tap A**: cycle idle mode.
- **Hold A (2s)**: start/stop current idle function (timer, game).
- **Tap B**: show status (LED pattern or OLED screen).
- **Hold B (2s)**: enter Meet mode (pairing window).
- **Tap C**: quick "ping" whitelist members (status request).
- **Hold C (2s)**: open DIY peripheral menu (if connected).
- **A+B hold (3s)**: toggle silent mode.
- **B+C hold (5s)**: factory reset (confirm with LED pattern).

## Feedback patterns
- **Meet mode**: slow pulse + short chirp on successful pair.
- **Whitelist update**: double blink + short buzz.
- **Low battery**: triple blink every 10 minutes.
- **DIY detected**: steady glow for 3 seconds.

## Idle mode examples
- Timer: simple countdown with chime on completion.
- Companion game: low-frequency reaction game.
- Transit: periodic status check from mobile app or LoRaWAN.

## Accessibility
- Provide tactile differentiators on buttons (shape or spacing).
- Keep long-press timings consistent across all actions.
