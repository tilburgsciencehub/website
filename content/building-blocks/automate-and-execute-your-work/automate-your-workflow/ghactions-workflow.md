---
title: "Build a workflow on a GitHub hosted runner" 
description: "Learn a practical example of a GitHub actions workflow for code formatting and testing"
keywords: "GitHub Actions, Data Science, Project, Project Structure, Reproducibility, Automation, Testing, Formatting, Workflows, Runners, Jobs, Events, Testing, Formatting"
weight: 2
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2023-10-14T22:01:14+05:30 
aliases: 
  - /github_actions/workflow
---

## Overview

This building block delves deeper into GitHub Actions by providing a hands-on example. We’ll craft a workflow specifically for code formatting and testing. 

If you are new to GitHub Actions, we suggest you review [this building block](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/automate-your-workflow/intro_ghactions/) first to get familiar with the foundational concepts.

By the end of this block, you will:

- Know how to set up a workflow for code formatting using Super Linter.
- Understand how to integrate code testing into your workflow.

## Building a GitHub Actions Workflow

In this section, we're going to build upon the `YAML` file structure introduced in the previous guide. Our primary goal is to integrate code formatting using the Super Linter and code testing.

### Code Formatting with Super Linter

[Super Linter](https://github.com/marketplace/actions/super-linter) is a simple combination of various linters to help validate source code. When incorporated into GitHub Actions, it can automatically validate and format code pushed into your repository.

Here’s a breakdown of the `YAML` configuration for the code formatting job using Super Linter:

{{% codeblock %}}
```yaml

# This section defines the list of jobs to run
jobs:

  # The first job is named 'format-check'
  format-check:

    # Specifies which operating system to run the job on
    runs-on: ubuntu-latest  # This will run on the latest version of Ubuntu hosted by GitHub
    
    # Determines how the job behaves if a matrix strategy is used (not used here, but kept for context)
    strategy:
      fail-fast: true  # If any step fails, stop the entire job immediately
    
    # List of sequential steps within this job
    steps:
    # The first step checks out your repository's code to the runner's environment
    - name: Checkout  
      uses: actions/checkout@v3  # GitHub Action that checks out your code
    
    # The second step runs the Super Linter to validate code formatting and linting
    - name: super_linter
      continue-on-error: false  # The job will fail if this step encounters an error
      uses: super-linter/super-linter@v5.0.0  # Specifies the version of Super Linter to use
      env:  # Environment variables for this step
        DEFAULT_BRANCH: main
        VALIDATE_PYTHON_MYPY: true   # Enables Python type checking with mypy
        VALIDATE_PYTHON_BLACK: true  # Enables Python formatting with Black
        VALIDATE_PYTHON_ISORT: true  # Enables Python import sorting with isort

```
{{% /codeblock %}}


This portion first checks out the code from the repository using actions/checkout@v3. After that, it uses the Super Linter action to validate the code. The environment variables under env specify the configuration for Super Linter.

### Code Testing with pytest

After code formatting, it's important to ensure that your code functions as expected. One popular tool for testing Python code is pytest.

Below is the configuration for the testing section of our workflow:

{{% codeblock %}}
```yaml
  # The second job is named 'code-testing'
  code-testing:

    # This job will only run if the 'format-check' job succeeds
    needs: format-check
    
    # Specifies which operating system to run the job on
    runs-on: ubuntu-latest  # This will run on the latest version of Ubuntu hosted by GitHub
    
    # Determines how the job behaves if a matrix strategy is used (not used here, but kept for context)
    strategy:
      fail-fast: true  # If any step fails, stop the entire job immediately
    
    # List of sequential steps within this job
    steps:
    # The first step checks out your repository's code to the runner's environment
    - name: Checkout  
      uses: actions/checkout@v3  # GitHub Action that checks out your code
    
    # The second step runs tests using pytest
    - name: Run tests  
      run: pytest  # Command to run pytest to execute tests

```
{{% /codeblock %}}

Note that originally, the runs-on field was set to run on a self-hosted runner. For simplicity, we've set it to ubuntu-latest, which means the job will run on GitHub's servers. You can, however, easily revert it back to your self-hosted runner if desired.

This portion again checks out the code and then runs pytest to execute tests present in your repository.

{{% tip %}}
**Want to use a self-hosted runner?**

A self-hosted runner can offer more computational power and flexibility. To learn more about setting it up, look out for our future building block dedicated to this topic.

{{% /tip %}}

### Integrate into Your Repository

To incorporate this workflow into your repository:

- Create a `.github/workflows/` directory at the root of your repository.
- Save the full `YAML` configuration (including both formatting and testing jobs) into a file, e.g., `formatting-testing.yml`.
- Push your changes to the repository. GitHub will automatically detect the workflow and run it based on the specified triggers.

{{% summary %}}

With GitHub Actions, you can automate code formatting using tools like Super Linter and integrate testing with tools like pytest. By structuring your workflow correctly with a `.yml` file and placing it in the .github/workflows/ directory, GitHub can automatically process your workflow, ensuring code quality and functionality every time you make changes to your repository.

{{% /summary %}}

## Additional resources

- GitHub Actions [Marketplace](https://github.com/marketplace?type=actions)
- Super Linter [Documentation](https://github.com/marketplace/actions/super-linter)
- Pytest [Documentation](https://docs.pytest.org/en/7.4.x/)
- [Workflow example](https://github.com/snpe-reputation-systems/snpe-reputation-systems/blob/master/.github/workflows/formatting-testing.yml) for code formatting and testing