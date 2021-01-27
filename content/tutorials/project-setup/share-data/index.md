---
tutorialtitle: "Data Sharing"
title: "Data Sharing"
type: "data-sharing"
description: "Document and share data for internal and external use"
keywords: "data sharing"
weight: 100
draft: false
---

## Document and share data for internal and external use

*Maintain, document, and share your data with your team and the public*

## Workflow

- Code and doc: Git
- Raw data, confidential (e.g., JSON files with like personal data it): stored at institution (or, in our case, some S3 bucket only we have access to)
- Data to be published: running code on confidential raw data
    - Make decisions on what your “public” or semi public data should consist of
- Final data set
    - Published to Dataverse with links to code/github repository for documentation
- Maintenance
    - Update code, rerun, re-publish

## Steps

### Create

- Create GitHub repository from template
- Store raw data on secure server (institution)
- Create data prep code to create derived version
- Create initial documentation from template
- Prototype workflow by running it with `make`

### Share

- Publish internally
  - Store on Dropbox
  - Store on S3, make available to coauthors (code snippet)

- Publish externally
  - Dataverse
    1. Create empty data verse
    2. Get Dataverse API credential
    3. Run push.sh or push.bat in repository to push data to server

### Maintain

- Update documentation
- Update data code
- Answer questions from users of the data set, and have an FAQ section
- Republish
