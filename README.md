<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo-wordmark-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="logo-wordmark.svg">
    <img src="logo-wordmark.svg" alt="Jalara" width="382">
  </picture>
</p>

# Jalara Brand Assets

**Jalara** is a modern, modular foundation for building simple, purposeful applications.

This repository contains the official Jalara visual identity. All logo variants are free of taglines or descriptive text. The master artwork is SVG and uses only vector paths: no embedded fonts, external images, or gradients.

## Logo variants

| Asset | Composition | Background | Use |
| --- | --- | --- | --- |
| [`logo.svg`](logo.svg) | Symbol only | Light | Default app icon and compact navigation |
| [`logo-dark.svg`](logo-dark.svg) | Symbol only | Dark | Dark-mode app icon |
| [`logo-wordmark.svg`](logo-wordmark.svg) | Symbol + `jalara` | Light | README, website headers, documentation |
| [`logo-wordmark-dark.svg`](logo-wordmark-dark.svg) | Symbol + `jalara` | Dark | Dark-mode headers and documents |

Use the light/dark variants with the matching background. The wordmark is outlined rather than rendered using an installed font.

## Other assets

| Asset | Purpose |
| --- | --- |
| `favicon.svg`, `favicon.ico` | Browser favicons |
| `favicon-32x32.png` | Legacy 32px favicon |
| `favicon-192x192.png`, `favicon-512x512.png` | PWA manifest icons |
| `apple-touch-icon.png` | Apple home-screen icon |
| `logo.png` | 512px transparent raster of the light symbol |
| `site.webmanifest` | Web app metadata |

Prefer SVG wherever supported. Additional PNG variants (`logo-dark.png`, `logo-wordmark.png`, `logo-wordmark-dark.png` and `logo-square.png`) can be generated locally using:

```bash
python -m pip install -r scripts/requirements.txt
python scripts/export-raster.py
```

The raster exports are derived from the canonical committed SVG artwork; no font files or raster source masters are required. The generated filenames are compatible with usage in JVST.

## Integration with JVST

The [JVST foundation](https://github.com/tomylana93/jvst) intentionally renders a compact icon and the configured application name separately. Retain that separation: map `logo.svg` and `logo-dark.svg` to the matching files in `jvst/public/` and use the wordmark files only for brand-facing material. Do not insert the wordmark inside `AppLogoIcon.vue` or it will render at icon size.

See [`brand/jvst-integration.md`](brand/jvst-integration.md) for the complete integration checklist. The JVST application also supports an app-specific custom logo through Brand Settings: its logo upload must continue to take precedence over default Jalara artwork.

## Visual identity documentation

- [Logo and usage guidelines](brand/brand-guidelines.md)
- [Colors](brand/colors.md)
- [Typography](brand/typography.md)
- [License](LICENSE.md)

Jalara is the brand; JVST is the repository where the foundation currently runs. Derived applications may have their own distinct brand identity.
