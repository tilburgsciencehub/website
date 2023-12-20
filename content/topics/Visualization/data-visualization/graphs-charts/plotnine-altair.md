---
title: "Visualizing data with Plotnine and Altair"
description: "Plotting in Python - comparison between plotnine and altair"
keywords: "data, visualization, python, plotting, plotnine, altair"
date: 2023-07-25
weight: 2
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /visualize/data
  - /python/plotting
---
## Overview

This building block is an introduction to `Plotnine` and `Altair`, two libraries used for data visualisation in Python. For each library, we provide a guide covering:
 * Installation 
 * Syntax
 * Plotting


## Plotnine

`Plotnine` uses a syntax that is similar to that of the R package `ggplot2` and is built on the principles of **grammar of graphics**. In this approach, plots are constructed incrementally, layer by layer.

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
ggplot(data = <DATA>) +         # to create the background layer containing the dataset as input
  <GEOM_FUNCTION>(              # main layer to build a chart type
     mapping = aes(<MAPPINGS>),
     stat = <STAT>, 
     position = <POSITION>
  ) +
  <COORDINATE_FUNCTION> +       # layer for axes, titles, etc
  <LABS>(
     title = <TITLE>,
     subtitle = <SUBTITLE>,
     caption = <CAPTION>
  )+
  <FACET_FUNCTION>              # optional layer
```

### Plotting

We illustrate how to visualize data with `plotnine` by using the Iris dataset from `sklearn`:

{{% codeblock %}}
```python
# Importing needed packages and dataset
import pandas as pd
import sklearn
from sklearn import datasets
import plotnine
from plotnine import *

iris = datasets.load_iris()

# Transforming Iris into a data frame
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
```
{{% /codeblock %}}

{{% codeblock %}}
```python
(ggplot(iris_df, aes(x = "sepal width (cm)", y = "sepal length (cm)"))
  + geom_point()
  + coord_cartesian()
  + labs(title = "Scatterplot", x = "Sepal Width", y = "Sepal Length")
  + theme_bw())

```
{{% /codeblock %}}

<div style="text-align: center;">
    <div style="position: relative; left: -20px;">
        <img src="../images/plotnine.png" width="500" alt="Forest Plot">
    </div>
</div>


Alternative geometric functions are `geom_bar()`, `geom_line()`, `geom_boxplot()`, and `geom_histogram()`.

## Altair

`Vega-Altair` is a declarative visualization library, built on `Vega-Lite` visualisation grammar, which allows for easy interactivity and customisation.

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

The basic syntax for plotting with `altair` is:

```
alt.Chart(data).mark_markname().encode(
       encoding1 = "column1",
       encoding2 = "column2")
```

We identify 3 basic elements: 
- *data*: input dataset used to make the plot
- *mark*: to specify the type of graphical representation (bar, point, line, etc..)
- *encoding*: visual properties of the chart (axes values, position channels, color, etc..)


### Plotting

We illustrate how to visualize data with `altair` by using the same dataset used for the `plotnine` example (Iris). However, this time, we import it from the `vega_datasets` library.

{{% codeblock %}}
```python
pip install altair vega_datasets 
```
{{% /codeblock %}}

{{% codeblock %}}
```python
import altair as alt
from vega_datasets import data
iris_df = data.iris()

```
{{% /codeblock %}}

To create a scatterplot change the `mark` argument to `mark_circle()`.

{{% codeblock %}}
```python
alt.Chart(iris_df).mark_circle().encode(
    x = "sepalWidth",
    y = "sepalLength"
)
```
{{% /codeblock %}}


<div style="text-align: center;">
    <div style="position: relative; left: -50px;">
        <img src="../images/altair1.png" width="400" alt="Forest Plot">
    </div>
</div>


To add a different colour for every unique species add the argument `color` to `encode()`. In addition, the argument `size` allows to change the size of each data point conditional on the length of the petals.

{{% codeblock %}}
```python
alt.Chart(iris_df).mark_circle().encode(
    x = alt.X("sepalWidth", axis = alt.Axis(title="Sepal Width")),
    y = alt.Y("sepalLength", axis = alt.Axis(title="Sepal Length")),
    color="species",
    size="petalLength"
)
```
{{% /codeblock %}}

<div style="text-align: center;">
    <img src="../images/altair2.png" width="500" alt="Forest Plot">
</div>

To create a different type of plot, you can change `mark_circle()` to `mark_bar()`, `mark_point()`, or `mark_line()`. 


{{% summary %}}
How to efficiently visualise your data with `plotnine` and `altair`:

1. Identify **variables** of interest within your dataset;

2. Select ideal **type of plot** (e.g., scattarplot, bar plot) according to chosen variables;

3. **Install** relevant packages; 

4. Starting from the basic syntax of each package, **generate insights** on your data and efficiently **communicate** them to others.

{{% /summary %}}