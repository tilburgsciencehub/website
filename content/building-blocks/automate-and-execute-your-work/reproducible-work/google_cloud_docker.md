---
title: "Import and run a Python environment on Google cloud with Docker" 
description: "Learn how to import a containerized python environment with docker, run it on a google cloud instance and connect it with Google cloud storage buckets"
keywords: "Docker, environment, Python, Jupyter notebook, Google cloud, cloud computing, cloud storage "
weight: 2
author: "Diego Sanchez Perez"
authorlink: "https://www.linkedin.com/in/diego-s%C3%A1nchez-p%C3%A9rez-0097551b8/"
draft: false
date: 2022-10-11T22:01:14+05:30
aliases: 
  - /run/jupyter-on-cloud


---

## Import and run a Python environment on Google Cloud with Docker

Take advantage of the versatility of containerized apps on Docker and the power of Google Cloud to easily reproduce and collaborate on projects! In this building block, you will learn step-by-step how to reproduce a containerized project environment on a Google Cloud virtual machine. Moreover, you will also see how to run Jupyter Notebook in your replicated environment and access to it so you can work with the project's Python code. 

{{% warning %}}

This building block is meant to be a complement to our previous one on [how to export project environments with Docker](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/dockerhub/). Thus, while the steps here presented are valid is a general sense, its details were designed to match the particularities of the containerization process described in the preceding building block. We strongly recommend you to [visit that other building block](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/dockerhub/) to get a firmer understanding of the present one's content.

{{% /warning %}}

### Step 1: Install and Set up Docker in your Google cloud instance

Google Cloud's virtual machines are configured to operate on Debian Linux by default. As a result, installing Docker on these machines follows the standard procedures for Linux-based systems. You can learn how to do so by visiting our building block on how to [Set up Docker](https://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/docker/), which covers the setup of Docker in Windows, MacOS and Ubuntu Linux.

For those who prefer a more streamlined approach, we have condensed these instructions into two Docker installation scripts available below. These scripts work for Debian and Ubuntu Linux, which are among the most commonly used Linux distributions on Google Cloud's virtual machines. Feel free to either follow these scripts step-by-step, or save them in a shell script format file (`.sh`) to upload and execute them on your virtual machine. Either method will successfully install Docker on your VM and thus allow you to continue with this building block!

{{% cta-primary-center "Script for installing Docker in Debian Linux" "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/building-blocks/automate-and-execute-your-work/reproducible-work/install-docker-debian.sh" %}}

{{% cta-primary-center "Script for installing Docker in Ubuntu Linux" "https://raw.githubusercontent.com/tilburgsciencehub/website/master/content/building-blocks/automate-and-execute-your-work/reproducible-work/install-docker-ubuntu.sh" %}}

{{% warning %}}

Docker's setup process differs slightly accros Linux distributions, so make sure to follow the appropriate instructions for your distribution whether it is Ubuntu, Debian, or any other. If your Google Cloud VM is not running in any of these distributions, check [the official Docker documentation](https://docs.docker.com/engine/install/debian/) which provides guidelines for installing Docker in many different Linux distributions.

{{% /warning %}}

<p align = "center">
<img src = "../img/output_dock_install.png" width="750">
<figcaption> If the installation was successful the final command line output should look similar to this!</figcaption>
</p>

{{% tip %}}

To run `docker` commands on your VM after following the Docker setup steps provided above, you will always have to do so alongside the `sudo` command. To avoid this, you can execute the code provided in the code block below. 

{{% /tip %}}

{{% codeblock %}}
```bash
# Add your user to the `docker`` command group
# to get rid of the need to `sudo` to handle Docker

usermod -aG docker your-user-name

