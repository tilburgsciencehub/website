# Tutorial to Implement an Efficient and Reproducible Workflow

Longing to put your knowledge from our [workflow guide](../workflow) into practice? Then follow this tutorial to implement a fully automated workflow to conduct sentiment analysis on tweets, using our [GitHub workflow template](https://github.com/hannesdatta/textmining-workflow).

## Objectives of this tutorial

-	Familiarize yourself with a [robust directory structure](../workflow/directories.md) for data-intensive projects
-	Experience the benefits of [automating workflows with makefiles/GNU make](../workflow/automation.md)
-	Learn to use Git templates for your own research projects
-	Adjust the workflow template to
    -	...download different datasets from the web
    - ...unzip data automatically
    -	...parse JSON objects and select relevant attributes
    - ...add new text mining metrics to the final data set using Python's `textblob`
    - ...modify the analysis in an RMarkdown/html document

## Prerequisites

-	Computer setup following our [setup instructions](../setup)
    - [Python](../setup/python.md) and the `textblob` package

        ```
        pip install -U textblob
        ```

        Then, open Python (`python`) and type

            import nltk
            nltk.download('punkt')

        If you receive an error message, please verify you are typing this command in python (opened on the terminal by typing `python`), and not *directly* in the terminal/Anaconda prompt.

    -	[R, RStudio](../setup/r.md) and the following packages:

        ```
        install.packages(c("data.table", "knitr", "Rcpp", "ggplot2", "rmarkdown"))
        ```

        When installing the packages, R may ask you to select a "CRAN-Mirror". This is the location of the package repository from which R seeks to download the packages. Either pick `0-Cloud`, or manually choose any of the location nearest to your current geographical location.

        !!! warning "R 4.0"

            Newer versions of R (>=R 4.0) may require you to download additional packages.

            ```
            install.packages(c("rlang", "pillar"))
            ```

            - If you're being asked whether to build these packages from source or not [options: yes/no], select NO.

            - If you're being asked to install RTools, please do follow these installation instructions.


    -	[GNU Make](../setup/make.md)

- Familiarity with our [workflows](../workflow), in particular on [pipelines and project components](../workflow/pipeline.md), [directory structure](../workflow/directories.md) and [pipeline automation](../workflow/automation.md).

-	Nice-to-haves:
    - Basic experience with Python and R
    -	Familiarity with common data operations using `data.table` in R
    -	Familiarity with text mining using Python and TextBlob
    - If you want to learn Git on the way...
        - Have Git installed on your computer (see here)
    	  - Have GitHub login credentials

## Disclaimer

To keep this tutorial as accessible as possible, it will mention Git/GitHub a few times, but assume you will acquire details on these skills elsewhere. In other words, versioning and contributing to Git repositories is not part of this tutorial.

<!-- to do:

add note what to put in make, and what to put in R-->
