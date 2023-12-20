---
title: "Safeguard Legal Compliance When Scraping"
description: "Obtain legal advice to limit your exposure to legal risks when web scraping"
keywords: "legal, debug, assessment, data quality, webscraping, scraping"
weight: 6
#date: 2021-03-05T22:01:14+05:30
draft: false
aliases:
  - /assess/legal-compliance-webscraping
---

## Overview
The legality of web scraping is an ongoing and complex issue, which might be perplexing for scholars interested in collecting and using web data. There is no clear consensus about whether collecting web data for scientific purposes is permissible under American and international intellectual and cybersecurity laws. Therefore, researchers should obtain legal advice to limit their exposure to legal risks when going forward. As legal experts may not be fully aware of all the steps involved in collecting and using web data, it is imperative to address aspects such as the purpose and framing of the research objective, the scale and scope of data capture, the characteristics of the data source, the relationship of the researcher with the data provider, and any details on the researcher’s data management and usage. Here we provide a template for researchers to prepare for such meetings.

## Key Issues - Legal Advice

### 1. Purpose and framing of the research objective
Collecting data via web scraping or APIs may violate a firm’s intellectual property or contractual rights. Valid reasons (e.g., including but not limited to a research project's scientific objective) may exempt researchers from these rules.

* Is the exact research question known/formulated?
* Is answering the research question societally relevant and urgent?
* Is the research carried out by members of a recognized research organization (e.g., a university, research
institute, or other organization with a primary goal of conducting scientific research)? What is the role of
the person(s) involved in collecting the data within that organization (e.g., student, employee)?
* Has the research project been approved by the institution’s legal or ethical review board?
* How much does the study depend on the web data (e.g., is the data entirely based on one scraped data
set, or only vaguely uses scraped data for some less-critical control variables)?
* Is the data provider the only data source with comparable data? Do viable alternatives exist (e.g.,
feasibility to gather alternative data, including projected resource use)?
* Are private parties involved in the project (e.g., for knowledge dissemination, as part of an industry
collaboration), or is it a purely scientific project?
* Are the results of the scientific research capable of commercial exploitation? If so, what product will be
commercially exploited (e.g., the collected data, the results based on the data, or a product developed based on the data)? Who will be exploiting the results for commercial purposes (e.g., the research organization vs. potential corporate collaborators)?
* Does any party have preferential access to the data, results, or derived product (e.g., an artificial intelligence algorithm trained on the data) of the research project?


### 2. Scale and scope of data capture
Web data collections vary in **scale** (e.g., number of instances and entities collected) and **scope** (e.g., real-time data collection for an unforeseeable time vs. a one-shot data collection within a day).

* What type of data is collected (e.g., on whom, from which location, has permission been obtained from users, has permission been obtained from the website or API – either implicitly or explicitly, does it contain personal or sensitive data? Is obtaining permission feasible?)?
* What is the scope of the data extraction (e.g., the absolute volume of data extracted, volume relative to all data available on the website; what is the frequency of the data collection (e.g., once, at regular intervals, in real-time); can the retrieval limit be determined and respected?)?
* Which extraction technology is used (e.g., identifying as a data collector, degree of intrusiveness, software toolkit)?
* How is the data extraction software deployed (e.g., outsourced to a data collector vs. self-administered via commercial tools, Python packages, or entirely self-coded software)?
* From which location is the data extraction software deployed (e.g., geographical region, part of the research organization’s infrastructure, or not)?


### 3. Characteristics of the data source (website/API)
Some types of data providers explicitly make data available for use in scientific research projects. Others merely provide data as a way to grow their business ecosystem (“developer API”).
* Where is the website or API owner located (e.g., registered office, central administration, place of business)? From where is the data extracted (e.g., server location)?
* What type of data provider is data being extracted from (e.g., scraped from a website, collected from an API; is the data provider explicitly offering the data for extraction, or is the data provided as part of a development platform? Is the data source aggregating/collecting data from third parties (e.g., through web scraping or APIs)? Does the data provider have the right to display the data?)?
* How public is the data access (e.g., public on the web, hidden behind a login screen but publicly accessible for anyone, hidden after a login screen only accessible with special permissions)?
* Is the displayed data personalized or customized in any way (e.g., not personalized, customized for a larger group of persons, customized for a specific user)?
* Could potential harm be inflicted from using the data, either for the users/entities or pertaining to the firm’s business model (e.g., competition)? What is the risk for users and/or firms if the raw data would become public unintentionally?
* Does the data provider disallow the use of automated collections, either via robots.txt, the site’s or API’s terms of use, or any other contracts? Have contracts been accepted (implicitly by continuing to use the site/service, or explicitly by signing up for an account with the website or service)?
* Does the data provider attach a specific license to the use of the data, and what does this license imply for subsequent data use?

### 4. Relationship of the researcher with the data provider
Some of the legal concerns could be resolved if the researcher obtained the data provider’s permission.

* Has the data provider approved the data collection (e.g., implicitly or explicitly)?
* What are the conditions under which approval has been given (e.g., disguise the identity of the data
provider in the paper)?
* Has the data provider been notified about the data collection (e.g., How? How many times? Has the data
provider reacted?)? Would notification be feasible?
* Are any fees being paid for the data collection (e.g., for an API)?


### 5. Data management and usage
A researcher may risk violating privacy regulations or other laws when storing, working with, or sharing data.
* Is the raw data being stored during the collection or directly parsed?
* How (e.g., file server, file format), why (e.g., reproducibility/verification of research results), and for
how long is the raw data stored after the collection?
* Is the data publicly accessible, are shared with members of a research unit or department? Or is the data
only accessible to coauthors?
* How will the stored data be used? How has the raw data been aggregated? Have entities been disguised
(anonymization?)
* At what level of detail are statistical results reported (e.g., summary statistics, correlation tables,
parameter estimates from a model, cross tabs, package with a trained machine learning model based on
the data)?
* Has a license been chosen for the final data set? Is the license compatible with potentially inherited
licenses (e.g., creative commons)?
