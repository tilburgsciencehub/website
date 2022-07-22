---
title: "Run RStudio on AWS using Docker"
description: "Docker - the bridge between R and AWS"
keywords: "docker,images, container, environments, virtual, R, cloud computing, virtual machine"
weight: 2
author: Roshini Sudhaharan
draft: false
aliases:
- /run/r-in-the-cloud
- /run/r-on-aws
- /reproduce/rstudio-on-aws

---

# Run RStudio on AWS using Docker

Seeking to run R in the cloud? Use this easy step-by-step guide to get started!

## Overview

While cloud services like [Amazon Web Services (AWS)](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/cloud-computing/) are great for big data processing and storage, it doesn’t give you immediate access to tools like R and RStudio. With [Docker](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/docker/), though, you can launch R and RStudio on AWS without trouble.

What are the benefits? 
- Avoid dependency issues and foster reproducible research
- Specify software versions which always work, regardless of which operating system you use
- Setup virtual computers for your colleagues - so that they can work as productively as you do!

{{% tip %}}

In this building block, we use DockerHub -- a hosted repository service like GitHub enabling you to find and share pre-built container images. These images contain application code, libraries, tools, dependencies and other files required to run applications. [Check out DockerHub](https://hub.docker.com/) to see what other amazing things you can build, or follow this building block to launch R on AWS.

{{% /tip %}}

## Steps to launch R on Amazon Web Services (AWS)

### Steps 1-3: Configure AWS instance for using Docker

1. [Launch and connect to an AWS instance](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/launch-instance/)

2. Install `docker` on the instance:
{{% codeblock %}}
```bash
# Update the packages on your instance
$ sudo yum update -y
# Install Docker
$ sudo amazon-linux-extras install docker
# Start the Docker Service
$ sudo service docker start
# Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
$ sudo usermod -a -G docker ec2-user
```
{{% /codeblock %}}

3. Install `docker-decompose` on the instance:

{{% codeblock %}}
```bash
# Copy the appropriate docker-compose binary from GitHub:
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# Fix permissions after download:
sudo chmod +x /usr/local/bin/docker-compose

#Verify if download was successful:
docker-compose version
{{% /codeblock %}}

### Steps 4-7: Run and configure your Docker image

4. [Move the R scripts or folder you'd like to run from your local machine to the AWS instance](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/move-files/)

{{% tip %}}
Remember to disconnect from the instance before proceeding to step 5 and execute the step on your local machine.
{{% /tip %}}


5.  Obtain docker template for running R on AWS

- [Fork this repo](https://github.com/shrabasteebanerjee/r-causalverse.git)

- Edit the `source` directory and `password` docker-compose.yml file. The source directory will contain the filepath of the folder containing all the R scripts you’d like to run on the AWS instance. Finally, set a password which serves as the log in password of RStudio once launched.

{{% tip %}}
The source directory should be based on the EC2 machine and not your local machine, i.e. assume the filepath after transferring the file/folder to the instance.  E.g. `/home/ec2-user/< FOLDER OR FILE NAME>`
{{% /tip %}}

- Re-connect to the instance and move this folder containing the docker-compose.yml file or just the docker-compose.yml file to the instance.

6. Pull the image from docker hub:
{{% codeblock %}}
```bash
docker pull shrabastee/r-causalverse:latest
{{% /codeblock %}}
{{% tip %}}
Got a permission denied error while trying to connect to the Docker daemon socket?

Run `sudo chmod 666 /var/run/docker.sock` on the command line and retry!
{{% /tip %}}

7. Run and configure docker image:
{{% codeblock %}}
```bash
docker-compose -f docker-compose.yml run --name rstudio --service-ports rstudio
```
{{% /codeblock %}}

{{% tip %}}
Make sure to change directory to the location of the docker-compose.yml file before executing the command above.
{{% /tip %}}

### Steps 8-9: Configure security group and launch R
8. Open the `8787` web server port on EC2
- Go to AWS management console and security groups
![](../img/open-portal1.gif)

- Edit inbound rules: IP version = IPv4; Type = Custom TCP; Port range = `8787`
![](../img/open-portal3.gif)


9. Launch R
- Copy the Public IPv4 DNS address for instance IP
- Open a new tab in your browser and paste the URL, including the port number, for example: `http://<instance IP>:8787`
![](../img/open-r.gif)

- To login, enter `rstudio` as username and the password specified earlier in the docker-compose file.
