---
title: "Run Computations on Amazon Web Services"
description: "Set-up and configure a virtual machine to run your scripts remotely"
keywords: "virtual machines, vm, cloud computing, aws, amazon, ec2"
date: 2021-04-30
weight: 1
aliases:
 - /run/aws-computations
---

## Overview <!-- Goal of the Building Block -->

With increasing demands in computations (i.e., high number of CPUs) or data (i.e., high memory), it can be worthwhile to move your computations and data preparation pipelines to the cloud. Amazon Web Services (AWS) offer virtual machines (VM) for rent that you configure to your own needs. For example, if you run out of RAM on your local machine due to complex computational tasks, you can launch an Amazon Elastic Compute Cloud (EC2) instance with a high amount of memory to execute the computations in the cloud. This building block outlines how to launch, monitor, and terminate virtual instances on AWS.

## Code
One of the most fundamental compute services of AWS is EC2 which is like a running computer running in one of Amazon's data centers that you can access for the deployment of code. It will have a certain amount of CPU, RAM, disk space, and network interface bandwidth assigned to it, and you can choose multiple flavors of Windows and Linux operating systems to run on your EC2 instance.

### Launch Instance
Although you can also launch instances via the command line, here we show you how to get started with the [AWS console](https://console.aws.amazon.com/console) in your browser.

1. After you have signed in, type “EC2” in the search bar.

2. Click on the orange button that says "Launch instance".

3. It asks you to choose an Amazon Machine Image (AMI) which is the operating system that will be launched on the system. If you're just getting started, we recommend to pick one that has a free tier eligible (e.g., Amazon Linux 2 AMI) and click on "Select".

4. Now it asks you to choose an instance type that fits your needs (i.e., number of CPUs, RAM Memory, network performance, etc.). In other words, how powerful do you want your machine to be? This depends on the computations that you plan on running on the VM. For example, the baseline `t2.micro` instance type (1 CPU and 1 GB RAM) is eligible for a free tier and is therefore recommended to get started. Other instance types can cost less than a penny per hour for the most basic offering up to 32 dollars per hour for a machine with 1152GB of RAM and 96 CPUs!

5. After you have selected an instance type, click on "Review and Launch" and then on "Launch".

6. Now you need to create a new key pair which is basically like a password to authenticate yourself and connect with the instance. Give the key pair a name (can be anything) and click on "Download Key Pair". Store this private key file (`*.pem`) in a secure and accessible location because you'll not be able to download the file again after it's created.

7. Finally, click on "Launch Instances". If you now return to the instances dashboard page, you'll see that Amazon is spinning up your configured instance. After a minute or so, the instance state should say "Running" which means we are ready to connect to it!



### Connect To Instance
Depending on whether you're using Mac or Windows as your own operating system, follow either of the instructions below.

*Mac*   
1. Click on your running EC2-instance in the console and copy the Public IPv4 DNS address (e.g., `ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com`).

2. Open the terminal and type `export HOST=<YOUR-PUBLIC-IPV4-DNS>` (see step 1) and `export KEY=<PATH_TO_KEY_PAIR_FILE>` (e.g., `/Users/Roy/Downloads/ec2-key-pair.pem`). This creates two variables, `HOST` and `KEY`, that we can reference in our terminal (e.g., if you type `$KEY` it returns the aforementioned file path).

3. Type `chmod 700 $KEY` to change the permissions of the private key file.

4. Type `SSH -i $KEY ec2-user@$HOST` to connect with the EC2-instance.

5. Type `yes` if it asks you to continue connecting and hit Enter. If done successfully, it prints the text "EC2" to the terminal followed by the AMI that you selected (e.g., Amazon Linux 2 AMI). So, in short, we connected to an EC2-instance that we can control through our terminal, however, there are no scripts or data on it yet so we first need to copy files to our instance before we can put it to work.


*Windows*
1. Download [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) MSI Windows Installer and follow the installation wizard. If it doesn't come with the PuTTY Key Generator pre-installed, also make sure to download `puttygen.exe` from the same page.

2. Open PuTTy Key Generator, click on "Load", and select the private key file you downloaded earlier.

3. Click on "Save private key" to convert the `*.pem` file into a `*.ppk` file.

4. Click on your running EC2-instance in the console and copy the Public IPv4 DNS address (e.g., `ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com`).

5. Open PuTTY (so not the Key Generator!) and enter the following as the host name: `ec2-user@<YOUR-PUBLIC-IPV4-DNS>`

6. In the left panel, click on Connection > SSH > Auth and click on "Browse" to add your `*.ppk` private key.

7. Click on "Open" to start the connection. So, in short, we connected to an EC2-instance that we can control through our terminal, however, there are no scripts or data on it yet so we first need to copy files to our instance before we can put it to work.



### Move Files
Also when it comes to moving files to your EC2 instance, there are multiple ways to go about it:

*Mac*
1. `cd` into the directory that contains the files that you want to transfer.

2. Type `scp -i $KEY -r $(pwd) ec2-user@$HOST:/home/ec2-user` to copy your entire working directory to the home directory of your VM. (tip: this method assumes you're not connected yet. If you are though, press Ctrl + D to disconnect).


*Mac/Windows*
1. Alternatively, install File Transfer Protocol (FTP) client [FileZilla](https://filezilla-project.org).
2. Click on File > Site Manager > New Site.
3. Change the protocol to "SFTP".
4. Use the public IPV4 DNS address (see AWS console) as the host name.
5. Choose "Key file" as the logon type, set the username to `ec2-user`, and add your `*.pem` file as the key file.
6. Click on "Connect". On the right side, all files on the EC2 Instance are listed, and on the left side you can find the files on your local machine. To copy files from one place to another, you can simply drag and drop them between both windows.


### Run Scripts
If you opted for the default Amazon Linux 2 AMI, you probably need to install some additional software to be able to execute your code files. To install Python 3 and any other packages on your EC2 instance, run the following commands:

{{% codeblock %}}
```bash
# install Python
sudo yum install python3

# install a single package
sudo python3 -m pip install <PACKAGE_NAME>

# install multiple packages from txt file
sudo python3 -m pip install -r requirements.txt
```
{{% /codeblock %}}

Next, you can run your scripts from the command line like you're used to with `python3 <SCRIPT_NAME>.py`.

{{% tip %}}
One of the key advantages of using a VM is that you can leave it running indefinitely (even if you shut down your laptop!). Take a look at the [task scheduling](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/task-scheduling/) building block to learn how to use crontab to schedule recurring tasks (e.g., run a Python script that scrapes a website every day at 3 AM). Keep in mind that the time at your VM may differ from your local time because the data center that hosts the VM is located in another time zone (tip: run `date` to find out the UTC time).
{{% /tip %}}



### Terminate Instances
Even though the very basic VMs can run for free forever, it is good practice to shut down inactive VMs. After all, you don't want to find out at the end of the month - once you receive your bill from AWS - that you accidentally left an instance running in the background. To terminate a VM follow the steps below:

1. Visit your "Instances" dashboard in the console
2. Tick the checkboxes of those instances you want to stop.
3. Click on the "Instant state" button. Here you can either stop or terminate the instance. Stop means that you can re-activate the instance at a later point in time, whereas terminate means that you remove it permanently (including all files stored on it).
