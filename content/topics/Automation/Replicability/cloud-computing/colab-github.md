---
title: "Leveraging GitHub and Google Colab for Collaborative Development" 
description: "Explore how integrating GitHub with Google Colab can streamline your development workflow, enabling more efficient project management and collaboration."
keywords: "GitHub, Google Colab, Collaboration, Project Management, Development Workflow, Git Commands, Persistent Storage, Project Visibility"
weight: 3
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2024-03-25T10:00:00+00:00
aliases: 
  - /github_colab/integration
---

## Introduction

This building block aims to enhance your development process by illustrating the synergistic relationship between GitHub and Google Colab. It's designed for students and researchers looking to optimize their workflow for more efficient and collaborative project management.

{{% tip %}}
**For Google Colab newcomers**
Worth to give a read to [this short introduction](https://tilburgsciencehub.com/topics/automation/replicability/cloud-computing/google-colab/) before diving into its integration with GitHub.

{{% /tip %}}

By the end of this guide, you will:

- Understand how to import GitHub repositories into Google Colab.
- Know how to mount Google Drive in Colab for persistent storage.
- Be familiar with executing Git commands and pushing changes directly from Colab.
- Learn strategies to enhance project visibility and collaboration using both platforms.

## Setting Up the Workspace

### Importing GitHub Repositories into Colab

Colab offers a seamless method to clone your GitHub repository into the environment, allowing you to work directly on your projects without switching platforms. This integration simplifies accessing and working on your code.

To set up the workspace, you'll first need a GitHub repository to work from, which can be either public or private. Also, make sure you are logged in into your Google Account. Then, do the following:

**1.** Go to [Google Colab](https://colab.google/) and click on *'Open Colab'*
**2.** In the *'File'* menu, select *'Open notebook'*, then go to the *'GitHub'* tab. You can enter the URL of your repository or search for it using your GitHub username. Include private repositories if necessary by clicking on the respective option.
**3.** After finding your repository, click on the notebook you want to open. 

<p align = "center">
<img src = "../images/open-nb-colab.png" width="700" style="border:1px solid black;">
<figcaption> Opening a notebook from GitHub in Google Colab.</figcaption>
</p>

Once you have the notebook open in Google Colab, you can start working directly on it. However, if you need access to other files or directories within your GitHub repository, like a dataset, cloning it might be necessary. This can be done by executing a git clone command in a cell:

```bash
!git clone https://github.com/your-username/your-repository.git
```
After doing this, go to the files tab and press the refresh button, as shown below:
<p align = "center">
<img src = "../images/clone-colab-repo.png" width="700" style="border:1px solid black;">
<figcaption> Clone to access the notebook's GitHub repo</figcaption>
</p>

{{% warning %}}
**Cloning private repos**

If you want to clone a private repository, you will need to provide your GitHub username and password. To do this securely, you can use Git credentials or SSH keys. Here's how you can clone a private repository using Git credentials:

1. Generate a personal access token (PAT) on GitHub. You can follow the instructions [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to generate a PAT.
2. In the Colab notebook, execute the following command, replacing `your-username` and `your-repository` with your GitHub username and repository name:

```bash
!git clone https://your-PAT:x-oauth-basic@github.com/your-username/your-repository.git
```
{{% /warning %}}

## Working with GitHub in Colab

### Executing Basic Git Commands

Google Colab's environment allows for the execution of Git commands, enabling version control operations directly within your notebook. This feature is crucial for tracking changes, managing branches, and collaborating on projects hosted on GitHub.

Some of the basic Git commands you can execute in Colab include:

- `!git status` to check the status of your repository.
- `!git add .` to stage all changes in the repository.
- `!git commit -m "Your commit message"` to commit the staged changes.
- `!git push` to push committed changes to the remote repository.

### Pushing Changes Using the Colab Interface

In addition to executing Git commands directly in Colab, you can also use the Colab interface to push changes to your GitHub repository. This provides a more user-friendly and visual way to manage your commits and push them to the remote repository.

To push changes using the Colab interface, follow these steps:

1. Make sure you have made the necessary changes to your notebook or files.
2. In the Colab menu, click on *'File'* and select *'Save a copy in GitHub'*.
3. A dialog box will appear, allowing you to specify the repository, branch, and commit message. Fill in the required information and click on *'OK'*.

<p align = "center">
<img src = "../images/save-copy-dialog.png" width="700" style="border:1px solid black;">
<figcaption> Dialog box for saving a copy in GitHub.</figcaption>
</p>

{{% tip %}}
To make it easier for you and your collaborators to access the notebook directly from the GitHub repository, it is recommended to tick the box *'Include a link to Colab'*. This way, you can simply go to the notebook file and click on the following icon to launch it:

<p align = "center">
<img src = "../images/colab-link.png" width="300" style="border:1px solid black;">
<figcaption> Click here to launch the notebook from the repo</figcaption>
</p>

{{% /tip %}}

4. Colab will create a new commit with your changes and push it to the specified repository and branch.

## Good Practices for storage management

### Mounting Google Drive for Persistent Storage

As mentioned in [this building block](https://tilburgsciencehub.com/topics/automation/replicability/cloud-computing/google-colab/), mounting your Google Drive in Google Colab is a good practice when working with large files. It provides convenient access to files, datasets, and resources stored in your Google Drive within the Colab environment.

Benefits of using Google Drive in Colab include:
- Storage of large files that exceed Git repository limitations.
- Easy collaboration and sharing with team members or collaborators.
- Persistent storage, ensuring accessibility across Colab sessions.

### Use Google Cloud Buckets

Another option for storage management in Google Colab is to use Google Cloud Storage Buckets. These are a scalable and durable object storage service provided by Google Cloud Platform. You can find more information in [this building block](https://tilburgsciencehub.com/topics/collect-store/data-storage/commercial-cloud/mem-storage-gcp/).

{{% summary %}}

This topic covers the steps to clone a repository, work with GitHub in Colab, execute basic Git commands, and push changes using the Colab interface. Additionally, it suggests good practices for storage management, such as mounting Google Drive for persistent storage and using Google Cloud Storage Buckets.

{{% /summary %}}

### Additional Resources

- [Google Cloud Storage Documentation](https://cloud.google.com/storage/docs)
- [Google Colab Documentation](https://colab.research.google.com/notebooks/intro.ipynb)
- [GitHub Guides](https://guides.github.com/)