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

## Social Sharing / Open Graph
- `site-url` in `_quarto.yml` must be `https://` — LinkedIn and other crawlers reject `http://` OG image URLs
- Every blog post should have an `image:` field in frontmatter for social preview cards
- Site-level config enables `open-graph: true` and `twitter-card` with `summary_large_image`
- Existing post images are in `posts/images/` (Midjourney collection, Norman Rockwell style)
- **LinkedIn crops to 1.91:1** (1200x628) — square images get top/bottom clipped. Always create a wide OG variant for social sharing

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