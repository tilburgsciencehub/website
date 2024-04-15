---
title: "Mastering Academic Writing"
description: "Learn strategies for academic writing, formatting, and referencing to ensure clear presentation of your research within your academic paper or thesis."
keywords: "latex, writing, paper, thesis, structure, academic, abstract"
weight: 4
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/academic-paper
  - /topics/more-tutorials/write-an-academic-paper/write-an-academic-paper
  - /topics/more-tutorials/write-an-academic-paper/_index
---

## Overview
Well-structured, academic writing is essential for effectively conveying your research in a paper or thesis. Here are key tips to refine your approach, divided into the following sections:
- Structured approach to writing
- Polish your writing
- Seek feedback
- Typesetting
- Tables and figures formatting
- References
- The review process

### Structured approach to writing

- **Divide your work**

Keep a structured approach and divide your work into manageable sections and set (realistic!) deadlines for each

- **Standard outline**: 

Stick more or less to [the standard outline of a thesis/academic paper](/masterthesisguide/outline).

Readers will appreciate that they find it easy to find their way, because your paper reads like many others. At the same time, make the structure of the paper work for you, to convey the contents as well as possible. Add subsections or whatever suits the purpose of the reader.

- Each paragraph usually makes one point or contains only one argument or line of thought.

- **Avoid lengthiness:** 
Don't be afraid that your paper will be too short. Usually, it will become long by itself, when you address all the concerns you learn about on the way and explain everything well, even if the analysis that you are doing is actually not too difficult.

- **Write and revise!**
Don't be afraid to delete things. Leave old text behind. Replace it. Make sure your paper contains only what is necessary. This will take a long time! One rule of thumb is that doing the analysis takes 50% of your time, writing your paper takes the other 50%. Therefore, start early with writing a very first rough draft and get your ideas on paper. Then refine it from there in steps. This will give you peace of mind.

Some other general tips about the structure are:
- Use page numbers, with the same font as your text.
- Be consistent in page settings over the whole document.
- Footnotes are usually placed after the end of a sentence.

### Polish your writing
- Use an active tense as much as possible.
- Keep sentences concise and easy to understand and read. Take the reader in mind as someone who has a general education in your field but might not be an expert on the topic. 
- Pay attention to spelling, using tools such as [Grammarly](https://app.grammarly.com/). 

### Seek feedback
- Seek feedback from peers during the writing process.
- [The Scriptorium](https://www.tilburguniversity.edu/students/studying/writing-information-skills/scriptorium) is also a great place to go for free-of-charge assistance in the writing process of your thesis. 

{{% tip %}}
Other great resources are:
- “How to Write a Lot: A Practical Guide to Productive Academic Writing”, by Paul Silvia.
- [Writing resources for graduate students](https://writingcenter.gmu.edu/writing-resources)
{{% /tip %}}


## Typesetting

### Latex
**[$\LaTeX$](https://www.latex-project.org)** is a typesetting system ideal for a thesis or academic paper. Although it has a bit of a learning curve, it offers substantial advantages like:

- It enables more precise formatting, especially in typesetting mathematical symbols and formulas.
- It is easy to stay consistent with the formatting throughout the whole document. 
- It can automatically update citations and cross-references with document structure changes. 

We prepared a short guide on [how to install](/setup/latex) a $\LaTeX$ distribution on your system, and [how to write your first LaTex document in 15 minutes](/write/latex). 

{{% tip %}}
Download a [ready-to-use LaTeX template for your thesis](/latex-template).
{{% /tip %}}

### LyX

LyX is an alternative platform for academic writing. There is a [short guide on LyX, including a research paper template](/write/paper-with-lyx). 

Some technical tips when you are using LyX:
- The booktabs package is nice.
- It's a good idea to put table and figure notes into minipage environments.
- Use a normal size font and the resizebox package to make tables smaller.
- Use Roman 12pt, 1.5 line space, and page margins 2.5cm on all margins as a starting point.

## Format of tables and figures
- Put only tables and figures that are important for what you want to say in your paper. The main body of the paper should not have more than 10 tables and figures, often less. 
- Tables and figures need to be clear enough to be understood without reading the main text! 
- There are packages available that format or combine output of your statistical analyses (e.g. `stargazer`, and [`kableextra`](/regressions/kableextra/) in R).
- Use a descriptive title that summarizes the main point ("X increases Y") rather than using a generic title ("Results").
- Give variables and figure axes clear names.
- Avoid colors in figures.
- Always refer back to tables and figures in the text. And place the tables and figures close to where you discuss them, don't put them in the very end of the paper as this is less convenient for the reader.
- Only the equations that are referred back to in the text need to be numbered.
- Use an (online) appendix for extra information, but only if it's referred to and discussed somewhere. Don't use this as a place to dump extra things you did at some point.
- Make sure capitalization is consistent. This for as well figure titles as within tables and figures. 

For titles, you either want all figure titles to be capitalized ("This is a Figure Title"), or not ("This is a figure title"). Usually the first letter is a capital one. Inside tables and figures, one easy way to go have no capitalization (except for names etc.). 

### References

Use tools for referencing that can automatically update the work. However, don't rely on them completely and still check the accuracy yourself. Check out [this topic](/reference/list) to learn more about the available tools for building and maintaining reference lists. 

{{% tip %}}
Add and manage your references while writing. Avoid leaving it for the last minute, this will cause a lot of stress!
{{% /tip %}}

### The review process

#### Academic papers
Finally, keep in mind from the very beginning that your paper will go through a messy reviewing process and that it may be rejected many times. Don't be discouraged. Learn from the comments, but don't sit on your paper for too long. Revise it and send it off again. 

{{% tip %}}
A good motivating read that also provides some background information in this context is ["Secrets of Economics Editors"](https://mitpress.mit.edu/books/secrets-economics-editors).
{{% /tip %}}

#### Master's or PhD Theses
The review journey for your thesis can be demanding as well. Anticipate iterations and feedback loops. Don't let feedback discourage you; instead, learn from it and revise!





