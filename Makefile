manuscript = resume
latexopt = -file-line-error -halt-on-error

# Build the PDF of the lab report from the source files
$(manuscript).pdf: $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex
	pdflatex $(latexopt) $(manuscript).tex

clean :
	rm -f *.aux *.log *.bbl *.lof *.lot *.blg *.out *.toc *.run.xml *.bcf
	rm $(manuscript).pdf

.PHONY : clean
