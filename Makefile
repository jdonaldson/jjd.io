# jjd.io build helpers

# Curvo-branded slide deck rendered from the HAR post's revealjs-conditional
# content. The site build (GitHub Actions `quarto render`) never touches this;
# slide config lives in posts/_har_slides.yml + posts/_curvo_slides.scss.
# Output: _slides/posts/hours_above_replacement.html (self-contained).
.PHONY: slides
slides:
	quarto render posts/hours_above_replacement.qmd --to revealjs \
		--metadata-file posts/_har_slides.yml --output-dir _slides \
		-M subtitle:"One metric for savings opportunity and supply risk — in quality-adjusted hours"

# Full site preview (what the GitHub Action deploys)
.PHONY: site
site:
	quarto render
