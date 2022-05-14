---
title: "Overleaf"
description: "Learn how to use Overleaf"
keywords: "overleaf, lyx, latex"

weight: 3
aliases:
 - /overleaf/
---

## Why should you use Overleaf?
Overleaf is an online Latex editor. It enables to collaborate on the cloud-based document and is mainly used for writing scientific papers.

## Why should you use Overleaf?
Overleaf is a very easy to use. It has a very user-friendly structure. You can use Overleaf when you want to collaborate with many people.

## How to set up an Overleaf account?
You can use your email address to set up an account as shown below :

<p align = "center">
<img src = "../Overleaf_LoginPage.png" width="500">
</p>





{{% codeblock %}}
```shell script
pip install git+https://github.com/mcaceresb/tablefill
tablefill --help
```
{{% /codeblock %}}

## How to use tableFill?
There are three steps to use tableFill function. To use tableFill, you should create one template file and a text file of results.

The template file is a markdown file that will be filled with results later on. The text file of results includes the results that you want to fill the table in the template. These results can be anything such as regression results and summary statistics.

### Step 1 : Create a markdown document template
This template will be filled with the results. The results can be anything ranging from regression results to summary statistics.

Below, there is an example of a template table. This tableFill function will look for a tag  "example" in the  when it fills the table.

{{% codeblock %}}
```R
<!-- tablefill:start tab:example -->

| Outcomes     | N    | Mean | (Std.) |
| ------------ | ---- | ---- | ------ |
| Outcomes ### | #0,# | #1,# | (#2,#) |
| Outcomes ### | #0,# | #1,# | (#2,#) |
| Outcomes ### | #0,# | #1,# | (#2,#) |
| Outcomes ### | #0,# | #1,# | (#2,#) |

<!-- tablefill:end -->
```
{{% /codeblock %}}



### Step 2 : Get your results and convert them to a text file
You should save you results (e.g., from a regression, summary statistics) in a text file.

{{% warning %}}
The tag name of the results should correspond to the the tag name of the section in the template that you want to fill in
{{% /warning %}}



Below, there is a function for saving your results in a text file in R.


{{% codeblock %}}
```R
saveTable <- function (outfile, tag, outmatrix) {
    cat(tag,
        sep    = "\n",
        file   = outfile,
        append = TRUE)

  # "outfile" : the name of the text file that will have your results
  # "tag" : the name of the table that the tablefill function will look for when
  #filling the placeholders.
  # "outmatrix" : the matrix of the results

    write.table(outmatrix,
                file      = outfile,
                sep       = "\t",
                append    = TRUE,
                quote     = FALSE,
                col.names = FALSE,
                row.names = FALSE)
}
```
{{% /codeblock %}}

The below code creates a text file named "test.txt". It saves the matrix "matrix(runif(16), 4, 4)" under the tag name "example". The tableFill function will then look for a tag "example" in the template file to fill the blanks with this matrix.

{{% codeblock %}}
```R
saveTable("test.txt", "<tab:example>", matrix(runif(16), 4, 4))
}
```
{{% /codeblock %}}

### Step 3 : Run the tableFill function in the Command Line (Windows) / Shell (Mac)
In the last step, you run the tableFill function in the Command Line or Shell as seen below. What the below code does is that it fills the "template.md" file with "test.txt" and saves the output file under the name "filled.tex".

{{% codeblock %}}
```Shell
tablefill -i test.txt -o filled.tex template.md
}
```
{{% /codeblock %}}



### Example repository

If you want to check out more about tableFill and see a basic example on how to use it, you can check out the GitHub repository below :

{{% cta-primary-center "Go to the GitHub Repository now" "https://github.com/tilburgsciencehub/tableFill.git" %}}

The structure of the repository is as follows :
```text
tableFill Repository
│
├── template.md ........ includes a markdown document template
├── saveTable.R ........ includes a function to save the results in a text file in R
├── test.txt  ........ saves the results from the saveTable.R file in the txt format
```
{{% warning %}}
Make sure that you do not overwrite the txt file that you save your results (e.g., "test.txt" in the tableFill repository)
{{% /warning %}}


## Additional Resources  
1. https://mcaceresb.github.io/tablefill/index.html
2. https://github.com/mcaceresb/tablefill
