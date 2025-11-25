# Assets to Replace

This document tracks assets that are currently using placeholders and need to be replaced with final Arcane Forge branding in the future.

## Social Media Card

**Current Status:** Using placeholder (`docusaurus-social-card.jpg`)

**Description:**  
Image displayed when links to the documentation are shared on social media platforms (Twitter, Facebook, LinkedIn, etc.). This appears in link previews.

**Specifications:**
- **Recommended Dimensions:** 1200x630 pixels (1.91:1 aspect ratio)
- **File Format:** JPG or PNG
- **File Size:** Keep under 1MB for optimal loading
- **Location in Project:** `static/img/docusaurus-social-card.jpg`
- **Current Placeholder:** `static/img/docusaurus-social-card.jpg` (Docusaurus default)

**Configuration:**
The social card is configured in `docusaurus.config.ts`:
```typescript
themeConfig: {
  image: 'img/docusaurus-social-card.jpg',
  // ...
}
```

**To Replace:**
1. Create or obtain the social card image with Arcane Forge branding
2. Save it as `static/img/docusaurus-social-card.jpg` (or update the filename in config)
3. Ensure it includes:
   - Arcane Forge logo
   - Site title: "Arcane Forge Documentation"
   - Tagline: "Build Real Game With Arcane Forge"
   - Visually appealing design that represents the brand

**Design Tips:**
- Use high contrast for readability
- Include key branding elements (logo, colors)
- Keep text minimal and legible at small sizes
- Test how it looks when shared on different platforms

---

## Favicon

**Current Status:** ✅ Handled by `utils/replace_favicon.py`

**Description:**  
The small icon displayed in browser tabs and bookmarks.

**Specifications:**
- **Recommended Sizes:** 16x16, 32x32, 48x48 pixels (multiple sizes in one ICO file)
- **File Format:** ICO
- **Location in Project:** `static/img/favicon.ico`

**To Update:**
Run the Python script:
```bash
python utils/replace_favicon.py
```

This script converts `logo.png` to `favicon.ico` with multiple sizes.

---

## Additional Assets (Future)

### Logo Variations
- **Dark mode logo:** If needed for dark theme
- **Favicon variations:** Different sizes for different platforms
- **Apple touch icon:** For iOS devices (180x180px PNG)

### Homepage Illustrations
Currently using Docusaurus default illustrations:
- `static/img/undraw_docusaurus_mountain.svg`
- `static/img/undraw_docusaurus_tree.svg`
- `static/img/undraw_docusaurus_react.svg`

These are used in the homepage features section. Consider replacing with Arcane Forge-themed illustrations.

---

## Notes

- All assets should maintain brand consistency with the main Arcane Forge website (arcaneforge.ai)
- Use the same color scheme and design language
- Test all assets on different devices and platforms
- Keep file sizes optimized for web performance

