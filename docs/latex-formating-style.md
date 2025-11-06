# Problem set LaTeX Style Guide

1. File Header

Use this exact header for all homework sets:

\documentclass[12pt, twoside]{article}
\input{../preamble}
\usepackage{float}

\title{IB}
\author{Chris Huson}
\date{<month year>}

\fancyhead[LE]{\thepage}
\fancyhead[RO]{\thepage \\ First \& last name: \hspace{2.25cm} \,\\ Grade: \hspace{2.25cm} \,}
\fancyhead[LO]{La Scuola d'Italia / Huson / Physics \\* <date>}

2. Section and Topic Headings

- Use \subsubsection*{Topic Name} to mark major content sections.
- Example:
\subsubsection*{2.1 PreTest: Precision, Scientific Notation, Vectors, Kinematics Intro}

3. Problem Structure

Use nested enumerate environments for both main and sub-numbering.

Example

\begin{enumerate}[itemsep=0.5cm]
\item Round each value to three sig figs.
  \begin{multicols}{2}
  \begin{enumerate}[itemsep=0.5cm]
    \item $\sqrt{2}$
    \item $\sqrt{3}$
  \end{enumerate}
  \end{multicols}
  \vspace{0.5cm}
\end{enumerate}

Rules

- No \textbf or manually typed numbers.
- Use [itemsep=...] to control spacing; adjust per section if needed.
- Use \vspace{0.5cm} after each major problem for answer space.
- Do not use \rule for answer blanks unless explicitly desired.
- Use \begin{multicols}{2} for short problems; single-column for longer derivations.

4. Spacing and Layout

- Default margins: 1 inch (set in preamble).
- No extra \\ at end of \item lines.
- Use consistent \vspace between sections, not blank lines.

5. Topics and Examples

Maintain consistent topic labeling, e.g.:

\subsubsection*{Scientific Notation}
\subsubsection*{Unit Conversions}
\subsubsection*{One-Dimensional Motion}

6. Compilation Notes

- Requires ../preamble.tex for fonts, geometry, and packages.
- Compile with XeLaTeX for multilingual text.
- Avoid loading duplicate packages already in the preamble.

7. General Notes

- Follow the IB-style header for all homework documents.
- Leave generous vertical spacing for student work.
- Use concise instructions and clear units in all problems.
- When possible, align topics with Giancoli textbook sections.
- Extend this document as new layout conventions are added.
