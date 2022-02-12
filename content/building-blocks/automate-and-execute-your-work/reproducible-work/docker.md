---
title: "Docker for Reproducible Research"
description: ""
keywords: "docker, images, container, environments, virtual"
weight: 2
#date: 2021-01-06T22:01:14+05:30
draft: false
aliases:
  - /setup/software-environment
  - /setup/virtual-environment
---

## What is Docker?


### Why should you use Docker?



### Docker basics

#### Jargon

#### Main commands
- `docker build`


### Setup Docker
Docker can be installed easily on [Linux (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/), [MacOS](https://docs.docker.com/desktop/mac/install/) and [Windows](https://docs.docker.com/desktop/windows/install/)


#### Verify your Installation
Once docker is up and running, verify your installation by running `docker run hello-world` on your terminal. You should get the following:


<img src="../verify-installation.png" width="600" alt="centered image"/>


{{% warning %}}
 Every time you modify or move a file the image will have to be rebuilt before running it again in order to copy such changes in your local machine into the container.
{{% /warning %}}
## Running an R script in docker

## Running a Python script in docker

## Multiple languages in a single container
Up until now, we created containers that started from either a Python or an R image. This limits our container to running only R or python scripts, respectively. Some images have already been built to run both python and R, for example this [docker image](https://hub.docker.com/r/jupyter/datascience-notebook). However, in a regular work environement you might be using both python and R along with other languages. In this sense, we can start from a more general image e.g. Ubuntu and add layers to the docker image so that it can run R, Python and whichever language we require in a single container.

How can we do this? Let's create an example repository and name it for instance, "docker_rpy". The directory structure is the following

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

### A look at the scripts

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

## Additional Resources  

1. More information on Conda environments: [https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)

2. Python virtual environments: [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. Information on package environments in Julia: [https://julialang.github.io/Pkg.jl/v1/environments/](https://julialang.github.io/Pkg.jl/v1/environments/)
