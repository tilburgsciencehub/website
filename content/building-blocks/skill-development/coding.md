---
title: "Principles for Good Coding"
date: 2020-11-11T22:01:14+05:30
draft: false
weight: 10
---

# Guiding Principles for Coding

## 1) Write programs for people, not computers

Make your code easy to understand for humans. If your code looks very complex or messy, you're probably doing it wrong.

- Organization
    - Define functions that do one mayor step each, instead of one giant script doing everything
    - Write short scripts that do one task each
    - Document only what your code **doesn't** say, but nothing else
- Style
    - Use meaningful and short variable names
    - Use consistent code and formatting styles (oneExample, one_example, example-one)
    - Make use of indents in your code

## 2) Define things once and only once

Let computers repeat and execute tasks.,

- Rule of 3: if you copy-paste code 3 times or more, write a function instead.
- If you do things often, automate them
    - e.g., by using scripts, macros, aliases/variables
    - write a dictionary with definitions
- Use build tools to [automate workflows](../workflow/automation.md)

## 3) Use a version control system

- Add all inputs, but no outputs/generated files
    - DO: everything created by humans, small data inputs
    - DON'T: things created by the computer from your inputs (generated files; those will be [reproduced via a workflow](../workflow/automation.md)). Also [do not version large data inputs](../workflow/directories.md).
- Work in small changes
    - Create [snapshots/commits](../workflow/versioning.md) in small and logical steps. This will allow you to go back in time if necessary, and to understand progression.
-  Use an issue tracking tool to document problems (e.g., such as the *Issue* tab on GitHub; email is not an issue tracker!)

## 4) Optimize software only after it works correctly

Even experts find it hard to predict performance bottlenecks.

- Get it right, then make it fast
- Small changes can have dramatic impact on performance
- Use a profile to report how much time is spent on each line of code


!!! thanks
    Content based on Ulrich Bergmann, Matteo Courthoud, Lachlan Deer (2020), [*Introduction and Motivation*, Programming Practices for Research in Economics](https://github.com/pp4rs/2020-uzh-course-material/blob/master/00-intro/intro.pdf), University of Zurich.
