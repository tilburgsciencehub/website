---
title: "Error Handling in Stata Workflows Using R"
description: "Learn how to use R to check for errors and the completion of Stata code in batch mode or in a Makefile."
keywords: "exception, handling, stata, R, make, makefile, error, automation, workflow, log file, error checking, pipeline, log"
#date: 2021-03-19 #updated 2023-08-18
weight: 4
author: "Nazli Alagöz"
authorlink: "https://www.tilburguniversity.edu/staff/n-m-alagoz"
aliases:
 - /error-handling/stata-make
 - /automate/stata
 - /building-blocks/automate-and-execute-your-work/error-handling/stata-error-handling-make/
---

## Learning Goals

- Learn how to use R to monitor and handle errors in Stata log files.
- Incorporate error-checking scripts into automated workflows, such as a Makefile.

## Overview

When you run Stata within an automated research pipeline (e.g., using a `makefile`), Stata does not stop the progression of the `makefile`, even if there is an error in your code!

As a result, you won't know if the Stata code executed without errors unless you check the Stata log files. To remedy this issue, you can use R to check for any error that may have occurred in the log file. If there was an error, we can make the workflow to interrupt.

## Guidelines

### Pre-requisites

We will show you how to simply check the Stata log files for errors and stop the `makefile` if there are any errors.

* Ensure you have installed [Make](/get/make), [Stata](/get/stata) and [R](/get/r/).
* Confirm that your Stata do-file is set up to generate a log file. This log file will be the primary source for error detection.
* Use the below code block to create an R script called `logcheck.R` that checks for errors and the completion of the do-file from the log file.

{{% warning %}}
It's crucial to add these software installations to your environment variable named "PATH" to ensure seamless integration. If you're unfamiliar with adding tools to the PATH, here's a [helpful resource](https://github.com/alexal1/Insomniac/wiki/Adding-platform-tools-to-the-PATH-environment-variable).
{{% /warning %}}


### Code

{{% codeblock %}}
```R
# Define the arguments
args = commandArgs(trailingOnly=TRUE)

# Test if there is at least one argument: if not, return an error
if (length(args)==0) {
  stop("At least one argument must be supplied (input file).n", call.=FALSE)
}

# Read the log file
filecontent = readLines(args)

# Check if the log file includes an error massage and if so stop and display an error message
if (any(grepl('^r[(][0-9]',filecontent,ignore.case=T))) {
 stop(paste0('Log file for ', args, ' contains errors!'))
}
# Check whether the do-file was executed completely
if (!any(grepl('(end of do-file)',filecontent,ignore.case=T))) {

  stop(paste0('File (', args, ') has not been processed entirely!'))
}
# If no errors, report that there are no errors.
cat(paste0('Log file for ', args, ' checked. No errors.'))
```
{{% /codeblock %}}

Here, you can replicate any rule where you run a do-file which creates a log file. We just use some random rule:

{{% codeblock %}}

```bash
# Define a rule where you use a do-file
target_file: prerequisite.do # define your target and prerequisites
	rm prerequisite.log # remove older log file produced by prerequisite.do previously
	StataMP-64.exe -e do prerequisite.do # execute the do-file
	Rscript logcheck.R prerequisite.log # check the log file for errors or incompletion
```

{{% /codeblock %}}

{{% example %}}
Imagine you're working on a research project where you have raw data named `raw_data.dta` that needs to be cleaned and processed. You've written a Stata do-file called `data_cleaning.do` that takes this raw data and outputs a cleaned dataset named `clean_data.dta`. 

Additionally, every time you run the `do-file`, a log file named `data_cleaning.log` is generated.

Here's how you can set up your `makefile`:
```
clean_data.dta: raw_data.dta data_cleaning.do
	rm -f data_cleaning.log  
	StataMP-64.exe -e do data_cleaning.do  
	Rscript logcheck.R data_cleaning.log  

```
To use this `makefile`, you would:

1. Place the `makefile` in the directory with your raw data and Stata `do-file`.
2. Run the `make` command in your terminal or command line. 

This would trigger the data cleaning process using Stata, followed by the log check using R.
If the R script finds an error in the Stata log, it would interrupt the process and notify you of the issue. If no errors are found, the process completes, and you have your cleaned data ready for analysis!

<p align = "center">
<img src = "../images/stata-logfile.png" width="500" style="border:1px solid black;">
<figcaption> Output if R script finds an error in the log</figcaption>
</p>

{{% /example %}}

Remember, the above example assumes you've set up your Stata `do-file` to generate a log and you have the `logcheck.R` script as outlined before. Make sure to adjust the paths and filenames as per your specific project structure.

## Additional Resources

- Learn Stata with this [guides](https://sites.tufts.edu/datalab/learning-statistics/stats-online-tutorials/stata-resources/)
- How to use log files in Stata [video](https://www.youtube.com/watch?v=3N9l9i5HyaE)
- How to create log file in Stata [video](https://www.youtube.com/watch?v=kIjn_xJM2yQ)