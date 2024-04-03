---
title: "Parallel Computing in R"
description: "Discover the potential of parallel computing for reducing execution times in R, by distributing tasks across multiple CRU cores."
keywords: "parallelization, parallel, time, efficiency, R, coding, code, data, open, science, package"
draft: false
weight: 2
author: "Valerie Vossen"
aliases:
  - /parallelization
  - /parallelization-r
  - /parallel-coding
---

## Overview

Parallel computing entails executing a computation in smaller tasks by breaking it down into smaller pieces and dividing them among the cores. Instead of letting a single processor handle everything, multiple cores work together on different parts of the problem at the same time which speeds up the tasks!

While some libraries, such as `data.table` or `dplyr` come with built-in parallelization, researchers can also parallelize code that was not meant to be run in parallel in the first place! Here, we show the basic principles of parallel computing using simple code examples in R. We also demonstrate how parallelization can increase time efficiency by comparing the execution time of the same computation with and without parallelization. Two approaches are covered: the *multicore* and *socket approach*. 

{{% warning %}}

The multicore approach is not available on all systems, as it requires support for forking. Generally, Unix-like systems as Mac and Linux allow for this and Window does not. The socket approach works on all systems.

{{% /warning %}}


## The method behind parallelization

The Central Processing Unit (CPU) of your computer contains small units called "cores". The number of cores available determines how many different tasks you can execute at the same time. Then, creating clusters is like forming teams of these "cores". You send data and functions to each cluster, where each core works on a different part of the task. In theory, the computation can be executed as many times faster as cores you have available, e.g. 4 available cores speeds up your computation to 1/4 of the time. 

However, overhead makes this less in practice. Overhead involves things as starting the sub-processes and copying the data over to those processes, and communicating back and collecting the results. Therefore, in reality, this maximum time-saving is not likely to reach.

You can determine the number of cores that are available, i.e. the number of computations that can be executed at the same time, with the `detectCores()` function. 

{{% codeblock %}}
```R
#load package
library(parallel)

detectCores()
```
{{% /codeblock %}}


## Multicore approach

The easiest application of the multicore approach is the `mclapply()` function of the `parallel` package in R. As `apply()` iterates over a data-structure while applying a function to each subset, `lapply()` is used to iterate over a list, `mcapply` applies parellization by iterating into multiple processes (the cores). The multicore approach copies the entire current version of R and moves it to a new core, so exporting variables and loading already loaded packages again is not necessary.

### Example 

This simple example calculates the mean sepal length for each species in the `iris` dataset available within R. If you want to know more about the data beforehand, you can check the summary statistic of the dataset yourself with running `summary(iris)`. 

{{% codeblock %}}
```R
# Load packages and Iris dataset
library(dplyr)
library(datasets)
data(iris)

# Define function
calculate_mean_sepal_length <- function(df) {
  species <- unique(df$Species)
  means <- vector("numeric", length = length(species))
  for (i in 1:length(species)) {
    means[i] <- mean(df[df$Species == species[i], "Sepal.Length"])
  }
  return(data.frame(Species = species, Mean_Sepal_Length = means))
}
```
{{% /codeblock %}}

Now the function is defined, the code will be executed, first as a normal computation and then with parallelization. The `system.time()` function is used to measure the execution times such that we can compare them. 

{{% codeblock %}}
```R
# Without parallelization (sequential computation)
start_time_normal <- Sys.time()
result_normal <- calculate_mean_sepal_length(iris)
end_time_normal <- Sys.time()

time_normal <- end_time_normal - start_time_normal
```
{{% /codeblock %}}

The following data frame is returned:

|   | Species     | Mean_Sepal_Length |
|---|-------------|-------------------|
| 1 | setosa      | 5.006             |
| 2 | versicolor  | 5.936             |
| 3 | virginica   | 6.588             |


Now, the same code with parallelization using `mclapply()`:

{{% codeblock %}}
```R
# With parallelization using mclapply
start_time_multi <- Sys.time()

result_multi <- bind_rows(
  mclapply(
    split(iris, iris$Species), calculate_mean_sepal_length
    )
)
end_time_multi <- Sys.time()

time_multi <- end_time_multi - start_time_multi

```
{{% /codeblock %}}

Comparing execution times:

{{% codeblock %}}
```R
time_normal
time_multi
```
{{% /codeblock %}}

The multicore computation appears to be slower than than the normal computation for this very small task, with `0.04` seconds against `0.02` seconds. These times likely differ for you. 

