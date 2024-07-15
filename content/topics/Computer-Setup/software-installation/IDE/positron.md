---
title: "Positron, A Promising Early-Stage IDE"
description: "Positron is an exciting new data-science working environment, offering powerful features, support for multiple languages, and customization options."
keywords: "positron, data, science, development, integrated, environment, IDE, posit, R, Python, guide"
draft: false
weight: 3
author: "Virginia Mirabile, Valerie Vossen"
aliases:
  - /get/positron
  - /positron
---

## Overview

[Positron](https://github.com/posit-dev/positron) is an exciting new entrant in the data science IDE (*Integrated Development Environment*) space, offering a blend of powerful features, customiaztion options, and support for multiple programming languages. 

While it is still under development and has some limitations, its potential to streamline and enhance data science workflows makes it a tool worth watching for data scientists seeking an efficient working environment. After this introductory article, you can start experimenting with this working environment yourself yourself!

{{% summary %}}

Positron stands out with several unique features, including:

- *Multi-language support*: Use Python and R, and additional languages like Rust, C++, Javascript and Lua. 

- *Dedicated console and variables pane*, to keep track of your variables without cluttering the main workspace

- An integrated *data explorer* makes it easy to visualize manipulate data within the IDE.

- Access to a wide range of *VS Code Extensions*: As Positron is a fork of Code OSS, users have access to VS Code extensions.

{{% /summary %}}

## Comparing Positron to other popular IDE's 

To find the added value of Positron compared to other popular IDE (e.g. Jupyter, Rstudio)


|                            | Positron                                              | VSCode                              | Rstudio                                                            | JupyterLab                     |
|-----------------------------------|-------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------|--------------------------------|
| **Main goal <br> of use**              | Data-science <br> specific tools <br> (IDE for R, Python)  | General-purpose <br> code editor         | IDE for <br> R and Python                                              | Web-based IDE                  |
| **Supported <br> programming <br> languages**| R and Python. <br> Through <br> extensions: <br> Rust, Javascript, <br> C/C++, or Lua | Almost every <br> major <br> programming <br> language, <br> such as R,  <br> Python, and SQL. | Core language <br> is R, <br> also supports <br> Python, SQL, <br> Markdown etc. | Python is  <br> the most <br> widely used <br>, but R, Julia, SQL, <br> etc. also supported. |
| **Customization <br> and <br> extensibility**| High: support  <br> for popular <br> VSCode extensions | Rich library <br> of extensions          | More limited                             | Limited                        |
| **Development <br> stability**         | Still under <br> development; <br> some features <br> might be unstable <br> or unfinished. | Stable                               | Stable                                                             | Stable                         |
| **Remote <br> development <br> (e.g., over SSH or <br> dev containers)**| Not supported <br> (yet) | Yes                                  | Yes                                                               | Yes                            |
| **Added value <br> compared <br> to Positron**|        | More extensions <br> (not all available <br> in Positron) | Inline output <br> for Quarto and <br> R Markdown, <br> profiling, Sweave, <br> Add-In support. | -                              |
| **Desktop or <br> in browser**         | Desktop                                       | Desktop or <br> in browser               | Desktop or <br> in browser                                              | Web-based                 |
| **Pane for <br> data explorer <br> and plots** | Yes                                                   | No                                   | Yes                                                               | No                             |


## How to install Positron 

Make sure you have [Python] or [R] installed (depending on what you plan to use Positron for) separately. Check [here](https://github.com/posit-dev/positron/wiki#machine-prerequisites) which latest version is required. 


### Windows 

- Visit the [Positron Releases page](https://github.com/posit-dev/positron/releases)

- Click the Assets section, and choose the file ending with `Setup.exe` to download the Windows Installer packagee. 
- Click on the installer in your download history. A set-up wizard will appear.
- Follow the wizard; allow the app to make changes in your computer, accept the license agreement and click "Next" and "Install". 
- Once the installation is complete, click "Finish" to close the setup wizard. 

### Mac

- Go to the [Positron Releases page](https://github.com/posit-dev/positron/releases). Click on the file ending with `.dmg` to install the Mac installer.
- Navigate to the download folder and double-click the file to start the installer. 
- Follow the installation wizard, agree to the license agreement, and click "Install".
- Once the installation is complete, click "Close".


??
Alternatively, you can install Positron directly from the command line on a Mac device. Open a terminal window and type:

{{% codeblock %}}
```bash
brew install positron
```
{{% /codeblock %}}


### Linux

`.deb` file for Debian-based Linux (Ubuntu)?

??
To install Positron from the command line, open a terminal window and type:

{{% codeblock %}}
```bash
sudo apt install positron
```
{{% /codeblock %}}

Now that Positron is installed, you can start using it! The next section 


## Usage

## Connections pane

?
allows you to explore database connections created within your R or Python sessions



### Data explorer



### Installing extensions

VSCode extensions in Positron. 
browse extensions in marketplace, which includes most popular VS Code extensions. 



warning. 
The R and Python extension do not work well with the original support for R and Python language. Unless for very specific reasons, the built-in Python and R language support should be enough, without the need for extra extension. 
warning



