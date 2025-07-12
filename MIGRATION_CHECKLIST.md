# Quarto Migration Checklist

## ✅ Completed

- [x] **Basic Quarto setup** - `_quarto.yml` configuration file created
- [x] **Homepage** - About page with profile information (`index.qmd`)
- [x] **Site structure** - All main pages created:
  - [x] Publications (`publications/index.qmd`)
  - [x] Research (`research/index.qmd`)
  - [x] CV (`cv/index.qmd`)
  - [x] Teaching (`teaching/index.qmd`)
  - [x] Projects (`projects/index.qmd`)
- [x] **Navigation** - Website navbar configured with all sections
- [x] **Styling** - Custom theme and CSS files created
- [x] **Bibliography** - Bibliography file moved and configured
- [x] **Profile image** - Image copied and configured
- [x] **Build system** - Quarto successfully installed and working
- [x] **Preview server** - Site rendering and preview working

## 🔄 Next Steps (Priority Order)

### High Priority
- [ ] **Update CV content** - Replace placeholder text with your actual CV information
- [ ] **Add real publications** - Update `assets/bibliography/papers.bib` with your publications
- [ ] **Customize About page** - Add/update your profile information
- [ ] **Update contact information** - Verify email, ORCID, Google Scholar links
- [ ] **Add research details** - Fill in your actual research projects and interests

### Medium Priority
- [ ] **Install academic icons** - Run `quarto add schochastics/academicons` for better icons
- [ ] **Customize colors** - Adjust the color scheme in `custom.scss`
- [ ] **Add teaching content** - Fill in your actual courses and teaching philosophy
- [ ] **Add project details** - Update projects page with real information
- [ ] **Test mobile responsiveness** - Check site on different screen sizes

### Low Priority
- [ ] **Add blog section** - If you want to keep blog functionality
- [ ] **PDF CV generation** - Install TinyTeX if you want PDF CV export
- [ ] **SEO optimization** - Add meta descriptions and keywords
- [ ] **Analytics** - Add Google Analytics if desired
- [ ] **404 page** - Create custom 404 error page

## 🚀 Deployment

### GitHub Pages Setup
1. Push your Quarto files to your repository
2. Create `.github/workflows/quarto-publish.yml` for automatic deployment
3. Enable GitHub Pages in repository settings
4. Set up custom domain if needed

### Local Development
```bash
# Preview site with live reload
quarto preview

# Build entire site
quarto render

# Check for issues
quarto check
```

## 📁 Files to Migrate/Update

### Content Files (High Priority)
- [ ] Copy content from `_pages/about.md` → `index.qmd`
- [ ] Update bibliography in `assets/bibliography/papers.bib`
- [ ] Migrate any custom content from Jekyll pages
- [ ] Update contact information and social links

### Assets
- [x] Profile image (`assets/img/eirik_4643_1200px.jpg`) ✓
- [ ] Add any other images you use
- [ ] Copy any PDFs (CV, papers, etc.)

### Optional Jekyll Files (Can Ignore)
- `_posts/` - Template files (not needed for your actual site)
- `Dockerfile` and Docker files - No longer needed
- Jekyll-specific config files

## 🎨 Customization Options

### Theme Colors
Edit `custom.scss` to change:
- Primary color (currently sea green `#2E8B57`)
- Font families
- Spacing and layout

### Layout Options
Edit `_quarto.yml` to adjust:
- Navigation structure
- Page layouts
- Footer content
- Search functionality

### Advanced Features
- **Citations**: Use `[@key]` syntax for bibliography references
- **Cross-references**: Link between sections with `@sec-label`
- **Code blocks**: Full syntax highlighting and execution support
- **Math**: LaTeX math rendering built-in

## 🔧 Troubleshooting

### Common Issues
- **Build errors**: Check `_quarto.yml` syntax with `quarto check`
- **Missing images**: Verify file paths in `assets/img/`
- **Bibliography issues**: Ensure BibTeX file is valid
- **Styling problems**: Check CSS syntax in custom files

### Useful Commands
```bash
# Test single page
quarto render index.qmd

# Clean build
rm -rf _site && quarto render

# Check configuration
quarto check

# Install extensions
quarto add extension-name
```

## 📚 Resources
- [Quarto Website Guide](https://quarto.org/docs/websites/)
- [Academic Website Tutorial](https://www.marvinschmitt.com/blog/website-tutorial-quarto/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Example Academic Websites](https://github.com/topics/quarto-website)
