---
title: 1.12 Sequences review
author: Chris Huson
date: 1 October 2023
presentation:
  width: 1280
  height: 720
  controls: true
  align: left
  center: false
export_on_save:
  html: true
---

<!-- slide -->
#### Standards

**Construct geometric and arithmetic sequences**
**Write a recursive formula for a geometric sequence**
  HSF-IF.A.3 Recognize that sequences are functions, sometimes defined recursively, whose domain is a subset of the integers.
  HSF-BF.A.2 Write arithmetic and geometric sequences both recursively and with an explicit formula, use them to model situations, and translate between the two forms
  HSF-LE.A.2 Construct linear and exponential functions, including arithmetic and geometric sequences, given a graph, a description of a relationship, or two input-output pairs
**Find the sum of a finite geometric series**
  HSA-SSE.B.4 Derive the formula for the sum of a finite geometric series, and use the formula to solve problems.

<!-- slide -->
### Definitions

- **Sequence**: a list of numbers in a specific order
- **Geometric sequence**: a sequence where each term is a constant multiple of the previous term
- **Arithmetic sequence**: a sequence where each term is a constant addition of the previous term

<!-- slide -->
### Function notation

- $y=f(x)$: we say "$f$ of $x$"
- $f: x \rightarrow y$: we say "$f$ maps $x$ to $y$"
- domain: the set of all possible inputs, examples:
  domain = $\{1,2,3,...\}$ 
  ${x \in \mathbb{R}}$ ("$x$ is a member of the set of real numbers")
- range: the set of all possible outputs

<!-- slide -->
### Notation for arithmetic sequences

Functional form: $f(n)=a + dn$ for $n \ge 0$ where

- $d$ is the common difference or rate of change
- $a$ is the initial term

Linear functions form: $f(x)=mx+b$ where

- $m$ is the slope or rate of change
- $b$ is the $y$-intercept or initial value

<!-- slide -->
### Notation for geometric sequences

Functional form: $g(n)=a \times r^n$ for $n \ge 0$ where

- $r$ is the common ratio or growth rate
- $a$ is the initial term when $n=0$

Exponential function form: $g(x)=a \times b^x$ where

- $b$ is the base or growth factor
- $a$ is the $y$-intercept or initial value

<!-- slide -->
### Recursive and explicit definitions of arithmetic sequences

- Recursive:  
$f(0)=a$\
$f(n)=f(n-1)+d$ for $n \ge 1$
- Explicit:
$f(n)=a+dn$ for $n \ge 0$

<!-- slide -->
### Write recursive and explicit definitions

$f(0)=2$, $f(1)=6$, $f(2)=10$, $f(3)=14$, ...

<!-- slide -->
### Solution

$f(0)=2$, $f(1)=6$, $f(2)=10$, $f(3)=14$, ...

- Recursive formula:
$f(0)=2$\
$f(n)=f(n-1)+4$ for $n \ge 1$
&nbsp;
- Explicit formula:
$f(n)=2+4n$ for $n \ge 0$

<!-- slide -->
### Write recursive and explicit definitions

$n$ | $f(n)$
--- | ---
1 | 3
2 | 6
3 | 12

<!-- slide -->
$n$ | $f(n)$
--- | ---
1 | 3
2 | 6
3 | 12

- Solution Recursive formula:
$f(1)=3$\
$f(n)=f(n-1) \times 2$ for $n \ge 2$
&nbsp;
- Explicit formula:
$\displaystyle f(n)=3 \times 2^{n-1}$ for $n \ge 1$
