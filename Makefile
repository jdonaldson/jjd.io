# jjd.io build helpers

# Curvo-branded slide deck rendered from the HAR post's revealjs-conditional
# content. The site build (GitHub Actions `quarto render`) never re-renders this;
# slide config lives in posts/_har_slides.yml + posts/_curvo_slides.scss.
# Renders self-contained to _slides/, then copies the deck to a committed path
# (posts/hours_above_replacement-slides.html) that CI publishes verbatim via the
# `resources:` glob in _quarto.yml — that committed copy is what the post links to.
# Re-run `make slides` and commit the result whenever the deck content changes.
.PHONY: slides
slides:
	quarto render posts/hours_above_replacement.qmd --to revealjs \
		--metadata-file posts/_har_slides.yml --output-dir _slides \
		-M subtitle:"One metric for savings opportunity and supply risk — in quality-adjusted hours"
	cp _slides/posts/hours_above_replacement.html posts/hours_above_replacement-slides.html

# Full site preview (what the GitHub Action deploys)
.PHONY: site
site:
	quarto render
