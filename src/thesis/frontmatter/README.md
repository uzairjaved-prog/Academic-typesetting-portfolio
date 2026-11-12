# Thesis front matter

[titlepage.tex](titlepage.tex) provides the title page. [abstract.tex](abstract.tex) contains the abstract and adds it to the table of contents.

The title, author and date are supplied by commands in [../preamble.tex](../preamble.tex). The title page identifies the document as a typesetting demonstration and states that its data are synthetic.

Build the complete thesis from the repository root with:

    make thesis

Edit these two .tex files when the front matter changes. The formatted pages appear in [../main.pdf](../main.pdf) after the thesis has been built.
