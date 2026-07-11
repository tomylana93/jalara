# Jalara Typography

The current asset package does not include font files or a typographic wordmark. This document therefore defines a **recommended typography system**, not a claim that any particular typeface is permanently embedded in the Jalara logo.

## 1. Primary Typeface

### Inter

Use **Inter** as the primary typeface for:

- application interfaces;
- dashboards;
- websites;
- documentation;
- digital presentations;
- screen-based marketing material.

Inter is recommended because it remains legible at small sizes, provides a complete range of weights, and has a neutral character suited to modern software products.

Fallback stack:

```css
font-family: Inter, ui-sans-serif, system-ui, -apple-system,
    BlinkMacSystemFont, "Segoe UI", sans-serif;
```

Do not store or redistribute font files in this repository unless their license and source have been verified.

## 2. Monospace Typeface

Use a system monospace stack for code, identifiers, commands, and technical data:

```css
font-family: "JetBrains Mono", "SFMono-Regular", Consolas,
    "Liberation Mono", monospace;
```

`JetBrains Mono` is recommended but is not bundled with the current assets.

## 3. Typographic Hierarchy

| Role | Desktop size | Weight | Line height |
|---|---:|---:|---:|
| Display | 48–64 px | 700 | 1.05–1.15 |
| Heading 1 | 36–48 px | 700 | 1.15–1.25 |
| Heading 2 | 28–36 px | 650–700 | 1.2–1.3 |
| Heading 3 | 22–28 px | 600 | 1.25–1.35 |
| Large body | 18 px | 400 | 1.55–1.7 |
| Body | 16 px | 400 | 1.5–1.65 |
| Small body | 14 px | 400–500 | 1.45–1.6 |
| Label | 12–14 px | 500–600 | 1.3–1.5 |
| Code | 13–15 px | 400 | 1.5–1.7 |

Sizes may be adjusted for context, but the hierarchy between roles should remain consistent.

## 4. Brand Name Styling

Write the brand name as:

```text
Jalara
```

Not as:

```text
JALARA
jalara
JaLaRa
```

All caps may be used only for small labels or navigation systems that consistently use uppercase styling. Use **Jalara** in headings, paragraphs, and product names.

Product name examples:

```text
Jalara Core
Jalara Finance
Jalara Logistics
Jalara Support
```

## 5. Voice and Writing Style

Jalara writing should be:

- direct;
- clear;
- active;
- restrained;
- focused on function;
- free of jargon that does not help the user.

### Recommended

> Manage modules according to your business needs.

> Keep data connected within one system.

### Avoid

> Revolutionize the digital ecosystem through next-generation modular synergy.

The second sentence sounds expensive while explaining almost nothing, a familiar achievement in technology marketing.

## 6. Interface Capitalization

Use **sentence case** for:

- page titles;
- buttons;
- form labels;
- menus;
- dialogs;
- system messages.

Examples:

```text
Add user
Save changes
Transaction history
```

Avoid unnecessary title case such as:

```text
Add User
Save Changes
Transaction History
```

Exceptions apply to official product names, organizations, people, and terms that require capitalization.

## 7. Emphasis

- Use weights `600` or `700` for headings and primary emphasis.
- Do not use italics for long paragraphs.
- Avoid uppercase for long text.
- Do not rely on color alone to indicate important information.
- Limit the number of active font weights to keep the interface consistent and lightweight.
