---
title: "Import and run a Python environment on Google cloud with Docker" 
description: "Learn how to import a containerized python environment with docker, run it on a google cloud instance and connect it with Google cloud storage buckets"
keywords: "Docker, environment, Python, Jupyter notebook, Google cloud, cloud computing, cloud storage "
weight: 2
author: Diego Sanchez Perez
draft: false
aliases: /run/jupyter-on-cloud


---

# Import and run a Python environment on Google cloud with Docker

Take advantage of the versatility of containerized apps on Docker and the power of Google cloud to easily reproduce and collaborate on projects! In this building block you will learn how to replicate a Jupyter notebook Python environment from a project on an existing Google cloud instance using Docker. Additionally you will also learn how to connect your replicated environment directly to Google cloud storage buckets to comfortably save and share your output. 

{{% warning %}}

In order to be able to follow this building block you will need that the project you want to import already provides both  a dockerfile and a docker-compose.yml file, with the adequate information to run the latter.

{{% /warning %}}

### Step 1: Install and Set up docker in a Google cloud instance

Unless you have specified it otherwise, at the time of creating your instance Google cloud will use an image of the Debian Linux distribution as base OS for the instance. Accordingly you will have to follow the instructions on how to install the docker engine for this specific Linux distribution. If you want to check a more detailed step-by-step version of these you can visit [the offical Docker documentation](https://docs.docker.com/engine/install/debian/), where you will also find instructions for installing Docker on other Linux distributions and operative systems through the command line. If on the contrary you prefer to cut it straight to the chase, you can simply execute one by one the code lines below on your instance's command line to get Docker installed.

{{% codeblock %}}
```bash
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
$ sudo groupadd docker 

#10
$ sudo usermod -aG docker <your-user-name>

#11
$ newgrp docker

#12
$ docker run hello-world

```
{{% /codeblock %}}

Code lines #1 to #8 from above deal with the installation of Docker itself, while code lines #9 to #11 are in charge of allowing your user within the instance to handle Docker without security privileges being required every time you use the `docker` command (This is done by adding you username to the Docker group, for more detailed information on these instructions you can visit [the Docker website](https://docs.docker.com/engine/install/linux-postinstall/)). Finally, the last line of the code (#12 - `$ docker run hello-world`) is meant to act as a check to see if the installation was completed successfully. The command line output after running it will tell you if this was the case.

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
 
Do not forget to include the dot at the end of the code block above as it indicates Docker that it has to look for your dockerfile in current directory.

{{% /warning %}}

With this command Docker will build the images and its context, being the latter comprised of all the files located in the same path as your dockerfile. As a result of this it is generally advised to place your dockerfiles in a directory with just the files it requires in order to ensure the building process is as efficient as posible. If you want to learn more about the build command and its options you can visit [this site](https://docs.docker.com/engine/reference/commandline/build/).

{{% tip %}}
 
You can  assign a name (i.e. tag) to your new Docker image by addign to the code above the flag "-t" followed by the name you want to assign in between of the build command and the dot at the end as shown in the code block below. 

Don't worry if you don't include this information as in that case Docker will automatically assign a name to the image. However specifying a name is advisable as it will allow you to identify your images more easily.

You can view a list of all your docker images in your Docker Desktop dashboard or by typing `docker images` in the command line.

{{% /tip %}}

{{% codeblock %}}
```bash
# Build a Docker image and assign a name to it
$ docker build -t <your-image-name> .
```
{{% /codeblock %}}

### Step 3: Docker compose

Docker compose is a tool within the Docker ecosytem whose main functionality is to coordinate your containers and provide them with the services required to run smoothly. These services include actions such as communication between containers or starting up containers which require aditional instructions to do so. Although this can sound a bit confusing if you are new to Docker (You can learn more about Docker compose [here](https://docs.docker.com/compose/)), the key takeaway is that it will assist and simplify the task of replicating your environment by providing some extra information to Docker about how to do so. Additionally it is worth noting that we could perform these actions manually employing the `docker run` command, however in this way the process is not as straightforward.

In the same way that you needed a dockerfile to provide Docker with the necessary instructions to build an image, a docker-compose file is required to tell docker how to provide these services to a (series of) container(s).

{{% tip %}}

Docker compose files must be YAML files, so make sure that your docker compose file is denoted as such with the extension ".yml" 

{{% /tip %}}

Now it is time to upload your Docker-compose in the same way you did it with your dockerfile, and then excute the following code in the directory where your docker-compose file is located:

{{% codeblock %}}
```bash
# Build the docker image
$ docker compose up 
```
{{% /codeblock %}}

 If the execution of docker-compose (and all its services) was succesful that means that your environment is up and running in jupyter and you should see something in your command line that resembles what is shown in the image below.

<p align = "center">
<img src = "../img/jupyter_on.png" width="750">
<figcaption> Typical log of a Jupyter instance, signaling you that the replication of the environment was completed. </figcaption>
</p>

{{% tip %}}

You can also specify which services do you want to run within a docker-compose file by executing the command shown above followed by the name of the service desired: `docker compose up <service-to-be-run>` .

{{% /tip %}}

#### Extra! - Connect the Docker container within your instance to a Google Cloud Storage bucket 

It is likely that your docker compose file provides Docker with the necessary instructions to employ [Docker volumes](https://docs.docker.com/storage/volumes/) to save any output file or data that you produce while working in your environment's container. If this is the case you may be also interested in connecting such volume to Google cloud storage so you don't have to manually download the output to your machine and make it easier to share and make available to your team.

In order to do this, first of all you will need to install [GCSFuse](https://github.com/GoogleCloudPlatform/gcsfuse) in your instance by running the following code:

{{% warning %}}
 
Carry out the following steps while your environment is not running. For that press "ctrl + c" to shut down Jupyter and then run `docker compose stop` in your instance to stop the execution of the container. 

{{% /warning %}}

{{% codeblock %}}
```bash
#1
$ export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

#2
$ sudo apt-get update

#3
$ sudo apt-get install gcsfuse
```
{{% /codeblock %}}

Now navigate to the directory of your instance which is connected to the container by the volume and create a new directory inside of it to be the one connected with your bucket. After you can run the following:

{{% codeblock %}}
```bash
$ sudo gcsfuse -o allow_other your-bucket volume_path/new_dir/
```
{{% /codeblock %}}

This code will tell GCSFuse to syncronize your new directory within the path with your bucket and allow your container to access it. After this you just have to store any output produced in your environment in this new directory that you just created in your instance a few moments ago (Referred in the previous codeblock as "new_dir") and it will be immediatly available to you in your GCS bucket.

{{% tip %}}

Bear in mind that the absolute path to your bucket-sincronized directory is not the same for your instance and for your container given that containers have independent file systems. However its relative path will be the same with respect to that where the Docker volume is mounted.

{{% /tip %}}


### Step 4: Expose the port where Jupyter is running to access the environment from your computer

At this point we need to make our instance accesible from the outside. The first element we need for this task is to know in which port of our instance is Jupyter running. To know this we just have to take a closer look to the last line of the output shown in the command line after we executed `docker compose up`. At the beggining of the line you should see an address like the one shown below, from there you are interested in the four digits underlined in blue coming after the internal IP and before the slash. These correspond with the port where Jupyter is running in your instance.

<p align = "center">
<img src = "../img/find_port.png" width="750">
<figcaption> Underlined in blue: The port that you need to expose. </figcaption>
</p>

{{% warning %}}

Note that the port in which your Jupyter environment is running (i.e the four-digit number that corresponds to that underlined in blue in the previous image) will probably be different to the one shown in the image above.

{{% /warning %}}

{{% tip %}}

You can actually choose in which port do you want Jupyter to be executed. In the context of this building block this should be done by modifying the docker-compose, where the instructions on how Docker should set up Jupyter for your environment are contained. [Learn more about docker compose.](https://docs.docker.com/compose/)

{{% /tip %}}

Now you should go to back to the Google cloud console and click the button "Set up firewall rules" which is below your instances list. Then click again on the "Create firewall rule" option located towards the upper side of the screen. There you have to:

1. Add a name of your choice for the rule (e.g. Jupyter_access_rule)
2. Make sure that traffic direction is set on "Ingress"
3. Introduce "0.0.0.0/0" in the field "Source IPv4 ranges"
4. In the section "Protocols and ports" check "TCP" and then in the box below introduce the four-digit number that identifies the port where Jupyter is being executed in your instance.

{{% warning %}}

In the point three of the steps listed above you are told to introduce "0.0.0.0/0" in the field "Source IPv4 ranges". Beware that what this means is that your instance will allow connections from any external IP (i.e. any other computer). If you are concerned about the safety risk this involves and/or you know beforehand the list of IP adresses that you want to allow to connect to your instance, you could list them here instead of typing the one-size-fits-all "0.0.0.0/0".

{{% /warning %}}

After completing the fields as described you can go to the bottom and click on "create" to make the firewall rule effective. 

### Step 5: Access to your Jupyter environment

To access the Jupyter environment you have to go back to the Google cloud console list of VM instances and copy your instance's external IP direction. With this information you can open a web browser in your local computer and type the following in the url bar: 
 - `http://< external_ip_address >:< jupyter_port>`

{{% example %}}

Imagine the external IP of your instance is "12.345.678.9" and the port where Jupyter is being executed is the port "1234". In that case you should paste the following url in your browser: http://12.345.678.9:1234

{{% /example %}}

After introducing the url as indicated, you will be directed to your intance's Jupyter landing page. Here Jupyter will request you a token in order to grant you acess. This token can be found in the same output line of your google cloud instance's command line where you look at the port were Jupyter is being ran.

<p align = "center">
<img src = "../img/find_token.png" width="750">
<figcaption> Underlined in green: The token to access Jupyter. </figcaption>
</p>

As you can see in the image above, the token consist of a string of randomly generated alphanumeric characters comprising all what comes after the equal sign ("="). 

{{% warning %}}

Note that in the image above the token is not fully depicted. You must copy all the characters that come after the equal sign, which compose a character string which is noticeably larger that the one underlined in green.

{{% /warning %}}

<p align = "center">
<img src = "../img/login_jupyter.png" width="750">
<figcaption> Jupyter landing page. </figcaption>
</p>

Now simply introduce this token in the box at the top of the landing page and click on "Log in" to access to your environment.

{{% tip %}}

You can also paste your token  in the "Token" box at the bottom at the page and generate a password with it by creating a new password in the "New Password" box. This way the next time you revisit your environment you will not need the full token, instead you will be able log in using your password. This is particularly useful in case you lose access to your token or this is not available to you at the moment.

{{% /tip %}}

















