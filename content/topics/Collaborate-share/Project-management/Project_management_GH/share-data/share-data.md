---
tutorialtitle: "Document and Share your Data using GitHub"
title: "Data Sharing"
type: "data-sharing"
keywords: "data sharing"
weight: 1
draft: false
aliases:
  - /share/data
  - /topics/reproducible-research/share-data/share-data
  - /topics/reproducible-research-and-automation/share-data/_index
---

## Overview

When conducting your empirical research, you typically spend a lot of time cleaning and documenting your data so that team members can use it.

Several open science tools can help you manage the process of cleaning, documenting, and - importantly - maintaining your dataset more efficiently. For this, we require a "data workflow."

## What's a data workflow?

A data workflow consists of a code repository (e.g., on GitHub), your raw data (e.g., on a server), and a place to share your data with team members (e.g., via public clouds like Dropbox, or data repositories such as Zenodo or Dataverse).

We adhere to the following principles:

- Your code used for data cleaning and documentation is maintained with a versioning tool. We use GitHub.
- Your raw data is always stored *outside* of your repository, ideally on an external server. We assume your raw data is confidential. It will never be shared.
- The workflow creates "public" versions of your dataset. Let's call them your "releases." Of course, the data does not need to be shared immediately with the public. You can use the workflow to share your data with your team members as a first step.

## How to get started in 6 steps

### Step 1: Start a new GitHub repository

Don't start from scratch, but use our data workflow template, which you can find here:

Just click on "use template"!

- https://github.com/hannesdatta/data-spotify-releases-2015-2018
https://github.com/hannesdatta/data-spotify-playlist-ecosystem

You can make the repository publicly available without worry - your raw data will be on a secure server, and others won't be able to run the workflow without it at this moment.

<!--@ BBlocK: develop a "stripped" version of this workflow with dummy data for release
-->

### Step 2: Upload your raw data to a secure location

Raw data ideally is stored on a server that is frequently backed-up. For small-scale projects, it may be enough to keep the data on your institutional network drives or even on your computer's hard disk.

The most important aspect is that you need to be able to *automatically retrieve your data* from that location later. Don't put it on a USB stick or on a laptop that you can lose during your commute!

<!-- BBlocK: add bblock on storing possibilities
-->

### Step 3: Clone your repository

Now let's move the repository from GitHub to your local computer by cloning it.

```
git clone https://github.com/your-username/your-repository-name
```

Navigate to the directory structure - do you recognize the components we've talked about earlier?

### Step 4: Download your data and store authentication credentials

Did you notice that the raw data folder is empty? It's supposed to be like this! Recall that raw data should never be versioned. To still work with the data, you need to write a little code snippet to *download* the data from its secure location to your local repository.
<!-- add building blocks -->

Probably you need to use some passwords to download the data. *Never* store them in your source code (after all, it will become public on GitHub).

<!-- add building blocks-->

### Step 5: Work on your data and documentation

You're set up to document and maintain your data set!

- Write code to clean your data, and make sensible decisions about what will remain "secure and private," what part of the data you can disclose to coauthors, and what part of the data can be used publicly.
- You can also automate your workflow using `makefiles`.
- Document your data using our handy templates. You find them [here](https://tilburgsciencehub.com/document/new-data).

Write your final output data - the one you or others will be using for your project - to the `release` folder.

### Step 6: Share your data and workflow

Write a little code snippet that pushes your final data set to your team members, for example, to Google Drive, Dropbox, or S3.

Whenever you are making updates to the data or documentation, you can "re-push"/upload the data and notify your coauthors about the update.

It's good practice to supply coauthors with a little code snippet to download the most recent data set. Ideally, you store that snippet in the (separate) GitHub repository of your empirical research project. As long as your team members' repository is up-to-date, they will always use the most recent version of your data.

### Advanced use cases

- Launch a website that tells potential users of your data about it. Check out [this excellent page](https://nijianmo.github.io/amazon/index.html) by Julian McAuley.

- Push your code, documentation, and final data set to Dataverse or Zenodo for long-term storage. Both offer DOI's, so your work becomes citable!

- Engage with your community of data users on GitHub (e.g., via issues or using the discussion board). It's good practice to maintain an FAQ, so you don't need to answer questions over and over again.

Above all, don't perceive the process as a burden. Instead, enjoy the experience of seeing how the *quality of your data* becomes better with each iteration of this process.


<!--
### Create

- Create GitHub repository from template
- Store raw data on secure server (institution)
- Create data prep code to create derived version
- Create initial documentation from template
- Prototype workflow by running it with `make`

### Share

- Publish internally
  - Store on Dropbox
  - Store on S3, make available to coauthors (code snippet)

- Publish externally
  - Dataverse
    1. Create empty data verse
    2. Get Dataverse API credential
    3. Run push.sh or push.bat in repository to push data to server
