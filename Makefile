# jjd.io build helpers

# Curvo-branded slide deck rendered from the HAR post's revealjs-conditional
# content; slide config lives in posts/_har_slides.yml + posts/_curvo_slides.scss.
# Renders self-contained to _slides/, then copies the deck to
# posts/hours_above_replacement-slides.html, which _quarto.yml's `resources:`
# glob publishes verbatim — that copy is what the post links to.
#
# The deck output is gitignored, NOT committed: CI (.github/workflows/main.yml)
# runs this target on a cache miss, keyed on a hash of the deck's inputs, so it
# only re-renders when the content actually changes. Run `make slides` locally to
# preview; no need to commit the result.
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
