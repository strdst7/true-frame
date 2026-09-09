# Trueframe

[![GitHub Pages](https://github.com/strdst7/true-frame/actions/workflows/pages.yml/badge.svg)](https://github.com/strdst7/true-frame/actions/workflows/pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-c4522a.svg)](LICENSE)

Trueframe is a free, browser-based image studio for making AI-generated images feel more photographic. It includes six practical tools for repairing synthetic-looking skin, enlarging images, creating film-inspired grades, composing prompts, and processing complete batches.

**[Open the live app](https://strdst7.github.io/true-frame/)**

## Features

- **Skin Fix** — reduce plastic-looking skin and restore texture, clarity, warmth, and natural contrast.
- **Upscaler** — enlarge images with adjustable sharpening and detail enhancement.
- **Presets** — apply ready-made photographic and cinematic color treatments.
- **Grade Lab** — build, save, and reuse custom color looks.
- **Prompt Studio** — compose production-ready prompts for Midjourney, DALL·E, Stable Diffusion, Flux, and other image generators.
- **Batch processing** — apply a fix, preset, or custom look to multiple images and download the results as a ZIP.
- **Interactive comparisons** — inspect before-and-after results with draggable comparison controls and a detail loupe.

## Privacy first

Image processing happens locally using browser APIs and canvas operations. Photos are not uploaded to a server, and no account is required. Saved looks and prompt history remain in the browser's local storage.

## Run locally

Clone the repository and serve the app directory with any static web server:

```bash
git clone https://github.com/strdst7/true-frame.git
cd "true-frame/true frame/realis"
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000).

The deployed app is a self-contained static page, so there are no runtime dependencies, package installs, accounts, or API keys.

## Project structure

```text
.
├── .github/workflows/pages.yml   # GitHub Pages deployment
├── true frame/
│   ├── realis/
│   │   ├── index.html            # Deployable application
│   │   ├── template.html         # Source template
│   │   ├── build.py              # Embeds optimized images into the template
│   │   ├── assets/               # Source images
│   │   └── web/                  # Web-optimized images
│   └── uploads/                  # Original uploaded source material
└── LICENSE
```

## Rebuild the standalone page

The build script embeds the files from `web/` into `template.html` as data URLs and writes the result to `index.html`:

```bash
cd "true frame/realis"
python3 build.py
```

Commit changes to `main` to trigger the GitHub Pages workflow. The workflow publishes `true frame/realis/` as the root of the site.

## Browser support

Use a current version of Chrome, Edge, Firefox, or Safari. Processing speed and maximum export size depend on the device, available memory, browser canvas limits, and source-image dimensions.

## License

Released under the [MIT License](LICENSE).
