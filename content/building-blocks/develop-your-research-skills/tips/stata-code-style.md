---
title: "Stata Coding Style Guidelines"
description: "Follow nice Stata coding style to make your code easier to understand and easier to the eye."
keywords: "style, code, Stata, guidelines, best practices"
weight: 6
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code/stata
  - /stata/style-guides
---
## Coding styles in STATA
We use two coding styles in Stata: a linear format for very short or simple scripts, and a functional style for longer or more complex scripts.

### 1. Linear Format.

{{% codeblock %}}

```
-Stata-

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

{{% /codeblock %}}


{{% tip %}}
If you include a comment as a header like this for one major block of code, you should include a similar header for every block of code at the same logical place in the hierarchy. This is a case where redundant comments are allowed. Comments are not there to provide information, but to make the code easy to scan.
{{% /tip %}}

### 2. Functional Style.

In the functional style in Stata, we enclose code within program... end blocks. **The first program is always called “main,” and the .do file always ends with an “Execute” step.**

```
-Stata-

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

In this example, these “functions” are really just blocks of code:
 - They do not accept any inputs and outputs.

 - But within this structure it is easy to add “syntax” commands to individual programs to define inputs and use “return” calls to pass back outputs.

{{% tip %}}
  - Functions in Stata should follow all the usual rules discussed in the [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf) manual for clear, logical abstraction.

  - Pay special attention to the input/output structure, making sure your functions increase rather than decrease the readability of code. (Because Stata’s way of passing inputs and outputs is so clunky, it is very easy to end up with lots of long argument lists and local variables that are actually harder to read than a simple linear version of the code.)
{{% /tip %}}

#### Shy Functions in Stata
Functions should be **shy** (see [Code and Data for the Social Sciences](http://web.stanford.edu/~gentzkow/research/CodeAndData.pdf)), that is, so that they operate only on local variables.

 - **Problem:** Data in memory is by definition a global variable in Stata.
 
 {{% example %}}

 From the following code:
   ```
   -Stata-

   use x y z using autodata.xls, clear
   prepare_data
   update_variables
   merge_new_data 
   regress productivity y_average z_average
   ```
 there is no way to tell what are the inputs and outputs to the `prepare_data`, `update_variables`, and `merge_new_data` functions and no way to tell where the `productivity`, `y_average`, and `z_average` variables came from.
 {{% /example %}}

- **Solution:**
  - When possible, write functions that only operate on variables that are explicitly passed to the function and do not otherwise touch the data in memory.

  - If a function creates new variable(s), the names of these variables can be specified as part of the function call.
    - This should always be true of ado files.
    - For programs only defined and used within a given .do file, it’s a matter of judgment.






## Merging

  *  By default, we should use Stata’s built-in merge command

  *  In older versions of Stata, the merge command was not robust, and we therefore used the add-on command `mmerge` instead. Much of our old code uses mmerge. The only cases we should use mmerge in new code is when we require functionality like the `urename()` option that does not exist in the built-in merge command.

{{% tip %}}  

  * Guidelines for using `merge`:

    *  Always specify the type of merge (`1:1`, `m:1`, or `1:m`). Failing to specify the merge type calls the old, non-robust version of merge.

    *  Never do many to many (`m:m`) merges, or at least, only do them when you have a very good reason.

    *  Always include the `assert()` option to indicate what pattern of matched observations you expect.

    *  Always include the `keep()` option to indicate which observations are to be kept from the merged data set.

    *   Whenever possible, include the `keepusing()` option and enumerate explicitly what variables you intend to be adding to the dataset; you can include this option even when you are keeping all the variables from the using data.

    *   Use the `nogen` option except when you plan to explicitly use the `_merge` variable later. You should never save a dataset that has `_merge` in it; if you need this variable later, give it a more informative name.

    *  You should follow analogous rules for `mmerge`. E.g., you should always specify the type() option.
{{% /tip %}}

## Miscellaneous

  *  Always use forward slashes (`/`) in file paths. (Stata allows backslashes (`\`) in file paths on Windows, but these cause trouble on non-Windows OS’s.)

  *  Use `preserve`/`restore` sparingly. Excessive use can make code hard to follow; explicitly saving and opening data files is often better.

  *  We should always use `save_data`, our custom version of Stata’s save command when saving datasets to /output/. The ado file and its help file can be found in the `/gslab_misc/ado/` directory of our `gslab_stata`
GitHub repository. `save_data` replaces both `save` and `outsheet`, the standard Stata commands and requires the user to specify a key for the file. The command confirms that the key(s) are valid, places the keys at the top of the variable list, and sort the file by its key(s). File manifest information is stored in a log file if there is an output folder.

  *  When the number of variables needed from a dataset is not too large, list the variables explicitly in the `use` command.
