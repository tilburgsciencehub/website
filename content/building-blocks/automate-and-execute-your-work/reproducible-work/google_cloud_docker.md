---
title: "Import and Run a python environment on Google cloud with Docker" 
description: "Learn how to import and run a python environment on google cloud with docker"
keywords: "docker, images, container, environments, virtual, Python, Jupyter, Jupyter notebook, environment, google cloud, cloud"
weight: 2
author: Diego Sanchez Perez
draft: false
aliases:


---

# Import and Run a python environment on Google cloud with Docker

Take advantage of the versatility of containerized apps on Docker and the power of Google cloud to easily reproduce and collaborate on projects! 

{{% summary %}}

In this building block you will learn step by step how to replicate a Jupyter notebook Python environment from an existing project using Docker on an existing Google cloud instance. 

{{% /summary %}}

{{% warning %}}

In order to be able to follow this building block you will need that the project you want to import already provides a both dockerfile and a docker-compose.yml file, with the adequate information to run the latter.

{{% /warning %}}

### Step 0: 

### Step 1: Install and Set up docker in a Google cloud instance

Unless you have specified it otherwise, at the time of creating your instance Google cloud will use an image of the Debian Linux distribution as base OS for the instance. Accordingly you will have to follow the instructions' on how to install the docker engine for this specific Linux distribution. If you want to check a more detailed step-by-step version of these you can visit [the offical Docker documentation](https://docs.docker.com/engine/install/debian/), where you will also find instructions for installing docker on other Linux distributions and operative systems through the command line. If on the contrary you prefer to cut it straight to the chase, you can simply execute one by one the code lines below on your instance's command line to have Docker installed on your instance.

{{% codeblock %}}
```bash
# Build a Docker image

#1
$ sudo apt-get remove docker docker-engine docker.io containerd runc

#2
$ sudo apt-get update

#3
$ sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

#4
$ sudo mkdir -p /etc/apt/keyrings

#5
$ curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

#6
$ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#7
$ sudo apt-get update

#8
$ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

#9
$ sudo docker run hello-world

```
{{% /codeblock %}}

The last line of the code above (`$ sudo docker run hello-world`) is meant to act as a check to see if the installation was completed successfully. The command line output after running it will tell you if this was the case.

<p align = "center">
<img src = "../img/output_dock_install.png" width="750">
<figcaption> If the installation was successful the final command line output should look similar to this!</figcaption>
</p>

### Step 2: Build the environment's image from a Dockerfile

Once you have Docker installed and working, the first thing you'll need to import your environment is a [Dockerfile](https://docs.docker.com/engine/reference/builder/). A Dockerfile provides Docker with the necessary indications to produce a Docker image, each of the instances of an image is known as a container. 

{{% tip %}}

You can think of the Docker image as a template of our environment, and the Dockerfile as the manual with instructions on how to build this template. This template can be used to generate containers, and containers can be thought of as instantiations (or, instances) of the template. So, each time you tell Docker to generate a new container from the image, it generates a new replica of the environment from the template you previously provided

{{% /tip %}}

First you will need to upload your dockerfile to the instance. In Google cloud's browser SSH the easiest way to do this is to click on the "Upload file" button located close to the top right corner of the interface. There you will be able to select the files you want to upload from your local machine and these will be transfered to the instance. 

{{% tip %}}

Recently uploaded files will be placen in your current directory at the moment of the upload

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
 
Do not forget to include the dot at the end of the code block above as it indicates Docker that it has look for your dockerfile in current directory.

{{% /warning %}}

