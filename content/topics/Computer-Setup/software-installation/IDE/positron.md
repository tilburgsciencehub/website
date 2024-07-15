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


| Feature                           | Positron                                              | VSCode                              | Rstudio                                                            | JupyterLab                     |
|-----------------------------------|-------------------------------------------------------|-------------------------------------|-------------------------------------------------------------------|--------------------------------|
| **Main goal of use**              | Data-science specific tools <br> (IDE for R, Python)  | General-purpose code editor         | IDE for R and Python                                              | Web-based IDE                  |
| **Supported programming languages**| R and Python as first-class supported languages. <br> Through extensions: Rust, Javascript, C/C++, or Lua | Almost every major programming language, <br> such as R, Python, and SQL. | Core language is R, but also supports <br> Python, SQL, Stan, C++, HTML/CSS, Markdown, Bash etc. | Python as the most widely used language, <br> but R, Julia, SQL, etc. are also supported. |
| **Customization and extensibility**| High: support for popular VSCode extensions <br> (possible to use without interfering <br> with your original VSCode extensions) | Rich library of extensions          | Yes, but limited compared to Positron                              | Limited                        |
| **Open source**                   | Yes                                                   | Mostly yes                          | Yes                                                               | Yes                            |
| **Development stability**         | Still under development, so some features <br> might be unstable or unfinished. | Stable                               | Stable                                                             | Stable                         |
| **Remote development (e.g., over SSH or dev containers)**| Not supported yet <br> (it is on the roadmap for development) | Yes                                  | Yes                                                               | Yes                            |
| **Added value compared to Positron (other features)**| -                                                     | More extensions <br> (not all available in Positron) | Inline output for Quarto and R Markdown, <br> profiling, Sweave, Add-In support. | -                              |
| **Desktop or in browser**         | Runs on desktop                                       | Desktop or in browser               | Desktop or in browser                                              | Only web-based                 |
| **Dedicated pane for data explorer and plots** | Yes                                                   | No                                   | Yes                                                               | No                             |






table
- first column: Positron
- second column: VSCode
- third: Rstudio
- fourth: JupyterLab

one row per feature

- Main goal of use:

Positron: Data-science specific tools (IDE for R, Python)

VSCode: General-purpose code editor
Rstudio: IDE for R and Python
Jupyter: Web-based IDE 


- Supported programming languages

1. R and Python as first-class supported languages. Through extensions: Rust, Javascript, C/C++, or Lua

2. Almost every major programming language, such as R, Python, and SQL.

3. Core language is R, but also supports Python, SQL, Stan, C++, HTML/CSS, Markdown, Bash etc. 

4. Python as the most widely used langauge, but R, Julia, SQL, etc. are also supported.



- Customization and extensibility

1. High: support for popular VSCode extensions (possible to use without interfering with your original VSCode extensions)
2. Vscode: Rich library of extensions
3. Rstudio: Yes, but limited compared to Positron
4. Jupyter: Limited 


- Open source
Positron: yes
Vscode: mostly yes
Rstudio: yes
Jupyter: yes

- Development stabilility

1. still under development, so some features might be unstable or unfinished. 
2. stable
3. stable
4. stable


- Remote development (e.g. over SSH or dev containers)

1. Positron: Not supported yet (it is on the roadmap for development)
2. Yes
3. Yes
4. Yes

- Added value compared to Positron (other features)


1. Positron: -


2. VSCode: More extensions (not all available in Positron)

3. Rstudio: 
Inline output for Quarto and R Markdown, profiling, Sweave, Add-In support.

4. Jupyterlab:


- Desktop or in browser

1. Runs on desktop
2. Desktop or in browser
3. Desktop or in broswer
4. Only web-based


- Dedicated pane for data explorer and plots. 

1. Yes
2. No
3. Yes
4. No




- 

Positron fully featured, more powerful compared to jupyter. 

Additional advantages of Positron
- Public API's; allows for addition of support of more languages that data scientists might use in the future. 




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



