# Post-Migration Cleanup Guide

## ✅ Keep These Files (Quarto Website)
- `_quarto.yml` - Main configuration
- `index.qmd` - Homepage
- `cv/index.qmd` - CV page
- `research/index.qmd` - Research page
- `publications/index.qmd` - Publications page
- `projects/index.qmd` - Projects page
- `teaching/index.qmd` - Teaching page
- `custom.scss` - Custom styling
- `styles.css` - Additional CSS
- `assets/` - Images and bibliography
- `QUARTO_MIGRATION.md` - Migration documentation
- `MIGRATION_CHECKLIST.md` - Task checklist

## 🗑️ Files You Can Remove (Jekyll/Docker)
- `Dockerfile` - No longer needed
- `docker-compose.yml` - No longer needed
- `docker-compose-slim.yml` - No longer needed
- `_config.yml` - Jekyll configuration (replaced by _quarto.yml)
- `Gemfile` - Ruby dependencies
- `Gemfile.lock` - Ruby lock file
- `_includes/` - Jekyll includes (functionality moved to Quarto)
- `_layouts/` - Jekyll layouts (replaced by Quarto themes)
- `_sass/` - Jekyll SASS (replaced by custom.scss)
- `_posts/` - Template blog posts (not needed)
- `bin/` - Jekyll scripts
- `purgecss.config.js` - CSS optimization (Quarto handles this)
- `.devcontainer/` - Dev container configuration

## 📁 Optional Cleanup (Template Files)
These were part of the Jekyll template and may not be relevant:
- `CONTRIBUTING.md`
- `CUSTOMIZE.md` 
- `FAQ.md`
- `INSTALL.md`
- Template files in `_posts/` (keep any actual blog posts you want)

## 🎯 After Reopening Locally

1. **Install Quarto** on your local machine
2. **Test the setup**:
   ```bash
   cd /path/to/your/repo
   quarto preview
   ```
3. **Continue development** with the simplified workflow:
   - Edit `.qmd` files
   - Run `quarto preview` for live development
   - Run `quarto render` to build
   - No Docker, no containers, no Jekyll dependencies!

## 🚀 Benefits of Local Development
- **Faster**: No container overhead
- **Simpler**: Direct file system access
- **Native**: Use your local tools and extensions
- **Portable**: Works on any machine with Quarto installed
- **Efficient**: No Docker resource usage
