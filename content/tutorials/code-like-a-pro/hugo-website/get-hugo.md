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

Hugo comes in two versions: a standard one and a so-called "extended" one. Here, we need the extended version.

Before you start, please check that [Git](/get/git) is properly installed and set up.

### MacOS & Linux

Make sure you have [Brew](/building-blocks/configure-your-computer/automation-and-workflows/commandline/#mac-users) installed. Then, to install Hugo. `Brew` automatically installs the "extended" version:

```
brew install hugo
```

### Windows
1. Install the ZIP file of the latest `hugo-extended` release for Windows from this [repository](https://github.com/gohugoio/hugo/releases) (scroll down to "assets")
2. Move the ZIP file and extract its content in the `c:\Hugo\bin` folder on your local machine. You should see three new files: Hugo executable (i.e., `hugo.exe` file), `license.md`, and `readme.md`.
3. Add Hugo to your Windows PATH settings by following these steps. Click on `System` -> `Advanced System Settings` -> `Environment Variables`. In the User variables section, double-click on `PATH` and click `New`. Then, type the file path `C:\Hugo\bin` where the `hugo.exe` was extracted. Click on OK and exit.
4. Verify if Hugo is installed properly. Type `hugo help` on a command prompt window. You should see the following output:

<p align = "center">
<img src = "../img/hugo-verify.png" width="500">
<figcaption> Verify Hugo Installation </figcaption>
</p>


If you use [Chocolatey](https://chocolatey.org):

```
choco install hugo-extended -confirm
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
