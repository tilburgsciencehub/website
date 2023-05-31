---
title: "Enhance the Reproducibility and Automation of your data science project with GitHub Actions" 
description: "The GitHub Actions platform offers set of tools for you to implement your own customized workflows, that can greatly amplify the automation and reproducibility in your projects. This building block introduces you to the essentials of GitHub Actions, guiding you through the necessary steps to modify your project structure to enable you to take advantage of it."
keywords: "GitHub Actions, Data Science, Project, Project Structure, Reproducibility, Automation, Testing, Formatting"
weight: 2
author: "Diego Sanchez Perez"
authorlink: "https://www.linkedin.com/in/diego-s%C3%A1nchez-p%C3%A9rez-0097551b8/"
draft: false
date: 2023-05-23T22:01:14+05:30
aliases: 
  - /github_actions/introduction


---

# GitHub Actions: a level up in terms of reproducibility and automation for your data science project

When it comes to enhancing your data science project's automation and reproducibility, GitHub Actions is a tool that you should definitely consider. This building block will introduce the basic concepts to understand how GitHub Actions works and why it is a great option for your project, as well as two implementation proposals and how to adapt your project structure to incorporate these. This building block is meant to complement that other on [data management and directory structure](https://tilburgsciencehub.com/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/directories/) presented within as part of our tutorial on [principles of project setup and workflow management](https://tilburgsciencehub.com/tutorials/reproducible-research-and-automation/principles-of-project-setup-and-workflow-management/project-setup-overview/) which we strongly recommend you to check out if you haven't already! 

### Introducing GitHub Actions

[GitHub Actions](https://docs.github.com/en/actions) is GitHub's native platform for workflow automation. With it you can define customized workflows for your project that are automatically triggered when certain pre-specified conditions are met. Examples of such workflows could include one in charge of re-training your model and updating its results whenever you add new data to your project, a workflow responsible for running an automated code testing pipeline each time you push new code to your repository, or a formatting workflow checking that your code adheres to certain desired standards. These are just a few examples, the great flexibility of GitHub Actions allows you to define workflows that can assist or automate most of your project's pipeline segments. When it comes to examples, in this building block the focus will be placed on the code testing and formatting workflows, two particularly popular and interesting use cases. 

Moreover, GitHub Actions also offers a number of interesting advantages in terms of reproducibility. With your workflows defined as YAML files (file format employed by GitHub Actions) you can easily share them with anyone interested in reproducing your project's pipeline. Furthermore, GitHub Actions also generates logs every time a workflow is executed which can be very useful when it comes to reproducing and comparing your results.

{{% tip %}}

 If you are not familiar with Git or GitHub feel free to check out our building blocks on the topic [here](https://tilburgsciencehub.com/search/?q=GitHub). They contain all the information you need to get started using Git and GitHub!

{{% /tip %}}

### GitHub Actions functioning and relevant concepts

The vehicles through which you will define your workflows in GitHub Actions are YAML files. In these files is where you indicate the set instructions to be followed by GitHub Actions to carry out your workflow, alongside other relevant details necessary to ensure that the workflow can be appropriately interpreted and executed. All workflows are shaped by the following elements:

- __Events__: An workflow's event in the context of GitHub Actions refers to the occurrence(s) that will trigger the execution of a workflow. These are commonly related to activity in your project's repository, such as pull requests or pushes, however there are many other options for triggering a workflow such as defining a periodical schedule or directly triggering it manually. You can visit [this page](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows) to learn more about events and workflow triggering.

- __Jobs__: After a workflow is triggered it will proceed to execute a job or series of jobs. These jobs are a collection of steps, with each of these steps consisting of an action or shell script in charge of conducting the tasks you would like your workflow to complete. A single workflow can be composed of many jobs, each one being by default executed in a parallel and independent manner. Meanwhile the steps within each job are executed serially and are dependent on each other. For further insight into the details of a workflow's jobs you can consult [GitHub's documentation on the topic](https://docs.github.com/en/actions/using-jobs).

- __Runners__: The runners are the servers where the jobs are executed once a workflow is triggered. GitHub provides users with different kinds of runners for their workflows based on either Linux, Windows or macOS depending. These GitHub-provided runners are typically enough to carry tasks that are not particularly computationally demanding. However if this is not the case with your workflow you may consider running your workflow's jobs inside your own self-hosted runner with a higher capacity to carry out computationally demanding tasks. If you are interested in this option you can take a look at our building block on [how to set up your own GitHub Actions self-hosted runner]().

- __Actions__: Probably one of the most interesting features of the GitHub Actions platform, actions are custom applications that automatically perform certain relatively complex tasks within your workflow without you having to worry about the details of their implementation. These actions are run within the steps of your workflow's jobs and can take care of things such as automatically exporting your project's code to the runner to operate over it, setting up dependencies within the runner or automatically committing changes made in your project during the workflow. These actions are typically developed by GitHub's community and there is a large number of them available for you to use according to your needs, you can explore available actions by visiting [GitHub's marketplace](https://github.com/marketplace?type=actions).

<p align = "center">
<img src = "../img/wf_concept.png" width="650">
<figcaption> Left: Conceptual structure of a workflow file. Right: Approximate appearance of an example workflow with the structure proposed on the left. </figcaption>
</p>

In the image above on the left you can see the conceptual structure of a GitHub Actions workflow, while on the right there is an example of how an actual workflow YAML file with the same proposed structure would look like. This example workflow consists of two jobs, each one with three steps. Note how the workflow starts with the events that will trigger it (line 3 of the right side of the image) right after the name given to the workflow. After that the different jobs are defined, first, a runner is assigned to each of these (lines 7 and 21 from the right side of the image) and then the steps are defined. You can include as many jobs within a workflow and steps within a job as you want and as long as the runner can handle it, however in this example things are kept simple so it is easier for you to familiarize yourself with the structure of a GitHub Actions workflow. For that same reason, this example workflow will not be explored in detail here. For learning more about how to build your own workflows and the details of how to do this we recommend you to check out [the second part of this building block](). There you will see how to design workflows using as a reference a popular implementation for these: a pipeline for code formatting and testing.

### Adapting your project structure to use GitHub Actions

The first elementary pre-requisite to take advantage of GitHub Actions is that your project is hosted in a GitHub repository. If this is the case then all you have to do is to include within your project's repository at the root level a directory called `.github` which in turn must contain another sub-directory called `workflows`. This subdirectory is where you will place your workflow YAML files so GitHub can take care of them. You can give your workflows any name you want as long as the files containing these have the appropriate extension `.yml`.