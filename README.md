<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./logo-wordmark-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./logo-wordmark.svg">
    <img src="./logo-wordmark.svg" alt="Jalara" width="480">
  </picture>
</p>

# Jalara Brand Assets

Official brand assets for **Jalara**, a modern, modular foundation for building simple, purposeful applications.

The artwork contains **no tagline or description**. Jalara has a rounded modular symbol and a custom lowercase geometric wordmark. The official SVGs are self-contained vectors, and the PNGs are generated from those exact masters.

## Four official logo variants

| Variant | SVG | PNG | Background |
| --- | --- | --- | --- |
| Symbol only · light | [`logo.svg`](logo.svg) | [`logo.png`](logo.png) | Light |
| Symbol only · dark | [`logo-dark.svg`](logo-dark.svg) | [`logo-dark.png`](logo-dark.png) | Dark |
| Symbol + wordmark · light | [`logo-wordmark.svg`](logo-wordmark.svg) | [`logo-wordmark.png`](logo-wordmark.png) | Light |
| Symbol + wordmark · dark | [`logo-wordmark-dark.svg`](logo-wordmark-dark.svg) | [`logo-wordmark-dark.png`](logo-wordmark-dark.png) | Dark |

All four PNG logo assets have transparent backgrounds. Use the corresponding light/dark variant rather than CSS filters.

## Automatic dark and light support in GitHub README

The top-of-page logo uses an HTML `<picture>` element with `prefers-color-scheme`, so GitHub can select the matching SVG automatically based on the reader's theme settings. A regular `<img>` is provided as the fallback.

The SVG variants do **not** need to detect the theme internally; the appropriate asset is selected by the browser.

## Favicons and application icons

| Asset | Usage |
| --- | --- |
| [`favicon.svg`](favicon.svg) | Modern browser favicon |
| [`favicon.ico`](favicon.ico) | Fallback 16/32/48 favicon |
| [`favicon-32x32.png`](favicon-32x32.png) | 32px browser favicon |
| [`favicon-192x192.png`](favicon-192x192.png) | PWA icon |
| [`favicon-512x512.png`](favicon-512x512.png) | PWA high-resolution icon |
| [`apple-touch-icon.png`](apple-touch-icon.png) | Apple home-screen icon |
| [`logo-square.png`](logo-square.png) | Square brand avatar |
| [`site.webmanifest`](site.webmanifest) | Web app manifest |

## Reproducible exports

All PNG, ICO, and Apple icon exports are generated from the four master SVG files, not separate recreated artwork:

```bash
python -m pip install -r scripts/requirements.txt
python scripts/export-raster.py
```

The repository workflow automatically regenerates and commits raster assets when a master SVG or the export script changes.

## Guidelines

- [Logo usage](brand/brand-guidelines.md)
- [Color system](brand/colors.md)
- [Typography](brand/typography.md)
- [Brand license](LICENSE.md)