With this command Docker will build the images and its context, being the latter comprised of all the files located in the same path as your dockerfile. As a result of this it is generally advised to place your dockerfiles in a directory with just the files it requires in order to ensure the building process is as efficient as posible. If you want to learn more about the build command and its options you can visit [this site](https://docs.docker.com/engine/reference/commandline/build/).

{{% tip %}}
 
You can  assign a name (i.e. tag) to your new Docker image by addign to the code above the flag "-t" followed by the name you want to assign in between of the build command and the dot at the end as shown in the code block below. 

Don't worry if you don't include this information as in that case docker will automatically assign a name to the image. However specifying a name is advisable as it will allow you to identify your images more easily.

You can view a list of all your docker images in your Docker Desktop dashboard or by typing `docker images` in the command line.

{{% /tip %}}

{{% codeblock %}}
```bash
# Build a Docker image and assign a name to it
$ docker build -t <your-image-name> .
```
{{% /codeblock %}}

### Step 3: Docker compose

Docker compose is a tool within the Docker ecosytem whose main functionality is to coordinate your containers and provide them with the services required to run smoothly. These services include actions such as communication between containers or starting up containers which require aditional instructions to do so. Although this can sound a bit confusing if you are new to Docker (You can learn more about Docker compose [here](https://docs.docker.com/compose/)), the key takeaway is that it will assist and simplify the task of replicating your environment by providing some extra information to Docker about how to do so. Additionally it is worth noting that we could perform these actions manually employing the `docker run` command, however in this way the process not as straightforward.

In the same way that you needed a dockerfile to provide Docker with the necessary instructions to build an image, a docker-compose file is required to tell docker how to provide these services to a (series of) container(s).

{{% tip %}}

Docker compose files must be YAML files, so make sure that your docker compose file is denoted as such with the extension ".yml" 

{{% /tip %}}

Now it is time to upload your Docker-compose in the same way you did it with your dockerfile, and then and excute the following code in the directory where your docker-compose file is located:

{{% codeblock %}}
```bash
# Build the docker image
$ docker compose up 
```
{{% /codeblock %}}

 If the execution of docker-compose (and all its services) was succesful that means that your envorinment is up and running in jupyter and you should see something in your command line that resembles what is shown in the image below.

<p align = "center">
<img src = "../img/jupyter_on.png" width="750">
<figcaption> Typical log of a Jupyter instance, signaling you that the replication of the environment was completed. </figcaption>
</p>

{{% tip %}}

You can also specify which services do you want to run within a docker-compose file by executing the command shown above followed by the name of the service desired: `docker compose up <service-to-be-run>` .

{{% /tip %}}

### Step 4: Expose the port where Jupyter is running to access the environment from your computer

At this point we need to make our instance accesible from the outside. The first element we need for this task is know in which port of our instance is Jupyter running. To know this we just have to take a closer look to the last line of the output shown in the command line after we executed `docker compose up`. At the beggining of the line you should see an address like the one shown below, from there you interested in the four numbers underlined in bluecoming after the internal IP and before the slash. These correspond with the port where Jupyter is running in your instance.

<p align = "center">
<img src = "../img/find_port.png" width="750">
<figcaption> Underlined in blue: The port that you need to expose. </figcaption>
</p>

{{% warning %}}

Note that the port in which your Jupyter environment is running (i.e the four numbers that correspond to those underlined in blue in the previous image) will probably be different to the ones shown in the image above.

{{% /warning %}}

{{% tip %}}

You can actually choose in which port do you want Jupyter to be executed. In the context of this building block this should be done by modifying the docker-compose, where the instructions on how Docker should set up Jupyter for your environment are contained. [Learn more about docker compose.](https://docs.docker.com/compose/)

{{% /tip %}}

Now you should go to back to the Google cloud console and click the button "Set up firewall rules" which is below your instances list. Then click again on the "Create firewall rule" option located towards the upper side of the screen. There you must:

1. Add a name of your choice for the rule (e.g. Jupyter_access_rule)
2. Make sure that traffic direction is set on "Ingress"
3. Introduce "0.0.0.0/0" in the field "Source IPv4 ranges"
4. In the section "Protocols and ports" check "TCP" and then in the box below introduce the four number which correspond to the port where Jupyter is being executed in your instance.

{{% warning %}}

In the point three of the steps listed above you are told to introduce "0.0.0.0/0" in the field "Source IPv4 ranges". Beware the what this means is that your instance will allow connection from any external IP (i.e. any other computer). If you are concerned about the safety risk this involves and/or you know beforehand the list of IP adresses that you want to allow to connect to your instance, you could list them here instead of typing the one-size-fits-all "0.0.0.0/0".

{{% /warning %}}

After completing the fields as described you can go to the bottom and click on "create" to make the firewall rule effective. 

### Step 5: Access to your Jupyter environment

To access the Jupyter environment you have to go back to the Google cloud console list of VM instances and copy your instance's external IP direction. With this information you can open a web browser in your local computer and type in the url bar the following: 
 - `http://< external_ip_address >:< jupyter_port>`

{{% example %}}

Imagine the external IP of your instance is "12.345.678.9" and the port where Jupyter is being executed is the port "1234". In that case you should paste the following url in your browser: http://12.345.678.9:1234

{{% /example %}}

After introducing the url as indicated, you will be directed to your intance's Jupyter landing page. Here Jupyter will request you a token in order to grant you acess. This token can be found in the same output line of your google cloud instance's command line where you look at port were Jupyter is being ran.

<p align = "center">
<img src = "../img/find_token.png" width="750">
<figcaption> Underlined in green: The token to access Jupyter. </figcaption>
</p>

As you can see in the image above, the token consist of a string of randomly generated alphanumeric characters comprising all what comes after the equal sign ("="). 

{{% warning %}}

Note that in the image above the token is not fully depicted. You must copy al the characters that come after the equal sign, which compose a character string which is noticeably larger that the one underlined in green.

{{% /warning %}}

<p align = "center">
<img src = "../img/login_jupyter.png" width="750">
<figcaption> Jupyter landing page. </figcaption>
</p>

Now simply introduce this token in the box at the top of the landing page and click on "Log in" to access to your environment.

{{% tip %}}

You can also paste your token  in the "Token" box at the bottom at the page and generate a password with it by creating a new password in the "New Password" box. This way the next time you revisit your environment you will not need the full token, instead you could log in using your password, which is specially useful in case you lose access to your token or this is not available to you at the moment.

{{% /tip %}}

















