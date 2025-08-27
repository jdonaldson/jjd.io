# jjd.io - Personal Website Project

## Project Overview
This is Justin Donaldson's personal website built with Quarto, showcasing professional background, blog posts, CV, and project portfolio.

## Site Structure
- **Technology**: Quarto static site generator
- **Domain**: jjd.io
- **Hosting**: GitHub Pages (via CNAME file)
- **Theme**: Sandstone theme with custom CSS

## Key Files
- `_quarto.yml`: Main configuration file
- `index.qmd`: About/homepage content
- `cv.qmd`: Curriculum Vitae page
- `blog.qmd`: Blog listing page
- `posts/`: Blog post content (mix of .qmd and .ipynb files)
- `images/`: Site images and photos
- `style.css`: Custom styling

## Content Guidelines
- **Tone**: Professional but approachable, academic background with industry focus
- **Focus**: AI/ML, data science, visualization, human-computer interaction
- **Updates**: Keep current role (Curvo Labs) prominent, past roles in chronological order
- **Blog topics**: Technical posts about AI/ML, data science tutorials, industry insights

## Image Management
- Team photos should include proper attribution
- Professional headshots and company logos in `/images/`
- Blog post images in `/posts/images/`

## Development Notes
- Uses Quarto's freeze feature for computational content
- Jupyter notebooks (.ipynb) and Quarto markdown (.qmd) supported
- Site builds to `_site/` directory
- Google Analytics tracking enabled

## Deployment
- **GitHub Actions**: Automated deployment via `.github/workflows/main.yml`
- **Trigger**: Pushes to `main` branch automatically deploy
- **Process**: Quarto render → GitHub Pages publish to gh-pages branch
- **Features**: 
  - TinyTeX for LaTeX/PDF support
  - WeasyPrint for PDF CV generation
  - Ready for Python/R/Julia dependencies if needed
- **Domain**: Deploys to jjd.io via CNAME file

## Maintenance Tasks
- Update CV with new roles, publications, patents
- Add new blog posts in `/posts/`
- Update team photos and professional images
- Keep bibliography files current in `/bibliographies/`

## Current Status
- **Role**: Chief Data Scientist at Curvo Labs (2024-present)
- **Previous**: Hushh.ai CTO, Salesforce Principal Data Scientist/Engineer
- **Recent additions**: Curvo Labs team photo, role updates completed

## Dependencies
- Quarto
- Python (for Jupyter notebooks)
- R (for some content)
- Polars preferred for data analysis examples