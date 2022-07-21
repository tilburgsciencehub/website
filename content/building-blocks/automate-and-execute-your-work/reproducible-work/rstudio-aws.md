---
title: "Run RStudio on AWS using Docker"
description: "Docker - the bridge between R and AWS"
keywords: "docker,images, container, environments, virtual, R, cloud computing, virtual machine"
weight: 2

draft: false
aliases:
- /reproduce/rstudio-on-aws
---
# Docker - The Bridge Between R and AWS

While cloud services like [AWS](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/cloud-computing/) are great for big data processing and storage, it doesn’t automatically give you computing softwares like RStudio. [Docker](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/docker/) is a clean way to launch R on AWS without potential dependency issues and fosters reproducible research, as one can specify software versions which can always be run regardless of the OS in use. [DockerHub](https://hub.docker.com/) is a hosted repository service like GitHub that enables one to find and share container images that are already built. These docker images contain application code, libraries, tools, dependencies and other files required to run the application. This building block elaborates on how to launch R on AWS using a pre-built docker image hosted on dockerhub.

## Steps to launch R on AWS

### Steps 1-3:  Configure AWS instance for Docker

1. [Launch and connect to an AWS instance](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/launch-instance/)

2. Install `docker` on the instance:
```c
# Update the packages on your instance
$ sudo yum update -y
# Install Docker
$ sudo amazon-linux-extras install docker
# Start the Docker Service
$ sudo service docker start
# Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
$ sudo usermod -a -G docker ec2-user
```
3. Install `docker-decompose` command on the instance:

```c
# Copy the appropriate docker-compose binary from GitHub:
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# Fix permissions after download:
sudo chmod +x /usr/local/bin/docker-compose

#Verify if download was successful:
docker-compose version
```
### Steps 4-7: Run and configure Docker image

4. [Move the R scripts or folder you'd like to run from your local machine to the AWS instance](https://tilburgsciencehub.com/tutorials/more-tutorials/running-computations-remotely/move-files/)

**Note:** Disconnect from the instance before proceeding to step 5 and execute the step on your local machine.


5.  Obtain docker template for running R on AWS

- [Fork this repo](https://github.com/shrabasteebanerjee/r-causalverse.git)

- Edit the `source` directory and `password` docker-compose.yml file. The source directory will contain the filepath of the folder containing all the R scripts you’d like to run on the AWS instance. Finally, set a password which serves as the log in password of RStudio once launched.

**Note:** the source directory should be based on the EC2 machine and not your local machine, i.e. assume the filepath after transferring the file/folder to the instance.  E.g. `/home/ec2-user/< FOLDER OR FILE NAME>`

- Re-connect to the instance and move this folder containing the docker-compose.yml file or just the docker-compose.yml file to the instance.

6. Pull the image from docker hub:
```c
docker pull shrabastee/r-causalverse:latest
```
{{% tip %}}
**Potential Error message:**

Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post `http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/create?fromImage=shrabastee%2Fr-causalverse&tag=latest: dial unix /var/run/docker.sock: connect: permission denied`

**Solution:** Run `sudo chmod 666 /var/run/docker.sock` on the command line and retry.
{{% /tip %}}

7. Run and configure docker image:
```c
docker-compose -f docker-compose.yml run --name rstudio --service-ports rstudio
```
**Note:** Make sure to change directory to the location of the docker-compose.yml file before executing the command above.
### Steps 8-9: Configure security group and launch R
8. Open the 8787 web server port on EC2
- Go to AWS management console and security groups
![](../img/open-portal1.gif)

- Edit inbound rules: IP version = IPv4; Type = Custom TCP; Port range = 8787
![](../img/open-portal3.gif)


9. Launch R
- Open a new web window and enter URL: `http://<instance IP> : 8787`
![](../img/open-r.gif)

**Note:** Copy the Public IPv4 DNS address for instance IP

- Enter `rstudio` as username and password as specified in the docker-compose file.
