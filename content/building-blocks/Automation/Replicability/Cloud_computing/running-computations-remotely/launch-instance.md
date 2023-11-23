---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
indexexclude: "true"
title: "Launch Instance"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 101
draft: false
aliases:
  - /learn/cloud/launch
  - /tutorials/more-tutorials/running-computations-remotely/launch-instance
---

# Launch Instance

Although you can also launch instances via the command line, here we show you how to get started with the [AWS console](https://console.aws.amazon.com/console) in your browser.

![Launch Instance](../img/launch-instance.gif)

1. After you have signed in, type “EC2” in the search bar.

2. Click on the orange button that says "Launch instance".

3. It asks you to choose an Amazon Machine Image (AMI) which is the operating system that will be launched on the system. If you're just getting started, we recommend to pick one that has a free tier eligible (e.g., Amazon Linux 2 AMI) and click on "Select".

4. Now it asks you to choose an instance type that fits your needs (i.e., number of CPUs, RAM Memory, network performance, etc.). In other words, how powerful do you want your machine to be? This depends on the computations that you plan on running on the VM. For example, the baseline `t2.micro` instance type (1 CPU and 1 GB RAM) is eligible for a free tier and is therefore recommended to get started. Other instance types can cost less than a penny per hour for the most basic offering up to 32 dollars per hour for a machine with 1152GB of RAM and 96 CPUs!

5. After you have selected an instance type, click on "Review and Launch" and then on "Launch".

6. Now you need to create a new key pair which is basically like a password to authenticate yourself and connect with the instance. Give the key pair a name (can be anything) and click on "Download Key Pair". Store this private key file (`*.pem`) in a secure and accessible location because you'll not be able to download the file again after it's created.

7. Finally, click on "Launch Instances". If you now return to the instances dashboard page, you'll see that Amazon is spinning up your configured instance. After a minute or so, the instance state should say "Running" which means we are ready to connect to it!
