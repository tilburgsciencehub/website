---
title: "Python Coding Style Guidelines"
description: "Follow nice language-specific coding styles to make your code easier to understand and easier to the eye."
keywords: "style, code, python, best practices, guidelines"
weight: 2
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code/python
  - /python/style-guides
---
#### PEP 8
We follow Python's style guide [PEP 8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations). Also we:

* Use docstrings for functions whose purpose may be unclear or that will be used outside of their own modules

#### Supplemental resources:

* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/), especially the sections on [coding style](http://docs.python-guide.org/en/latest/writing/style/) and [packaging conventions](http://docs.python-guide.org/en/latest/writing/structure/).

* [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html), especially recommendations concerning [string formatting](https://google.github.io/styleguide/pyguide.html#Strings) and the rule to always explicitly close [files and sockets](https://google.github.io/styleguide/pyguide.html?showone=Files_and_Sockets#Files_and_Sockets).

Additional notes:

* When opening text files for writing or appending text, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "wb"` or `mode  =  "ab"` respectively to  write in binary mode. This improves portability across operating systems.

* When opening text files for reading, use [`open`](https://docs.python.org/2/library/functions.html)'s option `mode = "rU"` to enable universal newline support.
