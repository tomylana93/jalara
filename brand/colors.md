# Jalara Color System — Identity v2

The official artwork uses flat colors (no gradients). All values are sRGB hex.

## Logo colors

| Token | Light logo | Dark logo | Role |
| --- | --- | --- | --- |
| `--jalara-blue` | `#2785F7` | `#4B9DFF` | Upper foundation module |
| `--jalara-ink` | `#182A43` | `#90ABC9` | Lower-left module |
| `--jalara-sky` | `#7EBBF7` | `#B5DBFF` | Lower-right module |
| `--jalara-wordmark` | `#182A43` | `#F6FAFF` | Wordmark outlines |

## Suggested application surfaces

| Token | Hex | Meaning |
| --- | --- | --- |
| `--surface-light` | `#FFFFFF` | Light artwork backdrop |
| `--surface-dark` | `#111F34` | Dark artwork backdrop |
| `--text-light` | `#182A43` | Body text on light backgrounds |
| `--text-dark` | `#F6FAFF` | Body text on dark backgrounds |

These application surface suggestions are not a mandate to recolor independently branded applications built using the foundation.

## Accessibility

Contrast-check text and UI components against their actual surfaces (WCAG AA: 4.5:1 for ordinary text and 3:1 for large text/essential graphical controls). The light-blue module is **decorative**, not a recommended body text color. Never encode a system status by color alone. Do not mix parts from light and dark logo sets.
