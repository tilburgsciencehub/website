---
title: "Citation Management within Rmarkdown"
description: "This article discusses Rmarkdown usage for academic writing, focussing on citation management within an Rmarkdown document. It provides a step by step procedure of the integration of bibliographic references, starting the process for creating scholarly articles, books, and technical reports."
keywords: "Rmarkdown, R, bookdown, LaTeX, BibTeX"
draft: false
weight: 1
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /Rmarkdown/Citations
  - /Bibtex
---

## Overview

[`Rmarkdown`](https://rmarkdown.rstudio.com/) is a format designed for building reproducible and dynamic reports using R. It's a useful tool for creating a wide range of academic documents, including journal articles, books, technical reports or assignments. 

This article includes a step by step procedure for citation management in Rmarkdown documents. This topic is intended to increase your capabilities to produce well-organized and professionally formatted Rmarkdown documents, further supporting your academic writing process.

Download the article's accompanying files [here](citation-management-rmarkdown.zip) (a .zip archive). Right-click and select "Download file as" to save them to your desired location. Use these files for a hands-on learning experience to improve your conceptual understanding.

{{% tip %}}

For students working on their thesis, consider using the tisemdown thesis [template](/get/latex-templates) available on our website. It's a pre-configured Rmarkdown template designed to meet the formatting standards of different study programs, simplifying the initial setup of your thesis work.

{{% /tip %}}

## Citations 
This section will walk you through the process of inserting citations in `RMarkdown` documents. This includes a step-by-step procedure for setting up a bibliography file, how to cite sources within your text, and customizing the location of your bibliography section. 

### Citing Articles & Bibliography 

**Step 1: Create or Obtain a `BibTeX` File**

A `BibTeX` file, identified by a .bib extension, organizes references in a structured, machine-readable format. While manual creation is an option, we recommend using citation management tools like [Zotero](https://www.zotero.org/) or [citr addin](https://github.com/crsh/citr). In addition, get the citation of R packages using the `citation()` function. Check out this [article](/reference/list) for a more in-depth approach.

Here's an example of the general syntax for manually recording a reference in a .bib file:

{{% codeblock %}}

```plaintext        

@article{key,
  author = {Author, A. and Author, B. and Cuthor, C.},
  year = {2024},
  title = {Title of the article},
  journal = {Journal of the article},
  volume = {1},
  number = {2},
  pages = {3-4},
  month = {5},
  url = {http://www.url.com}
}

{{% /codeblock %}}

Here's an example **for R and R packages**, using the `citation()` function:

{{% codeblock %}}

```R
# Citation for R
citation()

# Citation for a specific package (e.g., ggplot2)
citation("ggplot2")
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/citation-rmarkdown.PNG" width="300">
</p>

**Step 2: Link A `BibTeX` File in the YAML Header**

Start with linking your .bib file in the `RMarkdown` document's YAML header. This file contains your reference list in a specific `LaTeX` format. Insert the following code into the `YAML` header, substituting "directory"/"subdirectory"/bibliography.bib with the pathway and name of your `BibTeX` file:

{{% codeblock %}}

```plaintext
---
title: "Your title here" 
author: "Your name here"
output: html_document  
# Specify the location of the bibliography below  
bibliography: "directory"/"subdirectory"/bibliography.bib  
--- 
```
{{% /codeblock %}}

**Step 3: Enable Linking Citations**

To link in-text citations directly to their bibliography entry, add `link-citations: yes` in your YAML header:

{{% codeblock %}}

```plaintext
---
title: "Your title here" 
author: "Your name here"
output: html_document  
bibliography: "directory"/"subdirectory"/bibliography.bib  
# Switch on in-text citations
link-citations: yes
--- 
```
{{% /codeblock %}}

**Step 4: Add In-Text Citations**

Inside referencing within your report can be achieved using the `@key` syntax inside the markdown part. The key matches the citation key in your `.bib` file. Using the syntax within your document adds dynamic links to the corresponding reference in the bibliography section. For citing several sources at once, use semicolons to divide the keys, like this: `[@key-1; @key-2; @key-3]`. 

{{% tip %}}
To exclude the author's name from the citation, place a minus sign before the @ symbol, for example, [-@key-1].
{{% /tip %}}

### Changing the Citation Style

In `RMarkdown` documents, the default format for citations and references is the Chicago author-date style. If you're looking to employ a different citation style, this can be achieved by specifying a Citation Style Language (CSL) file in the `csl` field within the YAML metadata.

For example, if you wish to adopt the APA citation style, your YAML header should be adjusted as follows:

{{% codeblock %}}
```plaintext
---
output: html_document
bibliography: references.bib
# Ensure the CSL file path is correctly specified
## In this example, the apa.csl file is located in the same directory as the .Rmd file
csl: apa.csl
---
{{% /codeblock %}}

It's important to note that the CSL file, such as `apa.csl` for the APA style, needs to be downloaded and be referenced by the correct pathway to its current directory. To procure a CSL file aligned with your preferred citation style, the [Zotero Style Repository](https://www.zotero.org/styles) is an helpful source. This website allows users to easily find and download the necessary CSL file.

### Biblography Management

`Rmarkdown` only adds mentioned references in the bibliography. For some articlces, it is needed to include certain references in your bibliography without citing them directly in your text, or it is necesary to display every item in your bibliography regardless of citation. This can be achieved using the `nocite` metadata field in your document's YAML header.

To add specific items without in-text citations:

{{% codeblock %}}
```plaintext
---
nocite: |
  @item1, @item2
---
```
{{% /codeblock %}}

And to ensure all items from your bibliography are displayed:

{{% codeblock %}}
```plaintext
---
nocite: '@*'
---
```
{{% /codeblock %}}

These configurations allow you to manually include specific references or automatically list all entries in the bibliography.

#### Changing the Bibliography Location

By default, bibliographies appear at the document's end. To relocate the bibliography, set the output format to `bookdown::html_document2` (or equivalent for other formats) in the YAML and use the `<div id="refs"></div>` tag to specify the new location. 

{{% codeblock %}}

```plaintext       

# References 
<div id="refs"></div>

# More information

This will be Appendix A.

# One more thing

This will be Appendix B.

{{% /codeblock %}}

{{% summary %}}

This article discusses the process of citation management within `Rmarkdown` for academic writing, Specifically, it guides through:

- Creating and linking a `BibTeX` file to streamline reference management, including manual entry examples and using the `citation()` function for R packages.
- Dynamically inserting citations into the text, with tips on using multiple citations and excluding author names.
- Customizing the bibliography section's location and including unreferenced items or displaying all bibliography entries.
- Adjusting citation styles by specifying a CSL file, with an example of adopting APA style.

{{% /summary %}}