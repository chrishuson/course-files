---
header-includes:
  - \usepackage{tikz}
  - \usetikzlibrary{shapes.geometric,arrows}
---

# Graphs with TikZ (doesn't work)

1. The expression $\displaystyle \frac{x^2 + 6}{x^2 + 4}$ is equivalent to

```latex
\begin{tikzpicture}[scale=0.5]
% Draw the grid
\draw[gray, very thin] (0,0) grid (10,10);
% Draw the axes
\draw[thick, ->] (0,0) -- (10.5,0) node[right] {$x$};
\draw[thick, ->] (0,0) -- (0,10.5) node[above] {$p(x)$};
% Draw the curve
\draw[thick] plot [smooth, tension=1] coordinates {(0,0) (4,2) (6,8) (10,10)};
% Label the local minimum and maximum
\node[below right] at (4,2) {local minimum};
\node[above left] at (6,8) {local maximum};
\end{tikzpicture}
```
