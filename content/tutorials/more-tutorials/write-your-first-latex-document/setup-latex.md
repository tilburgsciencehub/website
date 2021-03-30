---
tutorialtitle: "Write Your First LaTeX Document in 15 Minutes"
type: "write-your-first-latex-document"
indexexclude: "true"
title: "Setup LaTeX"
description: "Learn to setup your computer to produce LaTeX documents."
keywords: "setup, latex, atom, editor"
weight: 101
draft: false
aliases:
  - /setup/latex
---

## Installation

The first step is to setup a {{< katex >}}\TeX{{< /katex >}} distribution on your machine.

1. If you haven't done it yet, you can read **[our guide](/get/latex)** on how to install $\LaTeX$:

{{% cta-primary-center "How to Install $\LaTeX$" "/get/latex" %}}

2. Once you've installed it, you'll need a text editor to work with. We recommend **[Atom](https://atom.io)**, a free and cross-platform editors with great functions and extra packages. You can download Atom from its official website or read the instructions from [our Building Block](/get/atom). Another great solution is [Visual Studio Code](https://code.visualstudio.com).

3. The last piece of the puzzle: let's setup Atom so that it can run $\LaTeX$. By default, Atom can only work as a general text editor with your `.tex` files. Luckily, there are a number of (free) Atom packages that we can install to boost its functionalities and transform it into a proper $\LaTeX$ editor:
    - `latex`, a package that allows Atom to compile $\LaTeX$ code: [download here](https://atom.io/packages/latex)
    - `language-latex`, a package for syntax highlighting: [download here](https://atom.io/packages/language-latex)
    - (Optional) `pdf-view`, a package for viewing PDF files side-by-side while you work: [download here](https://atom.io/packages/pdf-view)

## Setup

Before starting to write anything, let's setup a directory for this project.

Make a new folder wherever you prefer on your local disk. Then launch Atom, create a new file, and save it with a `.tex` file extension in said folder.

You're finally ready to start writing your first $\LaTeX$ document!
