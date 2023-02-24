---
title: "Debugging Makefiles With Remake"
description: "Tool to debug makefiles"
keywords: "make, remake, debugging, makefile, automation, recipes, workflow"
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /remake
---
# Overview
When working on complex projects that contain several datasets and scripts to be run, it can get quite tedious to keep track of the order of running scripts or check if certain scripts need to be executed again to keep up-to-date. In this regard, [`Make`](https://tilburgsciencehub.com/learn/makefiles/?utm_campaign=referral-short) is a great tool to automate the execution of the entire workflow with a single command, making it reproducible.

However, `make` can still be somewhat opaque when it comes to diagnostics. This is where the debugger `remake` comes in handy. Whenever you run into issues while running make, switching to `remake` is helpful as it provides extensive error information to then debug your workflow quickly.

## Steps to debugging

To illustrate the steps to debugging with `remake` we will use an example workflow with the following directory structure. Now suppose the files `cleaned_listings.csv` and `cleaned_listings1.csv` were created after running the `cleaning. R` were not saved in the temp folder. The files in the output folder are dependent on these files in the temp folder which will result in an error while executing make. Let’s see how `remake` helps spot this bug in the workflow easily.

{{% codeblock %}}


```bash
├── Airbnb data.Rproj
├── README.md
├── data
│   └── listings.csv
├── gen
│   ├── output
│   │   ├── ordinary_hosts.html
│   │   ├── plot_nrreviews.png
│   │   ├── plot_rating.png
│   │   ├── review_IR.html
│   │   ├── review_IR2.htm
│   │   ├── review_model.html
│   │   ├── super_hosts.html
│   │   ├── tobit1.html
│   │   └── tobit2.html
│   └── temp
│       ├── cleaned_listings.csv
│       └── cleaned_listings1.csv
├── makefile
├── report
│   ├── report.Rmd
│   └── report.html
└── src
    ├── analysis
    │   ├── Rplots.pdf
    │   ├── analysis.R
    │   └── makefile
    └── data-preparation
        ├── cleaning.R
        ├── download_data.R
        └── makefile


```

{{% /codeblock %}}

{{% cta-primary-center "Go to the GitHub Repository now" "https://github.com/srosh2000/Airbnb_Superhosts.git" %}}

### Tracing

When you run make, it simply spots the error without further information on how the target needs to be updated but we might get more information by consulting the rules for the target.

<p align = "center">
<img src = "../images/1.png" width="600">
<figcaption> Error output after running make </figcaption>
</p>

Now let us run *remake*:

<p align = "center">
<img src = "../images/remake.png" width="600">
<figcaption> Error output after running remake </figcaption>
</p>

This displays additional information. We get the line number inside the Makefile for target ***analysis*** (6) and the target that got us to this one.

For further traceback information, run `remake --trace analysis` or just `remake --trace` without target name.

<p align = "center">
<img src = "../images/trace.png" width="600">
<figcaption> Tracing output </figcaption>
</p>

The indentation in the first few lines containing file name and line numbers gives target level nesting. The target ***data-preparation*** was asked to be remade because it is a dependency of target ***analysis*** Thus, we get the dependency nesting as build and traverse the tree.

Finally, we also get details on the scripts that were run to build the target ***data-preparation*** This tells us to check the `cleaning.R` script for bugs.

Further, remake has lines of the form:

``` bash


##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```

These lines separate shell commands about to be run from the output that they produce.

{{% tip %}}
Run `remake -n` to see the sequence of steps that will be run to execute the workflow without actually running it.
{{% /tip %}}

### Entering the Debugger and Setting Breakpoints
The simple tracing method explained above is sometimes enough but we could also work with the built-in debugger which contains some useful commands for more efficient debugging.

Run `remake --debugger` , `remake -X` or `remake --debugger analysis` (with a specific target name, here: analysis) to enter the debugger.

<p align = "center">
<img src = "../images/remake-x.png" width="600">
<figcaption> Initiating debugger session </figcaption>
</p>

It first checks whether the Makefile itself is up to date. Now that we have initiated the debugger we can set a breakpoint and run until the dependent target. The debugger assigns a number to each breakpoint created. We could also set a breakpoint using a line number instead of a target name.  Both `continue` and `break` commands can be used to set breakpoints.

For a given target, there are three main stopping points:

- before target prerequisite checking: prereq
- after target prerequisite checking but before running commands: run
- after target is complete: end

<p align = "center">
<img src = "../images/breakpoint.png" width="600">
<figcaption> Setting breakpoint </figcaption>
</p>

Adding `run` to the end of `continue data-preparation` causes the debugger to stop after dependency checking. This is the default option. Previously, the debugger stopped *before* dependency checking , as shown by the icon `->`, so it lists the dependencies for the target. Here, the dependency for the target ‘analysis’ was ‘data-preparation’. Later, the debugger stopped *after* dependency checking, as shown by the `..` icon rather than `->`.

Furthermore, you can run `break` to get a list of all breakpoints. To delete breakpoints, run `delete` with the breakpoint number.

{{% tip %}}
[Click here](https://remake.readthedocs.io/en/latest/debugger/syntax.html#event-icons) for more information on the debugger syntax
{{% /tip %}}

Additionally, once you enter the debugger the `backtrace` command comes in handy to trace the root of the error.

<p align = "center">
<img src = "../images/backtrace.png" width="600">
<figcaption> Output from backtracing </figcaption>
</p>

{{% tip %}}
[Click here](https://remake.readthedocs.io/en/latest/debugger/commands.html) for a complete list of debugger commands.
{{% /tip %}}

Lastly, to exit the debugger session simply run `quit`.
<p align = "center">
<img src = "../images/quit.png" width="600">
<figcaption> Quitting debugger session </figcaption>
</p>

In summary, the following changes have been made to GNU Make to improve tracing and error reporting with remake:

- The Makefile name and the line inside this file are reported when referring to a target.
- A list of relevant targets with their locations is shown in the error message.
- The command invocation used to run make is also shown.
- There are useful options that allow for entering the debugger on error.
- The shell input that is about to be run is separated from the output in running that shell code.
