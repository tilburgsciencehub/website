---
tutorialtitle: "Write Your First LaTeX Document in 15 Minutes"
type: "write-your-first-latex-document"
title: "The Fine Art of Typesetting"
description: "Learn to write your very first professional-looking document with LaTeX."
keywords: "first, latex, beginner, typesetting"
weight: 100
draft: false
aliases:
  - /learn/latex
---

## The Design Philosophy

In this tutorial, you'll learn to write your very first document using {{< katex >}}\LaTeX{{< /katex >}} within 15 minutes.

[$\LaTeX$](https://www.latex-project.org) is a professional typesetting system widely used in academia because of its high-quality output and the relatively ease of use in setting up complex documents, like journal articles, books, technical reports, and similar.

One of its main features is that **it separates the writing and the formatting stages** - or the content and its presentation. With most word processors, the writer can see the result of their edits in real-time. With $\LaTeX$, the writer can focus solely on writing the content in plain text, and then use some markup tags and commands to stylize the text and define the document structure.

The typesetting is asynchronous. The author can only see the results afterwards. This allows them to focus only on **what** the document should be, while it's up to the engine to deal with the **how**. Therefore, if the end result is unsatisfactory, the author cannot directly modify what's on-screen, but they have to correct the source code.

This is mainly what sets $\LaTeX$ apart from WYSIWYG (an acronym for "What You See Is What You Get") editors, like Microsoft Word. Experienced users can **produce complex documents very quickly**, but at the expense of losing a Graphical User Interface.

## Why $\LaTeX$?

Because:

![Why LaTeX?](../img/why-latex.png)

Jokes aside, there are a few advantages in using $\LaTeX$:

- It can yield the highest-quality and professional-looking documents
- It deals with the page layout, so you don't have to
- It can generate complex structures with thousands of cross-references, notes, citations that stay always up-to-date when you edit your document
- It can produce gorgeous mathematical equations
- It's free
- Are you into chemistry? Did we mention that you can do this?

![Chemfig in LaTeX](../img/chemfig-latex.png)

## Is $\LaTeX$ Difficult to Learn?

You'll probably find yourself Googling a lot even for the most elementary commands at the beginning. However, with a bit of practice on simple documents, you can quickly master its functioning and all your time and effort will be rewarded by high-quality results.

In the end, if you're a researcher dealing with complex econometrics models on a daily basis, if you can read a financial statement, if you can prove the transcendence of $\pi$... we are pretty sure you can also learn to typeset documents professionally.

![Is LaTeX difficult?](../img/latex-comparison.jpg)

## When to Use It

To quickly sum up, it's useful to use $\LaTeX$ in any of the following scenarios:

- Your document needs a clear and solid logical structure
- Your document is very long
- You need to manage a lot of cross-references and a long bibliography
- Your document involves a lot of maths, tables, figures, graphic elements, chemical figures, flowcharts, diagrams, etc.
- You aim for the highest-quality output but you don't want to spend time dealing with the page layout
- A $\LaTeX$ template is given to you, because that's the standard in your industry or domain

{{% tip %}}
Because $\LaTeX$ is such widely used among academics, there are many packages for researchers that can speed up their workflow.

For instance, `stargazer` is a R package that can automatically create gorgeous summary tables in $\LaTeX$ from your R code (regression tables, summary statistics, etc...), saving you the trouble of manually filling in the table.
{{% /tip %}}
