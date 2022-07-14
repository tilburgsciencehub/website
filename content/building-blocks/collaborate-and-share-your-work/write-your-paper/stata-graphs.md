---
title: "Stata Graphs Made Easy"
description: "Learn how to quickly and efficiently prepare graphs in Stata."
keywords: "stata, graphs, data visualization"
weight: 104
date: 2022-06-20T22:02:51+05:30
draft: false
aliases:
  - /export/graphs
  - /use/stata
---

## Overview

Stata has a user-friendly interface especially for people using big data. It is quite easy to browse through the datasets in comparison to R.

The most easy way to use Stata graphs is the command `twoway`. Following this command you first state the type of the graph you want to create (e.g., line, scatter), and then the variables you want to create graph for. Let’s go through an example.

{{% tip %}}

- `auto.dta` is an example dataset created and provided by Stata itself. You can download it on your Stata by using the command `'sysuse "auto.dta"'`. Go this [link](https://www.stata.com/manuals13/gsw1.pdf) for more information about sample datasets in Stata!

{{% /tip %}}


## An Example


{{% codeblock %}}
```
-Stata-

* Load the dataset
sysuse "auto.dta", clear

* Create a two-way graph for weight length
twoway line price mpg  // line plot
twoway scatter price mpg  // scatter plot
twoway area price mpg   // area plot
twoway bar price mpg   // bar plot
twoway spike price mpg  // spike plot
```
{{% /codeblock %}}

You can also add titles to x-axis, y-axis and so on as well as change the color scheme of your graphs.

{{% codeblock %}}
```
-Stata-
* Add y-axis title, x-axis title and graph title
twoway line price mpg, ytitle("Price") xtitle("Mileage")

* Change the color and style of the line  
twoway line price mpg, ytitle("Price") xtitle("Mileage") lcolor(red) lpattern(dash_dot)

* Make use of the styles provided by Stata
set scheme s1color // this command sets the scheme s1color
twoway line price mpg
*
set scheme Economist // this command sets the scheme s1color
twoway line price mpg
```
{{% /codeblock %}}

{{% tip %}}

- There are many style schemes provided by Stata. Check this [link](https://people.umass.edu/biostat690c/pdf/stata%20schemes%20and%20palettes.pdf) to explore the style schemes further!  

{{% /tip %}}

You can also graph your variables based on different groupings or conditions!

{{% codeblock %}}
```
-Stata-
* Creating different lines for different groups
tab foreign // foreign variable equals to 1 if the observation is foreing, zero otherwise

// Let's create two lines for Domestic and Foreign cars
set scheme s1color // this command sets the scheme s1color
twoway (line price mpg if foreign == 0) (line price mpg if foreign == 1)

// Let's add a legend stating the different groups
cap drop Origin
gen Origin = 1 if foreign == 0 // domestic cars
replace Origin = 2 if foreign == 1 // foreign cars
tab Origin
*
twoway (line price mpg if Origin == 1) (line price mpg if Origin == 2), legend(label(1 Domestic) label(2 Foreign))

// Let's change the style of the lines with lcolor and lpattern options
twoway (line price mpg if Origin == 1, lcolor(blue) lpatter(dash)) (line price mpg if Origin == 2, lcolor(black) lpatter(solid)), legend(label(1 Domestic) label(2 Foreign))

// Preferably, you can also change the size of the legend
twoway (line price mpg if Origin == 1, lcolor(blue) lpatter(dash)) (line price mpg if Origin == 2, lcolor(black) lpatter(solid)), legend(size(small) label(1 Domestic) label(2 Foreign))

* Can also change the range of the axis
twoway (line price mpg if Origin == 1, lcolor(blue) lpatter(dash)) (line price mpg if Origin == 2, lcolor(black) lpatter(solid)), legend(size(small) label(1 Domestic) label(2 Foreign)) xlab(0(5)50) ylabel(5000(3000)15000)

```
{{% /codeblock %}}

{{% example %}}
Such an example code would create a graph below based on the `auto` dataset.

![Stata Grouping Graph.](../images/stata_group.png)
{{% /example %}}

{{% summary %}}
Stata can create graphs that can be modified easily such that Stata itself even provides style schemes to be used. You can graph variables based on different groupings very easily!
{{% /summary %}}


## Additional Resources  

1. [Complete manual on Twoway Graphs](https://www.stata.com/manuals/g-2graphtwoway.pdf#g-2graphtwoway)

2. [Style Patterns](https://www.stata.com/manuals13/g-4linepatternstyle.pdf#g-4linepatternstyle)

3. [Easy interactive tutorial on styling](https://www.stata.com/meeting/germany18/slides/germany18_Jann.pdf)
