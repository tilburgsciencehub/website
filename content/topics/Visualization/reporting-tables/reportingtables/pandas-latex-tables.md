---
title: "Converting Pandas DataFrames to LaTeX and Markdown Tables"
description: "Explore how to transform Python DataFrames into beautifully formatted LaTeX and Markdown tables for academic and web-based documentation"
keywords: "Python, Pandas, DataFrames, LaTeX Tables, Markdown Tables, Data Science, Documentation, Reporting, Formatting"
weight: 3
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2024-01-28
aliases:

/python_dataframe/latex_markdown_conversion
---

## Overview

This short building block provides a guide on converting Python DataFrames into LaTeX and Markdown tables. This skill is particularly useful when preparing data for academic publications or web-based documentation, such as GitHub repositories or other collaborative coding platforms. 

By the end of this block, you'll be able to seamlessly convert your DataFrame results, into well-formatted tables for different platforms.

## Converting DataFrame to LaTeX Table

LaTeX is widely used in academic and scientific documentation for its excellent handling of mathematical and technical typesetting. In Python, converting a DataFrame to a LaTeX table can be achieved using Pandas’ built-in `to_latex()` method.

__Example: ML Models Comparison__

Suppose we have a DataFrame df_models comparing various machine learning models:

{{% codeblock %}}
```python

import pandas as pd

data = {
    "Model": ["Random Forest", "SVM", "MLP"],
    "Accuracy": [0.85, 0.80, 0.90],
    "Precision": [0.88, 0.83, 0.91],
    "Recall": [0.84, 0.79, 0.88]
}
df_models = pd.DataFrame(data)
df_models
```
{{% /codeblock %}}

To convert this into a well-formatted LaTeX table:

{{% codeblock %}}
```python

latex_table = df_models.to_latex(
    index=False,  # To not include the DataFrame index as a column in the table
    caption="Comparison of ML Model Performance Metrics",  # The caption to appear above the table in the LaTeX document
    label="tab:model_comparison",  # A label used for referencing the table within the LaTeX document
    position="htbp",  # The preferred positions where the table should be placed in the document ('here', 'top', 'bottom', 'page')
    column_format="|l|l|l|l|",  # The format of the columns: left-aligned with vertical lines between them
    escape=False,  # Disable escaping LaTeX special characters in the DataFrame
    float_format="{:0.2f}".format  # Formats floats to two decimal places
)

print(latex_table)
```
{{% /codeblock %}}

This code will output a LaTeX formatted table, which you can directly include in your LaTeX documents. For our example, the LaTeX file would look like in the image below:

<p align = "center">
<img src = "../images/latex-tab.png" width="400" style="border:1px solid black;">
<figcaption> Python-generated LaTeX table</figcaption>
</p>

{{% warning %}}

The `to_latex()` method, despite being an easy and fast approach to convert your pandas dataframes into LaTeX tables, it is still quite limited for customization purposes. Hence, you may need to tweak further the generated table. For instance, you might add a '\centering' line in the LaTeX file to center the table. 

{{% /warning %}}

## Converting DataFrame to Markdown Table

Markdown tables are essential for documentation on various platforms like GitHub, Bitbucket, or Jupyter Notebooks. For a straightforward conversion of DataFrames to Markdown format, Pandas provides the `to_markdown()` method.

__Example: Using the Same DataFrame__

Continuing with the df_models DataFrame, here's how you can convert it to a Markdown table:

{{% codeblock %}}
```python

markdown_table = df_models.to_markdown(index=False)
print(markdown_table)

```
{{% /codeblock %}}

This method will print a basic Markdown table. If we copy and paste it into a .md file, when rendering it, it will look quite nice, as observed below:

<p align = "center">
<img src = "../images/md-tab.png" width="400" style="border:1px solid black;">
<figcaption> Python-generated markdown table</figcaption>
</p>

{{% warning %}}

While `to_markdown()` offers a quick and easy way to convert DataFrames to Markdown, it is somewhat limited in terms of customization and formatting. For more complex table formatting in Markdown, you might consider using the `tabulate` library, which offers a wider range of formatting options and styles.

{{% /warning %}}


{{% summary %}}
Converting Python DataFrames to LaTeX and Markdown tables is a straightforward process that greatly enhances the presentation of your data analysis results. Whether you are preparing a scientific paper or documenting your project on a website, these skills are useful for a clear and professional presentation of data.
{{% /summary %}}

## Additional Resources

- Pandas Documentation: Pandas DataFrame [to_latex](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html) and [to_markdown](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas.DataFrame.to_markdown)
- Overleaf LaTeX [Documentation](https://www.overleaf.com/learn)
- Tabulate [Documentation](https://pypi.org/project/tabulate/)
