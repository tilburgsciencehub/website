---
title: "Docker for Reproducible Research"
description: "Holy Grail of replicability: Say goodbye to *but it works on my computer*, embrace the power of containerisation"
keywords: "docker, images, container, environments, virtual"
weight: 2
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
- /setup/docker
---


## Docker basics

### Dockerfiles
The Dockerfile is a text file with no extension that contains the code that will be executed to produce a new Docker image, where the container will be ran. The basic structure of a Dockerfile is the following:

```dockerfile
FROM "base image:version"
RUN "additional packages required to run the image"
COPY "add files to be used into the container"
CMD "default command to be executed"
```
- The `FROM` instruction sets the base image upon which the container will be based. A **base image** is such that has no parent image, these are usually images at the OS level such as ubuntu or debian. Base images can either be:

  - **Official images**: are maintained and supported by Docker. These are for instance, `ubuntu`, `python`, `hello-world`.

  - **User images**: are created and shared by any user. Usually, they add additional functionality to a base image and are formatted as `user/image-name`.

- `RUN` adds layers to the base image. It allows to install additional packages needed for your Docker image to run smoothly.

- `COPY` allows to copy your local machine's directory structure into the image and/or add the necessary files into it, e.g. scripts.

- `CMD` is used to set the default command to be executed when running the container. There can only be one `CMD` command per Dockerfile, otherwise, only the last `CMD` command will run.

  - If you want to define a container with a specific executable it might be better to use `ENTRYPOINT` instead of `CMD`. You can find more information on `ENTRYPOINT` [here](https://docs.docker.com/engine/reference/builder/#entrypoint)


{{% tip %}}
Dockerfiles can be written in any text editor such as for instance, [Visual Study Core](https://code.visualstudio.com/), which is especially popular when working with Docker because of its official docker extension. This extension has some nice features such as debugging and auto-completion, making things a lot easier.
{{% /tip %}}

### Docker basic usage
Once the Dockerfile is ready to go, the first step is to build the image from the Dockerfile. To do so, you will have to make use of the following command in your terminal:
  - `docker build myname/myimage .`

Once the image is built, you can run it in a container by typing in:
 - `docker run myname/myimage`

These are the two basic steps to creating and running an image inside a container. Now we're ready to get hands on experience.


{{% tip %}}
  - For further information on image and container manipulation check out this [handbook](https://docker-handbook.farhan.dev/container-manipulation-basics)

  - Need further help with the basics or want to slow down the pace? Take a look at this [Docker curriculum](https://docker-curriculum.com/)
{{% /tip %}}

## Dockerise an Ubuntu application that runs both Python and R
In many projects, we can base our image on for instance, a Python or R image. This can be efficient but at the expense of limiting the container to running only R or python scripts, respectively. In this sense, some images have already been built to run both python and R, for example this [docker image](https://hub.docker.com/r/jupyter/datascience-notebook).

However, in a regular work environement you might be using both python and R along with other languages. In this sense, we can start from a more general image e.g. Ubuntu and add layers to the docker image so that it can run R, Python and whichever language we require in a single container.

### Example repository
How can we do this? Let's create a simple repository that generates a dataset drawn from a normal random sample using the NumPy library in Python, saves the data and obtains a histogram from such data in R. All these, instructed from a shell command. Let's name it for instance, "**docker_rpy**" and structure it in the following manner:

```text
docker_rpy
│
├── code
│   ├── packages.R  ....................... necessary packages to run the R script
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
Let's take a look at the scripts that will carry this out:
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

- As per `packages.R` and `requirements.txt`, the first one installs the `readr` package and the latter installs the `NumPy` library, which are the only packages required to run the above python and R scripts.

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

Line-by-line, this Dockerfile intructs the following:

- Starts from the **lastest Ubuntu image** available as the base image

- Suppresses the prompts for choosing your location during the R install

- Updates the `apt-get`: to install available updates of all packages currently installed

- Include **essential installation packages for Ubuntu**, installing only the recommended (and not suggested) dependencies

- Downloads **python version 3.9** and allows **pip** to be used to install the requirements

- Sets the path for python usage inside the container

- **Sets the working directory** for the container and **copies all files** into it, using the same structure as in the local machine

- **Installs necessary python libraries** from the `requirements.txt` file and the necessary **R packages** from the file `packages.R`

- Sets `instruction.sh` as the default command to run

### Running the container
Let's first build the image from the current working directory where the Dockerfile is (`.`) by typing in the following into the terminal:
```bash
docker build -t myname/myimage .
```
  - Here, the `-t` argument makes sure that you get some good formatting and a native terminal like experience

Building the image can take a few minutes. Once built, we run the container based on the image we just created by typing in:
```bash
docker run -it --rm  -v "PATH on local computer":"container path" myname/myimage
```
- The `-it` argument creates an interactive bash shell in the container. `--rm` makes sure the container is automatically removed once we stop it.

- The `-v` or `-volume` argument tells Docker which local folders to map to the created folders inside the container (**/docker_rpy** in this case). In this example, it is making sure that the dataset generated in the `pyscript.py` script and the histogram created in `r-script.R` are saved into the `data` and `output` folders in the local machine, respectively. Hence, the resulting directory structure should be the following:

    ```text
    docker_rpy
    │
    ├── code
    │
    ├── data
    │    └── data.csv ......................... data generated from pyscript.py
    ├── output
    │    └── histogram.png .................... histogram obtained from r-script.R
    │
    └── Dockerfile
    ```
{{% warning %}}
 Every time you modify or move a file, the container image will have to be rebuilt before running it again. Otherwise, the modifications made in the local machine will not be updated into the container.
{{% /warning %}}


## Additional Resources  

1. Complete handbook on Docker: [The Docker Handbook](https://docker-handbook.farhan.dev/)

2. [R script in Docker tutorial](https://www.r-bloggers.com/2019/02/running-your-r-script-in-docker/)

3. Easy interactive tutorial on combining [Docker and Makefiles](https://www.katacoda.com/ben_hall/scenarios/1)

4. Tutorial on [Docker for Data Science](https://www.robertmylesmcdonnell.com/content/posts/docker/)

5. Information on [containerisation](https://www.citrix.com/en-in/solutions/app-delivery-and-security/what-is-containerization.html?gclid=Cj0KCQiAu62QBhC7ARIsALXijXQK8FhkYuNqzmXxWwMzjp_04rp7iK-d6i0xXdSdS04_rzEffJiQUkEaApNGEALw_wcB&gclsrc=aw.ds)

6. [Containerizing a Multi-Container JavaScript Application](https://docker-handbook.farhan.dev/containerizing-a-multi-container-javascript-application)
