---
title: "Import and Run a python environment on Google cloud with Docker" 
description: "Learn how to import and run a python environment on google cloud with docker"
keywords: "docker, images, container, environments, virtual, Python, Jupyter, Jupyter notebook, environment, google cloud, cloud"
weight: 2
author: Diego Sanchez Perez
draft: true
aliases:


---

{{% warning %}}

## Some comments on the draft

- I have reproduced the steps I carried out for the docker assignment sent to me as basis for this draft. Though I learned a lot more about Docker during the assignment completion than what is reflected in this draft, I kept it close to the practical steps of being able to run a Python env. from a github repo that alredy provided the Dockerfile and Docker-compose without going too much into details.

- For this building block it has been asumed that the project environment to replicate already contained a dockerfile and docke-compose file in the first place. From this assumption, a reasonable adition to the building block could be a brief explanation on how to interpret a dockerfile and/or a dockercompose file.

- The focus of the building block could be easily reversed from import other's work to export our work if it is extended to include how to elaborate our own dockerfile though I am aware this may be too much information for a single building block. 

- A brief contextualization on docker may be of value for the building block though at the same this is also covered to some extent on other extisting building blocks so instead links to these could be added.

- Potential alternative: Docker DevEnvironments

{{% /warning %}}

# Import a Python environment from Github using Docker

Take advantage of the versatility of containerized apps on Docker to make your work easier to share and reporduce! 

{{% summary %}}

In this building block you will learn step by step how to import a Python environment from an existing project located in a Github repository using Docker.

{{% /summary %}}

## Steps to import the environment in a docker container

### Step 1: Install and Set up docker

For this first step you can check our building block on [how to set up Docker.](https://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/docker/)

### Step 2: Build the environment's image from a Dockerfile

Once you have Docker installed and working, the first thing you'll need to import your environment is a [Dockerfile](https://docs.docker.com/engine/reference/builder/). A Dockerfile provides Docker with the necessary indications to produce a Docker image, each of the instances of an image is known as a container. 

{{% tip %}}

In this case you can think of the Docker image as a model of our environment, and the Dockerfile as the manual on how to build this model. Each time you tell Docker to generate a new container (i.e. instance) of the image, this action would be equivalent to generate a new replica of the enviroment for us to use from the model you previously provided.

{{% /tip %}}

In order to tell Docker to build an image from the provided Dockerfile, open your command terminal in the directory were you have stored your dockerfile and run the following code:

{{% codeblock %}}
```bash
# Build a Docker image 
$ docker build .
```
{{% /codeblock %}}

{{% warning %}}
 
Do not forget to include the dot at the end of the code block above as it indicates Docker that it has look for your dockerfile in current directory.

{{% /warning %}}

{{% tip %}}
 
You can  assign a name to your new Docker image by addign to the code above the flag "-t" followed by the name you want to assign in between of the build command and the dot at the end as shown in the code block below. 

Don't worry if if you don't include this information as in that case docker will automatically assign a name to the image. However specifying a name is advisable as it will allow you to identify your images more easily. If you want to learn more about other options of the "build" command you can check [this link.](https://docs.docker.com/engine/reference/commandline/build/)

{{% /tip %}}

{{% codeblock %}}
```bash
# Build a Docker image and assign a name to it
$ docker build -t your_image_name .
```
{{% /codeblock %}}

### Step 3: Docker compose

Docker compose is a tool within Docker whose main functionality is to coordinate your containers and provide them with the services required to run coherently. Although this can sound a bit confusing if you are new to Docker (You can learn more about Docker compose [here](https://docs.docker.com/compose/)), the key takeaway is that it will assist and simplify the task of replicating your environment by providing some extra information to Docker about how to do so.

In the same way that you needed a dockerfile to provide Docker with the necessary instructions to build an image, a docker-compose file is required to tell docker how to provide these services to a (series of) container(s).

{{% tip %}}

Docker compose files must be YAML files, so make sure that your docker compose file is denoted as such with the extension ".yml" 

{{% /tip %}}

All Docker needs to carry out the instructions contained in our docker-compose file is to open the terminal at the location of our docker-compose file and excute the following code:

{{% codeblock %}}
```bash
# Build the docker image
$ docker compose up
```
{{% /codeblock %}}

## Checking if the environment has been replicated successfully and accessing it.

To check if docker has successfully replicated your environment you can go into your Docker desktop app and click on "containers" in the top left corner. If everything went correctly you should see the icons corresponding to the Docker compose instansce and the container containing your environment colored in green and their status set as "Running".

<p align = "center">
<img src = "../img/Check_status.png" width="750">
<figcaption> This is what you should see on Docker desktop if the operation was successful. </figcaption>
</p>

If this is the case, congratulations! You have succefully replicated your environment with Docker! 

### Option A: Jupyter Notebook

Finally, to access to your environment click on the container and then click again on "logs" at the top right corner of your screen. On the last line of the output you are seeing now you will find a link that will take you directly to your environment in Jupyter.

<p align = "center">
<img src = "../img/Jupyter.png" width="750">
<figcaption> Click on the link signaled to access Jupyter!</figcaption>
</p>

{{% tip %}}

Instead of clicking on the link you can also directly copy it in your browser to enter the local port where the environment is located. If you do this do not forget to also copy the access token generated by Jupyter in order to access directly without needing to introduce it manually.

{{% /tip %}}

### Option B: Visual Studio Code

An alternative option you have to access your environment is to do so with the code editor Visual Studio Code. For this you will have to click on the icon representing the Docker compose instance coordinating our environment and the asociated container(s) (just one  in this case) and Docker will offer you the option to Open your environment in Visual Studio Code.

<p align = "center">
<img src = "../img/VSCode.png" width="750">
<figcaption> Click on the button on the top-right corner to open the environment in VS Code</figcaption>
</p>
















