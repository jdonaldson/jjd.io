all:
	quarto render
	wkhtmltopdf \
		--enable-local-file-access \
		_site/index.html \
		cv.pdf
