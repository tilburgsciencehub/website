---
title: "A Reproducible Workflow for Economics Research Using Snakemake and R"
date: 2020-11-11T22:01:14+05:30
draft: false
description: "A platform-independent, reproducible research workflow with AirBnB data, using Stata, Python and R."
keywords: "snakemake, r, template, workflow, example"
weight: 5
author: "Lachlan Deer"
authorlink: "http://lachlandeer.github.io"
aliases:
  - /try/snakemake-workflow
---

## Overview

This is a template for a reproducible research project that uses `Snakemake` and the `R` programming language.

We use `Snakemake` to construct a set of *rules* to build our workflow from start to finish, starting with some data cleaning, running some regressions, constructung figures and tables, and then finishing with compiling a pdf article and slides.

We believe this mimics an approximate workflow of most empirical research in economics.

## Motivating Example

Our example project involves replicating the main tables and figures of Mankiw, Romer and Weil's classic 1992 QJE article "[A Contribution to the Empirics of Economic Growth.](https://eml.berkeley.edu/~dromer/papers/MRW_QJE1992.pdf)"
We hope by using an example that is simple in its methods readers focus on how we have chosen to assemble both pure R codes and the Snakemake rules that build our project, rather than getting lost on econometric methodologies.

## Get The Workflow

Check out the GitHub repository by Lachlan Deer to get started.

{{% cta-primary-center "Go to the GitHub Repository" "https://github.com/lachlandeer/snakemake-econ-r" %}}
