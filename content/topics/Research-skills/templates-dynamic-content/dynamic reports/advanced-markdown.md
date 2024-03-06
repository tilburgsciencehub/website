---
title: "Advanced Markdown Syntax for Writing Reports with Rmarkdown"
description: "This article discusses Rmarkdown usage for academic writing. Covering citation management, cross-referencing, figure formatting, and dynamic LaTeX equations."
keywords: "Rmarkdown, R, bookdown, LaTeX, BibTeX, equatiomatic,"
draft: false
weight: 1
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /Rmarkdown/advanced
  - /bookdown
  - /LaTeX/equations/equatiomatic
  - /dynamic/reports
---

## Overview

[`Rmarkdown`](https://rmarkdown.rstudio.com/) is a format designed for crafting reproducible and dynamic reports using R. It's a useful tool for creating a wide range of academic documents, including journal articles, books, and technical reports. 

Our website offers the `tisemdown` thesis [template](/topics/share-your-results-and-project/write-your-paper/bookdown-theses), which provides a read-to-go thesis template using `Rmarkdown`. This template pre-configures all the formatting requirements of your study programs, kickstarting the initial setup process. 

This article builds upon the thesis template article by exploring more sophisticated `Rmarkdown` syntax. While the initial guide covers basic syntax, here we further your understanding by covering:
- Efficient citation referencing and bibliography management.
- Techniques for cross-referencing figures and tables within your text.
- Advanced academic formatting tips: 
  - figure customization, 
  - subfigure integration, 
  - embedding regression results directly into `LaTeX`-formatted equations.

{{% example %}}

This article is structured arbitrarily, therefore feel free to directly access topics of interest.

- For the citations, bibliography, and cross-referencing section, access the corresponding RMarkdown file by clicking [here](R-markdown-advanced-citation.Rmd).
- To learn about the formatting of figures and the incorporation of subfigures, download the relevant RMarkdown guide [here](R-markdown-advanced-formatting-figures.Rmd).
- If you're interested in the automatic conversion of regression results into LaTeX-formatted equations, obtain the RMarkdown file [here](R-markdown-advanced-dynamic-equations.Rmd).
  
{{% /example %}}

## Citations 
This section will walk you through the process of inserting citations in `RMarkdown` documents. This includes a step-by-step procedure for setting up a bibliography file, how to cite sources within your text, and customizing the location of your bibliography section. 

### Citing Articles & Bibliography 

**Step 1: Create or Obtain a `BibTeX` File**

A `BibTeX` file, identified by a .bib extension, organizes references in a structured, machine-readable format. While manual creation is an option, We recommend using citation management tools like [Zotero](https://www.zotero.org/) or [citr addin](https://github.com/crsh/citr). In addition, get the citation of R packages using the `citation()` function. Check out this [article](/reference/list) for a more in-depth approach.

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

{{% tip %}}

Be sure to save the .bib file in the same working directory as your .Rmd file!

{{% /tip %}}

**Step 2: Link A `BibTeX` File in the YAML Header**

Start with linking your .bib file in the `RMarkdown` document's YAML header. This file contains your reference list in a specific `LaTeX` format. Insert the following code into the `YAML` header, substituting "Yourpathway"/"subdirectory"/bibliography.bib with the pathway and name of your `BibTeX` file:

{{% codeblock %}}

```plaintext
---
title: "Your title here" 
author: "Your name here"
output: html_document  
# Specify the location of the bibliography below  
bibliography: "Your-pathway"/"subdirectory"/bibliography.bib  
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
bibliography: "Your-pathway"/"subdirectory"/bibliography.bib  
# Switch on in-text citations
link-citations: yes
--- 
```
{{% /codeblock %}}

**Step 4: Add In-Text Citations**

Inside referencing within your report can be achieved using the `@key` syntax inside the markdown part. The key matches the citation key in your .bib file. Using the syntax within your document adds dynamic links to the corresponding reference in the bibliography section.

### How to move the bibliography location

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

## Referencing: Figures, Tables & Sections

### Set-up
When writing your report, you often encounter the need to refer to a table or figure within your document. The `bookdown` package supports cross-referencing elements within documents. A feature that is not available in the default `Rmarkdown` output formats. By setting the output to one of the `bookdown` formats, features such as automatic numbering and hyperlinks for figures, tables, and sections are enabled. Here's how to specify these settings in the YAML header.

{{% codeblock %}}

```plaintext
---
title: "Your title here" 
author: "Your name here"
output:
  bookdown::pdf_document2  # For PDF documents
  bookdown::html_document2 # For HTML documents
  bookdown::word_document2 # For Word documents
bibliography: bib/thesis.bib  
link-citations: yes
--- 
```
{{% /codeblock %}}

### Referring Figures

To cite a figure within your document, use the syntax `Figure \@ref(fig:your-chunk-name)`, where _your-chunk-name_ is the label you assign to the figure's code chunk. This setup allows for dynamic linking to figures generated from code chunks. 

Here is an example which visualizes GDP per capita trends in the Netherlands:

{{% codeblock %}}

```R
# Your R code Chunk 
 {r visualization-netherlands, 
    fig.cap = "From 1952 to 2007, the GDP per capita in the Netherlands saw a generally steady upward trend. There was a notable exception between 1977 and 1982 when this growth did not follow the usual linear pattern." # Adding a caption
    }

library(ggplot2)
library(dplyr)
library(gapminder)
gapminder %>%
  filter(country == "Netherlands") %>%
  ggplot(aes(x = year,
             y = gdpPercap)) + 
  geom_point()

# Specify this outside the code chunk: in the Markdown
GDP per capita in the Netherlands is higher than in the last 50 years!
(See Figure \@ref(fig:visualization-netherlands))
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/cross-referencing-figures-rmarkdown.PNG" width=500">
</p>

### Referring Tables
The same method can be applied for referring to tables inside your report. Use the syntax: `Table \@ref(tab:chunk-name)`. Again the _chunk-name_ is the label you assign to the table's code chunk.

We recommend creating tables from your data frames with the `knitr::kable` function. `kable` takes a data.frame as input, and outputs the table into a `markdown` table, which will be rendered into the appropriate output format.

{{% codeblock %}}

```R
# R Code Chunk
## {r table-netherlands, echo = FALSE, warning= FALSE, message = FALSE}
gapminder %>%
  filter(country == "Netherlands") %>%
  head() %>%
  knitr::kable(caption = "Raw gapminder data for the Netherlands", digits = 2)

## Specify this outside the code chunk: in the Markdown
We can see above in Table \@ref(tab:table-netherlands) the raw data used to create Figure \@ref(fig:visualization-netherlands).
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/cross-referecing-tables-rmarkdown.PNG" width=500">
</p>

### Referencing a section

To mention sections within your text, use the syntax: `Section \@ref(section-name)`. The `section-name` name refers to a header in your document containing a unique identifier (`{#section-name}`). This approach helps readers navigate to another section within your report with a single mouse click. 

For example, if you download the `Rmarkdown` file to create this article the section `# Citations` is labelled with the unique identifier `{#citing-sections}` and is now clickable with the syntax `Section \@ref(citing-sections)`

Used syntax inside the header: `# Citations {#citing-sections}`.

{{% tip %}}

The unique identifier is called a `slug` and is designed so it can not start with a number. Otherwise, it will print out the `slug`:
- This would not work: `## Section 4 {#section-4}`.
- Write instead: `## Section 4 {#section-four}`.

{{% /tip %}}

## Formatting of Figures

### Formatting through Chunk Options

`RMarkdown` enables figures to be formatted through chunk options, enabling full control over their presentation within your report. 

Here is a list of important figure formatting options: 

-   `fig.align`: Adjust the alignment of your figure. 
	- Options include "default", "center", "left", or "right".
-   `fig.cap`: Allows you to provide a caption for your figure, input as a character vector:
	- For instance, "A detailed caption here".
-   `fig.height` & `fig.width`: Specify the dimensions of your figure in inches.
	- each argument takes one number (e.g., 7, or 9).
-   `out.height` & `out.width`: Adjust the size of the figure in the output document, useful for scaling figures. 
	- For `LaTeX` outputs, use dimensions like `".12\linewidth"` or "`10cm`"; 
	- For `HTML`, use "`300px`".

Here's an example of how to use these options in a code chunk:

{{% codeblock %}}

```R
# Code Chunk specification
{r example-figure, echo=FALSE, warning=F, message=F, eval = F, 
    fig.cap="GDP per capita growth in the Netherlands, 1952-2007", 
    fig.width=7, 
    fig.height=5, 
    fig.align="left", 
    out.width="50%"}

# Code 
library(ggplot2)
library(dplyr)
library(gapminder)

gapminder %>%
  filter(country == "Netherlands") %>%
  ggplot(aes(x = year, y = gdpPercap)) + 
  geom_point()
```

{{% /codeblock %}}

And it will look like this:

<p align = "center">
<img src = "../images/formatting-chunk-figures.PNG" width=300">
</p>

### Formatting through Setting Global Figure Options

To avoid setting the same chunk options for each figure and to ensure uniform formatting across figures, set global options at the start of the document. This approach applies specified settings to all figures, saving time and ensuring consistency. You can do this with the following code:

{{% codeblock %}}

```R
knitr::opts_chunk$set(fig.width = "Your Settings", fig.height = "Your Settings", fig.align='Your Settings', out.width = "Your Settings")
```

{{% /codeblock %}}

### Saving Figures

Adjusting the display properties of figures can alter their presentation within the document, but it doesn't automatically save them as separate files. To ensure figures are saved, you must modify the YAML header to include `keep_md: true`, as shown below:

{{% codeblock %}}

```plaintext
---
output:
  html_document, pdf_document, word_document, or any other format:
    keep_md: true
--- 
```
{{% /codeblock %}}

This setup generates folders like "YOURFILENAME_files" to store figures. To directly control where your figures are saved, use the `fig.path` option in a setup chunk at the start of your document. Setting `fig.path` tells `RMarkdown` the exact folder to store your figures. For example, to save all figures in a folder named "figs", add this to a code chunk within your document:

{{% codeblock %}}

```R
knitr::opts_chunk$set(fig.path = "figs")
```

{{% /codeblock %}}

## Using Latex for Formatting of Figures

### LaTeX sub-figures

Display sub-figures inside into a single space, using the `LaTeX`'s `subfig` package. This package enables the use of sub-figures, each with its own caption, within a single-figure environment. This feature can be useful for comparative analyses or grouped visual data presentations. To use sub-figures, include the `subfig` package in your document's YAML via the `extra_dependencies` option as shown below:


{{% codeblock %}}

```plaintext
---
output:
  "Your Output Format":
    extra_dependencies: "subfig"
--- 
```
{{% /codeblock %}}

To create a single figure with sub-figures, place all related plots within a single R code chunk. Specify the following arguments:
 - Use the `fig.cap` option for the main caption and 
-  Use `fig.subcap` for individual sub-figure captions. 
   -  This is a character vector for sub-figures, for example, `c('(1)', '(2)', '(3)')`.
- Use `fig.ncol` for figures arrangement by column 
  - By default, all plots are arranged in a single row. You can break them into multiple rows.
- Use `out.width` for controlling plot size 
  - Standard practice is to divide 100% by the number of columns to ensure equal width for all plots. Otherwise, the plots may exceed the page margin.

Example syntax for arranging three sub-figures into two columns with centred alignment:

{{% codeblock %}}

```R
# Code chunk specification
{r, fig.cap='Figure about LaTeX sub-figures', fig.subcap=c('(1)', '(2)', '(3)'), fig.ncol=2, out.width="50%", fig.align="center"}

# Your R code for the sub-figures
plot(1:10)
boxplot(Sepal.Width ~ Species, data = iris)
hist(rnorm(100))
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/subfigures-rmarkdown.PNG" width=400">
</p>

This setup ensures that each sub-figure is properly captioned and aligned, facilitating a coherent and visually appealing presentation in your document.

## Dynamic Latex Equations

### Convert Regression Models Directly into Latex Equations

The `equatiomatic` package provides an elegant solution for displaying `LaTeX`-formatted equations derived from models specified in the report's R code. Let's delve into its capabilities with practical examples:

#### A Simple Regression Model
Transform a model into `LaTeX`, by passing your model inside `extract_eq()`:

{{% codeblock %}}

```R
# To install equatiomatic, you can use: 
## remotes::install_github("datalorax/equatiomatic")
## install.packages("equatiomatic")
library(equatiomatic)

# create your model:
fit <- lm(mpg ~ cyl + disp, mtcars)

# Display the theoretical model as an equation
equatiomatic::extract_eq(fit)

# For the model with actual coefficients:
equatiomatic::extract_eq(fit, use_coefs = TRUE)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/equatiomatic-1.PNG" width=400">
<img src = "../images/equatiomatic-2.PNG" width=400">
</p>


#### Categorical Variables

The `equatiomatic` package supports the automatic conversion of categorical variables to `LaTeX` formatted equations. When using categorical variables, it will recognize and automatically include the levels of these variables as subscripted variables in the equation.

{{% codeblock %}}

```R
fit_cat <- lm(Sepal.Length ~ Species, iris)
equatiomatic::extract_eq(fit_cat)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/equatiomatic-3.PNG" width=400">
</p>


#### Interaction terms

The package also supports the conversion of interaction terms to `LaTeX` formatted equations.

{{% codeblock %}}

```R
fit_int <- lm(data = iris, Sepal.Length ~ Species * Petal.Length)
equatiomatic::extract_eq(fit_int)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/equatiomatic-4.PNG" width=400">
</p>

#### Customizing the Output

Adjust the equation output using the following options: 
- `use_coefs`: This option reveals the actual coefficients within the model. 
  - Default = FALSE
- `terms_per_line`: Organizes the equation to display a specific number of terms on the equation's right-hand side. 
- `wrap`: Ensures the equation fits within a predetermined width.

{{% codeblock %}}

```R
library(palmerpenguins)
fit_glm <- glm(species ~ bill_length_mm + bill_depth_mm + flipper_length_mm, data = penguins, family = binomial)
equatiomatic::extract_eq(fit_glm, use_coefs = TRUE, terms_per_line = 3, wrap = 80)

fit_probit <- glm(species ~ bill_length_mm + bill_depth_mm + flipper_length_mm, data = penguins, family = binomial(link = "probit"))
equatiomatic::extract_eq(fit_probit, use_coefs = FALSE, terms_per_line = 2, wrap = 40)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../images/equatiomatic-5.PNG" width=400">
<img src = "../images/equatiomatic-6.PNG" width=400">
</p>

{{% summary %}}

This article discussed some advanced uses of `Rmarkdown` for academic writing, building upon a basic understanding to introduce sophisticated markdown syntax and features. Specifically, it guides through:

- Creating and linking a `BibTeX` file for citations.
- Dynamically inserting citations within the text and customizing the bibliography section's location.
- Utilizing `bookdown` for cross-referencing figures, tables, and sections within documents.
- Formatting figures through chunk options and global settings, including alignment, dimensions, and captions, to ensure a consistent presentation.
- Saving figures automatically and specifying storage locations to streamline document organization.
- Incorporating `LaTeX` for advanced figure formatting, such as creating sub-figures within a single-figure environment.
- Converting regression models to `LaTeX`-formatted equations using the `equatiomatic` package, including handling categorical variables and interaction terms, with customization options for equation output.

{{% /summary %}}