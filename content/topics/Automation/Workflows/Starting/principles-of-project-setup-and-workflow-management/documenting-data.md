---
tutorialtitle: "Principles of Project Setup and Workflow Management"
type: "principles-of-project-setup"
indexexclude: "true"
title: "Documenting Datasets"
description: "If your project contains data that has been newly created, you are required to include a documentation of that data in your project."
keywords: "document, data, dataset, derived, readme, describe"
date: 2020-11-11T22:01:14+05:30
draft: false
Weight: 5
aliases:
  - /document-data/project-setup
  - /topics/project-management/principles-of-project-setup-and-workflow-management/documenting-data
---

## Documenting Datasets

If your project contains data that has been newly created (i.e., which is not otherwise (publicly) available yet; including *derived* data sets), you are required to include a documentation of that data in your project.

Instances of "new data" may included, but are not restricted to be:

* data scraped from websites
* data gathered via APIs
* manually labeled data
	* e.g., to assign GDP per capita to a list of countries
	* e.g., to classify a music label as a major versus independent label
	* ...
* data *derived* from secondary data (e.g., a cleaned data set; making explicit how you cleaned the data is important for future use of that data)

{{% tip %}}

Think of "new data" as *any* data that feeds into one of the pipeline stages in your project; it really needs not to be "big" data, but can simply consist of a `.csv` file with
names and associated labels (e.g., as in the case of countries --> GDP per capita).

{{% /tip %}}

Check out [our building block for documenting data](/topics/store-and-document-your-data/document-data/documenting-new-data/)!
