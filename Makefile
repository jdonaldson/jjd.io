all:
	quarto render
	wkhtmltopdf \
		--enable-local-file-access \
		_site/index.html \
		cv.pdf

favico:
	magick images/nav-logo.png -background none -resize 128x128 -density 128x128 favicon.ico
