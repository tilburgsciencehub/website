---
title: "Contribute to Open Source Projects"
description: "Learn how to contribute to open source projects published on GitHub."
weight: 3
keywords: github, open source, pull request, collaborate
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /learn/git-collaborate
  - /learn/git-pr
---

# Overview

Ever wondered how to contribute to open source projects on GitHub? Here's how!

## Step 1: Get to know the repository

Familiarize yourself with the repository to which you want to contribute.

- Typically, each repository has a readme with general instructions on what the repository is about (& how to run the code).
- Also, new features and bugs are discussed at the repository’s issue page.
- Finally, many repositories contain a discussion forum and project board in which you can learn about the roadmap of the project.

{{% example %}}
For example, visit the [repository of Tilburg Science Hub](https://github.com/tilburgsciencehub/tsh-website).

- Browse through the repository’s readme (that’s what you see when you click on the links above)
- Head over to the issue page
- View the project/discussion boards.

Can you identify ways in which to contribute to the project?

{{% /example %}}

## Step 2: Run the repository’s code

After installing required software, you need to run the code to see whether you can actually test your changes to the project later.

- Open the repository on GitHub, and fork it (click on the fork button in the upper right corner on Git). This creates a copy of the code in your GitHub account.

- Clone your own fork to the disk, e.g., git clone https://github.com/your-user-name/tsh-website.

- Enter the directory of the cloned repository, and run the code.

{{% example %}}
- In the case of Tilburg Science Hub, you can type `hugo server` to start up the webserver (Hugo is a content management system we use for running the website).

- You can now open the website locally in your browser. Check the terminal for the exact address, but likely you just have to enter https://127.0.0.1:1313 in your browser!

- Check out the code in \docs - the websites are written in Markdown, and you can easily add/change. Observe how the site actually changes in your browser!

{{% /example %}}


## Step 3: Make changes

Find stuff that you want to add to the project, or fix! Each *new feature* that you introduce usually needs to be developed in a separate branch, which allows the repository owner to carefully screen which parts of the project to add to the public version of the main project.

1. Create a new branch (`git branch name-of-a-new-feature`)
2. Work on your new feature. Throughout, apply the Git workflow (`git status`, `git add`, `git commit -m "commit message"`)
3. When you’re done with all of your changes, push your changes to your GitHub repository `git push -u origin name-of-a-new-feature`

At this stage, your changes are visible at *your forked copy* of the repositoroy, but the repository owner of the main project doesn't know about these changes yet.

## Step 4: Ask Project Owner to Integrate your Changes via a Pull Request (PR)

Fully done and happy with your changes? Then let the project owner know about your new, amazing feature!

1. Open your forked repository on GitHub, select the branch you've just edited, and click on "pull request".

2. Carefully describe your changes (e.g., the new feature you developed, why it's useful, how you've tested it, etc.), and then submit your pull request.

The owner of the main repository will now review your changes, maybe request changes, and potentially integrates your new feature with the main project. Congrats on your first open source contribution!
