---
title: "Pandoc: An Easy Document Converter"
description: "Convert document formats directly from the command line with Pandoc"
keywords: "pandoc, documents, convert, converting, pdf, markdown, latex, HTML, command, command line, open-source"
weight: 3
author: "Valerie Vossen"
draft: false
aliases:
  - /pandoc
---

## Overview

[Pandoc](https://www.pandoc.org/) is a powerful command-line tool designed for converting documents between a wide range of formats, including Markdown, HTML, LaTeX (PDF), Word, Jupyter notebooks (.ipynb), and PowerPoint. It can handle complex syntaxes, such as LaTeX math, document metadata, and tables, making it an incredibly versatile choice for various document conversion needs.


{{% summary %}}

*Key features are*:

- Easy and quick to use, directly from the command line
- Converts numerous document formats
- Free and open-source
- Highly customizable with extensions
- Allows custom templates for consistent formatting
- Supports citations and bibliographies
- Create slideshows with LaTeX Beamer or PowerPoint

For detailed information on all available options, refer to the [Pandoc User Guide](https://pandoc.org/MANUAL#). To quickly find specific topics in this extensive document, use the Search (`Ctrl+F`) function!

{{% /summary %}}


## How to install Pandoc

Refer to [this TSH Guide](/install/pandoc) for instructions on setting up Pandoc.

## How to use it

To demonstrate how to use Pandoc, we'll convert a basic Markdown file to a PDF. 

1. Save the following content in a file named `example.md`:


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

Pandoc uses LaTeX to create PDFs by default, so you need to have a LaTeX engine installed. Refer to our [LaTeX Set up Guide](/get/latex) for setup instructions. 

If you prefer not to use LaTeX, alternative tools are available. For more information, refer to the [Pandoc User Guide, Creating a PDF section](https://pandoc.org/MANUAL#creating-a-pdf)
{{% /warning %}}


2. Open a terminal in the directory where you saved the file and run the following command:

{{% codeblock %}}
```bash
pandoc example.md -s -o output.pdf 
```
{{% /codeblock %}}

- `example.md` is the input file
- `-o` specifies the output file (named `output.pdf`)
- `-s` (or `-standalone`) tells Pandoc to create a self-contained document. It follows the default format template and adds the necessary header and footer material. 

3. Check your directory to find the newly created PDF document `example.pdf`. 

The Markdown content is now beautifully formatted into a PDF!

<p align = "center">
<img src = "../images/output-pdf.png" width="400">
</p>

{{% tip %}}

You can provide multiple input files. By default, Pandoc combines them into one document with blank lines in between. Use `--file-scope` to process them individually.

{{% /tip %}}


## Useful functions and use cases

Pandoc offers a wide range of options, which you can find in the [Options sections of the User Guide](https://pandoc.org/MANUAL.html#options). Here are a few of the most useful features:


### Customized templates

Pandoc allows custom templates to control the look of your documents. 

Run `pandoc -D` followed by a format to find the default template used to create the document. For example, find the default PDF format like this:

{{% codeblock %}}
```bash
pandoc -D latex
```
{{% /codeblock %}}

To use a custom template,  create `mytemplate.tex` yourself (you can adjust the default template file, for example). Then, run the following command, specifying the template with `--template=`: 

{{% codeblock %}}
```bash
pandoc -s --template=mytemplate.tex -o example.pdf example.md

```
{{% /codeblock %}}


### Citations and bibliographies

Pandoc supports citations and bibliographies, which are essential in academic writing. You can use `--citeproc` to process citations. For example, save the following markdown content as `example-citations.md`. 

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

And, save the following content in a bibliography file called `references.bib`: 

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

Run this command to include the references:

{{% codeblock %}}
```bash
pandoc --citeproc example-citations.md -o output-citations.pdf 
```
{{% /codeblock %}}

A PDF document is created with the bibliography specified at the start of the markdown file!


<p align = "center">
<img src = "../images/output-citations.png" width="400">
</p>

{{% tip %}}

To generate LaTeX output with `bibtex` (when converting to a `.tex` file instead of a PDF directly), replace `--citeproc` with `--natbib`. 

{{% /tip %}}


### Math rendering

Pandoc can render mathematical expressions using LaTeX, MathML, or other methods. To use KaTeX for rendering math expressions, you can add `--katex` after the command when converting a markdown file to HTML. For example, save the following content in a file named `example-maths.md`.


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

The following command will convert the markdown file to HTML: 

{{% codeblock %}}
```bash
pandoc example-maths.md -s -o output-maths.html --katex
```
{{% /codeblock %}}


<p align = "center">
<img src = "../images/output-maths.png" width="400">
</p>

### Code blocks and syntax highlighting

Pandoc supports syntax highlighting for various programming languages. You can specify the language for each code block to ensure proper highlighting. Below is a Markdown file with code blocks for R and Python. Let's see how this file converts to PDF!

Save the following content in a file named `example-code.md`:

{{% codeblock %}}
```markdown
---
title: "Code examples"
author: "Author name"
---

This document contains some code blocks for R and Python.

## Python code example
~~~python
# A simple Python function
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
~~~

## R code example

~~~R
outcome <- 1 + 1
print(outcome)
~~~

```
{{% /codeblock %}}

Use the following command to convert the Markdown file to a PDF:

{{% codeblock %}}
```bash
pandoc example-code.md -s -o output-code.pdf
```
{{% /codeblock %}}

This command produces a PDF in your directory with syntax-highlighted code blocks for both R and Python:

<p align = "center">
<img src = "../images/output-code.png" width="400">
</p>


## Extensions

Pandoc offers a variety of useful extensions that allow you to tailor and customize its features to suit your needs. Below is a list of some of the most useful extensions for Pandoc, along with brief descriptions. For a complete list of options, refer to the [Extensions section of the User Guide](https://pandoc.org/MANUAL.html#extensions) and the [specific Markdown Extensions section](https://pandoc.org/MANUAL.html#pandocs-markdown).

{{%table%}}
| **Extension**        | **Description**                                                | **Formats**                  |
|----------------------|----------------------------------------------------------------|------------------------------|
| `smart`              | Improves readability by  <br> enabling smart typography. Converts  <br> straight quotes (") to curly quotes (“),  <br> -- to en dashes (–), --- to em dashes (—),  <br> and three dots to ellipses (…) | All formats                  |
| `autolink_bare_uris` | Automatically turns bare URIs  <br> into clickable links.                      | Markdown  <br> CommonMark  <br> GFM    |
| `footnotes`          | Adds support for footnotes.                                    | Markdown  <br> CommonMark  <br> GFM    |
| `grid_tables`        | Adds support for grid tables                     | Markdown                     |
| `task_lists`         | Adds support for creating task lists  <br> with interactive checkboxes                          | Markdown  <br> GFM                |
| `table_captions`     | Enables table captions,  <br> making it easy to add  <br> descriptive titles to tables       | Markdown                     |
| `tex_math_dollars`   | Allows LaTeX math  <br> between dollar signs,  <br> simplifying the inclusion of  <br> math formulas in documents.                        | Markdown                     |
| `pipe_tables`        | Adds support for pipe  <br> tables, providing an  <br>  easy way to create  <br> simple tables. | Markdown                     |
| `implicit_figures`   | Treats images as figures  <br> when  they are the only  <br> element in  a paragraph,  <br> adding `<figure>` and `<figcaption>`  <br> tags for better display. | Markdown                     |
{{%/table%}}

### How to add an extension

To add an extension, specify it after the format name with a `+`. For instance, to use the `footnotes` extension with the Markdown format, include it after the `-f` or `-from` flag:

{{% codeblock %}}
```bash
pandoc input.md -s -o output.pdf -f markdown+footnotes
```
{{% /codeblock %}}


{{% summary %}}

Pandoc is a free, open-source tool for converting documents across a wide range of formats. It is easy and quick to use directly from the command line, and it is highly customizable. This article highlights some use cases and provides interesting examples, so you are ready to start experimenting yourself!

{{% /summary %}}


