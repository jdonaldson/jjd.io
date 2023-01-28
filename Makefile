all:
	quarto render
	wkhtmltopdf \
		--enable-local-file-access \
		resume.html \
		resume.pdf
