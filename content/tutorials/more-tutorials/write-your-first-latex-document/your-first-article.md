---
tutorialtitle: "Write Your First LaTeX Document in 15 Minutes"
type: "write-your-first-latex-document"
indexexclude: "true"
title: "Your First Article"
description: "Learn to write your very first professional-looking document with LaTeX."
keywords: "first, latex, beginner"
weight: 102
draft: false
aliases:
  - /write/latex
---

## The Preamble

The preamble is the first section of your `.tex` file. It comes before the the text of the document itself.

The preamble always **starts with the definition of a "document class"**. This is where you tell {{< katex >}}\LaTeX{{< /katex >}} what kind of document you're writing: an article, a book, a letter... More on that later.

You can then continue **specifying additional information and packages** in the preamble.

The preamble is then followed by the document text, the actual "content" of your document.

The overall structure resembles this one:

```latex
\documentclass{class}
This is your preamble, where you can specify packages.
\begin{document}
This is your document. This is the text that will be shown on the output file.
\end{document}
```

Notice how we specify the document class: beginning with a `\` backslash. You will find similar statements over and over in your code. These tell $\LaTeX$ that they're not actual text, but rather some instructions or commands.

All the commands follow the same structure: `\nameofcommand{option}`. Commands can also appear within the document body, not only in the preamble. You can also include some additional parameters within square brackets.

### Document Class

Let's start your new document. First, we need to tell $\LaTeX$ that we're going to write an article. Then, we write "Hello, world!" as our document text.

{{% codeblock %}}
```latex
\documentclass{article} % Specifies that we're writing an article
\begin{document}
Hello, world!
\end{document}
```
{{% /codeblock %}}

If you now compile the document, you should see "Hello, world!" together with a page number at the bottom, which $\LaTeX$ automatically added for us since we used the *article* document class.

That's because $\LaTeX$ **uses the document class to infer the page and document layout** that it should use.

There are many document classes available out there. Here's [a comprehensive list](https://ctan.org/topic/class). In this tutorial, we will only use the `article` class.

In case you wanted to slightly modify an existing class, you may use any of the available parameters for that class. For instance, you can specify a different font size (the default is 10pt) or a different paper format (the default is `letterpaper`) for the `article` class: `\documentclass[12pt,a4paper]{article}`.

As you can see, you can specify these **additional parameters within square brackets**.

### Packages

You can extend the functionalities of $\LaTeX$ by importing some packages in the preamble, similar to what you'd do with Python or R packages. However, contrary to those, most packages will be already installed by default - no need to download them manually[^1]. So, if you want to include a package, you only need to tell $\LaTeX$ that you want to use it.

Import packages in the preamble with the command: `\usepackage[options]{packagename}`.

For instance, if we wanted to add an equation to our document, we would need the `amsmath` package. This is a package from the American Mathematical Society designed to add features, facilitate writing formulas and improve the typographical quality of math equations.

So, our new code would look like this:

{{% codeblock %}}
```latex
\documentclass{article} % Specifies that we're writing an article
\usepackage{amsmath} % Imports amsmath
\begin{document}
Hello, world!
This is an equation:
  \begin{equation}
    E_0 = mc^2
  \end{equation}
\end{document}
```
{{% /codeblock %}}

There are *many* packages for a great variety of purposes, like adding pictures, a bibliography, flowcharts, links, and so on. Most of the time, you will simply need to look up which one is the one you need for the specific purpose.

{{% tip %}}
We provide a short list of the most important packages at the [end of this tutorial](/tips/latex).
{{% /tip %}}

## The Body

### Environments

You may have noticed some commands with `\begin` and `\end` statements in our code above. Actually, these are not commands. Instead, they define the so-called environments.

An environment is a section of your document where particular typesetting rules apply. Usually, you will have multiple environments in the same document. For instance, in our previous example, we've added the `equation` environment within our `document` environment.

{{% tip %}}
Try adding an `abstract` environment to your article on your own, if you feel you've mastered $\LaTeX$ environments so far.
{{% /tip %}}

{{% warning %}}
You may specify as many environments as you wish, nested into each other or in any sequential order. However, it is imperative to **specify the `document` environment as the very first one**. In other words, you cannot have any environment outside the document environment.
{{% /warning %}}

### The Title Page

Let's now add a title page to our article. This page will show the article title, the author and a date.

Add these to your preamble:

{{% codeblock %}}
```latex
\title{My First \LaTeX{} Article}
\author{John Doe}
\date{January 1st, 2000}
```
{{% /codeblock %}}

Great! Now let's build again our document and... Oh, wait. Why isn't the title showing up?

That's because we've only specified the information in the preamble. But we did not tell $\LaTeX$ where to show that information inside our document.

Therefore, we'll also need to add the `\maketitle` command at the place you want the title to be printed, which is right after we begin the `document` environment in our case. If we wanted to make the title fill the entire first page, we may also add the command `\newpage` so that the article content starts from the second page.

{{% codeblock %}}
```latex
\begin{document}
\maketitle
\newpage
Hello, world!
This is an equation:
  \begin{equation}
    E_0 = mc^2
  \end{equation}
\end{document}
```
{{% /codeblock %}}

{{% tip %}}
Try building your document with and without the `\newpage` command to see how it effects the output.
{{% /tip %}}

### Basic Formatting Options

A few formatting options that you'll need to remember:

| $\LaTeX$ | Output |
|-----------------------|-----------------------|
| `\textbf{This text is bold}` | **This text is bold** |
| `\textit{This text is italicised}` | *This text is italicised* |

---

These backslashes`\\`will break the line.

These backslashes

will break the line.

---

```latex
\begin{itemize}
  \item First bullet point.
  \item Second one.
\end{itemize}
```

- First bullet point.
- Second one.

### Sections

It's often important to give a logical structure to your document, especially when writing a paper. You can split up your article in different sections and subsections[^2]:

```latex
\section{This is the section title}
\subsection{These titles will be printed in your document}
\subsubsection{These will also show up in your table of content}
```

## Putting All Together

Congrats! You've just learned the basics of $\LaTeX$! Now, putting all together, your document code may look something like this:

{{% codeblock %}}
```latex
\documentclass{article} % Specifies that we're writing an article
\usepackage{amsmath} % Imports amsmath
\title{My First \LaTeX{} Article} % Defines the title
\author{John Doe}
\date{January 1st, 2000}
\begin{document} % Begins the document environment
  \maketitle % Prints the title
  \newpage % Ensures that the article starts from the next page
  \section{My First Section}
  Hello, world! I'm finally writing my first document. I've learned that \textbf{this is how you make a text bold}.
  % This is a comment, hidden in the final output
  \section{A Section for a Very Important Equation}
  This is an equation:
  \begin{equation} % Begins an equation environment
    E_0 = mc^2
  \end{equation}
\end{document}
```
{{% /codeblock %}}

{{% tip %}}
You've just scratched the surface. For more formatting options, you can check out this [great guide](https://www.overleaf.com/learn).
{{% /tip %}}

[^1]:
    Especially if you're working on a $\TeX$ Live distribution (on MacOS and Linux), where most packages are included in the "required" collection of packages.

[^2]:
    For other document classes, please refer to their documentation. For instance, in the `book` class you cannot have sections. Instead, you have chapters.
