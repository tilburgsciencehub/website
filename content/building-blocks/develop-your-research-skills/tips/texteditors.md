---
title: "Comparing text editors"
description: "Learn the differences between text editors Visual Studio Code, Sublime Text, Emacs and Vim"
keywords: "VSCode, Sublime, Emacs, Vim, text, editor"
draft: false
weight: 8
aliases:
  - /texteditors
  - /texteditors
  - /compare/texteditors
---

A good text editor lies at the heart of any serious programmer's toolkit: It can do almost anything and makes you much more productive. The text editors bundled with programming languages, like python's IDLE, are often not the best option (although there may be certain cases where you may want to use them). 

In this building block, we will compare some widely used text editors: **Visual Studio Code (VS Code), Sublime Text, Emacs and Vim**. 

Please download and install the text editor of your choice, along with any necessary packages, and stick with it for a while to get a feel for how it works. Despite a slight learning curve, you'll quickly find yourself wondering why you didn't start using it sooner!

## VS Code and Sublime Text
Both *VS Code* and *Sublime Text* are highly capable editors with their own strengths and weaknesses. Choosing between the two depends on your preferences and the features that are most important to you. For setting up these text editors, check our building blocks [Set up VS Code](/get/VSCode) and [Set up Sublime Text](/get/sublime).

Let's compare them in various aspects:

- **User interface**

*VS Code* has a feature-rich and modern user interface, with a sidebar for easy navigation, an integrated terminal, and customizable themes and extensions. It provides a visually appealing and immersive editing experience.

<p align = "center">
<img src = "../images/vscodeinterface.png" width="400">
<figcaption> VS Code interface </figcaption>
</p>

On the other hand, *Sublime Text* offers a cleaner and more minimalistic user interface, which can be less distracting. It is also customizable. 

<p align = "center">
<img src = "../images/sublimetextinterface.png" width="400">
<figcaption> Sublime Text interface </figcaption>
</p>

The advantage in this aspect depends on your personal preference - whether you prefer a feature-rich interface or a more streamlined and distraction-free environment.

- **Extensions**

*VS Code* offers a vast extension marketplace with a wide range of plugins and extensions for various programming languages, frameworks, and tools. *Sublime Text* also offers a range of extensions and packages, although the number of available extensions is smaller compared to VS Code.

- **Performance and speed**

*Sublime Text* is renowned for its exceptional performance and speed. It is one of the fastest text editors available and is known for its lightweight nature. *VS Code* is also fast and performs well, but it may have a higher resource usage compared to Sublime Text, especially when working with large projects or using many extensions. If speed, simplicity and lightweight usage are your priorities, Sublime Text may have an advantage in this regard.

- **Support**

*VS Code* benefits from a larger user base, extensive documentation, and a vibrant support community. It is likely easier to find tutorials, guides, and answers to questions related to VS Code due to its popularity and active community. *Sublime Text* has its own dedicated user base and documentation, but the community support and available resources may be relatively smaller compared to VS Code. 

## Emacs & Vim

Emacs and Vim are powerful text editors designed for efficient and productive editing in a terminal environment. While they may have a steeper learning curve than VS Code and Sublime Text, they offer unique features and capabilities that cater to the needs of experienced users and those who prefer working in a command-line environment. 

### Emacs/Vim compared to VS Code/Sublime Text
They are different than VS Code and Sublime Text in their approach: They prioritize efficiency and keyboard-centric workflows. This makes them often favored by advanced users who value speed and precise control over their editing. Key differences of Emacs/Vim with VS Code/Sublime Text are:

- Emacs and Vim are primarily designed as *command-line editors*, while they do offer graphical user interfaces by now. This makes them tend to have a lower memory footprint and require fewer system resources than GIU-based editors VS Code and Sublime Text. This can be advantageous, especially working on older or resource-constrained machines, or machines without a desktop environment.

- While Emacs and Vim are available on various platforms, including Windows and macOS, they have a strong presence in the Linux community. Many Linux users appreciate the lightweight nature and versatility of these editors, making them popular choices for programming tasks on Linux systems.

- Emacs and Vim offer more customization options compared to VS Code and Sublime Text. 

### Comparing Emacs and Vim
<p align = "center">
<img src = "../images/emacsinterface.png" width="400">
<figcaption> Emacs interface </figcaption>
</p>

<p align = "center">
<img src = "../images/viminterface.png" width="400">
<figcaption> Vim interface </figcaption>
</p>

While Emacs and Vim share a similar in goal of use, there are some notable differences:

- *Vim* is more lightweight and faster than Emacs. For instance, Vim minimizes the number of keystrokes required for certain commands. Emacs, on the contrary, involves pressing multiple keys simultaneously to enable a shortcut for a single function. 

- While both Emacs and Vim offer extensive customization options, *Emacs* stands out. Through Emacs Lisp, it provides users with the ability to modify almost every aspect of the editor's behavior and appearance. 

- *Emacs* is generally considered simpler to learn compared to Vim, because it provides a more natural interface. Vim has different editing modes, which could be unintuitive for beginners.

{{% tip %}}
Vim has two different editing modes: 
- Command Mode: In this mode, every character typed is interpreted as a command that performs an action on the text file being edited. You execute commands in this mode, like undo, find and replace and quit, etcetera. To swith from Command to Insert Mode, type `i`.

- Insert Mode: In this mode, the entered text is directly inserted into the file. Each character typed is added to the text, allowing you to write or edit content. Pressing the `Escape` key turns off the Insert Mode and returns to the Command Mode.
{{% /tip %}}

## Overview of the key comparing features
The following table provides the most important differences between the 4 text editors discussed in this building block:

|      | **VS Code** 	| **Sublime Text** 	| **Emacs** and **Vim** |
|---	|---	|--- | ---|
| *Goal of use* |   General-purpose <BR> editor |  General-purpose <BR> editor  |  Command line <BR>power editors    |
| *Ease of use*	| Beginner-friendly | Some learning, but <BR> user-friendly | Steep learning <BR> curve | 
| *Interface* | Feature-rich GUI | Distraction-free GUI | Text-based <BR> interface within <BR> command line <BR> interface |
| *Customization* | Extension <BR> marketplace | Variety of <BR> packages | Almost infinite <BR> customization <BR> options <BR> (particularly <BR> Emacs) |


{{% summary %}}
The best choice ultimately depends on your personal preferences and requirements since all 4 text editors are available cross-platform (on Windows, macOS or Linux). So, give them a try and see which one is the perfect fit for your programming journey! 
{{% /summary %}}

