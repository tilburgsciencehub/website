---
title: "Getting started with Tilburg's GitLab"
description: ""
keywords: "git, github, gitlab, continuous integration,continuous development, git flow"
date: 2024-20-06
weight: 3
author: "Krzysztof Wiesniakowski"
authorlink: "https://tilburgsciencehub.com/contributors/krzysztofwiesniakowski/"
aliases:
  - /learn/gitlab
---

## Introduction to Tilburg University GitLab

[GitLab at Tilburg University](https://gitlab.uvt.nl/) is a powerful platform for version control and collaborative software development. It offers a comprehensive suite of features that support the entire DevOps lifecycle, from project planning and source code management to CI/CD and monitoring. Key features include:

- **Version Control**: Utilize Git for distributed version control, enabling efficient collaboration and tracking of code changes.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automate the testing and deployment of your code to ensure high-quality releases.
- **Project Management**: Manage your projects with built-in tools like issue tracking, milestones, and Kanban boards.
- **Code Review**: Enhance code quality through merge requests and code reviews, facilitating peer feedback and collaboration.
- **Security**: Benefit from built-in security features such as vulnerability management and dependency scanning to ensure your projects remain secure.
- **Collaboration**: Work seamlessly with team members through features like wikis, snippets, and shared repositories.

Tilburg University's GitLab is an essential tool for students, researchers, and developers, providing a robust environment for managing and collaborating on software projects.

## Distinguishing GitLab and GitHub

GitLab and GitHub are both popular platforms for version control and collaborative software development, but they have distinct features and focuses. GitHub is widely known for its strong community and extensive integrations with other tools, making it a go-to choice for open-source projects. It provides a user-friendly interface and extensive documentation, catering to a broad range of developers. On the other hand, GitLab offers a more comprehensive suite of DevOps tools, including built-in Continuous Integration/Continuous Deployment (CI/CD) pipelines, issue tracking, and project management features. GitLab's self-hosting capabilities allow organizations to run GitLab on their own servers, providing greater control over their data and workflows. Additionally, GitLab emphasizes an all-in-one platform approach, aiming to support the entire software development lifecycle within a single application. While both platforms support Git for version control, GitLab's extensive built-in features and flexibility for self-hosting distinguish it from GitHub's community-centric and integration-focused model.

## How to Log in to GitLab and Import a Project from GitHub

### Logging in to GitLab

1. Go to [GitLab at Tilburg University](https://gitlab.uvt.nl/).
2. Use your Tilburg University credentials to log in.

### Importing a Project from GitHub into GitLab

1. Click on the `+` button in the top navigation bar.
2. Select `New project/repository`.
3. Choose `Import project`.
4. Select `GitHub` as the source.
5. Authenticate with your GitHub account if prompted.
6. Choose the repository you want to import and click on `Import`.

By following these steps, you can easily log in to GitLab and import a project from GitHub.

## Understanding SSH Keys in GitLab

### What is an SSH Key?

An SSH key is a secure way of connecting to a remote server or service, such as GitLab, without needing to enter a password every time. It involves creating a pair of cryptographic keys: a private key that you keep secure on your local machine and a public key that you add to your GitLab account. This setup enhances security and convenience for operations like cloning repositories, pushing code, and pulling updates.

### Why Do We Need SSH Keys in GitLab?

GitLab often requires SSH keys for authentication to ensure secure communication between your local machine and the GitLab server. Using SSH keys is particularly important when working with private repositories or when higher security is needed for sensitive projects. It allows for secure, password-less access, which is both more secure and convenient than traditional username/password authentication.

### Why Don’t We Need SSH Keys in GitHub?

While GitHub also supports and recommends using SSH keys for secure access, it provides additional authentication methods, such as HTTPS and GitHub CLI, which can be simpler for some users to set up. For example, you can clone repositories over HTTPS and authenticate using your GitHub username and personal access token, which is often perceived as easier for beginners. GitHub's emphasis on ease of use and flexibility in authentication methods makes it possible to use the platform effectively without SSH keys, although using them is still recommended for enhanced security.

In summary, SSH keys provide a secure and convenient way to authenticate with GitLab, ensuring safe and efficient interactions with your repositories. While GitHub also supports SSH keys, it offers alternative methods that can be more accessible for some users.

### Set up SSH key in Gitlab
Explain what is rsa

Please stay up to date with the current technologies for generating ssh keys as every week new vulnerabilities are discovered

```bash
ssh-keygen -t rsa
```

## Connect with VScode, Rstudio and operate through command line

### GitLab and RStudio

tutorial is here: https://handbook.gitlab.com/handbook/business-technology/data-team/platform/rstudio/

### Gitlab and VScode

Download an extension: https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/

## Through command line
Ask Hannes what he means with command line cause I think it is exactly the same as with Github