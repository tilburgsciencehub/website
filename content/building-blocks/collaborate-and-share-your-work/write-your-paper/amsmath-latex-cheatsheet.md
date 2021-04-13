---
title: "Cheatsheet for LaTeX Math Commands"
description: "Explore all the most important AMS-Math LaTeX commands and download your cheatsheet."
keywords: "ams, math, latex, tex, cheatsheet"
#weight: 105
#date: 2020-11-11T22:02:51+05:30
draft: false
author: "Manuele Macchia"
authorLink: "https://manuelemacchia.com"
aliases:
  - /learn/latex-math
---

## Overview

This is a quick overview of the main {{< katex >}}\LaTeX{{< /katex >}} commands to render mathematical expressions.

We also provide a compiled PDF version of this cheatsheet.

{{% cta-primary "Download the PDF Cheatsheet" "https://github.com/manuelemacchia/math-latex/raw/master/amsmath.pdf" %}}

## Commands

### Packages
The main package to load is `amsmath`. More symbols are included in `amssymb`.

{{% tip %}}
You can load packages in the preamble: `\usepackage{amsmath}`
{{% /tip %}}

### Typeset
- For text style (inline) math, use: `$...$`. This is inline: $E=mc^2$
- For display style math, which breaks the paragraph: `\begin{equation} ... \end{equation}` (numbered equation) or `\[ ... \]` (non-numbered). This is a display equation: $$E=mc^2$$

### Greek letters
#### Lowercase
|  |  |  |  |  |  |  
|-------------|-------------|------------|------------|---------------|---------------|
| $\alpha$    | `\alpha`    | $\beta$    | `\beta`    | $\gamma$      | `\gamma`      |
| $\delta$    | `\delta`    | $\epsilon$ | `\epsilon` | $\varepsilon$ | `\varepsilon` |
| $\zeta$     | `\zeta`     | $\eta$     | `\eta`     | $\theta$       | `\theta`      |
| $\vartheta$ | `\vartheta` | $\iota$    | `\iota`    | $\kappa$      | `\kappa`      |
| $\lambda$   | `\lambda`   | $\mu$      | `\mu`      | $\nu$         | `\nu`         |
| $\xi$       | `\xi`       | $\pi$      | `\pi`      | $\varpi$      | `\varpi`      |
| $\rho$      | `\rho`      | $\varrho$  | `\varrho`  | $\sigma$      | `\sigma`      |
| $\tau$      | `\tau`      | $\upsilon$ | `\upsilon` | $\phi$        | `\phi`        |
| $\varphi$   | `\varphi`   | $\chi$     | `\chi`     | $\psi$        | `\psi`        |
| $\omega$    | `\omega`    |

#### Uppercase
|  |  |  |  |  |  |
|-------------|-------------|------------|------------|---------------|---------------|
| $\Gamma$    | `\Gamma`    | $\Delta$   | `\Delta`   | $\Theta$      | `\Theta`      |
| $\Lambda$   | `\Lambda`   | $\Xi$      | `\Xi`      | $\Pi$         | `\Pi`         |
| $\Sigma$    | `\Sigma`    | $\Upsilon$ | `\Upsilon` | $\Phi$        | `\Phi`        |
| $\Psi$      | `\Psi`      | $\Omega$   | `\Omega`   |

{{% tip %}}
To ensure a consistent style throughout the document, use:
```latex
\renewcommand{\epsilon}{\varepsilon}  
\renewcommand{\theta}{\vartheta}  
\renewcommand{\rho}{\varrho}  
\renewcommand{\phi}{\varphi}
```
{{% /tip %}}

### Mathematical font
$$\mathcal{A} \\, \mathcal{B} \\, \mathcal{C} \\, \mathcal{D} \\, \mathcal{E} \\, \mathcal{F} \\, \mathcal{G} \\, \mathcal{H} \\, \mathcal{I} \\, \mathcal{J} \\, \mathcal{K} \\, \mathcal{L} \\, \mathcal{M} \\, \mathcal{N} \\, \mathcal{O} \\, \mathcal{P} \\, \mathcal{Q} \\, \mathcal{R} \\, \mathcal{S} \\, \mathcal{T} \\, \mathcal{U} \\, \mathcal{V} \\, \mathcal{W} \\, \mathcal{X} \\, \mathcal{Y} \\, \mathcal{Z}$$

