# Jalara Typography

## 1. Official wordmark: custom lettering, not a font

The lowercase **`jalara`** wordmark in Jalara's logo is **custom geometric vector lettering**. It was constructed from individually authored SVG shapes, not typeset with an existing font.

**There is no official font family, font file, or font weight associated with the logo itself.** In particular, **Inter is not the source of the Jalara wordmark**.

The following files are the canonical lettering and logo compositions:

- [`logo-wordmark.svg`](../logo-wordmark.svg) — light-background variant.
- [`logo-wordmark-dark.svg`](../logo-wordmark-dark.svg) — dark-background variant.

The letterforms are saved as SVG `<path>` and `<circle>` elements rather than `<text>` elements. The geometry includes a distinctive rounded, lowercase construction and is designed to remain consistent in every browser and operating system. No external font installation, web font loading, or font conversion is necessary.

The PNG versions (`logo-wordmark.png` and `logo-wordmark-dark.png`) are raster exports **of those exact SVG masters**; they are not independently typeset.

### Rules for reproducing the wordmark

- **Use the supplied wordmark SVG or PNG.** Do not recreate it by typing `jalara` in Inter or another font.
- Do not replace the SVG outlines with `<text>`, edit individual letter spacing, substitute typefaces, or modify letter shapes.
- Do not add a tagline or description inside the artwork.
- Keep the original proportions and select the appropriate light/dark variant.
- For changes to the official lettering, edit the vector masters intentionally and regenerate the PNG exports using `scripts/export-raster.py`.

Because the wordmark is outline-based, an editable text/font version of the official logo **is not available**.

## 2. Typography outside the logo

The suggested typeface for Jalara interfaces, documentation, headings, and marketing copy is **[Inter](https://rsms.me/inter/)**. This is a **recommendation for surrounding text only**, not a claim that the logo uses Inter.

| Context | Recommendation | Notes |
| --- | --- | --- |
| Official Jalara logo | Custom SVG geometric lettering | Always use the supplied asset |
| UI labels, buttons, body text | Inter | System UI sans-serif fallback |
| Website and documentation headings | Inter | Choose weight by content hierarchy |
| Technical commands and code | Monospace system stack | Use an appropriate code-oriented typeface |

Example CSS for surrounding interface copy:

```css
font-family: Inter, ui-sans-serif, system-ui, -apple-system,
    BlinkMacSystemFont, "Segoe UI", sans-serif;
```

For code:

```css
font-family: ui-monospace, "SFMono-Regular", Consolas,
    "Liberation Mono", monospace;
```

No font binaries are bundled in the Jalara brand repository. If an application loads Inter as a web font, it should obtain and distribute that font separately under the applicable font license.

## 3. Brand naming and voice

- In body text and headings, write **Jalara**.
- The official logo displays **`jalara`** in lowercase.
- Use clear, purposeful, functional language. Marketing copy and descriptions belong outside the logo artwork.
