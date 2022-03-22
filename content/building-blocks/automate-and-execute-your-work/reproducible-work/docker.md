---
title: "Docker for Reproducible Research"
description: "Holy Grail of replicability: Say goodbye to *but it works on my computer*, embrace the power of containerization."
keywords: "docker, images, container, environments, virtual"
weight: 2
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
- /setup/docker
---

## Why should you use Docker?

When publishing an academic paper, for **reproducibility verification** reasons, you are usually required to provide the code and data you have obtained your results. The results may work on your computer, but once the code is sent to someone else, it no longer reproduces the analysis results. The reasons behind this can be many (e.g., different software versions, different operating systems). In other cases, there might indeed be an issue. Reporting back the exact problem so that it can be fixed can be somewhat complicated, especially if the reviser and author do not work with a common environment.

Because [Docker](https://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/docker/) encapsulates everything that is needed for a project (e.g., Python, R, ...) and isolates it into containers (i.e., abstracting it from the host operating system), all of the issues mentioned above are solved. With Docker, you don't even need to have the program or the same version in which the project works installed to run the workflow. Thus, the “but-it-works-on-my-machine” argument is now either "it works in any machine, or it doesn't." Great, right?

{{% tip %}}
Still haven't downloaded Docker? Check our [building block](https://tilburgsciencehub.com/building-blocks/configure-your-computer/automation-and-workflows/docker/) on how to get Docker up and running.
{{% /tip %}}

## Docker basics

### Dockerfiles
The `dockerfile` is a text file (no file extension!) containing the code that will be executed to produce a new Docker image, where the container will be run. The basic structure of a `dockerfile` is the following:

```dockerfile
FROM "base image:version"
RUN "additional packages required to run the image"
COPY "add files to be used into the container"
CMD "default command to be executed"
```
- The `FROM` instruction sets the base image upon which the container will be based. A **base image** is one that has no parent image (e.g., typically an operating system such as ubuntu or debian). Base images can either be:

  - **Official images**: are maintained and supported by Docker. These are, for instance, `ubuntu`, `python`, `hello-world`. For example, check out some R images [here](https://hub.docker.com/search?q=RStudio&type=image).

  - **User images**: are created and shared by any user. Usually, they add additional functionality to a base image, and their file names are formatted as `user/image-name`.

- `RUN` adds layers to the base image. It allows to install additional packages needed for your Docker image to run smoothly.

- `COPY` allows you to copy your local machine's directory structure into the image and/or add the necessary files, e.g., scripts.

- `CMD` is used to set the default command to be executed when running the container. There can only be one `CMD` command per Dockerfile. Otherwise, only the last `CMD` command will run. 

  - If you want to define a container with a specific executable, it might be better to use `ENTRYPOINT` instead of `CMD`. You can find more information on `ENTRYPOINT` [here](https://docs.docker.com/engine/reference/builder/#entrypoint).


{{% tip %}}
Dockerfiles can be written in any text editor, such as [Visual Study Core](https://code.visualstudio.com/), which is especially popular when working with Docker because of its official docker extension. This extension has some excellent features such as debugging and auto-completion, making things a lot easier.
{{% /tip %}}

### Let's first learn some theory - Docker 101

Once the Dockerfile is ready to go, the first step is to build the image from the Dockerfile. To do so, you will have to make use of the following command in your terminal:
  - `docker build -t myname/myimage .`

Once the image is built, you can run it in a container by typing in:
 - `docker run myname/myimage`

These are the two basic steps to creating and running an image inside a container. Now we're ready to get hands-on experience.

{{% tip %}}
  - For further information on image and container manipulation, check out this [handbook](https://docker-handbook.farhan.dev/container-manipulation-basics)

  - Do you need further help with the basics or want to slow down the pace? Take a look at this [Docker curriculum](https://docker-curriculum.com/)

  - Running `CMD` in Docker but getting an error message? It could be your execution script cannot be read. Set its file permissions using `chmod +x src/run.sh`. See also [here](https://serverfault.com/questions/967580/chmod-changing-permissions-of-myscript-sh-operation-not-permitted).
  
{{% /tip %}}

## Let's dockerize a research workflow that runs both Python and R

In many empirical research projects, we can use R, Python, or both. The best thing is that these packages are free (i.e., you can run them anywhere without purchasing a license). In this application, we start from a very basic image (Ubuntu) and then add the required layers of R and Python to the image. 

{{% tip %}}

Want to run a container-based solely on an R image? Check out the following:
-  Tutorial on running an [R script in Docker](https://www.r-bloggers.com/2019/02/running-your-r-script-in-docker/)
- Our [dockerized R application](https://github.com/tilburgsciencehub/keywords-finder) that finds keywords and/or sentences from PDF files  
{{% /tip %}}

### Example repository

How can we do this? Let's create a simple repository that...
- generates a dataset drawn from a normal random sample using the `NumPy` library in Python, 
- saves the data in a `data` directory and obtains a histogram from such data in R (saving it in the `gen` folder).

All these steps are run with one shell script. Let's name our workflow "**docker_rpy**" for now and structure it in the following manner.

[__Check out the complete code base on GitHub__](https://github.com/tilburgsciencehub/docker-demo).

```text
docker_rpy
│
├── code
│   ├── packages.R  ....................... necessary packages to run the R script
│   ├── r-script.R  ....................... creates a histogram, saves it in \gen folder
│   ├── pyscript.py ....................... draws random normal sample, saves it in \data folder
│   ├── requirements.txt .................. library needed for pyscript
│   └── run.sh ............................ shell instruction to run both scripts
├── data
│   
└── gen
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
data <- read.csv("data/data.csv")
Z <- as.matrix(data)
# create a histogram and save it to output folder
dir.create('gen')
png("gen/histogram.png")
histogram <- hist(Z)
dev.off()
```

{{% /codeblock %}}

- As per `packages.R` and `requirements.txt`, the first one installs the `MASS` package (it's not really needed and just kept here for a demo...), and the latter installs the `NumPy` library used in the `.py` script.

### The Dockerfile
{{% codeblock %}}
```dockerfile
# Define base image/operating system
FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

# Install software
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
 python3.9 python3-dev python3-pip r-base
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set container's working directory
WORKDIR /docker_rpy

# Copy files and directory structure to working directory
COPY . .

# Install necessary packages for Python and R
RUN pip3 install -r src/requirements.txt
RUN Rscript src/packages.R

# Run commands specified in "instruction.sh" to get started
ENTRYPOINT ["sh", "src/run.sh"]
```
{{% /codeblock %}}

Line-by-line, this Dockerfile instructs the following:

- Starts from the **lastest Ubuntu image** available as the base image

- Suppresses the prompts for choosing your location during the R install

- Updates the `apt-get`: to install available updates of all packages currently installed

- Include **essential installation packages for Ubuntu**, installing only the recommended (and not suggested) dependencies

- Downloads **python version 3.9** and allows **pip** to be used to install the requirements

- Sets the path for python usage inside the container

- **Sets the working directory** for the container and **copies all files** into it, using the same structure as in the local machine

- **Installs necessary python libraries** from the `requirements.txt` file and the necessary **R packages** from the file `packages.R`

- Sets `run.sh` as the default command to run

### Running the container

Let's first build the image from the current working directory where the Dockerfile is (`.`) by typing in the following into the terminal:
```bash
docker build -t myname/myimage .
```
  - Here, the `-t` argument makes sure that you get some good formatting and a native terminal-like experience
  - Remember to also copy-paste/type the `.` at the end of the command!

Building the image can take a few minutes. Once built, we run the container based on the image we just created by typing in:
```bash
docker run -it --rm  -v "PATH on local computer":"container path" myname/myimage
```

- The `-it` argument creates an interactive bash shell in the container. For example, use it like: `docker run -it --rm -v "$(pwd)/.:/docker_rpy" myname/myimage`
- The `--rm` argument makes sure the container is automatically removed once we stop it.
- The `-v` or `-volume` argument tells Docker which local folders to map to the created folders inside the container (**/docker_rpy** in this case). This example makes sure that the dataset generated in the `pyscript.py` script and the histogram created in `r-script.R` are saved into the `data` and `gen` folders in the local machine, respectively. Hence, the resulting directory structure should be the following:

    ```text
    docker_rpy
    │
    ├── code
    │
    ├── data
    │    └── data.csv ......................... data generated from pyscript.py
    ├── gen
    │    └── histogram.png .................... histogram obtained from r-script.R
    │
    └── Dockerfile
    ```
    
{{% warning %}}
 Every time you modify or move a file, the container image will have to be rebuilt before rerunning it. Otherwise, the modifications made in the local machine will not be updated into the container.
{{% /warning %}}


## Additional Resources  

1. Complete handbook on Docker: [The Docker Handbook](https://docker-handbook.farhan.dev/)

2. [R script in Docker tutorial](https://www.r-bloggers.com/2019/02/running-your-r-script-in-docker/)

3. Easy interactive tutorial on combining [Docker and Makefiles](https://www.katacoda.com/ben_hall/scenarios/1)

4. Tutorial on [Docker for Data Science](https://www.robertmylesmcdonnell.com/content/posts/docker/)

5. Information on [containerisation](https://www.citrix.com/en-in/solutions/app-delivery-and-security/what-is-containerization.html?gclid=Cj0KCQiAu62QBhC7ARIsALXijXQK8FhkYuNqzmXxWwMzjp_04rp7iK-d6i0xXdSdS04_rzEffJiQUkEaApNGEALw_wcB&gclsrc=aw.ds)

6. [Containerizing a Multi-Container JavaScript Application](https://docker-handbook.farhan.dev/containerizing-a-multi-container-javascript-application)
