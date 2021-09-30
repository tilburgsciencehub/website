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

### Stata
We use two coding styles in Stata: a linear format for very short or simple scripts, and a functional style for longer or more complex scripts.

 1. **Linear Format.**

```{stata}
*****************************
* Prepare data
*****************************
* Format X variables
... 
* Format Y variables
...
*****************************
* Run regressions
*****************************
... 
*****************************
* Output tables
*****************************
 ...
```

If you include a comment as a header like this for one major block of code, you should include a similar header for every block of code at the same logical place in the hierarchy. This is a case where redundant comments are allowed. The comments are not there to provide information, but to make the code easy to scan.

In the functional style in Stata, we enclose code within program... end blocks. The first program is always called “main,” and the .do file always ends with an “Execute” step.

2. **Functional Style.**

```{stata}
* PROGRAMS

program main
    prepare_data
    run_regressions
    output_tables
end

program prepare_data
    X = format_x_vars
    Y = format_y_vars
    ...
end

program format_x_vars
    ...
end

program format_y_vars
    ...
end

program run_regressions
    ...
end

program output_tables
    ...
end

* EXECUTE
main
```
{{% warning %}}
The `main` command must come at the end of the script is because Stata (like Python) reads in programs in order of appearance.
{{% /warning %}}

In this example, these “functions” are really just blocks of code: they do not accept any inputs and outputs. But within this structure it is easy to add “syntax” commands to individual programs to define inputs and use “return” calls to pass back outputs. Functions in Stata should follow all the usual rules discussed in the [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf) manual for clear, logical abstraction. You should pay special attention to the input/output structure, making sure your functions increase rather than decrease the readability of code. (Because Stata’s way of passing inputs and outputs is so clunky, it is very easy to end up with lots of long argument lists and local variables that are actually harder to read than a simple linear version of the code.)

In [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf), we discuss the principle that functions should be “shy.” Stata poses a special problem in this respect, because the data in memory is by definition a global variable. From the following code

```{stata}
use x y z using autodata.xls, clear
prepare_data
update_variables
merge_new_data 
regress productivity y_average z_average
```

there is no way to tell what are the inputs and outputs to the `prepare_data`, `update_variables`, and `merge_new_data` functions and no way to tell where the `productivity`, `y_average`, and `z_average` variables came from. When possible, write functions that only operate on variables that are explicitly passed to the function and do not otherwise touch the data in memory; if a function creates new variable(s), the names of these variables can be specified as part of the function call. This should always be true of ado files; for programs only defined and used within a given .do file, it’s a matter of judgment.


#### Merging

  *  By default, we should use Stata’s built-in merge command

  *  In older versions of Stata, the merge command was not robust, and we therefore used the add-on command `mmerge` instead. Much of our old code uses mmerge. The only cases we should use mmerge in new code is when we require functionality like the `urename()` option that does not exist in the built-in merge command.

  *  Guidelines for using `merge`

      *  Always specify the type of merge (`1:1`, `m:1`, or `1:m`). Failing to specify the merge type calls the old, non-robust version of merge.

      *  Never do many to many (`m:m`) merges, or at least, only do them when you have a very good reason.

      *  Always include the `assert()` option to indicate what pattern of matched observations you expect.

      *  Always include the `keep()` option to indicate which observations are to be kept from the merged data set.

      *   Whenever possible, include the `keepusing()` option and enumerate explicitly what variables you intend to be adding to the dataset; you can include this option even when you are keeping all the variables from the using data.

      *   Use the `nogen` option except when you plan to explicitly use the `_merge` variable later. You should never save a dataset that has `_merge` in it; if you need this variable later, give it a more informative name.

      *  You should follow analogous rules for `mmerge`. E.g., you should always specify the type() option.


#### Miscellaneous

  *  Always use forward slashes (`/`) in file paths. (Stata allows backslashes (`\`) in file paths on Windows, but these cause trouble on non-Windows OS’s.)

  *  Use `preserve`/`restore` sparingly. Excessive use can make code hard to follow; explicitly saving and opening data files is often better.

  *  We should always use `save_data`, our custom version of Stata’s save command when saving datasets to /output/. The ado file and its help file can be found in the `/gslab_misc/ado/` directory of our `gslab_stata`
GitHub repository. `save_data` replaces both `save` and `outsheet`, the standard Stata commands and requires the user to specify a key for the file. The command confirms that the key(s) are valid, places the keys at the top of the variable list, and sort the file by its key(s). File manifest information is stored in a log file if there is an output folder.

  *  When the number of variables needed from a dataset is not too large, list the variables explicitly in the `use` command.

*Content based on Ulrich Bergmann, Matteo Courthoud, Lachlan Deer (2020), [Introduction and Motivation, Programming Practices for Research in Economics](https://github.com/pp4rs/2020-uzh-course-material/blob/master/00-intro/intro.pdf), University of Zurich.*

*The main principles we follow in writing code are summarized in [this Building Block](https://tilburgsciencehub.com/write/good-code) and the document [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf). See especially the Code Style appendix and chapters 1, 2, 6, and 7.*