newgrp docker
```
{{% /codeblock %}}

### Step 2: Build the environment's image from a Dockerfile

Once you have Docker successfully installed and working, the first thing you'll need to import your environment is a [Dockerfile](https://docs.docker.com/engine/reference/builder/). A Dockerfile provides Docker with the necessary indications to produce a Docker image, each of the instances of an image is known as a container. 

{{% tip %}}

You can think of the Docker image as a template of our environment, and the Dockerfile as the manual with instructions on how to build this template. This template can be used to generate containers, and containers can be thought of as instantiations (or, instances) of the template. So, each time you tell Docker to generate a new container from the image, it generates a new replica of the environment from the template you previously provided

{{% /tip %}}

First, you will need to upload your dockerfile to the instance. In Google Cloud's browser SSH the easiest way to do this is to click on the "Upload file" button located close to the top right corner of the interface. There you will be able to select the files you want to upload from your local machine and these will be transferred to the instance. 

{{% tip %}}

Recently uploaded files will be placed in your current directory at the moment of the upload

{{% /tip %}}


<p align = "center">
<img src = "../img/upload_base.png" width="700">
<figcaption> Locate the upload button in Google cloud's browser SSH</figcaption>
</p>

Upon having uploaded the dockerfile you can run the following code to tell Docker to build the image from it:

{{% codeblock %}}
```bash
# Build a Docker image 
$ docker build .
```
{{% /codeblock %}}

{{% warning %}}
 
Do not forget to include the dot at the end of the code block above as it indicates to Docker that it has to look for your dockerfile in the current directory.

{{% /warning %}}

With this command, Docker will build the image alongside its context, the latter comprised of all the files located in the same path as your dockerfile and which are relevant to the image. In the context of a research project whose environment is being reproduced with Docker, this would generally imply that you should place all the files which are relevant to your project's environments in the same directory as the dockerfile. However, this is highly dependent on the structure of the dockerfile and the particularities of the project. The safest approach is to follow each project's instructions on how to reproduce its environment through Docker.

{{% tip %}}
 
You can assign a name (i.e. tag) to your new Docker image by adding to the code above the flag "-t" followed by the name you want to assign in between the build command and the dot at the end as shown in the code block below. 

Don't worry if you don't include this information as in that case, Docker will automatically assign a name to the image. However, specifying a name is advisable as it will allow you to identify your images more easily.

You can view a list of all your docker images in your Docker Desktop dashboard or by typing `docker images` in the command line.

{{% /tip %}}

{{% codeblock %}}
```bash
# Build a Docker image and assign a name to it
$ docker build -t <your-image-name> .
```
{{% /codeblock %}}

### Step 3: Docker compose

Docker compose is a tool within the Docker ecosystem whose main functionality is to coordinate your containers and provide them with the services required to run smoothly. These services include actions such as communication between containers or starting up containers that require additional instructions to do so. Although this can sound a bit confusing if you are new to Docker (You can learn more about Docker compose [here](https://docs.docker.com/compose/)), the key takeaway is that it will assist and simplify the task of replicating your environment by providing some extra information to Docker about how to do so. Particularly, in this context, the Docker-compose file will be in charge of the following two "services":

1. Connect your environment's container with the rest of your system to make it possible to move files from one to the other.
2. Launch jupyter notebook.

{{% tip %}}

Docker compose files must be YAML files, so make sure that your docker-compose file is denoted as such with the extension ".yml" 

{{% /tip %}}

Now it is time to upload your Docker-compose in the same way you did it with your dockerfile, and then execute the following code in the directory where your docker-compose file is located:

{{% codeblock %}}
```bash
# Build the docker image
$ docker compose up 
```
{{% /codeblock %}}

{{% tip %}}

If your environment's `dockerfile` is hosted on Dockerhub you don't need to manually build it as explained in Step 2 of this building block. Instead, you could just run its associated docker-compose as shown above and Docker will take care of the rest automatically, pulling the image from Dockerhub, building it, and finally executing the instructions included in the docker-compose itself.

{{% /tip %}}

If the execution of docker-compose was successful that means that your environment's container is up and with Jupyter Notebook running. In such case you should see something in your command line resembling the following:

<p align = "center">
<img src = "../img/jupyter_on.png" width="750">
<figcaption> Typical log of a Jupyter Notebook instance, signaling it is running successfully. </figcaption>
</p>

### Step 4: Expose the port where Jupyter Notebook is running to access the environment from your computer

At this point, you need to make the Jupyter Notebook running on your container accessible from the outside. The first element we need for this task is to know in which port of your instance is it running. To know this we just have to take a closer look at the last line of the output shown in the command line after having executed `docker compose up`. At the beginning of the line, you should see an address like the one shown below, from there you are interested in the four digits underlined in blue coming after the internal IP and before the slash. These correspond with the port where Jupyter Notebook is running in your instance.

<p align = "center">
<img src = "../img/find_port.png" width="750">
<figcaption> Underlined in blue: The port that you need to expose. </figcaption>
</p>

{{% warning %}}

Note that the port in which your container's Jupyter notebook is running (i.e. the four-digit number that corresponds to that underlined in blue in the previous image) will probably be different from the one shown in the image above.

{{% /warning %}}

{{% tip %}}

It is possible to adjust the port in which you want Jupyter Notebook to be executed. In the context of this building block, this is defined by the instructions contained in the environment's docker-compose. [Learn more about docker-compose.](https://docs.docker.com/compose/)

{{% /tip %}}

Now you should go back to the Google cloud console and click the button "Set up firewall rules" which is below your instances list. Then click again on the "Create firewall rule" option located towards the upper side of the screen. There you have to:

1. Add a name of your choice for the rule (e.g. Jupyter_access_rule)
2. Make sure that traffic direction is set on "Ingress"
3. Indicate to which of your instances you want this rule to apply by selecting "Specified target tags" in the "Targets" drop-down list, and then specify the names of these in the "Target tags" box below. Alternatively, you can select the option "All instances in the network" in the drop-down menu so the rule automatically applies to all your instances. 
4. Introduce "0.0.0.0/0" in the field "Source IPv4 ranges"
5. In the section "Protocols and ports" check "TCP" and then in the box below introduce the four-digit number that identifies the port where Jupyter Notebook is being executed in your instance.

{{% warning %}}

In point three of the steps listed above you are told to introduce "0.0.0.0/0" in the field "Source IPv4 ranges". Beware that what this means is that your instance will allow connections from any external IP (i.e. any other computer). If you are concerned about the safety risk this involves and/or you know beforehand the list of IP addresses that you want to allow to connect to your instance, you could list them here instead of typing the one-size-fits-all "0.0.0.0/0".

{{% /warning %}}

After completing the fields as described you can go to the bottom and click on "create" to make the firewall rule effective. 

### Step 5: Access Jupyter Notebook within your environment's container

To finally access the Jupyter Notebook running inside your environment's container you have to go back to the Google Cloud console list of virtual machine instances and copy your instance's external IP direction. With this information, you can open a web browser on your local computer and type the following in the URL bar: 
 - `http://< external_ip_address >:< jupyter_port>`

