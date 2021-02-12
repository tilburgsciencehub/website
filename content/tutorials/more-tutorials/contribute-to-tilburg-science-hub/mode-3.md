---
tutorialtitle: "Contribute to Tilburg Science Hub"
type: "contribute-to-tsh"
indexexclude: "true"
title: "Mode 3: The Nerdy Way"
description: "Tutorials teach our users how to combine individual building blocks into a final product. Learn how to write one."
keywords: "template, pull, requests, contribute, github"
weight: 1004
draft: false
---

## The Ideal Way: Issue a Pull Request

On this page, we provide all the necessary resources and information for you to be able to write content autonomously.

{{% tip %}}

Please, notice that Tilburg Science Hub Building Blocks, Tutorials and Examples are written as [Markdown](https://guides.github.com/features/mastering-markdown/) files. We encourage you to familiarize with the Markdown formatting before starting to write - it's very easy!

{{% /tip %}}

## If you want to revise, modify, add, or remove content from existing pages, or report a bug

### Simple changes

The easiest method to make straightforward updates to Markdown files is to use [GitHub's web-based file editor](https://help.github.com/en/articles/editing-files-in-your-repository).

1. Browse the [Tilburg Science Hub repository](https://github.com/tilburgsciencehub/tsh-website/) to find the Markdown that roughly corresponds to the tilburgsciencehub.com URL structure.

2. In the upper right corner of the file view, click the pencil icon to open the file editor.

3. Edit the file and then submit a new pull request. That's it.

### Elaborate changes

For more complex updates or editing more than a file, it's better to use a local Git workflow to create a pull request.

After having [set up your GitHub account](/building-blocks/configure-your-computer/statistics-and-computation/git/), follow the following steps (required only the first time you set up a local project):

1. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

2. Within your version of the forked repository, move to the `tilburg-update` branch and create a **new branch for each significant change being made**.

3. Navigate to the file(s) you wish to change within the new branches and make revisions as required.

4. Commit all changed files within the appropriate branches.

5. Create individual pull requests from each of your changed branches to the `tilburg-update` branch within the originating repository.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.


## If you want to write new content

1. First, you'll need to prepare the content as Markdown file(s). Follow our templates [below](#what-is-a-building-block) to get started. In case you want to feature your project in the Examples section, please [contact us](/about/#who-maintains-tsh).

2. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

3. Within your version of the forked repository, move to the `tilburg-update` branch and
create a **new branch for each new topic you are writing about**.

4. Commit all the new Markdown files within the appropriate branches.

5. Create individual pull requests from each of your changed branches to the `tilburg-update` branch within the originating repository.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.

{{% tip %}}

Don't know how to do this? You can follow a great tutorial about [contributing on GitHub](https://github.com/firstcontributions/first-contributions).

{{% /tip %}}

## What is a Building Block?

Building blocks are the DNA of our platform. They are small code snippets that users can independently "mix" to create something unique. Think of building blocks like LEGO bricks - each one with its own color, shape and functionality.

Check out our platform's menu system to see in which categories we classify our building blocks. Want to add a new category? Let us know via a GitHub issue.

### Start with our Building Block Template

{{% warning %}}

First, make sure to read our [code of conduct](../code-of-conduct) as well as our [writing guidelines](../style-guide).

{{% /warning %}}

You can then download and fill in our **[Building Block Markdown template](https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/tutorials/more-tutorials/contribute-to-tilburg-science-hub/building-block-shell.md)**.

## What is a Tutorial?

Tutorials teach our users how to combine individual building blocks into a "final product". What that product really is is *your* choice.

When creating a new tutorial, you typically realize that you also need to create several new building blocks to make the tutorial work. So if you haven't contributed to our platform yet, try contributing a building block first before starting on a brand-new tutorial.

### Start with our Tutorial Template

{{% warning %}}

First, make sure to read our [code of conduct](../code-of-conduct) as well as our [writing guidelines](../style-guide).

{{% /warning %}}

You can then download and fill in our **[Tutorial Markdown template](https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/tutorials/more-tutorials/contribute-to-tilburg-science-hub/tutorial-shell.md)**.

<!--
The design should always accommodate all users' knowledge levels and avoid confusion. For instance, on a tutorial page, there should be a quick and concise explanation (a sort of TL;DR), as well as a more in-depth exposition for those who need to educate themselves first.

The design should be attractive and easy to use for all our target groups and should strike a balance between glossiness and nerdiness. We want to avoid unnecessary clutter and stock photos. Let's keep it simple.
-->
