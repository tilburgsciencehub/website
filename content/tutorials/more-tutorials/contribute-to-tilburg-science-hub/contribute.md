---
tutorialtitle: "Contribute to Tilburg Science Hub"
type: "contribute-to-tsh"
title: "Three Ways to Contribute"
description: "Learn how to contribute to Tilburg Science Hub."
keywords: "contribute, contribution, tsh"
weight: 1000
draft: false
---

## How to contribute to Tilburg Science Hub

We're glad for your interest in contributing to our project. Tilburg Science Hub is open-source, and as such, **anyone** can contribute! The process is really simple.

When writing for Tilburg Science Hub, please follow our [communication style guideline](../style-guide). By contributing, you agree that we may redistribute your work under [our license](/about#license). In exchange, we will address your issues and/or assess your change proposal as promptly as we can, and help you become a member of our community. Everyone involved agrees to abide by our [code of conduct](#contributor-code-of-conduct).

## How our content is organized

We provide content in three forms:

- **Building Blocks** are concepts in small doses. These allow us to explain the theory while also providing some practical examples and code snippets for a variety of programming languages or operating systems, sometimes attaching a small dummy data set too. Information is explained in a way that it is easy to clone or implement in an existing project. While everybody can follow our Building Blocks, they are generally more appealing to advanced users – or those who already know what to look for.
- **Tutorials** explain a broader argument compared to Building Blocks, and follow a sequential order. These are particularly useful for novices or anyone new to a certain topic because of their comprehensive nature and step-by-step guidance. We support and encourage the use of videos, exercises, and quizzes for Tutorials.
- **Examples** are real-life cases, publications, templates, or research projects that put into practice the concepts explained on this website.

Tilburg Science Hub Building Blocks, Tutorials and Examples are written as [Markdown](https://guides.github.com/features/mastering-markdown/) files.

## If you want to revise, modify, add, or remove content from existing pages, or report a bug

### Simple changes

The easiest method to make straightforward updates to Markdown files is to use [GitHub's web-based file editor](https://help.github.com/en/articles/editing-files-in-your-repository). Browse the [Tilburg Science Hub repository](https://github.com/tilburgsciencehub/tsh-website/) to find the Markdown that roughly corresponds to the tilburgsciencehub.com URL structure. In the upper right corner of the file view, click the pencil icon to open the file editor. Edit the file and then submit a new pull request.

### Elaborate changes

For more complex updates or editing more than a file, it's better to use a local Git workflow to create a pull request.

After having set up your GitHub account, follow the following steps (required only the first time you set up a local project):

1. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

2. Within your version of the forked repository, move to the `tilburg-update` branch and create a **new branch for each significant change being made**.

3. Navigate to the file(s) you wish to change within the new branches and make revisions as required.

4. Commit all changed files within the appropriate branches.

5. Create individual pull requests from each of your changed branches to the `tilburg-update` branch within the originating repository.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.


## If you want to write new content

1. First, you'll need to prepare the content as Markdown file(s). Follow our templates to get started. We provide a [template for Building Blocks](../building-block-shell), a [guide on how to write Tutorials](../create-tutorial), and a [tutorial page template](../tutorial-shell). In case you want to feature your project in the Examples section, please [contact us](/about).

2. Fork the originating repository to your GitHub profile (press the "fork" button
on GitHub, which creates a copy of this project in your own GitHub account).

3. Within your version of the forked repository, move to the `tilburg-update` branch and
create a **new branch for each new topic you are writing about**.

4. Commit all the new Markdown files within the appropriate branches.

5. Create individual pull requests from each of your changed branches to the `tilburg-update` branch within the originating repository.

6. Maintainers and other contributors will review your pull request. When your pull request is approved, it will be merged into the upstream Tilburg Science Hub repo. If you receive feedback, make changes using your issue-specific branches of the forked repository and the pull requests will update automatically.

7. Repeat as needed until all feedback has been addressed.

Don't know how to do this? You can follow a great tutorial about [contributing on GitHub](https://github.com/firstcontributions/first-contributions).

## Open call

We are currently looking for contributions.

<!-- The topics we are most interested in are exhibited in [our content roadmap](). -->

Please, submit your content anyway and we'll be happy to evaluate whether it fits our schedule.

## Contributor Code of Conduct

As contributors and maintainers of this project, we pledge to respect all people who contribute through reporting issues, posting feature requests, updating documentation, submitting pull requests or patches, and other activities.

We are committed to making participation in this project a harassment-free experience for everyone, regardless of level of experience, gender, gender identity and expression, sexual orientation, disability, personal appearance, body size, race, ethnicity, age, or religion.

Examples of unacceptable behavior by participants include the use of sexual language or imagery, derogatory comments or personal attacks, trolling, public or private harassment, insults, or other unprofessional conduct.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct. Project maintainers who do not follow the Code of Conduct may be removed from the project team.

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting one or more of the project maintainers.

This Code of Conduct is adapted from [the Contributor Covenant](http://contributor-covenant.org/version/1/0/0/), version 1.0.0.
