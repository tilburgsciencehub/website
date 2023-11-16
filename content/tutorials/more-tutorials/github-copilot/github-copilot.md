---
tutorialtitle: "GitHub Copilot in RStudio"
type: "github-copilot-in-rstudio"
title: "GitHub Copilot in RStudio"
description: "Learning what GitHub Copilot is, how and why it can be used"
keywords: "setup, RStudio, R, GitHub, GitHub Copilot, AI"
weight: 2
draft: false
aliases:
- /tutorials/more-tutorials/github-copilot/github-copilot
- /tutorials/more-tutorials/github-copilot/_index
---

## Overview 

In this tutorial you will learn what GitHub Copilot is and how it can be used for you research in RStudio. 

## What is GitHub Copilot

[GitHub Copilot](https://github.com/features/copilot) is an AI pair programmer that offers autocomplete-style suggestions as you code. The tool can give you suggestions based on the code you want to use or by simply inquiring about what you want the code to do. 

It is developed by [GitHub](https://github.com/) in partnership with OpenAI, and it is designated to best assist developers in writing code more efficiently. 

Some of its features include: 
- **Code autocompletion**: generating suggestions while typing the code. 
- **Code generation**: Copilot will use the context of the active document to generate suggestions for code that might be useful.
- **Answering questions**: it can also be used to ask simple questions while you are coding (e.g., "What is the definition of mean?").
- **Language support**: supports multiple programming languages, including R, Python, SQL, HTML, and JavaScript. In this tutorial, we will be focusing on R. 

{{% warning %}}

Verified students, teachers, and maintainers of popular open-source projects on GitHub can use Copilot for Individuals for free. Otherwise, a paid subscription is needed to use the tool.

For more information, visit [Copilot](https://docs.github.com/en/copilot/quickstart).

{{% /warning %}}


## Set up GitHub and Copilot 

1. To start using Copilot in RStudio, you must first install R and RStudio on your computer. 
If you haven't checked it out, Tilburg Science Hub has a building block on this: [Installing R & RStudio](https://tilburgsciencehub.com/get/r/). 

2. Once you have installed it, configure your GitHub account. To use Copilot in R you need an active GiHub account. 
A useful source is [Set up Git and GitHub](https://tilburgsciencehub.com/get/git/?utm_campaign=referral-short). 

3. As a student, you need to request specific access to use the service of Copilot. Follow this [link](https://education.github.com/). You will need to provide proof of enrollment.
    - Once you land on the website, scroll down until you see this image: 

    <p align = "center">
    <img src = "../img/Student-dev-pack.png" width="400">
    </p>

    - Click on "Get the Student Pack". 
    You will land on a page looking like this: 

    <p align = "center">
    <img src = "../img/Student-dev-pack-1.png" width="400">
    </p>

    - Click on "Sign up for Student Developer Pack”, find the box indicating the benefits for individuals, and click on "Get student benefits”. 

    <p align = "center">
    <img src = "../img/Student-dev-pack-2.png" width="400">
    </p>

    - Now, you will be directed to the page dedicated to your application. You will need to provide a valid University email address, the name of your institution, and a small motivation behind your request. 

4. Once your application has been approved, you will receive a notification via email (be careful; it could also be in the spam folder). 

5. To activate GitHub Copilot, go to the [landing page of Copilot](https://github.com/features/copilot) and make sure you are signed in with your GitHub account (the same with which you have requested the student access). 

    - Click on "Buy now", then after that, a message should appear saying you are eligible to use Copilot for free. Proceed with installation, and there you go; you now have access to this feature.

    For your reference, this is the message that should appear: 

    <p align = "center">
    <img src = "../img/Student-dev-pack-3.png" width="400">
    </p>

    
6. The process does not end here. To enable Copilot in RStudio, follow these steps. Open the app, click on Tools -> Global Options -> Copilot -> tick the box saying "Enable GitHub Copilot" -> sign in to your GitHub account, and there you go; you are ready to start!

    <p align = "center">
    <img src = "../img/R-copilot.png" width="400">
    </p>


## Applications

In this tutorial, we will see the application of Copilot in RStudio in the following contexts: 

- Exploratory analysis of a dataset 
- Data visualization 
- Data manipulation 
- Questions & answers 

### Exploratory data analysis 

For this tutorial, we will demonstrate the use of Copilot with the built-in R dataset called "swiss", containing different socio-economic variables for different cantons in Switzerland. 

As a first library, the package `ggplot2` is needed for visualization and load of the dataset "swiss". 

{{% codeblock %}}

```R
# Load packages
library(ggplot2)

# Load swiss dataset 
data("swiss")

```
{{% /codeblock %}}

Copilot will already start to give suggestions (as shown in the picture below); to follow those, you need to press the tab key. 

<p align = "center">
<img src = "../img/R-code-1.png" width="400">
</p>

Now, let's proceed with exploring the dataset with some summary statistics. Again, notice that just by typing "Exploratory data analysis" in the R script, ghost suggestions will appear for the following steps.
Such examples are the commands “summary" and "head". 

<p align = "center">
<img src = "../img/R-code-2.png" width="400">
</p>

{{% codeblock %}}

```R
# Exploratory data analysis 

# summary statistics
summary(swiss)
head(swiss)

# summary statistics on one variable (e.g., fertitlity)
mean(swiss$Fertility)
sd(swiss$Fertility)

```
{{% /codeblock %}}

{{% tip %}}

The simpler the instructions, the better for your output, as Copilot is a new introduction in RStudio and constantly being trained.
Moreover, to keep Copilot going, press the tab key on its previous suggestions to get more commands.

{{% /tip %}}

Another useful way to use Copilot is simply writing what you want to do, and suggestions will appear accordingly. For example, if we want to know the summary statistics for two variables (e.g. fertility and education) and their correlation, write it in a comment format (using #) and Copilot will provide the code as shown below. 

<p align = "center">
<img src = "../img/R-code-3.png" width="400">
</p>

{{% codeblock %}}

```R
# summary statistics on two variables (e.g., fertility and education)
mean(swiss$Education)
sd(swiss$Education)

#plot the correlation between fertility and education
cor(swiss$Fertility, swiss$Education)
plot(swiss$Fertility, swiss$Education)
```
{{% /codeblock %}}

The resulting plot should look like this: 

<p align = "center">
<img src = "../img/Rplot3.png" width="400">
</p>

The scatterplot looks unrefined, but no worries, the following section will show you how to improve this with the help of Copilot. 

### Data visualization 

A great advantage of using Copilot in RStudio is data visualization. With a simple request to Copilot, you can change the appearance of your visualization and implement small changes to elevate your graphs quickly. 
The first step is writing out in a comment form which variables you want to use and which figure you aim for. Copilot will suggest the simplest form of a graph; you can then proceed to refine the visualization to your best liking. 

An example is the following suggested code: 

{{% codeblock %}}

```R
# create a scatterplot between Fertility and Agriculture using ggplot2
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point()

# improve the visualization, add a title, impose minimal setting and change the color of the point to a more neutral one
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "grey") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland")

# I want the dots to be blue
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland")

# add the regression line to the plot
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland") + geom_smooth(method = "lm", se = FALSE)

# make the line dashed 
ggplot(data = swiss, aes(x = Fertility, y = Agriculture)) + geom_point(color = "blue") + theme_minimal() + labs(title = "Fertility and Agriculture in Switzerland") + geom_smooth(method = "lm", se = FALSE, linetype = "dashed")

```
{{% /codeblock %}}

For your reference, a comparison between the starting and the final scatterplot: 

<p align = "center">
<img src = "../img/Rplot.png" width="400">
</p>

<p align = "center">
<img src = "../img/Rplot1.png" width="400">
</p>

### Data manipulation 

In this case, the data manipulation consists of adding the cantons’ names as the first column instead of having them as indexes. This can be useful for performing a cluster analysis grouping cantons with similar socio-economic features. 

In case you do not know how to proceed, you can ask Copilot how to do it, and it will give you input, as you can see in the code block below: 

The following code block represents Copilot's input. It could be possible that your suggestion will be different. 

{{% codeblock %}}

```R
# I want to remove the index and add it as a column in the dataset. Suggest me a way to do it 
swiss$Cantones <- rownames(swiss) 
head(swiss)
```
{{% /codeblock %}}

After running this command, visualize the dataset. Notice that the cantons’ names were not removed as row names but added as the last column. 

<p align = "center">
<img src = "../img/Rdataset1.png" width="400">
</p>

Although, in principle, this is not wrong, it doesn’t look very clear, and it would be better to have them in the first column for a clearer and more structured dataset. 

After some research, one of the possible ways to do this is the following: 

{{% codeblock %}}

```R
data("swiss")
library(tibble)
swiss <- as_tibble(swiss, rownames = "Cantons")
```
{{% /codeblock %}}

<p align = "center">
<img src = "../img/Rdataset2.png" width="400">
</p>

{{% tip %}}

Before running the above code chunk, re-load the “swiss” dataset to work on the original version, otherwise you will be running the code on the modified data. 

{{% /tip %}}

This last step was to show you that Copilot, as every AI powered tool, is not to be followed blindly as it is constantly learning and can cause mistakes or not execute what you have in mind due to the phrasing of the request. 

### Questions & Answers

A nice feature of Copilot is the possibility to ask questions and receive a response on the RStudio script. A simple example is the following: 

{{% codeblock %}}

```R
# You can also ask questions to Copilot. 

# q: What is the definition of mean of a variable?
# a: The mean is the average of the numbers. It is easy to calculate: add up all the numbers, then divide by how many numbers there are. In other words, it is the sum divided by the count.

```
{{% /codeblock %}}

{{% tip %}}

To ensure accuracy, ask relatively clear and simple questions. 

{{% /tip %}}


{{% summary %}}
This tutorial provides an overview of GitHub Copilot and its application in RStudio for research purposes. 
It comprises three blocks: 

1. Explaining what GitHub Copilot is, its main features, and its applications. 
2. The setup process to ensure a smooth start with this new tool in RStudio. 
3. Demonstrations on how to use Copilot in RStudio. 
{{% /summary %}}

*Sources: [RStudio GitHub Copilot](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html); [GitHub Copilot](https://docs.github.com/en/copilot/overview-of-github-copilot/about-github-copilot-for-individuals)*
