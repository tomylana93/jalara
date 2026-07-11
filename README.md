# Jalara Brand Assets

This repository contains the official visual identity assets for **Jalara**, a modular application foundation designed to be flexible, modern, and organized.

> **Jalara — One foundation, many possibilities.**

## Brand Philosophy

The name **Jalara** represents interconnected parts working in harmony within a single system. This philosophy aligns with a modular monolith approach: each module has a clear responsibility while remaining part of one consistent application foundation.

Jalara is built around four principles:

- **Modular** — each capability can be developed as a focused and independent part of the system.
- **Flexible** — the platform can adapt to different product and business requirements.
- **Modern** — the technology and user experience are designed to remain relevant and efficient.
- **Organized** — clear structure, consistency, and responsibility boundaries guide development.

## Asset Structure

```text
.
├── README.md
├── LICENSE.md
├── brand/
│   ├── brand-guidelines.md
│   ├── colors.md
│   └── typography.md
├── favicon-32x32.png
├── favicon-192x192.png
├── favicon-512x512.png
├── favicon.ico
├── logo.png
├── logo.svg
├── logo-dark.png
├── logo-dark.svg
└── logo-square.png
```

## Asset Index

| File | Intended use |
|---|---|
| `logo.svg` | Primary logo for light backgrounds. Preferred for websites and digital interfaces. |
| `logo.png` | Transparent raster version of the primary logo. |
| `logo-dark.svg` | Logo variant for dark backgrounds. |
| `logo-dark.png` | Transparent raster version of the dark-mode logo. |
| `logo-square.png` | Square composition for profiles, social media, and promotional material. |
| `favicon.ico` | Broadly compatible browser favicon. |
| `favicon-32x32.png` | Standard small favicon. |
| `favicon-192x192.png` | Web application and Android icon. |
| `favicon-512x512.png` | High-resolution icon for PWAs and digital distribution. |

## Quick Usage

### HTML

```html
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/svg+xml" href="/logo.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" href="/favicon-192x192.png">
```

### Vue

```vue
<img
    src="/brand/logo.svg"
    alt="Jalara"
    class="h-10 w-auto"
>
```

Use `logo-dark.svg` on dark surfaces. Do not invert the primary logo with CSS filters because the result will not match the official dark-mode variant.

## Basic Rules

- Prefer SVG for digital use.
- Use the logo variant with the clearest contrast against its background.
- Preserve the original aspect ratio and surrounding clear space.
- Do not alter the logo's colors, shapes, gradients, proportions, or orientation.
- Do not add shadows, outlines, glow, bevels, or textures.
- Do not place the logo over visually busy or low-contrast backgrounds.

Full documentation:

- [`brand/brand-guidelines.md`](brand/brand-guidelines.md)
- [`brand/colors.md`](brand/colors.md)
- [`brand/typography.md`](brand/typography.md)
- [`LICENSE.md`](LICENSE.md)

## License and Usage

All Jalara names, logos, icons, and visual identity elements remain the property of the brand owner. Use outside official Jalara projects requires written permission.

Code examples in this repository may be used for Jalara asset integration.

See [`LICENSE.md`](LICENSE.md) for the full terms.