Use `\mathcal{\text{letter}}`.

### Superscript and subscript
| $\LaTeX$ | Code | $\LaTeX$ | Code |
|---------|-------|-----------|-------------|
| $x^y$ | `x^y` | $x^{a+b}$ | `x^{a+b}` |
| $x_y$ | `x_y` | $x_{a+b}$ | `x_{a+b}` |

### Root
| Type | $\LaTeX$    | Code    |
|-------------|-----------------|---------------|
| Square root | $\sqrt{x}$    | `\sqrt{x}`    |
| N-th root   | $\sqrt[N]{x}$ | `\sqrt[N]{x}` |

### Dots
| Type | $\LaTeX$    | Code    |
|---------------------|------------|----------|
| Multiplication dot  | $\cdot$  | `\cdot`  |
| Three centered dots | $\cdots$ | `\cdots` |
| Three baseline dots | $\ldots$ | `\ldots` |
| Three diagonal dots | $\ddots$ | `\ddots` |
| Three vertical dots | $\vdots$ | `\vdots` |

### Spaces
| Type | Code |
|----------------|----------|
| Negative space | `\!`     |
| Thinnest space | `\,`     |
| Thin space     | `\:`     |
| Medium space   | `\;`     |
| 1em space      | `\quad`  |
| 2em space      | `\qquad` |

### Braces
| $\LaTeX$ | Code |
|----------------|----------|
| $\overbrace{ ... }^{ \text{text over brace} }$ | `\overbrace{ ... }^{ \text{text over brace} }` |
| $\underbrace{ ... }_{ \text{text under brace} }$ | `\underbrace{ ... }_{ \text{text under brace} }` |

### Accents
| $\LaTeX$ | Code | $\LaTeX$ | Code | $\LaTeX$ | Code |
|---------------|-------------|--------------|------------|-------------------|-----------------|
| $\hat{a}$   | `\hat{a}`   | $\bar{a}$  | `\bar{a}`  | $\mathring{a}$  | `\mathring{a}`  |
| $\check{a}$ | `\check{a}` | $\dot{a}$  | `\dot{a}`  | $\vec{a}$       | `\vec{a}`       |
| $\tilde{a}$  | `\tilde{a}` | $\ddot{a}$ | `\ddot{a}` | $\widehat{AAA}$ | `\widehat{AAA}` |

### Operators

`\sin    \cos    \arcsin    \arccos    \sinh`    
`\cosh    \tan    \arctan    \log    \ln`        
`\max    \min    \sup    \inf    \tanh`    
`\cot    \sec    \csc    \det`    

{{% tip %}}
To define a custom operator:
`\DeclareMathOperator{\argmax}{argmax}`.
{{% /tip %}}

### Modulo
| $\LaTeX$ | Code |
|-----------------------|-----------------------|
| $a \bmod b$           | `a \bmod b`           |
| $a \equiv b \pmod{m}$ | `a \equiv b \pmod{m}` |


### Fractions
`\frac{ ... }{ ... }`

For instance, 3/4 can be displayed as $\frac{3}{4}$.

### Symbol stacking

| $\LaTeX$ | Code |
|-----------------------|-----------------------|
| $\overset{ A }{ B }$ | `\overset{ ... }{ ... }` |
| $\underset{ A }{ B }$ | `\underset{ ... }{ ... }` |

First argument is the main symbol, second argument is the symbol to put over or under the main symbol.

### Big operators
| $\LaTeX$ | Code | $\LaTeX$ | Code |
|---------------------------------|-------------------|--------------------------------|------------------|
| $\displaystyle \int_{a}^{b}$    | `\int_{a}^{b}`    | $\displaystyle \sum_{k=0}^{n}$ | `\sum_{k=0}^{n}` |
| $\displaystyle \prod_{k=0}^{n}$ | `\prod_{k=0}^{n}` | $\displaystyle \lim_{x \to 0}$  | `\lim_{x \to 0}` |

{{% tip %}}
For multiple integrals, use: $\iint$ `\iint` $\\,\\, \iiint$ `\iiint` etc.

