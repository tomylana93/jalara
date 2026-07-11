# Jalara Brand Guidelines

This document defines the basic rules for using the **Jalara** visual identity consistently across applications, websites, documentation, social media, and promotional material.

## 1. Identity Foundation

Jalara is a modular application foundation that connects different capabilities within one structured system.

The Jalara logo communicates:

- **One foundation** — the primary form works as a unified whole.
- **Modularity** — internal elements represent distinct parts that coexist within one structure.
- **Flow and connection** — curves and visual paths suggest relationships between components.
- **Stability** — the solid form reflects a dependable technical foundation.
- **Adaptability** — the open composition suggests a system that can evolve.

## 2. Brand Character

Jalara should feel:

- modern without being excessive;
- technical without feeling cold;
- structured without becoming rigid;
- premium without becoming decorative;
- simple without losing distinction.

## 3. Logo Variants

### Primary logo

Use `logo.svg` or `logo.png` on white, light, or pale neutral backgrounds.

The primary logo uses a navy gradient with a teal accent. It is the default choice for websites, documentation, light dashboards, and public-facing materials.

### Dark-mode logo

Use `logo-dark.svg` or `logo-dark.png` on navy, black, or other dark surfaces.

The dark-mode variant uses a light body with a brighter teal accent. Do not use the primary logo on a dark background when contrast becomes insufficient.

### Square logo

Use `logo-square.png` for:

- GitHub avatars;
- social media profiles;
- temporary Open Graph images;
- internal covers;
- square promotional layouts.

The square logo is not an automatic replacement for favicons. Use the dedicated favicon files for browser and PWA contexts.

## 4. Clear Space

Keep a minimum clear space around all sides of the logo equal to approximately **10% of the logo width**.

No text, lines, icons, or interface elements should enter this area. At small sizes, prioritize legibility instead of forcing the logo to fill its container.

## 5. Minimum Size

Recommended minimums:

| Context | Minimum size |
|---|---:|
| SVG logo in an interface | 24 px high |
| PNG logo in an interface | 32 px high |
| Presentations and documents | 12 mm high |
| Favicon | Use the dedicated 32 × 32 px asset |

Do not add supporting text or new decorative elements at very small sizes.

## 6. Backgrounds

### Recommended

- white;
- very light gray;
- dark navy;
- neutral black;
- solid colors with strong contrast.

### Avoid

- highly detailed photographs;
- gradients that compete with the logo colors;
- busy patterns;
- teal backgrounds that obscure the accent;
- navy backgrounds used with the primary logo when contrast is too low.

When the logo must appear over a photograph, use a solid panel or sufficient overlay to maintain contrast.

## 7. Incorrect Usage

Do not:

- change the aspect ratio or stretch the logo horizontally or vertically;
- rotate or flip the logo;
- replace the official colors with product-specific colors;
- remove any part of the logo;
- recreate the gradients by approximation;
- add strokes or outlines;
- add drop shadows, glow, bevels, or 3D effects;
- place the logo inside another shape without a clear system requirement;
- use CSS filters such as `invert()` to create a dark-mode version;
- add module names directly inside the logo shape.

## 8. Product and Module Naming

Use a consistent naming pattern:

```text
Jalara Core
Jalara Identity
Jalara Finance
Jalara Logistics
Jalara Inventory
Jalara Support
Jalara Insights
```

**Jalara** remains the master brand. Module names act as descriptors rather than independent brands.

## 9. Interface Style

Jalara applications should follow these principles:

- clear information hierarchy;
- sufficient whitespace;
- restrained use of accent colors;
- consistent components;
- short, functional animation;
- visual decoration that never interferes with user tasks.

Jalara's identity does not depend on exaggerated futuristic effects. The product should feel modern through precision, structure, and interaction quality.

## 10. File Formats

| Format | Primary use |
|---|---|
| SVG | Websites, dashboards, HTML documentation, and scalable use |
| PNG | Applications or platforms that do not support SVG |
| ICO | Browser favicons |

Do not automatically convert PNG files into SVG. Use the original SVG files to preserve accurate geometry and gradients.
