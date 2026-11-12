PY=python3
LATEXMK=latexmk -pdf -cd -interaction=nonstopmode -halt-on-error

.PHONY: all data figures tikz paper thesis dist previews before-after refresh-samples clean
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

before-after: data
	$(PY) scripts/before_after.py

refresh-samples:
	test -s dist/paper.pdf && test -s dist/thesis.pdf && test -s dist/tikz-showcase.pdf
	test -s dist/previews/portfolio-overview.jpg
	cp dist/paper.pdf docs/samples/paper.pdf
	cp dist/thesis.pdf docs/samples/thesis.pdf
	cp dist/tikz-showcase.pdf docs/samples/tikz-showcase.pdf
	cp dist/previews/*.jpg docs/previews/
clean:
	for d in src/paper src/thesis src/tikz; do (cd $$d && latexmk -C); done
	rm -rf dist/*
