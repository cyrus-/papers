MAIN = globaldsl13

${MAIN}.pdf:	*.tex
	pdflatex ${MAIN}
	pdflatex ${MAIN}
	bibtex ${MAIN}
	pdflatex ${MAIN}
	pdflatex ${MAIN}

open:	${MAIN}.pdf
	open ${MAIN}.pdf

clean:	${MAIN}.pdf
	rm ${MAIN}.pdf
	rm ${MAIN}.aux
	rm ${MAIN}.log
	rm ${MAIN}.bbl
	rm ${MAIN}.blg
