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
| `docs/physics/` | **Active** — 9th-grade physics, current year (2026–27), own `preamble.tex`. Prior year archived at `Physics2026/` |
| `docs/Italian-maturita/` | Active occasionally — Italian exam translations, self-contained `.tex` |
| Year folders at root (`IB2023/`, `Geom2023/`, `Precalc2024/`, `Physics2026/`, …) | **Frozen archive** — do not edit; old documents must keep compiling with their local preambles |

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

### `_MS` vs `-solutions` — both courses

The two suffixes mean different things and are not interchangeable:

| Suffix | What it is | Who makes it |
| --- | --- | --- |
| `<stem>_MS.tex` / `.pdf` | The **official typeset solutions** (markscheme) for a problem set | Authored — agents write these |
| `<stem>-solutions.pdf` | A **scan of Chris's handwritten** worked solutions | Chris scans these; never generated |

Agents name every solutions document they author `_MS` — never
`-solutions`, which would collide with the scans. Applies to physics as
well as IB Math (adopted 2026-09-17). Physics files written before that
date use `-solutions` for typeset solutions (`Physics2026/`); leave those
alone, and name new ones `_MS`.

Physics conventions: see the physics project
(`~/Documents/Professional/Physics/claude-physics-project/CLAUDE.md`);
same skeleton, algebra-based content, formulas provided on assessments.
