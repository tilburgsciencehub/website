---
title: "Understanding the language of ggplot2 in R"
description: "Building block that assists users in understanding the core concepts of ggplot2. Explains the inner workings, enabling readers to improve their visualisations."
keywords: "ggplot2, Grammar of Graphics, Layering, Data Visualization"
date: 11-12-23
weight: 2
author: "Matthijs ten Tije"
authorlink: "A link to your personal webpage"
aliases:
  - /ggplot2
  - /Grammar/of/Graphics
  - /Layering
  - /Data/Visualization
---

## Overview
In this building block, we will explore `ggplot2`, a powerful package for creating data visualisations in R. We'll begin by comparing ggplot2 to constructing sentences, where graphical elements are like words and punctuation, guided by the `Grammar of Graphics` concept. We'll emphasize the core philosophy of ggplot2, viewing a plot as a combination of independent layers.

I'll provide practical examples to illustrate these concepts, starting with creating a basic plot and gradually introducing colour, size, layering geoms, refining aesthetics, incorporating facets for multi-dimensional analysis, and adding labels and annotations.

By the end of this building block, you'll have a solid understanding of ggplot2's modularity, layering, and best practices, empowering you to craft compelling data visualizations and stories.

## Grammar of Graphics
Creating a graph in R using ggplot2 can be thought of as building a sentence. Just as words form clear sentences, ggplot2 combines graphical elements guided by the `Grammar of Graphics`. Like using basic parts of speech to build sentences, ggplot2 employs points, lines, and colors as fundamental components for flexible and meaningful data visualization.  

The term 'gg' in ggplot2 stands for 'Grammar of Graphics', reflecting its core philosophy. It views a plot as a combination of independent layers that, when put together, tell a visual story. Each layer in ggplot2 adds something new, just like every word adds meaning to a sentence. By layering these elements, you can create elaborate and detailed visualizations, turning data into insightful and easy-to-understand stories.

## Key Aspects of ggplot2

**Modularity and Layering** 

At its core, ggplot2 embraces `modularity`. Plots are constructed through a series of layers, each appended with the `+ operator`. While initially, this approach may seem less intuitive than generating a plot with a single function call, it's precisely this layer-by-layer construction that grants ggplot2 its versatility. This methodology enables you to build a wide range of plots, from simple bar charts to complex multi-layered visualizations.

*Another analogy*: Imagine you're painting a picture; you start with a sketch (your dataset) and then add layers of paint (aesthetics and geoms). Each stroke of the brush (layer) enriches your painting (plot), making it more detailed and colorful. This is the essence of ggplot2's layering - you build plots layer by layer, each adding new dimensions to your data story.

## Basic Ingredients of a ggplot:
1. The `ggplot()` function  
   
Every visualization with the ggplot2 package starts with the `ggplot()` function, where you specify the dataset and set up aesthetics (aes) that map data variables to visual properties. These mappings variables define how data variables are represented in terms of visual properties such as axes, colors, shapes, and sizes.

{{% codeblock %}}

