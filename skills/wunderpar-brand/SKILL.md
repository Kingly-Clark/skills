---
name: wunderpar-brand
description: Wunderpar brand guidelines for consistent styling across web projects. Use when building websites, landing pages, or micro apps for Wunderpar. Use with Lovable, v0, or other AI web builders. Provides colors, typography (including Fraunces display font), spacing, and border radii.
---

# Wunderpar Brand Guidelines

Apply these design tokens when building Wunderpar web projects.

## Colors

### Primary Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#40452F` | Primary olive green, CTAs, links |
| `secondary` | `#E3C895` | Gold accent, highlights, dark surface accents |

### Neutrals

| Token | Hex | Usage |
|-------|-----|-------|
| `white` | `#FFFFFF` | Cards, surfaces |
| `black` | `#000000` | Primary text |
| `background` | `#FFFEF3` | Page background (warm cream) |
| `surfaceLight` | `#FFFEF3` | Light surfaces |
| `surfaceDark` | `#40452F` | Dark surfaces, headers |
| `gray500` | `#ADB5BD` | Disabled states |
| `gray600` | `#6C757D` | Muted text |

### Semantic

| Token | Hex |
|-------|-----|
| `success` | `#40452F` |
| `warning` | `#D088F2` |
| `error` | `#FFC5AE` |
| `info` | `#E3C895` |

## Typography

### Dual Font System

Wunderpar uses two fonts:
- **Poppins** (F1) — Primary body text
- **Fraunces** (F2) — Display/highlight font for titles and emphasis

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Fraunces:wght@400;600;700&display=swap" rel="stylesheet">
```

```css
/* Primary font */
font-family: 'Poppins', sans-serif;

/* Display font for titles */
font-family: 'Fraunces', serif;
```

### When to Use Fraunces

- Hero headings
- Section titles
- Feature highlights
- Promotional text
- Any text that needs to "pop"

### Font Sizes

| Token | Size | Usage |
|-------|------|-------|
| `xs` | 12px | Captions, labels |
| `s` | 14px | Body small |
| `m` | 16px | Body default |
| `m2` | 18px | Body large |
| `l` | 24px | Subheadings |
| `l2` | 28px | Section headings |
| `xl` | 42px | Page titles |
| `xxl` | 72px | Hero text |

### Font Weights

| Token | Weight |
|-------|--------|
| `regular` | 400 |
| `semiBold` | 600 |
| `bold` | 700 |

## Spacing

Use 4px base unit:

| Token | Value |
|-------|-------|
| `xs` | 4px |
| `s` | 8px |
| `m` | 16px |
| `l` | 24px |
| `xl` | 32px |
| `xxl` | 40px |

## Border Radii

| Token | Value | Usage |
|-------|-------|-------|
| `container` | 24px | Cards, sections |
| `button` | 28px | Buttons (pill-shaped) |
| `input` | 50px | Input fields (fully rounded) |
| `modal` | 12px | Dialogs, modals |

## Button Styles

### Primary Button

```css
.btn-primary {
  background-color: #40452F;
  color: #FFFEF3;
  border-radius: 28px;
  padding: 16px 24px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
}
```

### Outline Button

```css
.btn-outline {
  background-color: transparent;
  color: #40452F;
  border: 1px solid #40452F;
  border-radius: 28px;
  padding: 16px 24px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
}
```

### Accent Button (Gold)

```css
.btn-accent {
  background-color: #E3C895;
  color: #40452F;
  border-radius: 28px;
  padding: 16px 24px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
}
```

## Logo

### Local Assets

| Asset | Path |
|-------|------|
| Logo only | `assets/wunderpar-logo.svg` |
| Logo + name | `assets/wunderpar-name-and-logo.svg` |

### Remote URLs

If assets are unavailable locally, reference from GitHub:

```
https://raw.githubusercontent.com/Kingly-Clark/skills/main/skills/wunderpar-brand/assets/wunderpar-logo.svg
https://raw.githubusercontent.com/Kingly-Clark/skills/main/skills/wunderpar-brand/assets/wunderpar-name-and-logo.svg
```

### SVG Color Customization

SVGs are provided with default colors (`#FFFEF3` stroke/fill). Update `fill` and `stroke` attributes to match your background/foreground requirements.

## CSS Variables Template

```css
:root {
  /* Colors */
  --color-primary: #40452F;
  --color-secondary: #E3C895;
  --color-background: #FFFEF3;
  --color-surface: #FFFFFF;
  --color-surface-dark: #40452F;
  --color-text: #000000;
  --color-text-muted: #6C757D;
  --color-text-inverted: #FFFEF3;
  
  /* Typography */
  --font-family: 'Poppins', sans-serif;
  --font-family-display: 'Fraunces', serif;
  --font-size-xs: 12px;
  --font-size-s: 14px;
  --font-size-m: 16px;
  --font-size-l: 24px;
  --font-size-xl: 42px;
  
  /* Spacing */
  --space-xs: 4px;
  --space-s: 8px;
  --space-m: 16px;
  --space-l: 24px;
  --space-xl: 32px;
  
  /* Border Radii */
  --radius-container: 24px;
  --radius-button: 28px;
  --radius-input: 50px;
  --radius-modal: 12px;
}
```

## Tailwind Config

```js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#40452F',
        secondary: '#E3C895',
        background: '#FFFEF3',
        'surface-dark': '#40452F',
      },
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
        display: ['Fraunces', 'serif'],
      },
      borderRadius: {
        container: '24px',
        button: '28px',
        input: '50px',
        modal: '12px',
      },
    },
  },
}
```

### Tailwind Typography Example

```html
<h1 class="font-display text-4xl">Hero Title in Fraunces</h1>
<p class="font-sans text-base">Body text in Poppins</p>
```
