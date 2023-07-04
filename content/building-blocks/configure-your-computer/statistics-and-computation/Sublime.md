---
title: "Set up Sublime Text"
description: "Learn how to install and use Sublime Text"
keywords: "Sublime, text, editor, setup, install, software"
draft: false
weight: 13
aliases:
  - /get/sublimetext
  - /get/sublime
  - /sublime
  - /sublimetext
  - /install/sublime
---

Sublime Text is a powerful and lightweight text editor that is widely used by programmers and developers. The current version, Sublime Text 4, offers a range of features designed to enhance coding productivity and efficiency. It provides support for multiple programming languages and comes with a Python application programming interface (API), allowing users to customize and extend its functionality.

With Sublime Text 4 installed, you are ready to dive into the world of coding and take advantage of its powerful features and customization options.

## Installing Sublime Text 4

#### Windows Users

Go to the official [Sublime Text downloads page](https://www.sublimetext.com/download) and download the installer for Windows. Run the downloaded installer by opening the .exe file,and follow the on-screen instructions. When the installation is complete, click "Finish" to exit the Setup. Sublime Text is now installed and can be accessed from your applications.  

#### Mac Users

Go to the official [Sublime Text downloads page](https://www.sublimetext.com/download) and download Sublime Text for Mac. Double-click on the downloaded .dmg file in your Downloads folder to open it. Drag the Sublime Text app into your Applications folder. You can now open Sublime Text by navigating to your Applications folder and clicking on the application.

#### Linux/Ubuntu users

On the [downloads page](https://www.sublimetext.com/download), click on the `direct downloads` link after `Linux repos`. Choose the appropriate version for your system. 


{{% tip %}}
**How to set up Sublime Text for Python**
 
Sublime Text can be enhanced with packages to support Python programming. Follow these steps to configure Sublime Text for Python development:

1. Install Python on your computer. If you haven't already, you can use our [Set up Python](/get/python) guide to install Python. Verify the installation by running `python --version` in your Command Prompt. If it is correctly installed, it should return the Python version. 

<p align = "center">
<img src = "../images/sublimeimage1.png" width="300">
</p>

2. Install `Package Control` in Sublime Text. 

`Package Control` is a package manager, which can be used for the installation of extensions. To install it, open Sublime Text and go to the "Command Palette" (under the "Tools" menu) or use the shortcut `Ctrl+Shift+P` (Windows) / `Cmd+Shift+P`(macOS). Type "Install Package Control" and select it from the options.

When successfully installed, the following message will pop-up as a confirmation:

<p align = "center">
<img src = "../images/sublimeimage2.png" width="300">
</p>

3. Install a package to execute Python code. The `Terminus` package is a popular choice, it brings a terminal as a window in Sublime Text.

A few alternatives to consider are `SublimeREPL`, which provides a REPL interface, or `Sublime-Jupyter` which allows you to work with Jupyter notebooks (.ipynb) directly within Sublime Text. To install any of these packages, open the "Command Palette" again, type "Package Control: Install Package", and search for the desired package.

4. To execute Python code, use the `Ctrl+B` (Windows) /`Cmd+B` (macOS) shortcut or go to "Tools" > "Build". The output will be displayed in the Sublime Text built-in terminal. 

<p align = "center">
<img src = "../images/sublimeimage3.png" width="400">
</p>

{{% /tip %}}