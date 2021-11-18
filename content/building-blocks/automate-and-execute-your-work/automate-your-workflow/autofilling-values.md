---
title: "Make tables and figures reproducible with Autofilling Values"
description: "Learn how to use R to check for errors and the completion of Stata code in batch mode or in a Makefile."
keywords: "autofilling, tablefill, latex, lyx"

weight: 3
aliases:
 - /autofilling-values/
---

## Hard-coded values

To facilitate reproducibility, figures and tables should always be generated programmatically and never include hard-coded values. The `tablefill` package of [gslab_make](https://github.com/gslab-econ/gslab_make) is a useful tool to help create complex tables.

## In-text values

Frequently, it is necessary to include values derived from calculations in the text of a document. For example, we may wish to reference a coefficient from a regression specification. To facilitate reproducibility and avoid text from becoming outdated, it is recommended to include values programatically. Below, we detail methods for doing so.

### LyX

1. Go to `Document`, `Settings`, and then `LaTeX Preamble`. Paste in the following. Here, `scalars` refers to a `scalars.tex` file located in the same directory as the LyX document. You may rename `scalars` according to your preferences. For example, `\input{../more_scalars}` would refer to a `more_scalars.tex` file located in the parent directory of the LyX document.

```
\input{scalars}
```

2. Using a program of your choice (e.g., Stata), generate file `scalars.tex` with the following. Here, `value` refers to the value you wish to include in the document. You may rename `scalarmath` and `scalartext` according to your preferences. Note that LaTeX places restrictions on how [new commands](https://en.wikibooks.org/wiki/LaTeX/Macros#New_commands) may be named.

```
\newcommand{\scalarmath}{value}
\newcommand{\scalartext}{\textnormal{value}}
```

3. Use the macro `\scalarmath` to display the value in math mode. Use the macro `\scalartext` to display the value in text mode.

### LaTeX

1. In the document preamble, paste in the following. Here, `scalars` refers to a `scalars.tex` file located in the same directory as the LyX document. You may rename `scalars` according to your preferences. For example, `\input{../more_scalars}` would refer to a `more_scalars.tex` file located in the parent directory of the LyX document.

```
\input{scalars}
```

2. Using a program of your choice (e.g., Stata), generate file `scalars.tex` with the following. Here, `value` refers to the value you wish to include in the document. You may rename `scalarmath` and `scalartext` according to your preferences. Note that LaTeX places restrictions on how [new commands](https://en.wikibooks.org/wiki/LaTeX/Macros#New_commands) may be named.

```
\newcommand{\scalarmath}{value}
\newcommand{\scalartext}{\textnormal{value}}
```  

3. Use the macro `\scalarmath` to display the value in math mode. Use the macro `\scalartext` to display the value in text mode.

{{% tip %}}
In cases where including a hard-coded value in-text is unavoidable, include a red LaTeX comment for fact-checking. Yellow LyX comments should be used for comments between coauthors to be resolved and deleted.
{{% /tip %}}