```R
# install package ggplot2
install.packages("ggplot2")
library(ggplot2)

# Creating the stage
ggplot(data = mpg, aes(x = displ, y = hwy)) 
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotfunction.png" width="450">
</p>

{{% example %}}

This code initializes a ggplot object for a  plot, using the `mpg` dataset with engine displacement (displ) and highway miles per gallon (hwy). In our analogy to constructing sentences, we've set the stage, but the plot remains empty, much like a sentence without verbs or adjectives. To bring it to life, we need to call upon a geom() function to specify the type of plot we want to create.

{{% /example %}}

2. Geometric Objects (Geoms): 

The next step involves adding one or more geometric objects, or 'geoms'. Geoms determine the type of plot you're creating. Whether it's a bar plot (`geom_bar`), a line plot (`geom_line`), a scatter plot (`geom_point`), or any other graphical representation, each geom layer takes the foundational setup from the ggplot call and visually interprets the data according to its type.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy)) +
    geom_point() # Adds a scatter plot layer
    geom_bar() # Adds a bar plot layer
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/scatterplot.png" width="250">
</p>

<p align = "center">
<img src = "../img/barplotggplot.png" width="250">
</p>

{{% tip %}}
**Data Visualization Best Practices**

In this [building block](/visualize/data), we go through the theory of data visualisation, describe the most common chart types and conclude with best practices for plotting.

{{% /tip %}}

## Understanding Aesthetic Layering in ggplot2
In ggplot2, layering aesthetics, like color and fill, is crucial for creating a detailed and visually appealing visualization. However, to make the most of this capability, it's essential to grasp two fundamental aspects of the ggplot2 language:

**Aesthetic Inheritance**: In ggplot2, aesthetics applied in the `ggplot()` fucntion initially flow through all layers, ensuring consistency, but be cautious to avoid unintended changes in later layers. 

**Overwriting Aesthetics**: Adding new layers to your plot introduces the potential for overwriting the aesthetic settings of previous layers. Therefore, be mindful of how each layer affects the overall aesthetics of the visualization to achieve your intended design.

### Aesthetic Inheritance in Layering:
Aesthetics defined in the initial `ggplot()` function serve as a base layer and are inherited by subsequent layers. This feature enables a consistent application of aesthetics like color or fill across the entire plot unless specifically overridden in subsequent layers. For instance:

{{% codeblock %}}
```R
ggplot(data = mpg, aes(x = displ, y = hwy)) +
    geom_point() +
    geom_smooth(aes(color = class))  # Only affects geom_smooth layer
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/gginheritance.png" width="450">
</p>

{{% example %}}

Here, the color aesthetic applied to the geom_smooth layer does not affect the geom_point layer, illustrating how layer-specific aesthetic settings can override the base layer settings.

{{% /example %}}

### Overwriting Aesthetics with New Layers:
In ggplot2, aesthetics set in the ggplot() function serve as global settings for the entire plot, while aesthetics set in a `geom_()` function apply only to that specific layer. This can lead to unexpected results if not handled carefully.

Therefore, when adding new layers, be cautious as they can overwrite the aesthetic settings from earlier layers. This is particularly relevant when you’re incrementally building a plot and want to maintain certain aesthetic features throughout. For example:


{{% codeblock %}}

