---
title: "Visualizing data with Plotnine and Altair"
description: "Plotting in Python - comparison between plotnine and altair"
keywords: "data, visualization, python, plotting, plotnine, altair"
date: 2023-07-25
weight: 3
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /visualize/data
  - /python/plotting
---

# Plotnine

An additional plotting library in Python is `plotnine`, which is an equivalent to the R package `ggplot2`. It has a similar syntax and uses a concept of grammar of graphics. This means that the plots are built incrementally, layer by layer. 

### Installation 

To install `plotnine` we can either use `pip` or `conda`: 

{{% codeblock %}}
```python
pip install plotnine

# to include extra packages

pip install 'plotnine[all]'
```
{{% /codeblock %}}

{{% codeblock %}}
```python
conda install -c conda-forge plotnine
```
{{% /codeblock %}}

### Syntax

The base syntax of `plotnine` is:


```
ggplot(data = <DATA>) +         #to create the background layer containing the dataset as input
  <GEOM_FUNCTION>(              #main layer to build a chart type
     mapping = aes(<MAPPINGS>),
     stat = <STAT>, 
     position = <POSITION>
  ) +
  <COORDINATE_FUNCTION> +       #layer for axes, titles, etc
  <LABS>(
     title = <TITLE>,
     subtitle = <SUBTITLE>,
     caption = <CAPTION>
  )+
  <FACET_FUNCTION>              #optional layer
```

### Plotting

We illustrate how to visualize data with `plotnine` by using the same examples as in [Matplotlib vs Seaborn](https://tilburgsciencehub.com/building-blocks/visualize-your-data/data-visualization/matplotlib-seaborn). Let's import the library and recreate the Iris scatterplot.

{{% codeblock %}}
```python
from plotnine import *

(ggplot(iris, aes("sepal width", "sepal length", color = "species"))
 + geom_point()
 + coord_cartesian()
 + labs(title = "Scatterplot", x = Sepal Width, y = Sepal Length)
 + theme_bw())

```
{{% /codeblock %}}


To create a bar plot, we just change the `geom function` from `geom_point()` to `geom_bar()`. We use the monthly stocks dataset.


{{% codeblock %}}
```python
(ggplot(data = stocks)+
    geom_bar(aes(x = "Date",
                 y = "GOOG"),
            stat = "identity")+
    labs(title = "Bar plot of GOOG closing price")+
    xlab("Date")+
    ylab("Closing price")+
    theme_bw())
```
{{% /codeblock %}}

To create a line chart we change the same function to `geom_line()`.


We can also create a box plot using the function `geom_boxplot()` or a histogram `geom_histogram()`.

# Altair

`Vega-Altair` is a declarative visualization library, built on `Vega` and `Vega Lite`.

### Installation

We can install `altair` using `pip` or `conda`:

{{% codeblock %}}
```python
pip install altair
```
{{% /codeblock %}}

{{% codeblock %}}
```python
conda install -c conda-forge altair 
```
{{% /codeblock %}}

### Syntax

The basic template for plotting with `altair` is:

```
alt.Chart(data).mark_markname().encode( 

       encoding1 = "column1", 

       encoding2 = "column2")
```

We identify 3 basic elements: 
- *data*: the input dataset used to make the plot
- *mark*: specifies the type of graphical representation (bar, point, line, etc)
- *encoding*: the visual properties of the chart (axes values, position channels, color, etc)


### Plotting

We illustrate how to visualize data with `altair` by using the same dataset used for the `plotnine` example (Iris). This time we import it from the `vega_datasets` library.

{{% codeblock %}}
```python
pip install altair vega_datasets 
```
{{% /codeblock %}}

{{% codeblock %}}
```python
from vega_datasets import data
df = data.iris()
df.head(15) # first glimpse of the dataset
```
{{% /codeblock %}}

To create a scatterplot change the `mark_markname()` function to `mark_circle()`.

{{% codeblock %}}
```python
alt.Chart(df).mark_circle().encode(
    x = "sepalWidth",
    y = "sepalLength"
)
```
{{% /codeblock %}}

To add a different colour for every unique species add the argument `color` to `encode()`. In addition, the argument `size` allows us to change the size of each data point conditional on the length of the petals.

{{% codeblock %}}
```python
alt.Chart(df).mark_bar().encode(
    x = "sepalWidth",
    y = "sepalLength",
    color = "species",
    size = "petalLength"
)
```
{{% /codeblock %}}

If you want to create a bar plot change the `mark_circle()` function to `mark_bar()`.

{{% codeblock %}}
```python
alt.Chart(df).mark_bar().encode(
    x = "sepalWidth",
    y = "sepalLength",
    color = "species"
)
```
{{% /codeblock %}}




