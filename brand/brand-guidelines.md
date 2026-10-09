# Jalara Brand Guidelines

## Design concept

Jalara is a modern, modular foundation for building simple, purposeful applications.

Its signature icon combines three visually separated forms: a rounded blue upper module, a deep-navy quarter-circle base, and a softly illuminated light-blue lower-right module. Negative space and the white diagonal seam express distinct building blocks fitting together into one purposeful form.

The wordmark **jalara** is custom geometric vector lettering. Do not replace it with a normal HTML font; use the official file.

## Four official variants

| File | Correct surface |
| --- | --- |
| `logo.svg` | Symbol-only on a light background |
| `logo-dark.svg` | Symbol-only on a dark background |
| `logo-wordmark.svg` | Symbol and wordmark on a light background |
| `logo-wordmark-dark.svg` | Symbol and wordmark on a dark background |

PNG exports follow exactly the same naming and visual geometry.

## Usage

- Use symbol-only for favicon, sidebar, square avatar, and compact spaces.
- Use the complete wordmark for README, websites and documentation.
- Do not include any tagline or description inside logo artwork.
- Keep sufficient clear space (approximately 12.5% of the icon width) and preserve aspect ratio.
- Do not recolor modules, flatten gradients, distort, rotate, add shadows, or apply CSS filters to create dark mode.
- For small symbols, use at least 24px, preferably 32px.
- For the complete wordmark, use at least 160px wide.

## Theme selection

For GitHub README use a `<picture>` with `(prefers-color-scheme: dark)` and `(prefers-color-scheme: light)` sources. In an application, switch between `logo-wordmark.svg` and `logo-wordmark-dark.svg` based on the UI theme. A site's CSS dark mode may differ from the OS preference.

See `README.md` for the working GitHub markup.
