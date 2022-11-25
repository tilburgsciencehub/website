---
tutorialtitle: "Create Your Own Website in 15 Minutes"
type: "hugo-website"
indexexclude: "true"
title: "Get Hugo"
description: "Learn how to install Hugo, a famous static site generator."
keywords: "hugo, static, website, generator, class, academic"
date: 2021-01-06T22:01:14+05:30
draft: false
weight: 11
author: "Andrea Antonacci"
authorlink: "https://www.tilburguniversity.edu/staff/a-d-antonacci"
aliases:
  - /get/hugo
  - /tutorials/open-education/hugo-website/get-hugo
  - /tutorials/educational-support/hugo-website/get-hugo/
---

## Install Hugo

First off, make sure to have [Git](/get/git) properly installed and set up.

### MacOS & Linux

Make sure you have [Brew](/building-blocks/configure-your-computer/automation-and-workflows/commandline/#mac-users) installed. Then, to install Hugo:

```
brew install hugo
```

### Windows

If you use [Chocolatey](https://chocolatey.org):

```
choco install hugo -confirm
```

Alternatively, see other installing options [here](https://gohugo.io/getting-started/installing).

## Create a New Local Website

You're now ready to start.

To create a new Hugo website, move to a directory of your choice and run:
```
hugo new site yourwebsitename
```
Where `yourwebsitename` is the name of the folder you've just created. Your entire website will live inside this folder on your computer.

Congrats! In the next sections, you will start tweaking your new website.

{{% tip %}}
Check out the Hugo documentation for the official [quick start guide](https://gohugo.io/getting-started/quick-start/).
{{% /tip %}}