<!-- system.time() user and elapsed are roughly the same; normal with no parallelization (what does elapsed mean). Now using mclapply(), elapsed < user time (although not 1/4 when we use 4 cores)
User time = CPU time spent executing your R code (adding all tasks together, whether it is executed sequentially or in parallel)
Elapsed time = total real-world time that has elapsed from start of computation until it is completed. -->

## Socket approach

The socket approach slightly differs from the multicore approach. Here, you have to make a socket cluster first, and manually copy the data and code to each cluster member (the cores). This is the key difference with multicore approach, in which exporting was not necessary.

### Example

The following example provides the basic steps how to make a cluster and let make it execute your task. To test its efficiency, we will compare the time needed to execute code being executed with and without parallelization.

{{% warning %}}

With the socket approach, a new version of R is launched on each core. Therefore, any message from your computer requesting permission for R to accept incoming connections you should accept.

{{% /warning %}}


1. Determine the number of cores available

Before you create a cluster, you can determine the number of cores that are available on your system.

<!-- floor() rounds down the result to the nearest integer
logical = T returns a logical value indicating whether the detected number of cores is reliable
all.tests = F means it won't run additional tests to determine the number of cores, making it faster -->

{{% codeblock %}}
```R
# Determine number of cores available
perc_use <- 0.8
ncpu <- floor(detectCores(all.tests = FALSE, logical = TRUE) * perc_use)

```
{{% /codeblock %}}

The number of cores is determined by your computer's hardware configuration, and is `4` in my case. The `perc_use` represents the percentage of CPU cores you want to use for parallel computing, set to `0.8`. The rationale behind using a percentage instead of all cores could be to leave some CPU capacity for other system tasks.The number of cores multiplied with the percentage you want to use determines the value for `ncpu`, i.e. the number of CPU cores to be used for parallel processing. 

2. Create cluster
   
{{% codeblock %}}
```R
# Create a parallel cluster
cl <- makePSOCKcluster(ncpu)
```
{{% /codeblock %}}


3. Execute code in parallel

The socket approach doesn't have anything loaded in yet, so any loaded packages, variables, data, functions etc. that the cluster needs to execute the code needs to be moved into each process. This can be done with the `clusterExport()` function. Below, a function is exported to the cluster as an example.

{{% codeblock %}}
```R
# Load packages if not done before
library(parallel)
library(dplyr)

# Export function to cluster
clusterExport(cl, 'calculate_mean_sepal_length')

# Parallel computation function
calculate_mean_sepal_length_parallel <- function(df) {
  clusterApplyLB(cl, split(df, df$Species), calculate_mean_sepal_length)
}

# Run parallel computation
start_time_socket <- Sys.time()
result_socket <- bind_rows(
  calculate_mean_sepal_length_parallel(iris)
  )
end_time_socket <- Sys.time()
time_socket <- end_time_socket - start_time_socket

```
{{% /codeblock %}}

{{% tip %}}

You can use the `parLapply()` function to perform an `lapply()` function across multiple nodes in a socket cluster.

{{% /tip %}}


4. Compare time to same task without parallelization

{{% codeblock %}}
```R
time_normal
time_socket
```
{{% /codeblock %}}

Again, for this small computation, overhead seems to be larger than the time parallelization has saved, with time for execution with the socket approach is `0.11`, compared to `0.02` for the normal computation.


## Multicore versus socket approach

Based on [Josh Errickson](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/parallel.html), this table summarizes the key differences between the multicore and socket approach.

|                   *Multicore*                  | *Socket*                                         |
|-----------------------------------------------|--------------------------------------------------|
| Available on Unix-like systems, <br> e.g. Mac and Linux | Works on all systems, <br> also Windows                           |
| Generally faster    | Slower due to extra overhead <br> time; launching new versions <br> of R on each core      |
| Workspace exists in each <br> process,   since it copies the <br> existing version of R  | Export variables, loaded <br> packages, etc. in each <br> process separately     |
|   Easier to implement   | A bit more complicated                          |


{{% warning %}}

When generating random numbers in parallel, be careful. This might give issues as is not possible to generate the exact same numbers in each of the cores. Also, reproducing the same random numbers with `set.seed()` will not work the same. The `parallel` package offers a way to overcome this issue. Check [Chapter 20.4 of this guide](https://bookdown.org/rdpeng/rprogdatascience/) for an example.

{{% /warning %}}


{{% summary %}}

There is benefit of parallelization especially in substantial computations. If the computation is already fast, the overhead involved with parallelization tasks might take more time than it saves.Discover the use of it yourself, and find out how it can offer advantages for you!

{{% /summary %}}
