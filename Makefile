PY=python3
LATEXMK=latexmk -pdf -cd -interaction=nonstopmode -halt-on-error

.PHONY: all data figures tikz paper thesis dist previews clean
all: figures tikz paper thesis dist previews

data:
	$(PY) scripts/make_data.py
figures: data
	$(PY) scripts/generate_figures.py
tikz: figures
	$(LATEXMK) src/tikz/showcase.tex
paper: figures
	$(LATEXMK) src/paper/main.tex
thesis: figures
	$(LATEXMK) src/thesis/main.tex
dist: paper thesis tikz
	mkdir -p dist
	cp src/paper/main.pdf dist/paper.pdf
	cp src/thesis/main.pdf dist/thesis.pdf
	cp src/tikz/showcase.pdf dist/tikz-showcase.pdf
previews: dist
	$(PY) scripts/make_previews.py --pdf-dir dist --output-dir dist/previews
clean:
	for d in src/paper src/thesis src/tikz; do (cd $$d && latexmk -C); done
	rm -rf dist/*
