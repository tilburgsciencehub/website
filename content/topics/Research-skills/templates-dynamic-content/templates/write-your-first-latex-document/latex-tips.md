---
tutorialtitle: "Write Your First LaTeX Document in 15 Minutes"
type: "write-your-first-latex-document"
indexexclude: "true"
title: "Useful Tips"
description: "Learn to write your very first professional-looking document with LaTeX."
keywords: "first, latex, beginner"
weight: 104
draft: false
aliases:
  - /tips/latex
---

Congratulations! You've completed this tutorial. Here are some useful tips when writing with $\LaTeX$.

## Specify The Encoding

It's always a good idea to specify the encoding of your document to allow characters beyond ASCII to be visible. It's recommended to use UTF-8. Unless you know what you're doing, simply add this in your preamble:

```latex
\usepackage[utf8]{inputenc}
```

## Use Labels

This will change your life. One of the greatest features and reasons why you should use $\LaTeX$ for complex documents.

It's a good practice to **always add a label** to virtually anything, so that you can then reference to it in your paper.

Are you creating a new section? Label it. Are you adding a footnote? Label it. Are you adding a figure? Label it. A table? Label it. You get the sense of it.

### Here's how it works

1. Create a label with `\label{marker}`. Place it next to the element you want to label.
2. Reference to it anywhere in your document with `\ref{marker}` or `\pageref{marker}` to print the page number where the element is positioned.

```latex
\section{Dogs}\label{sec:dogs}
Some text.
\section{Cats}
Some more text. A reference to a previous section \ref{sec:dogs}.
```

If, for instance, at the 3rd revision of your paper you decided to swap the two sections, all your cross-reference would still work! The references to your sections, tables, figures, etc. will be automatically updated to follow the new ordering and the new page numbering. Pretty neat, isn't it?

## Use a Reference Management Tool

Nobody writes their `.bib` files manually. It would be an insane amount of work.

You should use, instead, any kind of program that can generate these files for you. Most of the time, these are great tools that can also work as a "vault" for all your papers. You can use them to manage your library of references, categorize them, tag them, add notes, and so on. The following are the most famous ones that we recommend:

- [Zotero](https://www.zotero.org)
- [Mendeley](https://www.mendeley.com)
- The old and trusty [BibDesk](https://bibdesk.sourceforge.io)

## Useful Packages

Here's a list of the most used packages.

- `amsmath`, `amsfonts`, `amssymb` for awesome math typesetting
- `tikz` to draw almost any vector graphic you'll ever need
- `geometry` to resize elements, control margins, text areas, etc.
- `hyperref` to have hyperlinks within the text
- `lipsum` to generate random text, useful for prototyping

## See Also

- A very [comprehensive wiki](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) about $\LaTeX$
- A [good guide](https://www.learnlatex.org) to learn $\LaTeX$
