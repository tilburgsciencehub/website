---
title: "Set up Docker"
description: "Holy Grail of replicability: Say goodbye to *but it works on my computer*, embrace the power of containerisation"
keywords: "docker, images, container, environments, virtual, install"
#weight: 2
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /get/docker
  - /install/docker
---

## What is Docker?

*Docker* is the most common (and is also open-source) version of containerisation, i.e. a form of virtualisation where applications run in isolated **containers** while using a shared operating system (Linux in Docker's case).

### What are containers?
 <cite>"A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another" [^1]</cite>.  

 Hence, everything that is needed to run your project (e.g. python, R, packages...) is encapsulated and isolated into a container. This container is abstracted from the host operating system (OS) with only access to the binaries, libraries, configuration and dependencies that are built into such a container.

In a nutshell, it's like having a **lightweight virtual machine** that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

### Why should you use Docker?
Say goodbye to "*but it works on my computer*", embrace the power of containerisation:

{{% tip %}}
- **Holy grail of replicability**:

  - Can specify software versions (e.g. python 3.9 or even the OS)
  - **Will always run the same** (and will be able to run) regardless of the infrastructure for instance, regardless of the OS. Therefore, it's more replicable than using [software environments](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/software-environments/) such as via Conda

- **Increased portability and efficiency over VMs**:
  - Less overhead during startup and no need to set up a separate guest OS for each application.
  - Containers take up less space than VMs, they have just the necessary.

- **Share your projects easily with your team**:
  - With [Docker Hub](https://hub.docker.com/) it is very easy. In a way, it's the equivalent of Github for Git but instead, for Docker.
{{% /tip %}}

## Installing Docker

### Windows Users
Download docker from [Docker's official website](https://docs.docker.com/desktop/windows/install/), and follow the following steps to **install docker on windows**.
{{% summary %}}
Follow these steps:

1. Click on **Download Docker Desktop for Windows**

2. Double-click **Docker Desktop Installer.exe** to run the installer

3. When prompted, ensure that the **Enable Hyper-V Windows Features** or the Install required Windows components for WSL 2 option is selected on the Configuration page.

4. Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

5. When the installation is successful, click "Close" to complete the installation process.
{{% /summary %}}

{{% warning %}}
If your admin account is different to your user account, you must add the user to the docker-users group. Run Computer Management as an administrator and navigate to Local Users and Groups > Groups > docker-users. Right-click to add the user to the group. Log out and log back in for the changes to take effect.
{{% /warning %}}

### Mac Users
**Download Docker Desktop on Mac** from [Docker's official website](https://docs.docker.com/desktop/mac/install/), where you will also find detailed instructions.

{{% summary %}}
1. Double-click **Docker.dmg** to open the installer, then drag the Docker icon to the Applications folder.

2. Double-click **Docker.app** in the Applications folder to start Docker. In the example below, the Applications folder is in “grid” view mode.

3. The Docker menu displays the **Docker Subscription Service Agreement** window. Click the checkbox to indicate that you accept the updated terms and then click Accept to continue. Docker Desktop starts after you accept the terms.
{{% /summary %}}

#### Requirements
The requirements and recommendations are different depending on whether you have a Mac with an Intel chip or with Apple silicon:

  - **Mac with Intel chip**
  {{% warning %}}
  In this case, **macOS must be version 10.15 or newer**, you must have **at least 4GB of RAM** and **VirtualBox prior to version 4.3.30 must not be installed**.
  {{% /warning %}}

  - **Mac with Apple silicon**
  {{% tip %}}
  To get the best experience, it is recommended that you install Rosetta 2. To install Rosetta 2 manually from the command line, run the following command:
  ```bash
   softwareupdate --install-rosetta
  ```
  {{% /tip %}}
### Linux Users
The Docker engine can be installed in different ways: **setting up Docker's repositories**, manually by downloading the DEB package or using convenience scripts. Here we will go through the installation using the repository. If you prefer the other methods, find detailed instructions [Docker's install page](https://docs.docker.com/engine/install/ubuntu/)

#### Installing using the repository
{{% summary %}}

**Set up the repository**
1. Update the `apt` package and install packages.
```bash
$ sudo apt-get update
$ sudo apt-get install \
   ca-certificates \
   curl \
   gnupg \
   lsb-release
```
2. Add Docker's official key
```bash
 $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
3. Use the following command to set up the stable repository:
```bash
 $ echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
**Install the Docker Engine**

Update the `apt` package index and install the latest version of the Docker Engine:
```bash
$ sudo apt-get update
$ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
{{% /summary %}}
#### Requirements
To install Docker Engine on Linux, you need the 64-bit version of one of these Ubuntu versions:
- Ubuntu Impish 21.10
- Ubuntu Hirsute 21.04
- Ubuntu Focal 20.04 (LTS)
- Ubuntu Bionic 18.04 (LTS)

## Verify your Installation
Once installed, verify your installation works correctly by running the following on your terminal:
``` bash
docker run hello-world
```
If everything is working correctly, you should get the following output:

<img src="../img/verify-installation.png" width="600" alt="docker hello-world message"/>




[^1]:Docker.com ["What is a container"](https://www.docker.com/resources/what-container)
