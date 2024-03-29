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

Parallel computing is breaking down larger computations into smaller pieces, that can then be executed simultaneously. Instead of a single processor handling everything, multiple cores work together on different parts of the problem at the same time. This can speed up tasks by dividing the workload among the cores and completing them in parallel. While some libraries, such as `data.table` or `dplyr` have parallelization built in, researchers can also parallelize code that was not meant to be run in parallel in the first place! This topic shows the basic principles. Also, a simple code example is done with parallelization, and the time saved is demonstrated by comparing its time to execute to the same code that is run sequentially instead of simultaneously.

We discuss two approaches: multicore and socket approaching (The first one is not available for all operating systems?)

## The intuition behind parallel computing

The Central Processing Unit (CPU) of your computer contains small units called "cores". The number of cores available determines how many different tasks you can execute at the same time. Then, creating clusters are like forming teams of these "cores". You send data and functions to each cluster, where each core works on a different part of the task. In theory, the computation can be executed as many times faster as cores you have available. However, this is only in theory due to overhead, and this maximum time-saving is likely not possible. We will get back to this later.

{{% tip %}}

There is benefit of parallelization especially in substantial computations. If the computation is already fast, the overhead involved with parallelization tasks, such as starting the sub-processes and copying the data over to those processes, and communicating back and collecting the results, might take more time than it saves.

{{% /tip %}}

## Multicore approach

With the `mclapply()` function of the `parallel` package in R. As `apply()` iterates over a data-structure while applying a function to each subset, `lapply()` is used to iterate over a list. `mcapply` applies parellization by iterating into multiple processes (the cores). 


### Example 

This simple example calculates the mean sepal length for each species in the `iris` dataset available within R. If you want to know more about the data beforehand, you can check the summary statistic of the dataset yourself with running `summary(iris)`. 

{{% codeblock %}}
```R
# Load Iris dataset
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

screenshot of result_normal

Now, the same code with parallelization using `mclapply`():

{{% codeblock %}}
```R
# With parallelization using mclapply

start_time_multi <- Sys.time()
result_multi <- mclapply(split(iris, iris$Species), calculate_mean_sepal_length)
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

The multicore computation is 0.17, and the normal time computation is 0.45 seconds!

<!-- system.time() user and elapsed are roughly the same; normal with no parallelization (what does elapsed mean). Now using mclapply(), elapsed < user time (although not 1/4 when we use 4 cores)
User time = CPU time spent executing your R code (adding all tasks together, whether it is executed sequentially or in parallel)
Elapsed time = total real-world time that has elapsed from start of computation until it is completed. -->

## Socket approach

When forking is not available??

You make a socket cluster first, and manually copy the data and code to each cluster member (the cores). This is a key difference between "multicore" and "socket approach", as exporting is not necessary for the multicore approach.

{{% tip %}}
parLapply() is a function do to an lapply() function over a socket cluster
{{% /tip %}}


### Example

The following example provides the basic steps how to make a cluster and let make it execute your task. To test its efficiency, we will compare the time needed to execute code being executed with and without parallelization

1. Determine the number of cores available

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

The number of cores determines the number of computations that can be executed at the same time. Theoretically, having 4 number of cores would speed up your computation to 1/4 of the time. However, overhead time makes this less in practice. The perc_use represents the percentage of CPU cores you want to use for parallel computing, set to `0.8`. The rationale behind using a percentage instead of all cores could be to leave some CPU capacity for other system tasks. The number of cores available is detected with the function `detectCores` of the `parallel` package. This number is determined by your computer's hardware configuration. Multiplied with the percentage you want to use determines `ncpu`, the number of CPU cores to be used for parallel processing. 


2. Create cluster
   
{{% codeblock %}}
```R
# Create a parallel cluster
cl <- makePSOCKcluster(ncpu)
```
{{% /codeblock %}}


3. Execute code in parallel

With `clusterExport()`, you can export data and any other information that cluster will need to execute your code. By exporting, you send data or functions to the nodes of the cluster. In the example below, a function is exported to the cluster.

{{% codeblock %}}
```R
# Export function to cluster
clusterExport(cl, 'calculate_mean_sepal_length')

# Parallel computation function
calculate_mean_sepal_length_parallel <- function(df) {
  clusterApplyLB(cl, split(df, df$Species), calculate_mean_sepal_length)
}

# Run parallel computation
start_time_socket <- Sys.time()
result_socket <- calculate_mean_sepal_length_parallel(iris)
end_time_socket <- Sys.time()
time_socket <- end_time_socket - start_time_socket

```
{{% /codeblock %}}

4. Compare time to same task without parallelization

{{% codeblock %}}
```R
time_normal
time_socket
```
{{% /codeblock %}}

Time difference of 0.08 seconds for socket (compared to 0.45 for normal)


{{% warning %}}

Generating random numbers be careful; not possible to generate the exact same random numbers in each of the cores. Not possible to set.seed(). Way todo it in parallel package
{{% /warning %}}

{{% summary %}}

overhead time
difference multicore or socket approach, when to use which one?
{{% /summary %}}
