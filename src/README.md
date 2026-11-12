# LaTeX source projects

This directory contains the paper, thesis, and standalone TikZ showcase.
Each project has its own main .tex file and local supporting files.
The paper uses the IEEEtran journal class.
The thesis uses the book class and includes separate chapter files.
The TikZ showcase compiles the diagrams without the paper or thesis.
Build all three from the repository root with make all.
Build one project with make paper, make thesis, or make tikz.
The PDFs are written under src/ during compilation and copied to dist/.
Generated PDFs and LaTeX auxiliary files are build products; do not edit them.
Edit the .tex sources and rebuild to change document content.
