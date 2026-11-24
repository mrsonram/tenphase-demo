# TENPHASE — VILLAIN Interactive Experience & Design System Demo

Interactive web pitch experience and Thai Gothic design system built for **TENPHASE**, showcasing the **VILLAIN** music video visual direction alongside the official **TΣNPHASE - Topic** catalog.

## Included Chapters & Highlights

- **Chapter I — Hero & Live MV Stage:** Fullscreen YouTube IFrame API background integration for **VILLAIN** (`o7zS0_cbOlo`) paired with live film-grain fallback controls.
- **Chapter II — Interactive Key Visual Altar:** Interactive composition breakdown, before/after comparison curtain, and lighting mood lenses.
- **Chapter III — VILLAIN Sound Forge & Quote Card Studio:** Multi-stem Web Audio / FX pad mixer, synchronized lyric structure explorer, and exportable `1080×1920` PNG Quote Card generator.
- **Chapter IV — Archive Turntable & 3D Cover Lightbox:** Mechanical vinyl deck playing all 12 official **TΣNPHASE - Topic** tracks, featuring pixel-locked dynamic groove-tracking tonearm, `33⅓ / 45 RPM` speed toggle, draggable sleeve switcher, and a 3D Cover Artwork Lightbox with `2.2×` optical magnifier loupe and `180°` embossed liner-note flip.
- **Chapter V — Credits & Fan Pre-Save Pass:** Official channel links and interactive digital collector pass.
- **Design System Tab:** Complete token specification, typography specimen, WCAG contrast tester, Experience Map, and exportable CSS / YouTube integration snippets.

## Local Development

Run the local static server (required for YouTube embeds over HTTP):

```bash
./start-demo.sh
# or directly:
python3 serve.py
```

The server binds `127.0.0.1` across ports `4173..4185` (default **`http://localhost:4173`**) and sends `Referrer-Policy: strict-origin-when-cross-origin` headers for embedded YouTube playback.

## GitHub Pages

`index.html` and the `assets/` directory are pure static files and work directly when published with GitHub Pages from the `main` branch root (`/`).
