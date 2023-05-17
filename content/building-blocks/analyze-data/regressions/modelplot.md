---
title: "Generate a coefficient plot in R with the `modelplot` function"
description: "An example on how to use the `modelplot` function to generate nice coefficient plots in R"
keywords: "modelplot, modelsummary, packages, regression, model, plot, R"
draft: false
weight: 7
author: "Valerie Vossen"
authorlink: "https://nl.linkedin.com/in/valerie-vossen"
aliases:
  - /modelplot
  - /run/modelplot/
  - /run/modelplot
author: "Valerie Vossen"
date: "2023-05-16"
output: html_document
---

# Overview 

The `modelplot` function, part of the `modelsummary` package, enables the plotting of model estimates and confidence intervals. In this building block, we will provide you with two examples of coefficients plots to demonstrate the useful functions of `modelplot`. 

We will be using the models from the paper ["Doing well by doing good? Green office buildings"](https://www.aeaweb.org/articles?id=10.1257/aer.100.5.2492) These models regress the logarithm of rent per square foot in commercial office buildings on a dummy variable representing a green rating (1 if rated as green) and other building characteristics. Please refer to the [`modelsummary` building block](https://tilburgsciencehub.com/building-blocks/analyze-data/regressions/model-summary/) for more information about the paper.

We will generate two coefficient plots using the `modelplot` function:
- A single coefficient across multiple models 
- Multiple coefficients within a single model 

## Load packages and data

Let's begin by loading the required packages and data:

{{% codeblock %}}
```R

# Load packages

library(rlang)
library(ggplot2)
library(modelsummary)
library(dplyr)
library(fixest)
library(stringr)
library(extrafont)

# Load data 

data_url <- "https://github.com/tilburgsciencehub/website/blob/buildingblock/modelsummary/content/building-blocks/analyze-data/regressions/data_rent.Rda?raw=true"
load(url(data_url)) #data_rent is loaded now

```
{{% /codeblock %}}

## The `modelsummary` table

Below you see the five regression models for which results are displayed in Table 1 of Eiccholtz et al. (2010). For a detailed overview and understanding of these regressions, please refer to the [`modelsummary` building block](https://tilburgsciencehub.com/building-blocks/analyze-data/regressions/model-summary/).

{{% codeblock %}}
```R
reg1 <- feols(logrent ~ green_rating + size_new + oocc_new + class_a + class_b + net + empl_new| id, data = data_rent)

reg2 <- feols(logrent ~ energystar + leed + size_new + oocc_new + class_a + class_b + net + empl_new| id, data = data_rent)

reg3 <- feols(logrent ~ green_rating + size_new + oocc_new + class_a + class_b + net + empl_new + age_0_10 + age_10_20 + age_20_30 + age_30_40 + renovated | id, data = data_rent)

reg4 <- feols(logrent ~ green_rating + size_new + oocc_new + class_a + class_b + net + empl_new + age_0_10 + age_10_20 + age_20_30 + age_30_40 + renovated + story_medium + story_high + amenities  | id, data = data_rent)
  #regression 1 until 4 include fixed effects for "id"

reg5 <- feols(logrent ~ size_new + oocc_new + class_a + class_b + net + empl_new  + renovated + + age_0_10 + age_10_20 + age_20_30 + age_30_40 + story_medium + story_high + amenities | id + green_rating, data = data_rent)
  #regression 5 includes fixed effects for "id" and "green_rating" variable
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/kableextraimage4.png" width="500">
</p>


## Example 1: A single coefficient across multiple models

In this example, we will create a coefficient plot of the Green rating variable. This plot visualizes the relationship between the presence of a green rating and the rent of the building. The Green rating variable indicates whether a building is rated as green (1 if rated as green and 0 otherwise). 

We will include the regression models 1, 3, and 4 in the models list, as these include the Green rating variable. The order of the models in `models2` will determine the order of the variable rows in the plot. 

We can customize the variable names displayed in the coefficient plot using the `coef_map` argument. In the vector `cm`, we assign a new name to the original term name. Only variables included in `coef_map` will be shown in the plot. 

{{% codeblock %}}
```R
models2 <- list(
  "(4)" = reg4,
  "(3)" = reg3, 
  "(1)" = reg1)

cm = c('green_rating' = 'Green rating (1 = yes)')
modelplot(models = models2, 
          coef_map = cm
          )
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/modelplotimage1.png" width="500">
</p>

### Changing the confidence level

By default, the confidence level is set to 95%. We can change this by specifying the desired level using the `conf_level` argument. 

{{% codeblock %}}
```R
modelplot(models = models2, 
          conf_level = 0.99, 
          coef_map = cm
          )
```
{{% /codeblock %}}

## Further customization of the plot

Further customization of the plot can be done using `ggplot2` functions. In the next code block, the following changes are made:
- Add a theme
- Change the font type to Times New Roman
- Modify the color of the lines
- Adjust the order of the legend 

Within the `scale_color_manual()` functions, we specify the colors of the lines and control the order of the regressions in the legend. To do this, we need to define two vectors: `color_map` for the colors of the lines, and `legend_order` for the order of the regressions in the legend. 

{{% codeblock %}}
```R
color_map <- c("(1)" = "black", "(3)" = "blue", "(4)" = "red")
legend_order <- c("(1)", "(3)", "(4)")

modelplot(models = models2, 
          coef_map = cm
          ) +
  theme_minimal() +
  theme(text = element_text(family = "Times New Roman")) +
  scale_color_manual(values = color_map, 
                     breaks = legend_order
                     )
```
{{% /codeblock %}}

{{% tip %}}
Before specifying Times New Roman as the font type in our plot, we need to import this font into R. You can use the following code to import the font:

```R
library(extrafont)

font_import() 
loadfonts(device = "win")
```

Note that running `font_import()` may take a few minutes to complete. 
{{% /tip %}}


### Changing the labels

We can modify the labels of the plot using the `labs()`
argument. We omit the x-axis label and add a title, subtitle, and caption. Also, the title of the legend is changed by specyfying it as a character string and assigning it to the `color` parameter within `labs()`. 

Furthermore, we can change the position of the text elements within `theme()`. Specifically, we adjust the position of the title and subtitle to be centered by setting `hjust = 0.5`. Similarly, the caption is placed on the left side by setting `hjust = 0`. 

{{% codeblock %}}
```R
modelplot(models = models2, 
          coef_map = cm
          ) + 
  theme_minimal() +
  theme(text = element_text(family = "Times New Roman")) +
  scale_color_manual(values = color_map, 
                     breaks = legend_order
                    ) +
  labs(x= "", 
       title = "Coefficient 'Green rating' with 95% confidence intervals",
       subtitle = "Dependent variable is log(rent)",
       caption = "source: Doing well by doing good?: Green office buildings by Eiccholtz et al. (2010)",
       color = "Regression models"
       ) + 
  theme(plot.title = element_text(hjust = 0.5), 
        plot.subtitle = element_text(hjust = 0.5),
        plot.caption = element_text(hjust = 0)
        )

```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/modelplotimage2.png" width="500">
</p>

This plot visualises the relationship between the presence of a green rating and the rent of the building. For the different regression models, the magnitude and the statistical significance of the green rating is unchanged. Thus, the plot reveals that the rent in a green-rated building is significantly higher by 2.8 to 3.5 percent compared to building without a green rating. 

## Example 2: Multiple Coefficients within a single model
In this example, we will create a coefficient plot to showcase the coefficients of the Age variables in regression 3. This plot allows us to understand the individual effects of different age variables on the outcome variable.

Note that when including more variables in the plot, the `coef_map` argument is also useful for rearranging the order of the coefficients. 

{{% codeblock %}}
```R
cm2 = c('age_30_40' = '30-40 years',
        'age_20_30' = '20-30 years',
        'age_10_20' = '10-20 years',
        'age_0_10' = '<10 years')

modelplot(models = reg3, 
          coef_map = cm2
          )
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/modelplotimage3.png" width="500">
</p>

### Further customizations

Similar to the first example, we can customize the plot further with `ggplot` functions. We add a theme, change the font type and adjust the labels and captions.

{{% codeblock %}}
```R
modelplot(models = reg3, 
          coef_map = cm2
          ) + 
  theme_minimal() +
  theme(text = element_text(family = "Times New Roman")) +
  labs(x= "", 
       title = "Coefficients in Age category of regression (3)",
       subtitle = "Dependent variable is log(rent)",
       caption = "source: Doing well by doing good?: Green office buildings by Eiccholtz et al. (2010)"
       ) + 
  theme(plot.title = element_text(hjust = 0.5), 
        plot.subtitle = element_text(hjust = 0.5),
        plot.caption = element_text(hjust = 0)
        )
```
{{% /codeblock %}}

<p align = "center">
<img src = "../images/modelplotimage4.png" width="500">
</p>

This plot clearly demonstrates that newer buildings command a significant premium compared to older ones, indicating a positive relationship between building age and rent in these models.

{{% summary %}}
The `modelplot` function from the `modelsummary` package offers a useful tool for creating clear and informative coefficients plots in R. In this building block, two examples are provided. The first example demonstrates how to visualize a single coefficient across multiple models. The second example showcases how to visualize multiple coefficients within a single model.  
{{% /summary %}}
