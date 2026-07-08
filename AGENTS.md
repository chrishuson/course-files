# AGENTS.md — course-files repo

Context for AI agents (Codex, Claude Code) working directly in this
repository. `CLAUDE.md` in this repo is identical — update both together.

## What this repo is

Chris Huson's teaching materials, 10+ years. **Public repo** — never add
student names, rosters, scores, or scanned work. Student data lives on
the school Google Drive (`Math_Assessments/`), managed from the IB Math
project repo (below).

## Active vs archive

| Area | Status |
| --- | --- |
| `docs/ib/` | **Active** — IB Math AA SL, current year. Unit subfolders `01-Sequences` … `11-Review`, shared `preamble.tex`, `graphics/` |
| `docs/ib_HL/` | **Active** — HL track (one advanced student) |
| `docs/physics/` | **Active** — 9th-grade physics, own `preamble.tex` |
| `docs/Italian-maturita/` | Active occasionally — Italian exam translations, self-contained `.tex` |
| Year folders at root (`IB2023/`, `Geom2023/`, `Precalc2024/`, …) | **Frozen archive** — do not edit; old documents must keep compiling with their local preambles |

## Compile rules

- Always compile from within the unit subfolder so `\input{../preamble}`
  resolves: `cd docs/ib/<unit>/ && pdflatex <file>.tex`
- Compile every generated `.tex` and **visually review the PDF** —
  a clean exit status is not enough.
- Do not commit or push — Chris handles git manually.

## Authoring conventions

The full specs live in the IB Math project repo
(`~/Documents/Professional/IB_Math/claude-ib-project/`):

- `workflows/authoring/overview.md` — end-to-end recipe, layout types
- `workflows/authoring/tex-conventions.md` — file skeleton, answer
  boxes, figures, notation, page-layout sizing
- `workflows/authoring/markscheme-spec.md` — `_MS.tex` rules
- `workflows/authoring/key-json-spec.md` — `_key.json` schema

Quick facts: `\documentclass[12pt, twoside]{article}`; file naming
`<unit>-<section><Type>_<Topic>.tex` (types DN/CW/HW/PreQuiz/Q/Test);
every problem set gets a `_MS.tex`; quizzes/tests also get `_key.json`;
figures black-and-white; pgfplots for axis graphs, TikZ otherwise;
"(no calculator)" in the title when GDC is disallowed.

Physics conventions: see the physics project
(`~/Documents/Professional/Physics/claude-physics-project/CLAUDE.md`);
same skeleton, algebra-based content, formulas provided on assessments.
