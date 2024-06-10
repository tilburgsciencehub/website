---
title: "Pandoc: An Easy Document Converter"
description: "Convert documents of all types, e.g. PDF, Markdown etc., from your command line with Pandoc"
keywords: "pandoc, documents, convert, converting, pdf, markdown"
weight: 1
draft: false
aliases:
  - /pandoc
---

## Overview

[Pandoc](https://www.pandoc.org/) is a powerful command-line tool for converting documents between various formats. It supports a wide range of formats, including Markdown, HTML, LaTex, Word, Jupyter notebooks (.ipynb), PowerPoint, and many others. Pandoc can convert complex syntaxes, such as LaTeX math, document metadata, and tables, and more. 


{{% summary %}}
*Some of its useful features*:

- Easy and quick to use, directly from the command line
- Converts between numerous documents formats
- Free and open-source
- Highly customizable with extensions
- Allows for custom templates for consistent templates
- Supports citations and bibliographies

The [Pandoc User guide](https://pandoc.org/MANUAL#), on which this article is based, is very extensive but provides information on everything. Use the Search (Ctrl+F) function to find something specifically easier.

{{% /summary %}}


## How to install Pandoc

Refer to [this guide](/install/pandoc) for instructions on setting up Pandoc.

## How to use it

To demonstrate how Pandoc can handle formatting and produce a polished outputs, let's convert a basic Markdown file to a PDF. First, save the following content in a file named `example.md`:


{{% codeblock %}}
```markdown
# My First Document

This is a simple markdown document.

## Section 1

Here is some text in section 1.

## Section 2

Here is some text in section 2.
```
{{% /codeblock %}}


{{% warning %}}

By default, Pandoc uses LaTeX to create PDFs, so you need to have a LaTeX engine installed. Refer to the [LaTeX Set up Guide](/get/latex) for setup instructions. If you prefer not to use LaTex, alternative tools are available. Find instructions in the [Pandoc User guide, Creating a PDF section](https://pandoc.org/MANUAL#creating-a-pdf)
{{% /warning %}}


Open a terminal and run the following command:

{{% codeblock %}}
```bash
pandoc example.md -s -o output.pdf 
```
{{% /codeblock %}}

In this command:
- the first file (`example.md`) is the input file
- - `-o` specifies the output file, which is named `output.pdf`
- `-s` (or `-standalone`) tells Pandoc to create a self-standing document, using a template depending on the file format.

Now, check the directory where you ran the command to find the newly created `example.pdf` file. The Markdown content is now beautifully formatted in a PDF document!

<p align = "center">
<img src = "../images/output-pdf.png" width="400">
</p>

{{% tip %}}

You can provide multiple files as input. As a default, Pandoc will combine them into one document with blank lines in between. Use `--file-scope` to process them individually.

{{% /tip %}}


## Useful functions and use cases

While the functions of Pandoc are almost endless, and you can refer to the [User Guide](https://pandoc.org/MANUAL#) for the full options, a few are given here that we think are the most important / useful.
 
### Customized templates

Pandoc allows you to use custom templates to control the look of your documents. Use the `--template` option to specify a custom template. For the default template of a format, you can use `-s` or `-standalone` template to add header and footer material that is needed for a self-standing document. Run `pandoc -D` followed by a format to find the default template used to create. For example, find the default PDF format like this:

{{% codeblock %}}
```bash
pandoc -D latex
```
{{% /codeblock %}}

Or, specify a custom template with `--template`. First make `mytemplate.pdf` yourself (for example, adjust it from the default template). Then, the following command:

{{% codeblock %}}
```bash
pandoc -s --template=mytemplate.pdf -o example.pdf example.md

```
{{% /codeblock %}}


### Citations and bibliographies

Pandoc supports citations and bibliographies, which are essential in academic writing. You can use `--citeproc` to process citations. For example, the following markdown document includes citations, which you can save as `example-citations.md` to follow the example. 

{{% codeblock %}}
```markdown

---
title: "Sample document"
author: "Author name"
bibliography: "references.bib"
---

# Introduction

This is a sample document to demonstrate how Pandoc processes citations. 
Here is a citation to a book [@doe2020book].

# Method

The method used in this research is based on [@smith2019article].

# Results

The results were consistent with those found in earlier studies [@johnson2018study].

# References

```
{{% /codeblock %}}

And the bibliography file (`references.bib`) that is specified in the metadata at the start of the markdown file is:

{{% codeblock %}}
```

@book{doe2020book,
  title     = {Example Book Title},
  author    = {John Doe},
  year      = {2020},
  publisher = {Publisher Name},
}

@article{smith2019article,
  title     = {Example Article Title},
  author    = {Jane Smith},
  journal   = {Journal Name},
  year      = {2019},
  volume    = {10},
  number    = {2},
  pages     = {123--456},
}

@article{johnson2018study,
  title     = {Another Study Title},
  author    = {Alex Johnson},
  journal   = {Another Journal},
  year      = {2018},
  volume    = {5},
  number    = {1},
  pages     = {789--1011},
}

```
{{% /codeblock %}}

The following code with `--citeproc` includes the references taken from the `.bib` file that was specified in the metadata of the markdown file.

{{% codeblock %}}
```bash
pandoc --citeproc -o output-citations.pdf example-citations.md
```
{{% /codeblock %}}

This is a screenshot of the output PDF file:

<p align = "center">
<img src = "../images/output-citations.png" width="400">
</p>

Alternatively, for generating LaTex output that can be processed with `bibtex` (not directly PDF, but a `.tex` file), you can use `--natbib` instead. 


### Math rendering

Pandoc can render mathematical expressions using LaTex, MathML, or other methods. For example, to use KaTeX for fast math rendering in HTML, add `--katex` to your command. Like this markdown file, save it in a file named example-maths.md


{{% codeblock %}}
```markdown
---
title: "Math examples"
author: "Author name"
---

This document contains some math examples.

## Inline Math

Einstein's equation: 

$$
E = mc^2
$$

## Display Math

Integral:

$$
\int_{a}^{b} f(x) \, dx = F(b) - F(a)
$$


Quadratic formula:

$$
x = \frac{{-b \pm \sqrt{{b^2 - 4ac}}}}{{2a}}
$$
```
{{% /codeblock %}}

The following command with --katex behind it will render the maths (otherwise you will get an error).

{{% codeblock %}}
```bash
pandoc example-maths.md -s -o output-maths.html --katex
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/output-maths.png" width="400">
</p>

### Code blocks and syntax highlighting

Pandoc supports syntax highlighting for code blocks. You can specify the language for each code block and Pandoc will highlight it accordingly. 


For example. 

### Extensions

Pandoc has a variety of useful extensions. For example, add support for footnotes with `footnotes`, `task_lists` allows for task lists, `table_captions` enables table captions. Refer to the [Extensions section of the User guide]() for a full list., 

You can add an extension with a + after the code. 


### Creating slide shows

Pandoc can create slide shows from Markdown files, supporting formats like LaTeX Beamer and Powerpoint (`.pptx`). 

Example for LaTex Beamer:

