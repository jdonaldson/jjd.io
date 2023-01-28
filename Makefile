all:
	pandoc \
		--lua-filter=utils/multiple-bibliographies.lua \
		--css=resume-css-stylesheet.css \
		--output=resume.html \
		resume.md
	wkhtmltopdf \
		--enable-local-file-access \
		resume.html \
		resume.pdf

clean:
	rm -r $(builddir)
	rm $(manuscript).pdf

