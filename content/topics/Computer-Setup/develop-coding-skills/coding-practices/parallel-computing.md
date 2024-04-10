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

The multicore approach is not available on all systems, as it requires support for forking. Generally, Unix-like systems such as Mac and Linux allow for this and Windows does not. As Google Colab operates on Linux, you can use this on all systems for multicore parallelization! The socket approach works on all systems.

{{% /warning %}}


## The method behind parallelization

The Central Processing Unit (CPU) of your computer contains small units called "cores". The number of cores available determines how many different tasks you can execute at the same time. Then, creating clusters is like forming teams of these "cores". You send data and functions to each cluster, where each core works on a different part of the task. In theory, the computation can be executed as many times faster as the cores you have available, e.g. 4 available cores speed up your computation to 1/4 of the time. 

However, overhead makes this less in practice. Overhead involves things such as starting the sub-processes and copying the data over to those processes, and communicating back and collecting the results. Therefore, in reality, this maximum time-saving is not likely to be reached.

You can determine the number of available cores, i.e. the number of computations that can be executed at the same time, with the `detectCores()` function. 

{{% codeblock %}}
```R
#load package
library(parallel)

detectCores()
```
{{% /codeblock %}}


## Multicore approach

The easiest application of the multicore approach is the `mclapply()` function of the `parallel` package in R. As `apply()` iterates over a data structure while applying a function to each subset, `lapply()` is used to iterate over a list, `mcapply` applies parallelization by iterating into multiple processes (the cores). The multicore approach copies the entire current version of R and moves it to a new core, so exporting variables and loading already loaded packages again is not necessary.

### Example 

This simple example calculates the mean sepal length for each species in the `iris` dataset available within R. Check the summary statistic of the dataset yourself by running `summary(iris)`, if you want to know more about this data set.

{{% tip %}}

[This Google Colab file](https://colab.research.google.com/drive/1viBfVPepuSukf8jndaII9pPN2nznVybD?usp=sharing) contains all the code examples of parallelization used in this article!
{{% /tip %}}

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
    Sys.sleep(2) # Simulating a 2-second computation
    means[i] <- mean(df[df$Species == species[i], "Sepal.Length"])
  }
  return(data.frame(Species = species, Mean_Sepal_Length = means))
}
```
{{% /codeblock %}}

The function simulates a computionationally intensive task by pausing the execution of the code for 2 seconds in each iteration with adding `Sys.sleep(2)`. The code will be executed, first as a normal computation and then with parallelization. The `system.time()` function is used to measure the execution times such that we can compare them and show the benefits of parallelization. 

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

The multicore computation is faster than the normal computation, with `4.035` seconds against `6.018` seconds. These times likely differ for you. 

## Socket approach

The socket approach slightly differs from the multicore approach. Here, you have to make a socket cluster first, and manually copy the data and code to each cluster member (the cores). This is the key difference with the multicore approach, in which exporting was not necessary.

### Example

The following example provides the basic steps on how to make a cluster and let it execute your task. To test its efficiency, we will compare the time needed to execute code being executed with and without parallelization.

{{% warning %}}

With the socket approach, a new version of R is launched on each core. Therefore, any message from your computer requesting permission for R to accept incoming connections you should accept.

{{% /warning %}}


1. Determine the number of cores available

Before you create a cluster, you can determine the number of cores that are available on your system.

{{% codeblock %}}
```R
# Determine number of cores available
ncpu <- detectCores()
```
{{% /codeblock %}}

The number of cores is determined by your computer's hardware configuration and is `2` in my Google Colab. This can differ for you, and therefore might lead to different results in computation speed. 

Sometimes you might want to use only a percentage of the available CPU cores instead of all cores, to leave some CPU capacity for other system tasks. In that case, you can multiply the `detectCores()` value by the percentage you want to use (e.g. `0.8`) and set that as a value for `ncpu` (i.e. the number of CPU cores to be used for parallel processing).

2. Create cluster
   
{{% codeblock %}}
```R
# Create a parallel cluster
cl <- makePSOCKcluster(ncpu)
```
{{% /codeblock %}}


3. Execute code in parallel

The socket approach doesn't have anything loaded in yet, so any loaded packages, variables, data, functions, etc. that the cluster needs to execute the code needs to be moved into each process. This can be done with the `clusterExport()` function. Below, a function is exported to the cluster as an example.

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

You can use the `parLapply()` function to perform a `lapply()` function across multiple nodes in a socket cluster.

{{% /tip %}}


4. Compare time to that of the same task without parallelization

{{% codeblock %}}
```R
time_normal
time_socket
```
{{% /codeblock %}}

Again, parallelization has saved time, comparing `4.035` seconds for executing the task with the socket approach to `6.018` seconds for the normal computation. 

## When to parallelize

As already mentioned in the beginning, the theoretical time saving is not the same as the realistic increased efficiency, due to the overhead that is involved with copying data and function to each processor. The potential speedup may follow Amdahl's Law, a principle in computer science that tells us the overall speedup you can achieve is limited by the proportion of the computation that can be parallelized, as well as the number of cores. For example, if only 60% of your task can be parallelized, the overall task can only be twice as fast since the other 40% is still limited by other processes that have not been parallelized. As the examples in this article pointed out, the repetitive task with the loop intuitively has the highest potenital for being parallelized and indeed showed time saving when parallelizing.



### Multicore versus socket approach

Based on [Josh Errickson](https://dept.stat.lsa.umich.edu/~jerrick/courses/stat701/notes/parallel.html), this table summarizes the key differences between the multicore and socket approach.

|                   *Multicore*                  | *Socket*                                         |
|-----------------------------------------------|--------------------------------------------------|
| Available on Unix-like systems, <br> e.g. Mac and Linux | Works on all systems, <br> also Windows                           |
| Generally faster    | Slower due to extra overhead <br> time; launching new versions <br> of R on each core      |
| Workspace exists in each <br> process,   since it copies the <br> existing version of R  | Export variables, loaded <br> packages, etc. in each <br> process separately     |
|   Easier to implement   | A bit more complicated                          |


{{% warning %}}

When generating random numbers in parallel, be careful. This might cause issues as is not possible to generate the exact same numbers in each of the cores. Also, reproducing the same random numbers with `set.seed()` will not work the same. The `parallel` package offers a way to overcome this issue. Check [Chapter 20.4 of this guide](https://bookdown.org/rdpeng/rprogdatascience/) for an example.

{{% /warning %}}


{{% summary %}}

There is benefit of parallelization especially in substantial computations. If the computation is already fast, the overhead involved with parallelization tasks might take more time than it saves. After reading this topic, you have a comprehensive understanding of parallel computing and you can discover the use of it yourself, and find out how it can offer advantages for you!

{{% /summary %}}
