# Integrating Jalara brand assets into JVST

This document records the compatibility audit of `tomylana93/jvst` as of 2026-10-09. It is a **reference**, not an automatic upstream synchronization.

## File mapping

| Jalara source | JVST target | Purpose |
| --- | --- | --- |
| `logo.svg` | `public/logo.svg` | Default icon on light surfaces |
| `logo-dark.svg` | `public/logo-dark.svg` | Default icon on dark surfaces |
| `favicon.svg` | `public/favicon.svg` | Modern browsers |
| `favicon.ico` | `public/favicon.ico` | Fallback favicon |
| `apple-touch-icon.png` | `public/apple-touch-icon.png` | Apple devices |
| `logo-wordmark.svg` | optional new brand-facing asset | Jalara README/header only |
| `logo-wordmark-dark.svg` | optional new dark brand-facing asset | Dark README/header only |

`AppLogoIcon.vue` uses `/logo.svg` and `/logo-dark.svg` when `page.props.brand.logo_url` is absent. `AppLogo.vue` renders that icon next to the configured site name. **Never replace the icon files with the long wordmark**: they are displayed at 32×32px.

`resources/views/app.blade.php` uses `/favicon.ico`, `/favicon.svg` and `/apple-touch-icon.png` unless a favicon is uploaded in Brand Settings. Keep those filenames intact.

The JVST README currently uses the icon in its header. To use a full Jalara wordmark, change that README's `<picture>` source attributes to the wordmark variants after placing those assets in `public/`; no application component changes are required.

## Independence of derived apps

Brand Settings allows uploads of an app-specific logo and favicon. Preserve this override: Jalara art is **only a default**. Derived applications may use completely different names, colors, logos and assets.

Note that the settings uploader accepts raster images: the default artwork in `public/` remains SVG, while a manual upload in Settings should use a PNG export if its SVG upload is rejected. Dynamic logo uploads use one image URL; automatic light/dark source switching is provided for the default artwork only.

## Verification

1. Confirm the two default icons look correct at 32px in sidebar/navigation and light/dark themes.
2. Confirm the configured site name remains alongside the icon without displaying the Jalara wordmark twice.
3. Confirm an uploaded custom logo and favicon override the Jalara defaults.
4. Check browser favicon in SVG-capable and ICO fallback contexts.
5. Check README header if switched to the wide wordmark.
6. Run JVST's existing branding/UI tests before merging an integration PR.

Keep changes to this source brand repository separate from JVST application integration to avoid forcing default-brand changes onto downstream installations.