For a closed path integral, use: $\oint$ `\oint`
{{% /tip %}}

### Delimiter size
Change the delimiter size by adding one of these modifiers immediately before the delimiter itself: `\big  \Big  \bigg  \Bigg`.

Let $\LaTeX$ determine the correct size using `\left` and `\right` immediately before the opening and closing delimiters, respectively.

### Absolute value and norm
| $\LaTeX$ | Code |
|-------------------|-------------------|
| $\lvert x \rvert$ | `\lvert x \rvert` |
| $\lVert x \rVert$ | `\lVert x \rVert` |

The same can be achieved by defining:
```latex
\usepackage{mathtools}
\DeclarePairedDelimiter{\abs}{\lvert}{\rvert}
\DeclarePairedDelimiter{\norm}{\lVert}{\rVert}
```

Use starred variants `\abs*` and `\norm*` to produce the correct delimiter height for any kind of equation.

### Arrows
| $\LaTeX$ | Code | $\LaTeX$ | Code | $\LaTeX$ | Code |
|----------|------|----------|------|----------|------|
| $\uparrow$ | `\uparrow` | $\downarrow$ | `\downarrow` | $\updownarrow$ | `\updownarrow` |
| $\Uparrow$ | `\Uparrow` | $\Downarrow$ | `\Downarrow` | $\Updownarrow$ | `\Updownarrow` |
| $\leftarrow$      | `\leftarrow` or `\gets` | $\rightarrow$     | `\rightarrow` or `\to` | $\leftrightarrow$ | `\leftrightarrow`       |
| $\Leftarrow$      | `\Leftarrow`          | $\Rightarrow$     | `\Rightarrow`           | $\Leftrightarrow$ | `\Leftrightarrow`     |
| $\mapsto$         | `\mapsto`               | $\longleftarrow$      | `\longleftarrow`      | $\longrightarrow$     | `\longrightarrow`     |
| $\longleftrightarrow$ | `\longleftrightarrow` | $\Longleftarrow$      | `\Longleftarrow`      | $\Longrightarrow$     | `\Longrightarrow`     |
| $\Longleftrightarrow$ | `\Longleftrightarrow` | $\longmapsto$         | `\longmapsto`         |

### Binary relations
| $\LaTeX$ | Code | $\LaTeX$ | Code | $\LaTeX$ | Code |
|-------------|-------------|-------------|-------------|-----------|-----------|
| $\ne$       | `\ne`       | $\le$       | `\le`       | $\ge$     | `\ge`     |
| $\equiv$    | `\equiv`    | $\ll$       | `\ll`       | $\gg$     | `\gg`     |
| $\doteq$    | `\doteq`    | $\sim$      | `\sim`      | $\simeq$  | `\simeq`  |
| $\subset$   | `\subset`   | $\supset$   | `\supset`   | $\approx$ | `\approx` |
| $\subseteq$ | `\subseteq` | $\supseteq$ | `\supseteq` | $\cong$   | `\cong`   |
| $\in$       | `\in`       | $\ni$       | `\ni`       | $\propto$ | `\propto` |
| $\mid$      | `\mid`      | $\parallel$ | `\parallel` | $\perp$   | `\perp`   |

{{% tip %}}
It's possible to negate these symbols by prefixing them with `\not` (for example: $\not\equiv$ with `\not\equiv`).
{{% /tip %}}

### Binary operators
| $\LaTeX$ | Code | $\LaTeX$ | Code | $\LaTeX$ | Code |
|-------------|-------------|-------------|-------------|-----------|-----------|
| $\pm$     | `\pm`     | $\mp$     | `\mp`     | $\cdot$          | `\cdot`          |
| $\div$    | `\div`    | $\times$   | `\times`  | $\setminus$      | `\setminus`      |
| $\star$   | `\star`   | $\cup$    | `\cup`    | $\cap$           | `\cap`           |
| $\ast$    | `\ast`    | $\circ$   | `\circ`   | $\bullet$        | `\bullet`        |
| $\oplus$  | `\oplus`  | $\ominus$ | `\ominus` | $\odot$          | `\odot`          |
| $\oslash$ | `\oslash` | $\otimes$ | `\otimes` | $\smallsetminus$ | `\smallsetminus` |

