# Quarto Website Migration

This directory contains your migrated website from Jekyll to Quarto.

## Getting Started

1. **Install Quarto**: Download from [https://quarto.org/docs/get-started/](https://quarto.org/docs/get-started/)

2. **Preview your site locally**:
   ```bash
   quarto preview
   ```

3. **Build your site**:
   ```bash
   quarto render
   ```

## File Structure

```
├── _quarto.yml          # Main configuration file
├── index.qmd            # Homepage (About page)
├── publications/        # Publications page
├── research/           # Research page  
├── cv/                 # CV page
├── teaching/           # Teaching page
├── projects/           # Projects page
├── assets/
│   ├── bibliography/   # Bibliography files
│   └── img/           # Images
├── custom.scss         # Custom styling (SCSS)
└── styles.css         # Additional CSS styles
```

## Key Changes from Jekyll

### Configuration
- `_config.yml` → `_quarto.yml`
- All settings now in YAML format
- Navigation defined in website section

### Content Files
- `.md` files → `.qmd` files (Quarto Markdown)
- Frontmatter largely similar but some options changed
- Can now include executable code if needed

### Styling
- Custom themes using SCSS
- Bootstrap-based (like Jekyll al-folio theme)
- Responsive design built-in

### Bibliography
- Bibliography files moved to `assets/bibliography/`
- Citations work with `[@cite-key]` syntax
- Automatic reference list generation

## Next Steps

### 1. Content Migration
- [ ] Update your CV with actual information
- [ ] Add your real publications to the bibliography
- [ ] Customize the research page with your projects
- [ ] Update teaching page with your courses
- [ ] Add any missing profile information

### 2. Styling Customization
- [ ] Adjust colors in `custom.scss` to match your preferences
- [ ] Add any custom CSS needed in `styles.css`
- [ ] Test responsive design on different screen sizes

### 3. Advanced Features
- [ ] Set up academic icons (install quarto-academicons extension)
- [ ] Add blog section if needed
- [ ] Set up automatic deployment to GitHub Pages

### 4. Deployment
- [ ] Test local build with `quarto render`
- [ ] Set up GitHub Actions for automatic deployment
- [ ] Update domain settings if needed

## Useful Commands

```bash
# Preview with live reload
quarto preview

# Render the entire site
quarto render

# Render specific page
quarto render index.qmd

# Check for broken links
quarto check

# Install extensions
quarto add extension-name
```

## Academic Extensions

Consider installing these Quarto extensions for academic websites:

```bash
# Academic icons
quarto add schochastics/academicons

# Enhanced bibliography features  
quarto add quarto-ext/lightbox

# For interactive plots
quarto add quarto-ext/plotly
```

## Resources

- [Quarto Documentation](https://quarto.org/docs/)
- [Academic Website Tutorial](https://www.marvinschmitt.com/blog/website-tutorial-quarto/)
- [Quarto Extensions](https://quarto.org/docs/extensions/)
- [Bootstrap Theme Customization](https://quarto.org/docs/output-formats/html-themes.html)
