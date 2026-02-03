---
name: wunderfan-brand
description: Wunderfan brand guidelines for consistent styling across web projects. Use when building websites, landing pages, or micro apps for Wunderfan. Use with Lovable, v0, or other AI web builders. Provides colors, typography, spacing, and border radii.
---

# Wunderfan Brand Guidelines

Apply these design tokens when building Wunderfan web projects.

## Colors

### Primary Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `primary` | `#007AFF` | Primary brand blue, CTAs, links |
| `primaryLight` | `#4DA1FF` | Hover states, accents |
| `primaryDark` | `#0051A8` | Active states |
| `secondary` | `#50D8DD` | Teal accent, highlights |

### Neutrals

| Token | Hex | Usage |
|-------|-----|-------|
| `white` | `#FFFFFF` | Cards, surfaces |
| `black` | `#000000` | Primary text, dark surfaces |
| `background` | `#F6F7FB` | Page background |
| `gray100` | `#F8F9FA` | Subtle backgrounds |
| `gray500` | `#ADB5BD` | Disabled states |
| `gray600` | `#6C757D` | Muted text |
| `gray800` | `#343A40` | Secondary text |

### Semantic

| Token | Hex |
|-------|-----|
| `success` | `#007AFF` |
| `warning` | `#D088F2` |
| `error` | `#FFC5AE` |
| `info` | `#88DEFB` |

## Typography

### Font Family

**Poppins** — Use Google Fonts:

```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
```

```css
font-family: 'Poppins', sans-serif;
```

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
| `medium` | 500 |
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
  background-color: #007AFF;
  color: #FFFFFF;
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
  color: #007AFF;
  border: 1px solid #007AFF;
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
| Logo only | `assets/wunderfan-logo.svg` |
| Logo + name | `assets/wunderfan-name-and-logo.svg` |

### Remote URLs

If assets are unavailable locally, reference from GitHub:

```
https://raw.githubusercontent.com/Kingly-Clark/skills/main/skills/wunderfan-brand/assets/wunderfan-logo.svg
https://raw.githubusercontent.com/Kingly-Clark/skills/main/skills/wunderfan-brand/assets/wunderfan-name-and-logo.svg
```

### SVG Color Customization

SVGs are provided with default colors. Update `fill` and `stroke` attributes to match your background/foreground requirements.

## CSS Variables Template

```css
:root {
  /* Colors */
  --color-primary: #007AFF;
  --color-primary-light: #4DA1FF;
  --color-primary-dark: #0051A8;
  --color-secondary: #50D8DD;
  --color-background: #F6F7FB;
  --color-surface: #FFFFFF;
  --color-text: #000000;
  --color-text-muted: #6C757D;
  
  /* Typography */
  --font-family: 'Poppins', sans-serif;
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
        primary: '#007AFF',
        'primary-light': '#4DA1FF',
        'primary-dark': '#0051A8',
        secondary: '#50D8DD',
        background: '#F6F7FB',
      },
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
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
