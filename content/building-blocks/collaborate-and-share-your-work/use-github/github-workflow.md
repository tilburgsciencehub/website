---
title: "The GitHub Workflow"
description: "GitHub flow is a lightweight, branch-based workflow. The GitHub flow is useful for everyone, not just developers."
keywords: "github, workflow tutorial, branch, pull, push, fork, share, commit, merge, peer review"
weight: 3
#date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /learn/github
  - /learn/workflow
  - /github/workflow
---
# Overview
By default, we follow the [Github Flow](https://guides.github.com/introduction/flow/) workflow model, which is explained below. This information is also summarized in a [Github Cheatsheet](../github_cheatsheet_tsh.pdf), so you can easily follow along or refresh your memory in case you ever forget a step in the workflow!

{{% summary %}}
 - All work on an issue happens in a separate repository *branch*.

 - When work is done, whoever is assigned to the issue creates a *pull request* which may include a request for peer review.

 - Once review (if any) is complete, the changes are *merged* back to the master branch and the final comment / deliverable are posted.
{{% /summary %}}

## Branch

* The assignee should create a new branch using `git branch` or `git checkout -b` on the command line, by clicking the "add branch" icon in the Github desktop client, or by creating the branch on the repository's Github page.

* If you are resolving an issue you can create a new branch most easily by going to the issue page and clicking "Create a branch" under Development. This will automatically link the branch to the issue and their pull requests. 

  ![Create a branch for an issue.](../create-issue-branch.png)

* The issue branch should be named `issueXXX-description`, where `XX` is the Github issue number and `description` is a version of the issue title (e.g., `issue123-update-appx-figures`). The description can be more compact than the issue title itself, but should be descriptive enough that other team members can understand what is being worked on in the branch.

{{% tip %}}
For complex issues, additional branches can be made off of the main issue branch. These should be named `issueXXX-description/sub-branch-description` (e.g., `issue123-update-appx-figures/refactor`) These sub-issue branches should be merged into the main issue branch before the main issue branch is merged back to the master branch.
{{% /tip %}}

## Commit

* All commits related to an issue should be made to the issue branch(es).

* Every commit must have a commit message whose first line has the form `#X Description of commit` where `X` is the Github issue number (e.g., "#123 Add first appendix figure").

* Any commit to master, that is merged to master, or that defines an issue deliverable should follow a complete run of the relevant modules / directories' build scripts (e.g., `make.py`).

{{% warning %}}
Crafting good commit messages is crucial to the history of work on a project being clear and readable. In this sense, a good commit message:
  - should describe the purpose of the commit

  - should not be redundant with what Git is already recording ("Update code" or "Modify slides.lyx" are redundant; "Refactor estimate() function" and "Add robustness figure to slides" are better).

  - should be written in sentence caps, use the imperative mood, and not end in a period ("#123 Revise abstract") not ("#123 abstract.").

  [This post](https://chris.beams.io/posts/git-commit/) by Chris Beams has an excellent discussion of what makes a good commit message.
{{% /warning %}}



## Pull Request

* When work on an issue is complete, the assignee should create a pull request by selecting the issue branch on the `code` tab of the repository's Github page then clicking `New Pull Request`.

* The title of the pull request should be `PR for #X: original_issue_title` where `X` is the Github issue   number (e.g., "PR for #123: Update appendix figures").

* The description / first comment of the pull request should begin with a line that says `Closes #X` where `X` is the number the Github issue number (e.g., "Closes #123"). This will close the original Github issue and create a link in that issue to the pull request. Subsequent lines of the description can be used to provide instructions (if any) to the peer reviewer.

* The pull request should be assigned to the assignee of the original issue.

## Peer Review

If an issue requires **peer review**, the assignee should assign the reviewer(s) in the pull request. In this case the description / first comment of the pull request should provide instructions that define the scope of the peer review along with any information the reviewer will need to execute it efficiently.

{{% warning %}}
Any issue that involves substantial changes to code should be peer reviewed by at least one other lab member (e.g. a research assistant), though it is ultimately up to the assignee's discretion whether or not to send the issue for peer review.
{{% /warning %}}

The job of the peer reviewer **IS** to verify that:
   *  The deliverable is clear, complete, and conforms to the standards from the deliverables section [here](https://tilburgsciencehub.com/building-blocks/collaborate-and-share-your-work/project_management/write-good-issues/)
   *  Files committed to the repository conform to our organizational and code style rules
   *  Empirical and theoretical results are clear and appear correct

It is **NOT** typically the job of the peer reviewer to:
  * go over every detail of the output and every line of code.

While commenting on fine points of code style from time to time is fine, for example, this should not be the primary content of the peer review. When requesting peer review the assignee can request feedback in addition to the above: e.g., particular code or results that need a careful check.


{{% warning %}}
* All peer review comments should be made on the pull request itself, not on the original issue.

* Revision to the code and other files in the repository as part of the peer review process should be made in the original issue branch (`issueXXX_description`) since the pull request will automatically track changes made in the branch.
{{% /warning %}}

## Merge

When peer review is complete, the output is finalized, and issue-specific content like the `/issue/` subdirectory has been deleted, the issue branch should be merged back to `master` using a [__squash__ merge](https://help.github.com/articles/about-pull-request-merge-squashing/). You can normally perform this merge automatically from the pull request page on Github.

Once the merge is complete, you should delete the issue branch.

## Exceptions to the Standard Workflow
In some cases we may use simpler workflows, for example skipping the branch/merge steps and just committing directly to `master`. Here are a few exceptions:

1. **No issue branch:** It is permissible to skip the step of creating an issue branch and commit changes directly to `master` when all of the following are true:
- The issue is small in scope and will involve no more than a few commits
- No one else is likely to be working on the same content at the same time
- All commits follow complete runs of relevant build scripts (e.g., `make.py`)

  {{% warning %}}
Separately, for some projects or repositories we may decide to use a simplified workflow where we commit everything to `master` by default. This could happen, for example, if some co-authors are unfamiliar with `git` and prefer the simpler workflow. In such cases we need to pay attention to avoid cases where many people will be working on the same content at the same time. We also impose a strict rule that all commits follow complete runs of `make.py`.
  {{% /warning %}}

2. **No pull request:** It is permissible to skip the step of creating a pull request if an issue does not require pull review and no changes will be merged back to the master branch.

3. **No peer review:** It is permissible to skip the peer review step when the assignee is confident the output is correct and the issue involves no changes or only minor changes to code that is being merged back to the repository.
