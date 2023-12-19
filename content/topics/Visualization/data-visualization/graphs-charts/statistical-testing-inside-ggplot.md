---
title: "Combining Analysis and Visualization in R with ggpubr and rstatix"
description: "This building block blends ggpubr's visualization tools with rstatix's statistical analysis in R. It's designed for researchers and data scientists who seek to elevate their data stories with visually engaging and statistically sound plots."
keywords: "ggplot2, bar chart, ggpubr, categorical variable, dplyr, rstatix, data visualization"
date: 11-12-2023
weight: 5
author: "Matthijs ten Tije"
authorlink: "https://tilburgsciencehub.com/contributors/matthijstentije/"
aliases:
  - /ggpubr
  - /rstatix
  - /data/visualization
---

## Overview
This building block delves into the integration of ggpubr and rstatix packages in R, providing step-by-step guidance on conducting statistical tests and seamlessly incorporating the results into your visualizations.

`ggpubr` is a R package that eases the creation of elegant, publication-quality plots. Its strength lies in  integrating statistical analysis results, such as significance testing, directly into plots. This building block will delve into utilizing key functions like `compare_means()`,` ggbarplot()`, and `stat_p_value()` to create a bar plot that not only displays data but also its statistical significance. 

Furthermore we will use the `rstatix` package. `rstatix` provides functions for statistical tests and data preparation, while ggpubr is used for creating elegant plots. Together, they streamline the process of visualizing statistical comparisons.

## Step-by-Step Guide: Crafting Publishable charts with ggpubr

### Data preparation 

#### Step 1: Installing and Loading ggpubr adn rstatix
First, ensure that you have ggpubr and rstatix installed and loaded in your R environment:

{{% codeblock %}}

```R
install.packages("ggpubr")
install.packages("rstatix")
library(ggpubr)
library(rstatix)
```

{{% /codeblock %}}

#### Step 2: Data Cleaning and preparation
Next in important step is data cleaning and preparation. 

{{% codeblock %}}

```R
# Load data 
data_url <- "https://github.com/tilburgsciencehub/website/tree/master/content/building-blocks/prepare-your-data-for-analysis/data-visualization/piaac.rda"
load(url(data_url)) #piaac.Rda is loaded now

# Data cleaning and Preparation (General)
ggpubr_data <- data %>%
  # Remove observations with missing values
  drop_na("Specify Variables of Interest") %>% 
  # Group by your categorical variable 
  group_by("Categorical variable") %>%
  # convert variables to appropriate types, and order categorical variable
  mutate( 
         "Numeric Variable" = as.numeric("Numeric Variable"),
         "Categorical variable" = factor("Categorical variable", 
                                         levels = c("Level 1", "Level 2", "Level 3")
                                         )
        )

# Data cleaning and Preparation (Example)
ggpubr_data <- data %>%
  # Remove observations with missing values for hourly earnings, gender, and education level
  drop_na(earnhr, edlevel3, gender_r) %>% 
  # Focus on the Netherlands and exclude the top and bottom 1% of earners to remove outliers
  filter(cntryid == "Netherlands", 
         earnhr > quantile(earnhr, 0.01) &
         earnhr < quantile(earnhr, 0.99)) %>%
  group_by(edlevel3) %>%
  # Create a gender dummy variable, convert variables to appropriate types, and order education levels
  mutate( 
         earnhr = as.numeric(earnhr),
         edlevel3 = factor(edlevel3, levels = c("Low", "Medium", "High")),
         gender_r = factor(gender_r, levels = c("Female", "Male")))
```

{{% /codeblock %}}

### Statistical Analysis using Rstatix
In this building block, I will use the `compare_means()` function from the rstatix package. rstatix offers easy-to-use functions for conducting statistical tests, such as t-tests and ANOVA, which can then be directly incorporated into ggpubr for creating informative visualizations. This integration with the ggplot2 ecosystem enhances the ease and efficiency of the analysis process. 

