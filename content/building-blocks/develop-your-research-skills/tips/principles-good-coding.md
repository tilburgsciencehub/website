---
title: "Principles for Good Coding"
description: "Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong."
keywords: "style, optimize, definition, human"
weight: 2
date: 2020-11-11T22:01:14+05:30
draft: false
aliases:
  - /write/good-code
---

## Write programs for people, not computers

Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong.

- Organization
    - Define functions that do one mayor step each, instead of one giant script doing everything
    - Write short scripts that do one task each
    - Document only what your code **doesn't** say, but nothing else
- Style
    - Use meaningful and short variable names
    - Use consistent code and formatting styles (oneExample, one_example, example-one)
    - Make use of indents in your code

## Define things once and only once

Let computers repeat and execute tasks.,

- Rule of 3: if you copy-paste code 3 times or more, write a function instead.
- If you do things often, automate them
    - e.g., by using scripts, macros, aliases/variables
    - write a dictionary with definitions
- Use build tools to [automate workflows](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/automation/)

## Use a version control system

- Add all inputs, but no outputs/generated files
    - DO: everything created by humans, small data inputs
    - DON'T: things created by the computer from your inputs (generated files; those will be [reproduced via a workflow](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/automation/)). Also [do not version large data inputs](/tutorials/project-setup/principles-of-project-setup-and-workflow-management/directories/).
- Work in small changes
    - Create [snapshots/commits](/building-blocks/share-your-results-and-project/use-github/versioning-using-git/) in small and logical steps. This will allow you to go back in time if necessary, and to understand progression.
-  Use an issue tracking tool to document problems (e.g., such as the *Issue* tab on GitHub; email is not an issue tracker!)

## Optimize software only after it works correctly

Even experts find it hard to predict performance bottlenecks.

- Get it right, then make it fast
- Small changes can have dramatic impact on performance
- Use a profile to report how much time is spent on each line of code

## Be a good code citizen
- Team members should take the time to improve code they are modifying or extending even if they did not write it themselves.
- A core of good code plus a long series of edits and accretions equals bad code.
  - Why? The logical structure that made sense for the program when it was small no longer makes sense as it grows.

- It is critical to regularly look at the program as a whole and improve the logical structure through reorganization and abstraction. Programmers call this **refactoring**. Check this [link](https://refactoring.guru/refactoring/) to learn how to implement refactoring.

{{% tip %}}
- Even if your immediate task only requires modifying a small part of a program, we encourage you to take the time to improve the program more broadly.

- At a minimum, guarantee that the code quality of the program overall is at least as good as it was when you started.
{{% /tip %}}
## Keep it short
- No line of code should be more than 100 characters long.
  - All languages we work in allow you to break a logical line across multiple lines on the page (e.g, using `///` in Stata or `...` in Matlab).

{{% tip %}}
   Set your editor to show a “margin” at 100 characters.
{{% /tip %}}
- Functions should not typically be longer than 200 lines.
