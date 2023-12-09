---
title: "Coding, Workflow, and Data Management in the Master Thesis"
description: "Part 2 of the Master Thesis Guide: coding, workflow and data management as the core foundation of your research."
keywords: "master, thesis, guide, marketing, economics, management, tisem, research, guidance, preparation, question, proposal, skills, resources"
date: 2023-07-10
weight: 3
author: "Valerie Vossen"
aliases:
  - /masterthesisguide/datacoding
---

## Overview

The Master Thesis Guide will serve as support throughout the entire thesis process, consisting of an empirical research project for studies in marketing, economics, data science, management, and related fields. This page covers the **coding, workflow and data management**, divided into the following sections:

- Code versioning: GitHub
- Data collection techniques
- Data import
- Raw data exploration and visualization
- Model estimation
- Establishing workflow and reproducibility

## Code versioning: GitHub

GitHub is a powerful version control platform that allows you to manage and track changes in your code. This ensures transparency, and organization throughout the research process. 

### Why use GitHub for the Master Thesis?

Even though your thesis is probably not a collaborative project, keeping your work on GitHub still offers a lot of advantages:

- *Version control* 
<br>
Easily track changes, view previous versions, and revert to earlier drafts if needed. No more confusions with multiple versions of the same document (e.g. saving the file as "Thesisdraft1", "Thesisdraft2" and so on). 

- *Transparent documentation*
<br>
The commit history provides a clear record of all the edits made. Leaving clear commit messages help in understanding what edits you made when revisiting your work after months of working on it. 

- *Branching*
<br>
You can create branches for different sections without impacting the main thesis draft in which you can experiment as much as you want.  

- *Remote accessibility*
<br>
Access your thesis from anywhere as GitHub is a cloud-based platform.

- *Backup*
<br>
GitHub serves as a secure backup, minimizing the risk of losing your data or work.  

- *Showcasing your work*
<br>
After finishing the thesis, you can keep your thesis on GitHub, making it accessible for others to use and showcasing your research!

Follow [this building block](/share/data) to learn how to use GitHub for your project!

## Data collection techniques

Depending on your research, you might want to create your own data. Techniques for data collection include web scraping or APIs. 
- The [Web scraping and API Mining tutorial](/learn/web-scraping-and-api-mining) discusses the difference between web scraping and API mining. It also shows you how to scrape static and dynamic websites and how to extract data from APIs. 
- When you are new to web scraping and APIs, you can follow the open course [Online Data Collection and Management](https://odcm.hannesdatta.com/) of Tilburg University. 

## Data import

You might want to analyze data sets for your thesis that already exist somewhere. There are several techniques to import data, dependent on your data source. Use these building blocks to learn about importing data and see example cases.

- [Download data directly from URLs using R and Python](/download-data/)
- [Import larger datasets into R](/large-datasets-r/)
- [The package `Dask` for processing large datasets in Python](/large-datasets-python/)
- [Integrating SPSS data in R](/spss-files-in-r/): useful when your data source is an SPSS file.
- [Text pre-processing in R](/text-preprocessing/): useful when working with text data in R.
- Data sources for economists


## Inspecting raw data

Upon importing your raw data, explore it right away to assess its quality. There's several things you can do:

- **Visually inspect your data:** Load the data into your software program (e.g. R, Excel) and visually inspect the data tables and its structure. 

- **Cross-tabulate data:** organize your data in a table format to see the frequency distribution of variables' categories in relation to each other. Do this with `table()` in R or pivot tables in Excel.

- **Plot your data** to explore trends (e.g. with `plot()` in R), or distributions (e.g. with `hist()` in R). Aggregate data by a common unit before plotting (e.g. time periods, categories like countries or brands).


### Important considerations

Key considerations when assessing your raw data quality include the following points:

- **Documentation**: study any provided ReadMe file or documentation thorougly. Or if there is no documentation available, create your own using [this building block which includes a template](/documenting-new-data/).

- **Variable names and columns**: Ensure you understand the meaning of each variable and column. Confirm if any columns are incomplete.

- **Data quality**: 
    - Check for feasibility and consistency in variable values. Are there any values that seem unrealistic?
    - Detect missing values and identify if missing values truly represent *Not available (NA)* data or if they imply zero values. 
    - Verify the consistency in data definitions across the dataset, including the measurement units of your variables.
    - Pay attention to proper encoding of strings and headers.

{{% tip %}}
**GDPR compliance**
When dealing with data, ensuring compliance with your organization's data management policies is crucial. This often entails promptly anonymizing personally identifiable information during your data preparation phase. 

Tilburg University has provided [specific guidelines for students](https://www.tilburguniversity.edu/sites/default/files/download/Student%20research%20and%20personal%20data%20in%20your%20research.pdf). Moreover, the legal department at Tilburg offers valuable [guidance on handling personal data with care](https://www.tilburguniversity.edu/about/conduct-and-integrity/privacy-and-security/careful-handling-personal-data).
{{% /tip %}}

## Building your project pipeline 

A project pipeline is a systematic framework that gives a structured sequence of the steps included in your research. It outlines the flow of tasks, from data collection and cleaning to analysis and visualization. 

Depending on your field of study, your project pipeline might quickly become more complex, which makes a clear structure even more important. A good project pipeline ensures consistency and facilitates efficiency by breaking down the complex process into smaller manageable steps. 

It also ensures transparency. For example, a project where code files are separated into multiple smaller components (e.g. one for data cleaning, one for running the model, one for producing tables and figures) is way easier for others to read and understand.

Use [this tutorial that covers the principles of project setup and workflow management](/project-setup-overview/) as a guidance. 

{{% tip %}}
[A checklist to improve your project's structure and efficiency](/workflow-checklist/) to help you ensure you meet all the requirements when building your pipeline.
{{% /tip %}}

#### Pipeline automation
If your thesis is data-oriented, e.g. in marketing analytics or data science, consider automating your pipeline. [This tutorial](/pipeline-automation-overview/) is helpful to teach you how to automate your pipeline automation using `Make`.

{{% summary %}}
This part of the Master Thesis guide aims at making the data management and coding of your thesis as smoothly as possible. [The next section](/masterthesisguide/writing) is about the writing of your thesis, providing you with useful tips and resources. 
{{% /summary %}}