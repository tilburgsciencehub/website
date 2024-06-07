---
title: "Getting Started With Pandoc: An Easy Document Converter"
description: "Convert documents of all types, e.g. PDF, Markdown etc., from your command line with Pandoc"
keywords: "pandoc, documents, convert, converting, pdf, markdown"
weight: 1
draft: false
aliases:
  - /pandoc
---

## Overview

[Pandoc](https://www.pandoc.org/) is a universal document converter, they call themselves your swiss-army knife to convert one format into the other. Think of Markdown, HTML, LaTex, Word, Jupyter notebooks (ipynb), Powerpoint, and many others. It understands and is able to convert syntaxes like LaTex maths, document metadata, tables etc.

{{% summary %}}
*Some of its useful functions**:

- Easy and quick to use (directly from your command-line)
- Free, and open-source
- Customizable
- Citations

{{%/summary %}}


## How to install?


Click the version compatible with your computer's operation system on [the installing page](https://github.com/jgm/pandoc/releases/tag/3.2).

*Windows:* choose the .msi file, which is a Windows Installer package.
- Find the installer in your download history. A setup wizard will appear. 
- Tick the box to accept the terms in the License Agreement, and click Install. 
- When Pandoc is installed, you can click Finish to close the Setup Wizard.

*Mac:* Download the PKG file,  which is a macOS Installer package. 
- Navigate to the download folder, and double-click the PKG file to start the installer
- Follow the installation wizard, and click "Agree" to accept the license agreement, and "Install" to begin the installation. 
- Once the installation is done, click "Close

### Verify installation

Open your command prompt and type:

{{% codeblock %}}
```bash
pandoc --version
```
{{% /codeblock %}}

You should see the version information for Pandoc, confirming that it was installed correctly. You're all set!


{{% tip %}}
Download instructions for example installing pandoc with Linux, how to run pandoc in a Docker container, or with GitHub Actions, you can find [here](https://www.pandoc.org/installing.html). 
{{% /tip %}}


## How to use it?

The most basic usecase will be demonstrated with conversing this a Markdown file to a HTML file. 

-o -> output to a file
-s -> nice format
multiple files

bash codeblock


tip

if you give multiple files as input, they will be put together with blank lines inbetween. Use `--file-scope` to get them individually. 
tip

### Specifying the format

bash
pandoc -f html -t markdown hello.html

To convert hello.html from HTMl to Markdown

If you don't specify the format of the input file, it will guess from the file extension and otherwise the default that is assumed is Markdown. If the output file is unknown, HTML is the default. 

## Special usecases

### PDF

It uses LaTeX to create a PDF, so install the LaTeX engine for this option to work in the easiest way. 


## References

- [Pandoc's user guide](https://pandoc.org/MANUAL#)