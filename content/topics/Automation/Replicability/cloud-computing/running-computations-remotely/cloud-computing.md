---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
title: "Cloud Computing"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 100
draft: false
aliases:
  - /learn/cloud
  - /topics/more-tutorials/running-computations-remotely/cloud-computing
  - /topics/scale-up/running-computations-remotely/_index
  - /topics/automate-and-execute-your-work/cloud-computing/
  - /topics/more-tutorials/running-computations-remotely/
  
---

## Why Cloud Computing?
With increasing demands in computations (i.e., high number of CPUs) or data (i.e., high memory), it can be worthwhile to move your computations and data preparation pipelines to the cloud. Cloud providers offer virtual machines (VM) for rent that you configure to your own needs. For example, if you ran out of RAM on your local machine due to complex computational tasks, you can launch a VM instance with a high amount of memory to execute the computations in the cloud. This not only speeds up computations, but also minimizes errors (e.g., avoid computer restart) and interference from others.

In this tutorial we outline how to launch, monitor, and terminate virtual instances on Amazon Web Services (AWS).


## Comparison Cloud Providers
The three biggest cloud VM infrastructure providers are: Amazon Elastic Cloud 2 (EC2), Google Compute Engine (EC), and Microsoft Azure Virtual Machines (VM). VM instances can be perceived as real computers with CPU, memory, network, storage configurations, and an operation system (also known as image). The table below indicates the differences between the three providers.

| | [Amazon EC2](https://portal.aws.amazon.com/billing/signup#/start) | [Google CE](https://accounts.google.com/signin/v2/identifier?service=cloudconsole) | [Azure VM](https://azure.microsoft.com/en-us/free/) |
| ---: | :--- | :--- | :--- |
| CPUs | 1-40  | 1-32 | 1-32  |
| RAM memory | 0.5 - 244 GB | 0.6 - 208 GB | 0.75 - 448 GB |
| Temporary storage limit | 48 TB | 3 TB | 4 TB |
| Number of image templates  | 39  | 18 | 40 |
| Free credits students | $200  | $300 | $100 |
| Creditcard required  | No | Yes | No |

We choose for AWS EC2 here because of its "always free" tier of the most basic VMs, ease of use, and the educational programme they have in place ([AWS Educate](https://aws.amazon.com/education/awseducate/)) that allows educators to create classes, allocate credits to students, and invite them to sign up without a credit card.
