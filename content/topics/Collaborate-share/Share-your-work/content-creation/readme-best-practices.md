---
title: "README Best Practices"
description: "Learn how to write a convincing and effective README file. Get to know the best practices with our examples and templates for GitHub README.MD"
keywords: "git, commands, important, essential, cheat, template, readme, examples, project, github, documentation, repository"
#date: 2021-02-08
draft: false
weight: 2
aliases:
  - /write/readme
  - /learn/readme-best-practices
  - /topics/share-your-results-and-project/use-github/readme-best-practices/
---

## Overview
A README is like the book cover of your project. It's the first thing a person sees when opening your repository. A great README not only gets people to jump into your project much quicker, but also helps your project to stand out from the sea of open source software on GitHub. Your README thus not only serves for documentation, but also for marketing purposes.

And while we all loathe sleazy marketing, documentation can't be sleazy because it solves a real purpose: teaching everyone about the project. In this building block, we provide you with a template and some examples you can use for your own projects.


## Markdown

A README is a markdown (`.md`) file that you can format text using a plain-text editor. Like an academic paper, we recommend working with headers and subheaders to impose a structure. Better still, if you link to other files within the repository so that the reader not only knows what the project is about but also which files are a priority.

{{% tip %}}
Below we list the most common markdown commands:

* `**This is bold text**` = **This is bold text**
* `*This text is italicized*` = *This is bold text*
* `This is a [link](https://tilburgsciencehub.com)` = This is a [link](https://tilburgsciencehub.com)
* To create a heading, add 1-6 `#` symbols before your header. The number of hashtags will determine the size of the heading.
* Images can be inserted by linking to either an image URL (e.g., [example](https://www.tilburguniversity.edu/sites/default/files/styles/epic_compact_large/public/image/TilburgU%20logo.jpg?h=f0edcced&itok=lnj4S1OC)) or a relative file path ([`../images/git_workflow.png`](../images/git_workflow.png)). Use the following syntax: `![image description](link)`
* Visit [this](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax) cheat sheet for a comprehensive list of markdown commands.
{{% /tip %}}

## The Basic Structure

We recommend to include at least the following sections in your README:

{{% codeblock %}}
```markdown
# Project title

A subtitle that describes your project, e.g., research question


## Motivation

Motivate your research question or business problem. Clearly explain which problem is solved.


## Method and results

First, introduce and motivate your chosen method, and explain how it contributes to solving the research question/business problem.

Second, summarize your results concisely. Make use of subheaders where appropriate.


## Repository overview

Provide an overview of the directory structure and files, for example:

```
├── README.md
├── data
├── gen
│   ├── analysis
│   ├── data-preparation
│   └── paper
└── src
    ├── analysis
    ├── data-preparation
    └── paper
```

## Running instructions

Explain to potential users how to run/replicate your workflow. If necessary, touch upon the required input data, which secret credentials are required (and how to obtain them), which software tools are needed to run the workflow (including links to the installation instructions), and how to run the workflow.


## More resources

Point interested users to any related literature and/or documentation.


## About

Explain who has contributed to the repository. You can say it has been part of a class you've taken at Tilburg University.

```
{{% /codeblock %}}


{{% tip %}}

Rather than creating the repository overview all by hand, you can leverage the `tree` command to automatically generate the directory structure in the terminal. Mac users may first need to install the [tree package](https://formulae.brew.sh/formula/tree) (`brew install tree`).

{{% /tip %}}

## The README Template

We provide a more comprehensive README template - which you can preview in the image below - that follows best practices defined by a number of data editors at social science journals. You can read here the [full list of endorsers](https://social-science-data-editors.github.io/template_README/Endorsers.html).

You can always access **[the most recent version of this template here](https://social-science-data-editors.github.io/template_README/)** or download them quickly:

{{% cta-primary-center "Download the Markdown version" "https://raw.githubusercontent.com/social-science-data-editors/template_README/releases/README.md" %}}
{{% cta-secondary-center "Download the Word version" "https://social-science-data-editors.github.io/template_README/templates/README.docx" %}}

![A preview of the README template](../images/preview-readme-template.png)

## Examples

The repositories below serve as examples from which you can draw inspiration for your own README files.

* [Tilburg Science Hub](https://github.com/tilburgsciencehub/website)
* [Categorization of Spotify Playlists](https://github.com/hannesdatta/spotify-playlist-clustering)
* [Hiding of Instagram Likes](https://github.com/RoyKlaasseBos/Hiding-Instagram-Likes)
* [musicMetadata](https://github.com/hannesdatta/musicMetadata)


## Advanced Use Cases

By default Github showcases your pinned repositories on your profile page (click on your profile picture in the top right corner > "Your profile"). A little secret is that you can add a README to your profile page by creating a new repository called `<YOUR_USERNAME>`. Make sure it's public and initialize it with a README to get started. As you can see in [this](https://www.youtube.com/watch?v=Y1z7_GfEPiE) video, you can even spice things up with emojis and gifs!

{{% tip %}}
Want to go the extra mile? Include your [GitHub Stats Card](https://github.com/anuraghazra/github-readme-stats) in your README! Simply add `https://github-readme-stats.vercel.app/api?username=<YOUR_USERNAME>` to the end of your README to incorporate a real-time widget of your number of stars, commits, PRs, issues, and contributions on GitHub ([see example](https://github-readme-stats.vercel.app/api?username=hannesdatta)).
{{% /tip %}}

{{% tip %}}
A useful external resource is [Make A Readme](https://www.makeareadme.com/). With Make A Readme, you can create READMEs for repositories. Furthermore, it provides suggestions and good tips for good READMEs. 
{{% /tip %}}

{{% summary %}}

- A README serves as both documentation and marketing for your project, making it essential to create a well-crafted one.

- Markdown format is the standard for README files.

- Including key sections like project title, motivation, method and results, and repository overview helps users understand and engage with your project.

- Providing a directory structure overview makes it easier for users to navigate your repository.

- Examples of well-crafted README files ar a great source of inspiration for creating your own.

{{% /summary %}}