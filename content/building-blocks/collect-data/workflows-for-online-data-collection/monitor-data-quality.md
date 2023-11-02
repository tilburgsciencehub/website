---
title: "Monitor and Safeguard Your Data Quality"
description: "10 common issues and potential solutions to troubleshoot your data collection"
keywords: "monitor, debug, assessment, data quality, webscraping, scraping, data collection"
#weight: 3
#date: 2021-03-05T22:01:14+05:30
draft: false
aliases:
  - /monitor/data-quality
---

## Overview
After carefully planning and prototyping, researchers can begin the actual data collection. It is important to note that the data collection process is best considered “work-in-progress.” Thus, researchers need to remain agile and adapt the code where required. Here we outline the 10 most common data quality issues and how you can resolve them.

## 10 Common Issues

#### 1. It cannot be verified whether all the data that should have been collected was indeed collected.
* Log each web request (i.e., URL call), along with response status codes, timestamps of when the collection was started, and when the request was made.
* Save raw HTML websites, along with the parsed data, and compare them.

#### 2. The data collection has been interrupted or stopped unexpectedly.
* Verify timestamps in log files or content of parsed data to gauge severity.
* Try to identify and fix the cause of the interruption.
* Record issues in a logbook (e.g., in the documentation) and notify potential users of
the data.
* Set up a monitoring tool to timely alert you to any future issues.
* Move data collection to a more stable environment (e.g., a cloud computer rather than a local office PC).

#### 3. It is cumbersome/takes a lot of time to conduct quality checks.
* Automatically generate reports on data quality (e.g., using RMarkdown).
* Automate data preparation workflows.

#### 4. The data collection takes place in a highly dynamic environment.
* Monitor the data collection environment (e.g., subscribe to the focal firm’s blog, keep an eye on the websites of related firms, etc., to identify any additional data that needs to be captured). Record any important events in the documentation.

#### 5. The data collection breaks frequently.
* Choose more stable data selectors (e.g., CSS is less stable than HTML tag words; “English” class names may be better than cryptic class names, etc.).
* Make use of error handling to avoid interruptions (e.g., try and except in Python),
but do not blindly ignore any error.
* Store raw HTML files, along with parsed data for recovery of data.
* Consider using an API (over web scraping).

#### 6. The data collection is unexpectedly slow.
* Check whether you obey the retrieval limit or fair use policy and implement timers/pauses where possible.
* Check for traces of being banned/blocked/slowed down by the website (e.g., by investigating the retrieved content).
* Notify data provider(s) about potential bandwidth issues (e.g., in the case of using a provider’s API).
* Update the technically feasible retrieval limit, and re-calculate desired sample size, extraction frequency, etc.

#### 7. Fewer data than expected is retrieved.
* Check for any time-outs and erroneous server responses.
* Verify that the extraction software is suitable for the type of data source (e.g.,
static vs. dynamic websites).
* Store raw HTML files of websites or JSON response of an API during the data collection, inspect what data is available in the raw data, and verify it has been parsed correctly.

#### 8. Disk space is exceeded, or many files are generated.
* Move data to a remote file location (potentially zip files before uploading them to save bandwidth, e.g., every day).
* Make use of external databases (e.g., by the university or in the cloud).

#### 9. The computer, which collects the data, crashes.
* Verify whether the computer has had an uninterrupted power supply (and ask University to place the computer on a secure power line or notify you about planned power outages).
* Move scraping software to the cloud, and implement checks that data collection runs.

#### 10. Cloud service provider bills exceed projected costs.
* Verify that computing resources are appropriate (e.g., downscale servers on which collection scripts run, verify that database runs optimally). Consider the costs of data transfer.
* Verify whether any backup data can be moved to a different location or placed in a glacier for which lower storage costs will be charged.
* Consider writing data to files after collection, rather than keeping them in an actively running database in the cloud.
