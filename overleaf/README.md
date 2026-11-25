# DietSense: IEEE Conference Paper Draft (Overleaf Project)

This directory contains the complete, compilable LaTeX source code and BibTeX database for the academic paper:

**Title**: DietSense: A Data-Grounded and Safety-Aware Conversational AI Agent for Personalized Dietary Assessment and Weight Management  
**Target Conference**: IEEE International Conference on Electronic Information and Biomedical Engineering / Electronic Information and Business (ICEIB)  
**Format**: IEEE Conference Two-Column Style (`IEEEtran.cls`)

## Project Files

- `main.tex`: Full paper source document, containing all sections (Abstract, Index Terms, Section I Introduction, Section II Related Work, Section III Proposed Architecture & Methodology, Section IV Experimental Evaluation, Section V Conclusion & Future Work, and Acknowledgment).
- `references.bib`: Complete BibTeX citations with verified author lists, journal/conference titles, volumes, page numbers, years, and official DOIs.
- `README.md`: Setup and compilation documentation.

## How to Import into Overleaf

1. Compress this folder (`overleaf/`) or select `main.tex` and `references.bib` into a `.zip` archive:
   ```bash
   # In PowerShell / Terminal:
   Compress-Archive -Path overleaf\main.tex, overleaf\references.bib -DestinationPath DietSense_ICEIB_Overleaf.zip
   ```
2. Log in to [Overleaf](https://www.overleaf.com/).
3. Click **New Project** -> **Upload Project**.
4. Select `DietSense_ICEIB_Overleaf.zip`.
5. Overleaf will automatically detect `main.tex` as the root document and compile using TeX Live (pdflatex / bibtex).

## Local Compilation (TeX Live / MacTeX / MikTeX)

If you have a local TeX distribution installed, run:

```bash
cd overleaf
pdflatex main
bibtex main
pdflatex main
pdflatex main
```

Or using `latexmk`:
```bash
latexmk -pdf main.tex
```

## Key LaTeX Packages Used

The document relies strictly on standard, universally supported IEEE packages:
- `cite`: Automatic numerical citation sorting and compression ([1]--[3]).
- `amsmath`, `amssymb`, `amsfonts`: High-quality mathematical equations and symbol rendering.
- `algorithmic`, `algorithm`: Formatted algorithm pseudocode with line numbers.
- `booktabs`: Professional three-line tables (`\toprule`, `\midrule`, `\bottomrule`).
- `graphicx`: Graphic handling.
- `url`: Proper URL breaking in references.

