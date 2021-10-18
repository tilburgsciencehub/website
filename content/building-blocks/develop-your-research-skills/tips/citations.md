---
title: "How to cite in text"
description: "Cite efficiently and according to a style guide/formats"
keywords: "citation, reference, bibtex, formats, literature"
weight: 3
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /citations/formats
---
# Efficiently citing sources in academic writing

## Citation Styles
Many academic journals, publishers or university departments require a specific citation style. If that is the case, check their guidelines. However, if nothing is specified you still have to choose one and be consistent with it.

Which style should be chosen? Usually your choice will depend on your field/discipline or even country of publication. For instance, APA is one of the most common styles for social sciences, MLA in humanities, AMA in medicine, OSCOLA for law in the UK mainly etc.

Luckily enough if you use the right tools changing from one style to another comes at no additional effort.

## Citing in LaTex
To cite in LaTeX make sure you have a `.bib` file in the same folder as your`.tex` file.

### Choose your citation style

```LaTex
\bibliographystyle{stylename}
```

### Cite in text
 The basic command to add citation in text is `\cite{label}`.

#### Natbib
The package Natbib can be employed by adding `\usepackage{natbib}` in the preambule of your document. Natbib allows you to modify how your citations in the text appear. The table below describes some examples of additional citation commands that come with Natbib:

<center>

| Command       |               Description                | Example |
| ------------- |:----------------------------------------:| -------:|
| \citet{}      |             Textual citation             |   $1600 |
| \citep{}      |          Parenthetical citation          |     $12 |
| \citeauthor{} |  Prints only the name of the authors(s)  |      $1 |
| \citeyear{}   | Prints only the year of the publication. |      $1 |

</center>

### Print your formatted references
```LaTex
\bibliography{bibfile} %Wherever you want your references to be printed
```

{{% tip %}}
 To cite efficiently in LaTeX export your references to a `.bib` file straight from a reference management tool. This way, you avoid manually typing in the references or downloading them one by one from the journal.

  - Not familiar with reference management tools? Check our [building block](https://tilburgsciencehub.com/building-blocks/develop-your-research-skills/tips/reference-list/)

{{% /tip %}}


## Citing in Word
Prefer Word to LaTeX? Well, though not as easy as in LaTeX,
