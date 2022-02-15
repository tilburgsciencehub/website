---
title: "Docker for Reproducible Research"
description: ""
keywords: "docker, images, container, environments, virtual"
weight: 2
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
- /setup/docker
---

## What is Docker?
[Docker](https://www.docker.com/) is the most common (and is also open-source) version of containerisation, i.e. a form of virtualisation where applications run in isolated **containers**, while using a shared operating system (Linux in Docker's case).

What are containers?  <cite>"A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another"[1]</cite>.  Hence, everything that is needed to run your project (e.g. python, R, packages...) is encapsulated and isolated into a container. This container is abstracted from the host operating system (OS) with only access to the binaries, libraries, configuration and dependencies that are built into such a container.

In a nutshell, it's like having a **lightweight virtual machine** that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

### Why should you use Docker?
Say goodbye to "*but it works on my computer*", embrace the power of containerisation:

{{% tip %}}
- **Holy grail of replicability**:

  - Can specify software versions (e.g. python 3.9 or even the OS)
  - **Will always run the same** (and will be able to run) regardless of the infrastructure for instance, regardless of the OS. Thus, more replicable than using [software environments](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/software-environments/) such as via Conda

- **Increased portability and efficiency over VMs**:
  - Less overhead during startup and no need to set up a separate guest OS for each application.
  - Containers take up less space than VMs, they have just the necessary.  
{{% /tip %}}

### Setup Docker
The Docker Engine can be easily installed following these steps for [Linux (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/), [MacOS](https://docs.docker.com/desktop/mac/install/) and [Windows](https://docs.docker.com/desktop/windows/install/).


#### Verify your Installation
Once installed, verify your installation works correctly by running `docker run hello-world` on your terminal. You should get the following:

<img src="../verify-installation.png" width="600" alt="centered image"/>

Now that Docker is up and running, let's start with the basics

### Docker basics

#### Jargon
- **Images**

- **Containers**

#### Main commands
- `docker build`

- `docker run`



{{% warning %}}
 Every time you modify or move a file the container will have to be rebuilt before running it again. Otherwise, the modifications made in the local machine will not be updated into the container.
{{% /warning %}}
## Running an R script in docker

## Running a Python script in docker

## Multiple languages in a single container
Up until now, we created containers that started from either a Python or an R image. This limits our container to running only R or python scripts, respectively. Some images have already been built to run both python and R, for example this [docker image](https://hub.docker.com/r/jupyter/datascience-notebook). However, in a regular work environement you might be using both python and R along with other languages. In this sense, we can start from a more general image e.g. Ubuntu and add layers to the docker image so that it can run R, Python and whichever language we require in a single container.

### Example repository
How can we do this? Let's create an example repository and name it for instance, "**docker_rpy**". The directory structure is the following:

```text
docker_rpy
│
├── code
│   ├── packages.R  ....................... necessary packages to run R script
│   ├── r-script.R  ....................... creates a histogram
│   ├── pyscript.py ....................... draws random normal sample
│   ├── requirements.txt .................. library needed for pyscript
│   └── instruction.sh .................... shell instruction to run both scripts
├── data
│   
└── output
│
└── Dockerfile
```

### The Scripts

{{% codeblock %}}
```shell script
#!/bin/sh
python code/pyscript.py
#!/bin/sh
Rscript code/r-script.R
```
```Python
# Create a normal random sample
import numpy as np
mu, sigma = 0, 0.1
np.random.seed(1)
data = np.random.normal(mu, sigma, 1000)
# save it
np.savetxt('data/data.csv', data, delimiter=',', header='X')
```

```R
# import data
library(readr)
data <- read.csv("data/data.csv")
Z <- as.matrix(data)
# create a histogram and save it to output folder
png("output/histogram.png")
histogram <- hist(Z)
dev.off()
```

{{% /codeblock %}}

As per `packages.R` and `requirements.txt`, the first one installs the `readr` package and the latter installs the `NumPy` library, which are the only packages required to run the above python and R scripts.

### The Dockerfile
{{% codeblock %}}
```dockerfile
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
 python3.9 python3-dev python3-pip r-base
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set container directory
WORKDIR /docker_rpy
# Copy files and directory structure
COPY . .
# Get necessary packages
RUN pip3 install -r code/requirements.txt
RUN Rscript code/packages.R
# Run
CMD code/instruction.sh
```
{{% /codeblock %}}

Line-by-line, the Dockerfile intructs the following:

- Starts from the **lastest Ubuntu image** available

- Suppresses the prompts for choosing your location during the R install

- Updates the `apt-get`: to install available updates of all packages currently installed

- Include **essential installation packages for Ubuntu**, installing only the recommended (and not suggested) dependencies

- Downloads **python version 3.9** and allows **pip** to be used to install the requirements

- Sets the path for python usage inside the container

- **Sets the working directory** for the container and **copies all files** into it, using the same structure as in the local machine

- **Installs necessary python libraries** from the `requirements.txt` file and the necessary **R packages** from the file `packages.R`

- Sets `instruction.sh` as the command to run

### Running the container
Let's first build the container from the current working directory where the Dockerfile is (`.`):
```bash
docker build -t myname/myimage .
```
This can take a few minutes. Once built, we run the container by typing in
```bash
docker run -it --rm  -v "PATH on local computer":"container path" myname/myimage
```
In this example, the container path was set to "**/docker_rpy**" in the dockerfile.


```text
docker_rpy
│
├── code
│   ├── packages.R
│   ├── r-script.R
│   ├── pyscript.py
│   ├── requirements.txt
│   └── instruction.sh
├── data
│    └── data.csv ......................... data generated from pyscript.py
├── output
│    └── histogram.png .................... histogram obtained from r-script.R
│
└── Dockerfile
```
## Additional Resources  

1. Complete handbook on Docker: [The Docker Handbook](https://docker-handbook.farhan.dev/)

2. Docker tutorial for beginners: [Docker curriculum](https://docker-curriculum.com/)

3. [R script in Docker tutorial](https://www.r-bloggers.com/2019/02/running-your-r-script-in-docker/)

4. Easy interactive tutorial on combining [Docker and Makefiles](https://www.katacoda.com/ben_hall/scenarios/1)

5. Tutorial on [Docker for Data Science](https://www.robertmylesmcdonnell.com/content/posts/docker/)

6. Information on [containerisation](https://www.citrix.com/en-in/solutions/app-delivery-and-security/what-is-containerization.html?gclid=Cj0KCQiAu62QBhC7ARIsALXijXQK8FhkYuNqzmXxWwMzjp_04rp7iK-d6i0xXdSdS04_rzEffJiQUkEaApNGEALw_wcB&gclsrc=aw.ds)

[1]:Docker.com ["What is a container"](https://www.docker.com/resources/what-container)
