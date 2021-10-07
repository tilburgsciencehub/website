---
title: "Set up the AWS Client"
description: "A command-line interface for using Amazing Web Services"
keywords: "AWS, CLI, command line, terminal, command"
#weight: 1
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /get/awscli
---

Amazon Web Services (AWS) provides cloud-computing and storage facilities that can be used for research projects. To make optimal use of AWS, you can control AWS resources (e.g., starting computers, downloading data) using a so-called command-line interface.

The AWS command-line interface is a light-weight tool that provides you with a "remote control" to the AWS cloud.

Here, we show you how to install and configure AWS CLI.

## Step 1: Install AWS CLI

- Install AWS client by following the [installation instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) provided by Amazon

Note: here, we install AWS CLI version 1, not version 2 (required for backwards-compatibility for some of the projects run by Tilburg Science Hub).

## Step 2: Configure AWS client

- Open a new terminal / command line window
- Type: `aws configure`
- Enter your login credentials for AWS. Typically, these are provided to you by your research institution or team member.

```
AWS Access Key ID [****************7EPQ]: [enter here]
AWS Secret Access Key [****************PdsF]: [enter here]
Default region name [eu-central-1]: eu-central-1
Default output format [None]: [just press enter]
```
