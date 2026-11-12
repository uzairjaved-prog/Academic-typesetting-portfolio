# Services and scope

The repository contains examples of the document work listed below. They are samples of layout and implementation, not fixed packages or page limits.

| Type of work | Example in this repository | Information needed to start |
|---|---|---|
| Paper formatting | Three-page IEEEtran paper with equations, citations, a table and figures | Manuscript, target journal or conference template, and bibliography |
| Thesis formatting | Sixteen-page book-class sample with front matter, chapters, appendices and index | University template, required page order, manuscript and citation rules |
| Mathematical typesetting | OLS equations, matrices, theorem environment and cross-references | Equations, notation, numbering rules and any supplied source |
| TikZ / PGFPlots | Transformer diagram, finite-state machine, control-loop diagram and step-response plot | Sketch or written specification, labels and final size |
| Figures and tables | Python-generated time series, correlation matrix, site box plot, scatter plot and summary table | Dataset, column definitions, units and preferred output format |

## Files behind the examples

The paper and thesis use the same generated sensor dataset. scripts/make_data.py creates the CSV; scripts/generate_figures.py creates the charts, table and numeric macros. The diagrams are LaTeX sources in src/tikz/.

## Scope of a client project

For a formatting project, the supplied manuscript, document template, references and submission instructions determine the work. Data analysis, interpretation of results or changes to research claims are separate from typesetting and should be agreed before work begins.

The sensor readings in this repository are simulated. The control diagrams illustrate notation and system behaviour; they are not evidence that a controller was tested on a real system.
