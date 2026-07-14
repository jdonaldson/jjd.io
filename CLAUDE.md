# jjd.io - Personal Website Project

## Project Overview
This is Justin Donaldson's personal website built with Quarto, showcasing professional background, blog posts, CV, and project portfolio.

## Site Structure
- **Technology**: Quarto static site generator
- **Domain**: jjd.io
- **Hosting**: GitHub Pages (via CNAME file)
- **Theme**: Solarized — `theme-light.scss` / `theme-dark.scss` layered over cosmo/darkly,
  with a native light/dark toggle (`theme: {light, dark}` in `_quarto.yml`) plus custom
  `style.css`. TOC is the left rail; tips & small images go in the right margin
  (`::: {.column-margin}` / `.callout-tip`), matching the osgood post.

## Information Architecture (restructured 2026-06-27)
- **Home = blog listing** (`index.qmd`): the writing is the front door — short hero + post
  listing. `aliases: [blog.html]` redirects the old blog URL here; `blog.qmd` was retired.
- **About** (`about.qmd`): the full bio / career narrative (was the old homepage).
- **CV** (`cv.qmd`): formal CV with `#publications` / `#patents` / `#pro-bono` anchors.
- Navbar: blog (→ index) · about · cv + social icons.

## Key Files
- `_quarto.yml`: Main config (theme toggle, navbar, `toc-location: left`)
- `index.qmd`: Home — blog listing + hero
- `about.qmd`: Bio / career narrative
- `cv.qmd`: Curriculum Vitae page
- `posts/`: Blog post content (mix of .qmd and .ipynb files)
- `images/`: Site images and photos
- `theme-light.scss` / `theme-dark.scss`: Solarized themes (palette + callout colors)
- `style.css`: Custom styling (content background is theme-driven via `--content-bg`)

## Content Guidelines
- **Tone**: Professional but approachable, academic background with industry focus
- **Focus**: AI/ML, data science, visualization, human-computer interaction
- **Updates**: Keep current role (Curvo Labs) prominent, past roles in chronological order
- **Blog topics**: Technical posts about AI/ML, data science tutorials, industry insights

## Image Management
- Team photos should include proper attribution
- Professional headshots and company logos in `/images/`
- Blog post images in `/posts/images/` (now JPEG, converted from PNG for size)
- Team photos were cropped to focus on faces (originals in Trash if needed)
- Blog post art images (Midjourney/Norman Rockwell) converted from PNG to JPEG (~30MB savings)

## Development Notes
- Uses Quarto's freeze feature for computational content
- Jupyter notebooks (.ipynb) and Quarto markdown (.qmd) supported
- Site builds to `_site/` directory
- Google Analytics tracking enabled

## Title Banners (site-wide convention, 2026-07-10)
- Every post with an `image:` also sets `title-block-banner: "<same image path>"` and
  `title-block-banner-color: white` — the post's OG image becomes the title background.
- The darkening gradient overlay + white text/shadow CSS is **global** in `style.css`
  (`.quarto-title-banner` rules, `::before` overlay) — image-agnostic, do not inline
  per-post styles. Tune crop via `background-position` there if a banner clips badly.
- Posts without an `image:` (book_bot, intelligence_chases_chaos, perchance_to_dream,
  quarto, rumpus) fall back to the plain title block; give them an image to opt in.

## Viz Section (added 2026-07-13)
- `viz/` hosts standalone interactive pages; `viz/index.qmd` is the landing page (navbar: blog · viz · about · cv)
- Raw HTML pages are copied verbatim via the `resources: viz/*.html` glob in `_quarto.yml` (Quarto only renders .qmd/.ipynb)
- Pages must be self-contained (inline JS/CSS; wasm as base64) and carry their own `<!DOCTYPE html>` skeleton with charset + viewport meta
- Convention: each viz supports a `?lite` URL param — fraction of full complexity, UI hidden, name centered — used as the live preview iframe on viz/index (iframe is pointer-events:none, wrapped in an anchor to the full page)
- MURMURATION (40k boids, deck.gl) is canonical at https://jdonaldson.github.io/murmuration/ (repo jdonaldson/murmuration, main branch); jjd.io's `viz/boids.html` is the self-contained light rebuild that powers its preview card

## Slide Decks (revealjs from a post; HAR pattern, 2026-07-13)
- A post can carry a talk version: split content with `::::::  {.content-hidden when-format="revealjs"}` (article) and `{.content-visible when-format="revealjs"}` (deck) in the same .qmd
- `make slides` renders self-contained to `_slides/` then copies to `posts/<slug>-slides.html`; `_quarto.yml`'s `resources:` glob publishes that copy verbatim; the post links to it
- The `-slides.html` output is **gitignored, not committed**. CI (`.github/workflows/main.yml`) renders it on a cache miss via `actions/cache` keyed on `hashFiles()` of every deck input (qmd, `_har_*`/config, curvo scss, embedded arcs.svg + logo, Makefile) — only re-renders when an input changes
- Deck config: `posts/_har_slides.yml` (revealjs opts) + `posts/_curvo_slides.scss` (Curvo theme). Section-break slides use `background-image=images/curvo_arcs.svg`
- `curvo_arcs.svg` gotcha: artwork extends past a naive `0 0 1200 1200` viewBox (outer C-arc bulges to x≈-108, top leads to x≈1278) — viewBox must be `-128 92 1426 1024` to avoid edge-clipping

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