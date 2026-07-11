# Jalara Color System

The Jalara palette is derived directly from the color definitions in the official SVG assets.

## 1. Primary Logo Palette

### Deep Navy

| Token | Hex | Use |
|---|---|---|
| `jalara-navy-700` | `#082A63` | Navy gradient start, dark headings, primary brand elements |
| `jalara-navy-800` | `#052B69` | Navy gradient end |
| `jalara-navy-900` | `#031F52` | Deepest navy and gradient center |

Practical CSS approximation of the primary logo gradient:

```css
background: linear-gradient(
    143deg,
    #082A63 0%,
    #031F52 55%,
    #052B69 100%
);
```

The CSS angle above is an implementation approximation. Always use the official SVG file when reproducing the logo instead of redrawing its gradient in CSS.

### Teal

| Token | Hex | Use |
|---|---|---|
| `jalara-teal-700` | `#0B7E88` | Teal gradient start |
| `jalara-teal-500` | `#0AA7A4` | Teal gradient end and primary accent |

Practical accent gradient:

```css
background: linear-gradient(
    125deg,
    #0B7E88 0%,
    #0AA7A4 100%
);
```

## 2. Dark-Mode Palette

### Light Body

| Token | Hex | Use |
|---|---|---|
| `jalara-light-blue-300` | `#CDDDF5` | Dark-mode body gradient start |
| `jalara-light-blue-50` | `#F4F8FF` | Primary light color |
| `jalara-light-blue-200` | `#D7E5FA` | Dark-mode body gradient end |

### Bright Teal

| Token | Hex | Use |
|---|---|---|
| `jalara-cyan-500` | `#18B8C0` | Dark-mode accent start |
| `jalara-cyan-300` | `#2AE0CF` | Dark-mode accent end |

## 3. Recommended Interface Colors

The following colors are interface recommendations. They are not embedded in the logo assets.

| Token | Hex | Function |
|---|---|---|
| `surface-light` | `#FFFFFF` | Primary light-mode background |
| `surface-muted` | `#F4F7FB` | Secondary panel or surface |
| `surface-dark` | `#06152F` | Primary dark-mode background |
| `surface-dark-muted` | `#0B1E3D` | Secondary dark-mode panel |
| `text-primary` | `#10213D` | Primary light-mode text |
| `text-muted` | `#607089` | Secondary text |
| `text-on-dark` | `#F4F8FF` | Primary dark-mode text |
| `border-light` | `#DCE4EF` | Light-mode border |
| `border-dark` | `#20395F` | Dark-mode border |

Treat success, warning, danger, and information colors as functional colors. Do not replace every status color with teal merely for visual consistency. Users need clarity more than blind loyalty to a palette.

## 4. Usage Ratio

For general interfaces, use this approximate balance:

- **70–80%** neutral colors and surfaces;
- **15–20%** navy for structure, navigation, and hierarchy;
- **5–10%** teal or cyan for accents and important actions.

Do not use teal simultaneously for every button, icon, badge, and link. An accent only works when it is not shouting from every corner of the interface.

## 5. Accessibility

- Maintain a minimum contrast ratio of **4.5:1** for normal text.
- Large text and essential graphical elements should reach at least **3:1**.
- Do not use color as the only status indicator.
- Add labels, icons, patterns, or shape changes to distinguish states.
- Test color combinations separately in light mode and dark mode.

## 6. CSS Custom Properties

```css
:root {
    --jalara-navy-700: #082a63;
    --jalara-navy-800: #052b69;
    --jalara-navy-900: #031f52;

    --jalara-teal-700: #0b7e88;
    --jalara-teal-500: #0aa7a4;

    --jalara-light-blue-300: #cdddf5;
    --jalara-light-blue-50: #f4f8ff;
    --jalara-light-blue-200: #d7e5fa;

    --jalara-cyan-500: #18b8c0;
    --jalara-cyan-300: #2ae0cf;
}
```
