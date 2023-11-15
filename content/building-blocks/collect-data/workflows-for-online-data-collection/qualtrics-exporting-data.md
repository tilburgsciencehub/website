---
title: "Creating Qualtrics Surveys and Exporting Data to R, Pyhton, and Stata"
description: "Being Qualtrics one of the most widely used tools to create online surveys, this building block aims at providing a step by step guide to creating online surveys, instructions on how to export the results to R (qualtRics R package), Python, and Stata. "
keywords: "qualtrics, surveys, export, R, Python, Stata"
date: 24/10/2023
weight: #
author: "Matteo Zicari"
authorlink: "https://tilburgsciencehub.com/contributors/matteozicari/"
aliases:
  - /qualtrics/survey
  - /export/data
  - /R/Python/Stata

---

## Overview

When writing a thesis, a paper, or conducting market research, surveys are among the most frequently used and reliable alternatives to pre-existing datasets. [Qualtrics](https://www.qualtrics.com) is an experience management platform that allows one to create professional surveys to obtain valuable data on a specific target. Being able to integrate such results with statistical software is crucial for performing more advanced data analysis and gaining relevant insights.



Among the `advantages` of surveys are the ability to:
* target a specific niche;
* tailor questions to one's exact research needs;
* generate data that would not otherwise exist for novel research ideas.

In terms of `drawbacks`, surveys often suffer from the following issues:
* limited generalisability to the entire population due to potential biases that can affect the data;
* difficult to design optimally;
* despite the substantial amount of work required, lower rigor when compared to pre-existing datasets.


{{% warning %}}

It is essential to be aware of survey data collection limitations to account for possible biases when designing questions.

{{% /warning %}}

### Design your own survey

During the design phase, a general **rule of thumb** is to ask *broad and general questions at the beginning* (e.g., gender, age), followed by *more specific questions* (e.g., strictly related to research question), and finally more *easy to answer questions* (e.g., demographics) at the end of the questionnaire.

{{% tip %}}
While drafitng the questions, one should consider that:

* the survey must align with the main `research` `question` and `target` `sample`. Always think about your respondents and tailor your questions to them;

* at the outset of the survey, include an `exclusion` `question` to filter out respondents who do not fall within your target audience. For instance, if you are focusing on married couples, the initial question could inquire about the respondent's current relationship status;

* survey `length` is crucial; typically, respondents should be able to complete it within 5 to 10 minutes. Beyond this threshold, an increasing number of respondents are likely to drop out;

* `avoid` complex (e.g., technical jargon) and loaded (e.g., unjustified assumptions about the respondent) questions as well as non-specific ones (e.g., asking two or more questions at once).

{{% /tip %}}

## Qualtrics

This section provides a `step-by-step` `guide` to designing a survey in Qualtrics.

1. Sign in/sign up on Qualtrics [here](https://www.qualtrics.com), and you will be directed to your Qualtrics `homepage` which should resemble the image below.

<div style="text-align: center;">
    <img src="../img/qualt1.png" width="700" alt="homepage">
</div>

2. Click `Create` `a` `survey` to start creating your survey from scratch, or click `Create` `a` `new` `project` to access survey templates and guided projects. Then, click `Survey` to begin.

3. Enter the `name` of your `survey` and then select `Create` `a` `blank` `survey` `project` to access the `survey` `editor`.

<div style="text-align: center;">
    <img src="../img/qualt2.png" width="500" alt="create project">
</div>

4. Within the `survey` `editor` you will find Qualtrics' most relevant features to help you create your online survey. 

<div style="text-align: center;">
    <img src="../img/qualt3.png" width="700" alt="homepage">
</div>

<br/>
<br/>

**(A)**: tabs that allow you to build and edit survey features. For now, we will focus on the default tab (`builder`).

**(B)**: select the most appropriate `question` `type` and customise it according to your needs.

**(C)**: type your actual questions and all the available answers. 

**(D)**: once the survey is complete, you can generate a `preview` to identify and address any potential issues, and then `publish` it. 




## R 

The [qualtRics](https://cran.r-project.org/web/packages/qualtRics/vignettes/qualtRics.html) R package is designed to facilitate the retrieval of survey data through the Qualtrics API with the goal of streamlining the preprocessing required for the analysis of these surveys. This package offfers an alternative to manually downloading surveys from Qualtrics and then importing them into R. Moreover, it allows to update your dataset in real time without having to download and updated version and upload it again into R.

The following points will guide you to successfully importing your survey data into R by using the Qualtrics API:

1. Log in to your Qualtrics profile and navigate to `Account` `Settings` > `Qualtrics` `IDs`. Your instituion must support API access, and you should ensure that the API is enabled for your account. 

2. Within `Qualtrics` `IDs`, you are going to need your `API` `Token` (click `generate` `token` if you don't have one), `Datacenter` `ID`, and `Survey` `ID`. 

3. Open/Install [RStudio](https://posit.co/download/rstudio-desktop/) and follow the code snippets below.



{{% codeblock %}} 

```R
# You need to install the package only once in your environment
install.packages("qualtRics")

library(qualtRics)

```

{{% /codeblock %}}


{{% codeblock %}} 

```R
# API info
qualtrics_api_credentials(api_key = "ADD_YOUR_API_Token", 
                          base_url = "ADD_YOUR_DATACENTER_ID.qualtrics.com/",
                          install = TRUE,
                          overwrite = TRUE)

readRenviron("~/.Renviron")                          

```

{{% /codeblock %}}

{{% tip %}} 

Using `readRenviron("~/.Renviron")` enables you to reload your environment and use your credentials without having to restart R.

{{% /tip %}}

{{% codeblock %}} 

```R
# List of all your available surveys
surveys <- all_surveys()  

# Select survey to download
mysurvey <- fetch_survey(surveyID = surveys$id[1], # Open "surveys" and replace "1" with the position of the survey you want to download
                         force_request = TRUE) # Needed to update "mysurvey" with new responses if still active
```
{{% /codeblock %}}

After you have worked with your data, you can export the new file as a `.csv` file.

{{% codeblock %}} 

```R
write.csv(mysurvey, file = "/YOUR/PATH/file_name.csv")

```
{{% /codeblock %}}


## Python

Package: [QualtricsAPI](https://pypi.org/project/QualtricsAPI/)

{{% codeblock %}} 
```python
pip install QualtricsAPI

```
{{% /codeblock %}}


{{% codeblock %}} 
```python
from QualtricsAPI.Setup import Credentials

```
{{% /codeblock %}}




{{% codeblock %}} 
```python

#Call the qualtrics_api_credentials() method (Non-XM Directory Users)
Credentials().qualtrics_api_credentials(token='Your API Token',data_center='Your Data Center')

#Call the qualtrics_api_credentials() method (XM Directory Users)
Credentials().qualtrics_api_credentials(token='Your API Token',data_center='Your Data Center',directory_id='Your Directory ID')

```
{{% /codeblock %}}


{{% codeblock %}} 

```python
from QualtricsAPI.Survey import Responses

```
{{% /codeblock %}}

{{% codeblock %}} 
```python
#Get Survey Questions
Responses().get_survey_questions(survey="<survey_id>")

```
{{% /codeblock %}}


{{% codeblock %}} 
```python
#Get Survey Responses
Responses().get_survey_responses(survey="<survey_id>")

```
{{% /codeblock %}}



## Stata






{{% summary %}}


{{% /summary %}}