#### Step 3: Performing T-Test with rstatix
The compare_means function in rstatix is designed to compare the mean values of a specific variable across different groups. Here's a structured guide on how to use this function:

- **Syntax**:
  - compare_means(formula, data, method, ref.group)
- **Components:**
- formula: This is where you specify the comparison you want to make.
  - Example: height ~ gender implies comparing the average height across different genders.
- data: This parameter is used to specify the dataset in which the comparison is to be made.
- method: This parameter defines the statistical test to be used for comparison.
- ref.group: This is the reference group against which other groups are compared.
  - Example: If you have groups 'A', 'B', and 'C', and 'A' is set as the reference group, the function will compare 'B' and 'C' with 'A'.
  
This function is a powerful tool for conducting and interpreting various statistical comparisons, particularly useful in data analysis and research.

{{% codeblock %}}

```R
# Performing a statistical t-test using the compare_means function from the rstatix package
stat.test <- compare_means(
  earnhr ~ edlevel3,     # Formula indicating we compare 'earnhr' across 'edlevel3' groups
  data = ggpubr_data,    # The dataset used for the test
  method = "t.test",     # Specifies that a t-test is used for the comparison
  ref.group = "Low"      # The reference group for the comparison is the 'Low' education level
)

# Display the results of the statistical test
stat.test
```

{{% /codeblock %}}

### Data Visualization ggpubr

#### Step 4: Initial Bar Plot Creation with ggbarplot()
`ggbarplot()` is a function from the ggpubr package, which is used to create bar plots. 

**Key Features of ggbarplot():**

*Simplicity:*  
One of the main advantages of ggbarplot() is its simplicity. It allows you to create bar plots with minimal coding, making it user-friendly, especially for those new to data visualization in R.


*Customization:*   
Despite its simplicity, ggbarplot() offers a wide range of customization options. You can change colors, add labels, adjust the width of the bars, and much more.
  
*Integration with ggplot2:*    
ggpubr, the package that includes ggbarplot(), is built on top of ggplot2, a powerful and popular plotting system in R. This means that ggbarplot() benefits from the robustness and flexibility of ggplot2.


Let's look at a practical example: 

{{% codeblock %}}

```R
# Creating a bar plot with ggbarplot from the ggpubr package
ggbarplot(
  data = ggpubr_data,   # The dataset used for the plot
  x = "edlevel3",       # The variable on the x-axis, here 'edlevel3' representing education levels
  y = "earnhr",         # The variable on the y-axis, here 'earnhr' representing hourly earnings

  # Visual and aesthetic settings:
  fill = "edlevel3",    # Sets the fill color of the bars based on 'edlevel3' categories
  add = "mean_se",      # Adds error bars to each bar, showing mean and standard error
  width = 0.35,         # Sets the width of the bars in the plot
  color = "black",      # Sets the color of the bar outlines to black

  # Positional adjustments:
  position = position_dodge(0.8),  # Adjusts the position of the bars to avoid overlap

  # Color palette for the bars:
  palette = c("white", "grey", "black")  # Sets a color palette ranging from white to black
)
```
{{% /codeblock %}}

#### Step 5: Adding Statistical Significance with stat_p_value()`
Now, integrate the test results (step 3) into the bar plot (step 4) using `stat_p_value()`.  
The stat_pvalue_manual() function comes from the ggpubr package in R, and it's used in conjunction with bar plots or other types of plots to add statistical annotations, specifically p-values, to the plot.  
Adding these to a plot can provide a quick visual cue about the statistical differences between groups.

**Breaking Down stat_pvalue_manual():**
- *stat.test*: This is your statistical test result that you want to annotate on the plot. The function uses information from this result to create the annotations.
- *tip.length*: This parameter controls the length of the 'tips' or the small lines that point to the bars or groups being compared. 
- *y.position*: It sets the vertical (y-axis) position of the p-value labels on the plot. You can adjust these numbers to position the labels higher or lower relative to the bars.
- *label*: Here, you specify what kind of label you want to use for your p-value. For example, "p.signif" will automatically convert the p-value into a significance level (like '**' for highly significant results).

