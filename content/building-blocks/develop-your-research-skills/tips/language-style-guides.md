---
title: "Language-specific style guides"
description: "Follow nice language-specific coding styles to make your code easier to understand and easier to the eye"
keywords: "style, code, python, R, Stata"
weight: 3
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /coding/style-guides
---
## Python
We follow Python's style guide [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations). Also we:

* Use docstrings for functions whose purpose may be unclear or that will be used outside of their own modules

Supplemental resources:

* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/), especially the sections on [coding style](http://docs.python-guide.org/en/latest/writing/style/) and [packaging conventions](http://docs.python-guide.org/en/latest/writing/structure/).

* [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html), especially recommendations concerning [string formatting](https://google.github.io/styleguide/pyguide.html#Strings) and the rule to always explicitly close [files and sockets](https://google.github.io/styleguide/pyguide.html?showone=Files_and_Sockets#Files_and_Sockets).

Additional notes:

* When opening text files for writing or appending text, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "wb"` or `mode  =  "ab"` respectively to  write in binary mode. This improves portability across operating systems.

* When opening text files for reading, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "rU"` to enable universal newline support.

### R
We follow the general guidelines in [Google's R Style Guide](https://google.github.io/styleguide/Rguide.xml).

Exceptions:
* We do not follow their naming conventions (don't use dots, and underscores or camel-case are fine).
* See [conventions for line length](https://github.com/tilburgsciencehub/onboard/wiki/Code#keep-it-short)
* We do not require that all functions have a comment block describing their uses, though these are encouraged when the purpose of a function would not be clear or where it will be used outside of the file in which it is defined.


*Content based on Ulrich Bergmann, Matteo Courthoud, Lachlan Deer (2020), [Introduction and Motivation, Programming Practices for Research in Economics](https://github.com/pp4rs/2020-uzh-course-material/blob/master/00-intro/intro.pdf), University of Zurich.*

*The main principles we follow in writing code are summarized in [this Building Block](https://tilburgsciencehub.com/write/good-code) and the document [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf). See especially the Code Style appendix and chapters 1, 2, 6, and 7.*