```R
ggplot(mpg, aes(x = displ, y = hwy, color = class)) +
  geom_point(aes(color = "red"), size = 3)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggoverwriting.png" width="450">
</p>

{{% example %}}

In this example, the first `geom_point() ` layer uses the global aesthetic defined in ggplot(), coloring points by the class variable. However, when the second geom_point() layer is added with color = "red", it overwrites the color for all points, making them red, regardless of their class.

{{% /example %}}

This demonstrates the pitfall: Even though the color was set globally to map to class, specifying a different color in the geom_point() layer overwrites this setting. It's a common mistake to expect the global aesthetic to persist through all layers, but each layer's aesthetics are independent unless specified otherwise.

### Best Practices for Layering Aesthetics
To effectively use layering in ggplot2:
- *Be Consistent*: Maintain a consistent theme across layers for a cohesive story.
- *Plan Your Layers*: Think ahead about how each layer contributes to your plot.
- *Simplify*: Avoid overcomplicating your plot. Sometimes, less is more.
- *Use Comments*: Annotate your code with comments for better understanding and readability.
- *Visualize Progress*: Check the output of your plot as you add layers.

## Practical Example
Every ggplot2 visualization starts with a foundational layer. This initial step involves defining the dataset and basic aesthetics.

#### Example 1: Creating a Basic Plot

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy)) + 
  geom_point()
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample1.png" width="450">
</p>

*Description*: Starting with a basic scatter plot using the 'mpg' dataset. This foundational plot maps engine displacement (displ) to the x-axis and highway miles per gallon (hwy) to the y-axis. It's a simple yet effective way to visualize the relationship between these two variables.

#### Example 2: Introducing Color and Size
Adding color and size to a plot can significantly enhance its interpretability and appeal.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy, color = manufacturer, size = cyl)) + 
  geom_point()
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample2.png" width="450">
</p>

*Insight*: By introducing color and size, we differentiate data points by manufacturer and cylinder count. This addition turns a simple scatter plot into a more detailed and informative visualization, highlighting multiple variables at once.

#### Example 3: Layering Geoms
Different geometrical shapes, or 'geoms', can be layered to present data in various formats, such as lines, bars, or points.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy)) + 
  geom_point() + 
  geom_smooth()
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample3.png" width="450">
</p>

*Analysis*: Adding a smooth line (geom_smooth) to our scatter plot provides an overview of the general trend. This layer helps in visualizing the relationship between displacement and highway MPG across different vehicle segments.


#### Example 4: Refining Aesthetics, Adjusting Scales and Themes
Fine-tuning scales and applying themes can transform the appearance and readability of a plot.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy, color = manufacturer, size = cyl)) + 
    geom_point() + 
    scale_color_brewer(type = "qual") +
    theme_minimal()
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample4.png" width="450">
</p>

*Explanation*: By applying `scale_color_brewer(type = "qual")`, we introduce a qualitative color palette from the Color Brewer tool, which is particularly effective for distinguishing categories (in this case, different manufacturers).   
The `theme_minimal()` function is then used to apply a minimalistic theme to the plot. This theme reduces visual clutter, emphasizing the data points and making the plot cleaner and more readable. 

Overall, these refinements enhance both the aesthetic appeal and interpretability of the plot, making it more engaging and informative for the viewer.

#### Example 5: Incorporating Facets for Multi-Dimensional Analysis
Faceting allows for the creation of multiple, related plots grid-like based on the data's dimensions.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy, color = manufacturer)) + 
    geom_point() + 
    facet_wrap(~class)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample5.png" width="450">
</p>

*Context*: Faceting based on vehicle class creates a grid of plots, each focusing on a different class. This approach allows for a more granular analysis, enabling comparisons across different vehicle categories.

#### Example 6: Final Touches, Adding Labels and Annotations
Labels and annotations bring clarity and context to a plot, making it more informative and reader-friendly.

{{% codeblock %}}

```R
ggplot(data = mpg, aes(x = displ, y = hwy, color = manufacturer)) + 
    geom_point() + 
    labs(title = "Engine Displacement vs. Highway MPG",
         x = "Engine Displacement (L)",
         y = "Highway Miles per Gallon",
         color = "Manufacturer") +
    theme_minimal()
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggplotexample6.png" width="450">
</p>

*Detailing*: The final step involves adding informative labels and annotations. A clear title, axis labels, and a legend make the plot self-explanatory. These finishing touches ensure the plot communicates effectively with its audience.

{{% summary %}}

Wrapping up our exploration of ggplot2, let's reflect on the fundamental concepts learned:

- **Modularity and Layering**: The `modularity` of ggplot2 enables the creation of a wide range of plots through layering, from simple bar charts to intricate multi-layered visualizations.
- **Aesthetic Layering**: We've delved into the nuances of `aesthetic inheritance` and the potential for overwriting aesthetics, vital for creating detailed and visually appealing visualizations.
- **Best Practices**: We've discussed best practices for effective layering, emphasizing consistency, planning, simplicity, commenting, and visualizing progress.
- **Practical Examples**: Through practical examples, we've seen how to create basic plots, introduce color and size, layer geoms, refine aesthetics, incorporate facets, and add labels and annotations.

By grasping these concepts, you are well-equipped to leverage ggplot2's power and flexibility for crafting compelling data visualizations and stories.

{{% /summary %}}

