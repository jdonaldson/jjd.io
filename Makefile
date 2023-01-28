all:
	quarto render
	wkhtmltopdf \
		--enable-local-file-access \
		docs/index.html \
		resume.pdf