{{% codeblock %}}

```R
ggbarplot(# Setup) + 
# Adding p-value annotations to the plot using stat_pvalue_manual
stat_pvalue_manual(
  stat.test,               # The statistical test result to annotate on the plot
  tip.length = 0.002,      # Controls the length of the 'tips' pointing to the bars
  y.position = c(25, 30),  # Sets the vertical position of the p-value labels on the plot
  label = "p.signif"       # Specifies the label format for p-values (e.g., '**' for significance)
)
```

{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggpubr.png" width="450">
</p>

{{% tip %}}
For a step-by-step guide on creating professional bar charts and saving them, refer to this [building block](//bar/chart). It provides a detailed walkthrough of the process to help you create publishable bar charts with ease.

{{% /tip %}}

## Advanced case: Multiple Categorical Variables 
In our previous analysis, we delved into the relationship between education levels and hourly earnings, focusing on a single categorical variable, which was education level. Now, let's take our analysis a step further by considering the influence of not just one, but two categorical variables. Specifically, we aim to understand how both education level and gender collectively impact the mean hourly wages of individuals.

{{% codeblock %}}

```R
# Step 1: Prepare the data
grouped_data <- data %>%
  # Remove missing values
  drop_na(earnhr, edlevel3, gender_r) %>% 
  # Filter data for the Netherlands and remove earnings outliers
  filter(cntryid == "Netherlands", 
         earnhr > quantile(earnhr, 0.01) &
         earnhr < quantile(earnhr, 0.99)) %>%
  group_by(edlevel3) %>%
  # Prepare variables
  mutate( 
         earnhr = as.numeric(earnhr),
         edlevel3 = factor(edlevel3, levels = c("Low", "Medium", "High")),
         gender_r = factor(gender_r, levels = c("Female", "Male")))

# Step 2: Perform statistical tests and adjust p-values
res.stats <- grouped_data %>%
  group_by(edlevel3) %>% # Grouping the data by education level ('edlevel3'), This step allows us to analyze each education level separately.
    t_test(earnhr ~ gender_r) %>% # Next, we conduct a t-test comparing hourly earnings ('earnhr') between different genders ('gender_r'), within each education level. 
  adjust_pvalue() %>% # After obtaining the test results, we adjust the p-values to account for multiple comparisons
  add_significance() # add significance labels to the results to visually indicate which comparisons are statistically significant.

# Step 3: Create a stacked bar plot with error bars
p <- ggbarplot(
  grouped_data, x = "edlevel3", y = "earnhr", add = "mean_se", 
   fill = "gender_r", error.plot = "errorbar", position = position_dodge())

# Step 4: Add p-values to the bar plot
p + stat_pvalue_manual(
  res.stats,
  x = "edlevel3",
  position = position_dodge(0.9),
  y.position = c(24, 28, 32), 
  label = "p"
) + 
# Theme settings (hidden for simplicity)
# ... (theme settings here)

ggsave("my_plot.png", plot = p)
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/ggpubr2.png" width="450">
</p>

{{% summary %}}
This building block explores the integration of R packages, `ggpubr` and `rstatix`, to blend statistical analysis with data visualization. 
- It covers essential steps, from data preparation and package installation to conducting statistical tests and creating publication-quality bar plots. 
- The process involves loading data, cleaning it, and performing tests using `compare_means() `from rstatix. Then, `ggbarplot() `from ggpubr is employed to create bar plots. To enhance the plots, statistical significance is added with `stat_p_value()`. 
- An advanced case considers the influence of multiple categorical variables on mean hourly wages. This comprehensive guide empowers users to produce informative and visually appealing charts in R.

{{% /summary %}}