{{% example %}}

Imagine the external IP of your instance is "12.345.678.9" and the port where Jupyter is running is port "1234". In that case, you should paste the following URL into your browser: http://12.345.678.9:1234

{{% /example %}}

After introducing the URL as indicated, you will be directed to your instance's Jupyter Notebook landing page. Here Jupyter will request you a token to grant you access. This token can be found in the same output line of your Google Cloud instance's command line where you look at the port where Jupyter is being run.

<p align = "center">
<img src = "../img/find_token.png" width="750">
<figcaption> Underlined in green: The token to access Jupyter Notebook. </figcaption>
</p>

As you can see in the image above, the token consists of a string of alphanumeric characters comprising all that comes after the equal sign ("="). 

{{% warning %}}

Note that in the image above the token is not fully depicted. You must copy all the characters that come after the equal sign, which compose a character string that is noticeably larger than the one underlined in green.

{{% /warning %}}

<p align = "center">
<img src = "../img/login_jupyter.png" width="750">
<figcaption> Jupyter landing page. </figcaption>
</p>

Now simply introduce this token in the box at the top of the landing page and click on "Log in" to access your environment.

{{% tip %}}

You can also paste your token in the "Token" box at the bottom of the page and generate a password with it by creating a new password in the "New Password" box. This way the next time you revisit your environment you will not need the full token, instead, you will be able to log in using your password. This is particularly useful in case you lose access to your token or this is not available to you at the moment.

{{% /tip %}}

















