---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
title: "Terminate Instance"
indexexclude: "true"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 105
draft: false
aliases:
  - /learn/cloud/terminate
  - /tutorials/more-tutorials/running-computations-remotely/terminate-instances
---
# Terminate Instance

Even though the very basic VMs can run for free forever, it is good practice to shut down inactive VMs. After all, you don't want to find out at the end of the month - once you receive your bill from AWS - that you accidentally left an instance running in the background. To terminate a VM follow the steps below:

![Terminate instance](../img/terminate-instance.gif)


1. Visit your "Instances" dashboard in the console
2. Tick the checkboxes of those instances you want to stop.
3. Click on the "Instant state" button. Here you can either stop or terminate the instance. Stop means that you can re-activate the instance at a later point in time, whereas terminate means that you remove it permanently (including all files stored on it).
