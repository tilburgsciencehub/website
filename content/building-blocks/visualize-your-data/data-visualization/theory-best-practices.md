---
title: "Data Visualization Theory and Best Practices"
description: "An introduction to data visualization: data encoding, marks and channels, chart types, elements of a chart, best practices to visualization"
keywords: "data, visualization, introduction, theory, encoding, chart, types, elements, marks, channels"
date: 2023-07-18
weight: 1
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /visualize/data
  - /data/encoding
  - /choose/chart
  - /best/practices
---

## Introduction and Learning Goals

The process of analyzing data does not stop after obtaining the requested statistics. Simply having some numbers or datasets could not transmit much information, but mapping them into charts and figures can help tell a story. Data visualization facilitates making comparisons, following trends and distributions or identifying outliers. It can also speed up the decision making process, as it makes it easier for the reader to comprehend the information, especially if it is a vast amount of complicated data. 

In this building block we go through the theory of data visualization, describe the most common chart types and conclude with best practices for plotting.

## Theory of Data Visualization

### Data Encoding

Data visualization makes use of **marks** (geometric primitives) and **channels** (appearance of marks) to create a chart. Marks can consist of:
- points
- lines
- areas
- any other complex shapes

Channels are ways in which we present the marks and consist of:
- position (horizontal, vertical)
- color (hue, saturation, luminance)
- size (length, area, volume)
- shape (orientation/tilt, curvature)

Several aspects should be considered when constructing a data visualization:

1. What is the data and how is it structured
2. Who is the user/reader
3. What should the user be able to do - exploration/confirmation/communication of data
4. What are the actions and targets
5. How to map between data items and visual elements

### Chart Elements

The chart below contains all necessary elements for a proper visualization.

<p align = "center">
<img src = "../../img/chart_elements.png" width=450">
</p>

First of all, a chart needs to have a **coordinate system** , **axes** and **scaling** of data. In the above example there are two coordinates, the X and Y axes representing months on the horizontal axis and financial indicators on the primary vertical axis. Additionally, it has a secondary vertical axis showing the ROI. 

A complete chart also has a **legend** for providing mapping information, **axes titles**, a **chart title**, **data labels** and **gridlines** for better readability of the data.

### Chart Types


There is a vast range of chart types that could be used to visualize data, however in this building block we describe 7 of the most common ones, as they cover most of the visualization goals.

#### 1. Scatterplot

The scatterplot can represent data with 2 quantitative attributes in horizontal and vertical channel positions. The used marks are points and the purposes of a scatterplot are to find trends or outliers, visualize a distribution or correlations, or identify clusters. 

<p align = "center">
<img src = "../../img/scatterplot.png" width=350">
</p>

#### 2. Bar plot

The bar plot can visualize one categorical and one quantitative attribute. It uses bars (thick lines) as marks and the used channels are length (to express quantitative value) and spatial regions (one per mark). These can be separated horizontally and aligned vertically (or the other way around) and are ordered by attribute values (either by label/alphabetical or by attribute length). The task of the bar chart is to compare or lookup values. 

<p align = "center">
<img src = "../../img/bar_chart.png" width=450">
</p>

#### 3. Stacked bar chart

The stacked bar chart can visualize two categorical attributes and one quantitative attribute. As a mark it uses a vertical stack of line marks. For the channels the stacked bar chart uses length and color hue, as well as spatial regions to represent data. Its task is again to compare and lookup values, and additionally, it can inspect part-to-whole relationships. 

<p align = "center">
<img src = "../../img/stacked_bar.png" width=350">
</p>

#### 4. Line chart

The line chart represents 2 quantitative attributes and uses points with line connections between them as marks. The channels are aligned lengths to express quantitative value and are separated and ordered by attributes into horizontal regions. The task of the line chart is to find trends. 

<p align = "center">
<img src = "../../img/line_chart.png" width=400">
</p>

#### 5. Heatmap

The heatmap can visualize 2 categorical attributes, usually in order, and one quantitative attribute. It uses areas as marks in the shape of a matrix indexed by the 2 categorical attributes. The channel is color hue ordered by the quantitative attribute. The purpose of the heatmap is to find clusters and outliers.

<p align = "center">
<img src = "../../img/heatmap.png" width=400">
</p>

#### 6. Histogram

The histogram is used to find the distribution or shape inside some data. It visualizes the frequency of an attribute from a table by using bins and counts. The bins are intervals in which the range of values is divided into, and counts are the frequencies of the values inside each interval. 

<p align = "center">
<img src = "../../img/histogram.png" width=350">
</p>

#### 7. Box plot

The box plot is also used to find the distribution of the data. It maps the attributes by calculating 5 quantitative values: 
- median: central value/line
- lower and upper quartile: boxes
- lower and upper limits: whiskers

Any values outside the limits are considered outliers. 

<p align = "center">
<img src = "../../img/box_plot.png" width=350">
</p>

## Best Practices

{{% tip %}}

1. Design the charts for color deficiency - the safest color combination is blue-orange
2. Use position for the most important aspects to visualize and color for categories
3. Limit the amount and detail of data in a visualization
4. Default formats are easier to read
5. Consider the reader's context - representation formats for different devices/printing and directional orientation for reading
6. Always include descriptive titles, axes labels and units (if applicable), legends and captions
7. Choose appropriate ranges for the axes and appropriate font sizes

{{% /tip %}}
