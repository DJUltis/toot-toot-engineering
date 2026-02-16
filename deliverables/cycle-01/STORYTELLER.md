# STORYTELLER (cycle-01)

## Narrative focus
The K10 becomes a palm-sized TTDB globe: a quiet, glowing archive that you tilt and click to traverse coordinates like constellations. The interface should feel like a pocket observatory: dark canvas, warm highlights, and calm motion.

## UX beats
- **Arrival:** The first screen shows the TTDB name and a highlighted node, inviting the user to step into the record list.
- **Navigation:** Buttons step through records with an audible/visual rhythm; tilt gestures accelerate movement and let you skim.
- **Discovery:** Each record opens with a bold header color and a short preview, emphasizing the “node on a globe” feeling.

## Visual tone (adapted from `ttdb_navigator.py`)
- Background: deep charcoal (`#0f0f12` / `#111318`).
- Primary text: soft white (`#e9e9f0`).
- Accents: warm gold (`#ffd166`), orange (`#f4a261`), and cool blue (`#7cc7ff`) for selection and edges.

## Interaction mapping
- `Button A`: previous record.
- `Button B`: next record.
- `Button A+B`: toggle between list and detail view.
- Tilt left/right: rapid record stepping.
- Tilt forward/back: scroll within the current record preview.
