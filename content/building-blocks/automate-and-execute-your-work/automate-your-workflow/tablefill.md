---
title: "Tablefill for Reproducible Tables"
description: "Learn how to use the function tablefill in R to create reproducible tables and autofill values."
keywords: "autofilling, tablefill, latex, lyx, markdown"

weight: 3
aliases:
 - /tablefill/
---

## Why should you use Tablefill?

Tablefill allows to automatically update Latex, LyX and Markdown tables. Its primary aim is to create reproducible reports, which can be automatically updated.

## How to install Tablefill?
Run the following code in the command line (Windows) or terminal (Mac).

{{% codeblock %}}
```shell script
pip install git+https://github.com/mcaceresb/tablefill
tablefill --help
```

### Example repository


{{% cta-primary-center "Go to the GitHub Repository now" "https://github.com/tilburgsciencehub/tableFill.git" %}}



```text
docker-demo
│
├── code
│   ├── packages.R  ....................... necessary packages to run the R script
│   ├── r-script.R  ....................... creates a histogram, saves it in \gen folder
│   ├── pyscript.py ....................... draws random normal sample, saves it in \data folder
│   ├── requirements.txt .................. library needed for pyscript
│   └── run.sh ............................ shell instruction to run both scripts
├── data
│   
└── gen
│
└── Dockerfile
```





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
