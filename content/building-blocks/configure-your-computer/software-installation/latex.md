---
title: "LaTeX"
date: 2020-11-11T22:02:51+05:30
draft: false
---

LaTeX is a great typesetting system that includes a lot of features that allow to produce scientific documents. Many researchers use LaTeX to produce their papers and presentations, and many journals require authors to hand in their articles in a LaTeX format.

## Installing a TeX distribution
LaTeX is free to use. To use the LaTeX system, a TeX distribution needs to be installed. Detailed instructions for the different platforms are provided below.

After following the instructions, check whether everything worked by checking the output of the following command:

```bash
tex --version
```

This should give an output similar to this one, where version numbers and details will change depending on your platform.

```bash
TeX 3.14159265 (TeX Live 2019/Debian)
kpathsea version 6.3.1
Copyright 2019 D.E. Knuth.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the TeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the TeX source.
Primary author of TeX: D.E. Knuth.
```

!!! note "For Windows Users"
    Download the file `install-tl-windows.exe` from [here](https://www.tug.org/texlive/acquire-netinstall.html) and follow the instructions.

!!! note "For Mac Users"
    We can install this using `homebrew`:

    ```bash
    brew cask install mactex
    ```

!!! note "For Linux Users (Ubuntu-based)"
    Install it from the terminal using

    ```bash
    sudo apt-get install texlive-latex-extra
    ```

    Note that additional packages for Tex Live should be installed through the apt package manager as well (using `tlmgr` leads to problems due to different versions)
