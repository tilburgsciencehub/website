---
tutorialtitle: "Write Your First LaTeX Document in 15 Minutes"
type: "write-your-first-latex-document"
indexexclude: "true"
title: "Add a Bibliography"
description: "Learn to write your very first professional-looking document with LaTeX."
keywords: "first, latex, beginner"
weight: 103
draft: false
aliases:
  - /cite/latex
---

Please notice that there are different ways to include a bibliography in $\LaTeX$, namely `bibtex`, `natbib`, and `biblatex`.
In this tutorial, we will deal with `bibtex` only. For more advanced uses, consider researching which system works best for you.

## Create a .bib File

A `.bib` file contains all the bibliographic information for your document. Think of it as a sort of database of all the references you *may* want to include in your article (but you don't have to necessarily).

Your `.bib` file must contain specific information for each entry (i.e., for each article, book, proceeding, etc. that you want to cite.)

The following is an example for an article entry:

```bib
@article{surname2020placeholder,
	Author = {Surname, Name},
	Date-Added = {2020-10-12 11:31:07 +0200},
	Date-Modified = {2020-10-12 11:31:07 +0200},
	Journal = {Placeholder Journal},
	Number = {1},
	Pages = {100-200},
	Publisher = {PLACEHOLDER PUBLISHER},
	Title = {This is the title of a paper},
	Volume = {10},
	Year = {2020}}
```

We **strongly** suggest to use a *bibtex generator* for this task. Some reference management tools can build `.bib` files automatically for you. More on this at [the end of this tutorial](/tips/latex).

{{% cta-primary "Download a Dummy .bib File for Prototyping" "../assets/bibliography.bib" %}}

## Use BibTeX

Once the `.bib` file is prepared, you will need to include it in the $\LaTeX$ document.

1. Place this file in the same directory of your $\LaTeX$ project.
2. Add the following to your code, before closing your `document` environment:
```latex
...
\bibliography{bibliography}
\bibliographystyle{apalike}
\end{document}
```

Notice that our file is saved as `bibliography.bib` but we did not include the extension `.bib` in the `\bibliography{filename}` command.

You can also specify a bibliography style which will indicate how your references will look like in the bibliography section. `apalike` is just one of the many ones available. Here's [a comprehensive list](http://www.cs.stir.ac.uk/~kjt/software/latex/showbst.html).

3. Lastly, you just need to add citations in your article. You can do so by using the `\cite{entrytag}` command, where the `entrytag` is a custom-defined tag for each entry that you can find right after the opening brace `{` - in our case, `surname2020placeholder`.

```latex
This is some text. Here a citation will be appended\cite{surname2020placeholder}.
```

{{% tip %}}
Notice that you're not obliged to cite all the entries in your `.bib` file! Only those that you've actually cited will appear in the bibliography section.
{{% /tip %}}

## Wrap Up

Adding a bibliography to our previous article, we should get the following $\LaTeX$ code and output:

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
  Hello, world! I'm finally writing my first document. I've learned that \textbf{this is how you make a text bold}. And this is a citation \cite{surname2020placeholder}.
  % This is a comment, not shown in final output.
  \section{A Section for a Very Important Equation}
  This is an equation:
  \begin{equation} % Begins an equation environment
    E_0 = mc^2
  \end{equation}
\bibliography{bibliography} % Adds a bibliography
\bibliographystyle{apalike}
\end{document}
```
{{% /codeblock %}}

![Our final LaTeX example.](../img/article-example.png)