### Logic symbols
| $\LaTeX$ | Code | $\LaTeX$ | Code | $\LaTeX$ | Code |
|-------------|-------------|-------------|-------------|-----------|-----------|
| $\lor$     | `\lor`     | $\land$    | `\land`    | $\neg$    | `\neg`    |
| $\exists$  | `\exists`  | $\nexists$ | `\nexists` | $\forall$ | `\forall` |
| $\implies$ | `\implies` | $\iff$     | `\iff`     | $\models$ | `\models` |

### Other symbols
| Symbol | $\LaTeX$ | Code |
|--------------------|---------------------|---------------------|
| Infinity           | $\infty$            | `\infty`            |
| Partial derivative | $\partial$          | `\partial`          |
| Empty set          | $\emptyset$         | `\emptyset`         |
| Nabla              | $\nabla$            | `\nabla`            |
| Angle brackets     | $\langle x \rangle$ | `\langle x \rangle` |

### Multi line equation
Use the `multline` environment.
```latex
\begin{multline}
    ...
\end{multline}
```

To align equations, use the `align` environment. Specify the alignment position with `&` and separate equations with `\\`.
```latex
\begin{align}
    ... &= ...\\
    ... &= ...
\end{align}
```

### Vectors
| $\LaTeX$ | Code |
|----------|------|
| $\vec{x}$ | `\vec{x}` |
| $\bm{x}$ | `\bm{x}` |

{{% warning %}}
The `\bm` command requires the `bm` package.
{{% /warning %}}

{{% tip %}}
Best practice to easily switch between types:
```latex
\usepackage{bm}
\renewcommand{\vec}{\bm}
```
{{% /tip %}}

### Arrays
Use the `array` environment. Use `\\` to separate rows, and `&` to separate elements of each row. To produce large delimiters around the array, use `\left` and `\right` followed by the desired delimiter.

{{< katex display >}}
\left(
\begin{array}{lcr}
  a & b & c \\
  d & e & f \\
  g & h & i
\end{array}
\right)
{{< /katex >}}

```latex
\left(
\begin{array}{lcr}
      a & b & c \\
      d & e & f \\
      g & h & i
\end{array}
\right)
```

Each letter in the argument of the array represents a column.
- `l`: left aligned text
- `c`: centered text
- `r`: right aligned text

### Cases
Use the `cases` environment. Use `\\` to separate different cases, and `&` for correct alignment.

{{< katex display >}}
\begin{cases}
  x & \text{if } x > 0 \\
  0 & \text{if } x \le 0
\end{cases}
{{< /katex >}}

```latex
\begin{cases}
  x & \text{if } x > 0 \\
  0 & \text{if } x \le 0
\end{cases}
```

### Matrices
Use one of the following environments.
- `matrix`: No delimiter
- `pmatrix`: $($ delimiter
- `bmatrix`: $[$ delimiter
- `Bmatrix`: $\\{$ delimiter
- `vmatrix`: $\lvert$ delimiter
- `Vmatrix`: $\lVert$ delimiter

Use `\\` to separate different rows, and `&` to separate elements of each row.

{{< katex display >}}
\begin{bmatrix}
      1 & 2 & 3 \\
      4 & 5 & 6 \\
\end{bmatrix}
{{< /katex >}}

```latex
\begin{bmatrix}
      1 & 2 & 3 \\
      4 & 5 & 6 \\
\end{bmatrix}
```

{{% tip %}}
To produce a small matrix, useful for inline math, use the `smallmatrix` environment: $\left[\begin{smallmatrix} a & b \\\\ c & d \end{smallmatrix}\right]$.
```latex
\left[\begin{smallmatrix}
a & b \\\\ c & d
\end{smallmatrix}\right]
```
{{% /tip %}}

### Blackboard bold
$\mathbb{A}$ `\mathbb{A}`
...
$\mathbb{R}$ `\mathbb{R}`

Include the package `bbm` for these symbols. All letters are supported.

{{% cta-secondary "Visit this project's repository" "https://github.com/manuelemacchia/math-latex" %}}
