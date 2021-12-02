---
title: "Learn About the Various Ways to Setup a Research Infrastructure"
description: "The main considerations before launching any empirical research project."
keywords: "collaboration, security, data management, run-time, data storage, computation, code versioning"
weight: 2
date: 2021-03-05T22:01:14+05:30
draft: false
aliases:
  - /learn/infrastructure-requirements
---

## Overview

Before diving right into the nitty gritty details, there are a couple of questions that you should always ask yourself at the start of any empirical research project. Here we present to you a 5-step plan that outlines these main considerations in a structured manner.

{{% tip %}}
As with many of the workflow procedures, we realize that it may come across as a series of redundant steps. And truth be told, it probably does take more time before you experience the benefits. However, we also believe that you should not reinvent the wheel each and every time you launch a new project. In fact, these ideas may become an integral part of your workflow as you get more experience with it.
{{% /tip %}}


## 5 Step Plan

### 1. Will you collaborate with others on writing code?
If you do, using a version control system like Git is a must-have, as you need to be able to work on a project simultaneously, without running the risk of overwriting each other’s work.

{{% example %}}

Unlike Google Docs, where you can work on the same file at the same time, in a code editor you tend to work independently from one another. Of course, it can still happen that one of your co-editors and you make changes to same file. For example, you may use the variable name `aggregated_df`, while your team member referred to it as `df`. In these cases, there is not a good or bad answer per se (both may work totally fine!). Yet, in the end, we do need to be consistent with how we reference variables or our script will likely break at some point.

To prevent his from happening, Git informs you about so-called *merge-conflicts*. That is, it indicates where two versions of the same file - that are about to be merged into one - differ from one another. Then, you can make the necessary changes (i.e., choose one of either approaches) and proceed with the merging procedure.

{{% /example %}}


### 2. What’s the technical proficiency of your team members?
It’s not uncommon that your team members may be unfamiliar with tools like Git, make, or the terminal. First, that’s not a problem at all. You can stay in charge of the main workflow, and integrate others’ work as it is being updated (e.g., on Dropbox). However, it’s way better to help team members develop the skills to use Git and automation, just to name a few.

{{% example %}}
To illustrate why this is important, we should note that in any academic project a researcher has certain degrees of freedom. How are variables operationalized, on which level is the data aggregated, are outliers excluded (or not), just to name a few. As the number of these decisions tends to add up quickly, it is essential that not only you can reproduce your own results, but also that others can do so and critique your choices. This stands or falls, however, by your collaborators' technical proficiency to get the tools up and running, which is why this is an important infrastructure consideration.
{{% /example %}}

### 3. What minimum security levels do you have to ensure? Can you make your code public?

Although the reproducible science community strongly advocates for transparency and openness, there are circumstances in which you are simply constrained by regulations, and you may even be required to take additional measures to prevent data leakage. This, in turn, affects how you should configure your tools and which safety measures you need to take.

{{% example %}}
Industrial partners may ask you to sign a Non-Disclosure Agreement (NDA) that enforces you to keep the supplied data private. As data leakage can severely harm a company's reputation, this comes with a great responsiblity on your end.

For example, you may need to use a private (instead of a public) repository, configure 2-factor authentication for your Github account, and use environmental variables as placeholders in your script rather than hard-coded login credentials of databases or APIs).
{{% /example %}}


### 4. How will you manage your data?
Related to the previous consideration, some data management solutions are easier to implement than others. Cloud storage services like Dropbox and Google Drive may be easy to get started with as most people are familiar with them nowadays, yet they have their own set of limitations.

{{% example %}}
Although most cloud services offer some free data storage, you may quickly reach its limits. In particular for longitudinal studies or web scraping projects, this is an important aspect to consider upfront. After all, you don't want to switch up your data storage in the middle of your project because you run out of space.

In addition to size limitations, there are other reasons to choose for a more dedicated data management solution. For example, you may want to enforce a data type (e.g., values in the `id` column can only be integers), link multiple tables together (e.g., normalized database schema), or GDPR regulations require you to rely on legacy systems (e.g., on-premise database) - as opposed to cloud solutions - to obtain the data you're after.

At the end of this building block, we provide some links to resources that help you get started with structured (e.g., `SQL database`) and unstructured (e.g., `JSON` files) data management solutions.
{{% /example %}}




### 5. How long will the workflow run?
Even though importing a dataset and running a multitude of regression models typically happens with a matter of seconds, you may encounter circumstances in which you need to factor in the expected run time already in the project set-up.

For example, if you need to throttle API calls, experiment with a variety of hyperparameters, or run a process repeatedly (e.g., web scraping) the hardware of your local system may not suffice. Also, keeping your system up and running all day long (e.g., throughout the nights) is typically not desirable. In these cases, creating a virtual instance (i.e., a computer in the cloud that you can control) adjusted to your specific needs (e.g., more memory than your own machine) can overcome runtime issues.


{{% summary %}}

Together, these 5 considerations can guide your decision-making in terms of (a) code versioning, (b) raw data storage, and (c) computation (local vs remote).

{{% /summary %}}


## See Also
* If you're unfamiliar with Git, you may first want to take a more comprehensive look at its features to better evaluate the pros and cons. [Here](/get/git) we explain how to install Git and create an account. [This](/use/git) building block illustrates how to get started with Git repositories.  
* Amazon Simple Storage Service (often referred to as S3) provides an alternative way to store data into buckets. [This](/use/aws-s3) building block summarizes the main commands you need to download and upload files.
* [This](https://www.youtube.com/watch?v=pd-0G0MigUA) video tutorial shows how to leverage Python SQLite to create a database, table, and run queries on a local SQL database. The same ideas can be applied to cloud databases as well.
