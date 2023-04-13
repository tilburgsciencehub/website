---
title: "Practical Example with Dask"
description: "Dask in action, a practical example for how to use Dask in a simple analytics task: how is it different from Pandas, how to do descriptive statistics, create new variables, perform grouping, filtering and plotting."
keywords: "any, relevant, keywords, separated, by, commas, like, this"
date: 2023-04-06
weight: 2
author: "Ana Bianca Luca"
authorlink: "https://www.linkedin.com/in/ana-bianca-luca-b555561b2/"
aliases:
  - /learn/dask
  - /analytics/task
  - /real/example
---

## Using Dask to Describe Data
We learned how to [Handle Large Datasets in Python](https://tilburgsciencehub.com/building-blocks/prepare-your-data-for-analysis/data-preparation/large-datasets-python/) in a general way, but now let's dive deeper into it by implementing a practical example. To illustrate how to use Dask, we perform simple descriptive and analytics operations on a large dataset. We use a flights dataset, available at [Kaggle.com](https://www.kaggle.com/datasets/usdot/flight-delays), containing over 5M flight delays and cancellations from 2015. When loaded with `pandas`, the dataframe occupies more than 1.3GB of memory, which would make operations rather slow. Let's load the data with `dask`. For all operations we also provide the equivalent `pandas` code for comparison.

### Loading the data 

The first thing we need to do is import the `dask` library and load the data. Make sure that the downloaded data is in the same working directory as the Python file of the code.

{{% codeblock %}} 

[python-link](code.py) <!-- OPTIONAL: You can also provide your code as a downloadable file (useful for very long codes). Make sure you place this file in the same folder. Specify in [square brackets] the language followed by "-link" as shown here.-->


```dask
# import the Dask DataFrame module
import dask.dataframe as dd

#read the downloaded csv file
flights = dd.read_csv('flights.csv', assume_missing=True, dtype={'CANCELLATION_REASON': 'object'})
```

```pandas
# import the pandas module
import pandas as pd

#read the downloaded csv file
flights = pd.read_csv('flights.csv')

```

{{% /codeblock %}}


{{% tip %}}
The arguments `assume_missing` and `dtype` are added because it is likely that `dask` will raise a _ValueError_ due to its attempts to infer the types of all columns by reading a sample of the data from the start of the file. This attempt is sometimes incorrect, thus it may require to manually specify the type each column should have (with `dtype`) or to assume all integer columns have missing values and request their conversion to float (with `assume_missing`).

If you don't mention these arguments when reading the data and it raises the error, Python will suggest a possible solution to fixing it. 

{{% /tip %}}

### Inspecting the data

Now that we loaded the data, let's see how it looks like and find some basic info about it.
We can check to see in how many partitions the data has been divided and display the data using the following commands:

{{% codeblock %}}

```dask
#check number of partitions
flights.npartitions

#display dataframe
flights.compute()
```

```pandas
#display dataframe
flights
```
{{% /codeblock %}}

_Output:_
<p align = "center">
<img src = "../img/output1.png" width=400">
</p>


Because the dataframe is large, it is hard to see all the columns, so we can print them as follows. Additionally, we can also check the shape of the dataframe:

{{% codeblock %}}
```dask
#display dataframe columns
flights.columns

#check shape of dataframe
flights.shape  #outputs delayed object
flights.shape[0].compute() #actually calculates number of rows
```
```pandas
#display dataframe columns
flights.columns

#check shape of dataframe
flights.shape 
```
{{% /codeblock %}}

_Output:_
<p align = "center">
<img src = "../img/output2.png" width=400">
</p>


When running the code we can notice that the function `shape` doesn't display the expected output we know from `pandas`, but gives this: `(Delayed('int-4b01ce40-f552-432c-b591-da8955b3ea9c'), 31)`. We can only see the number of columns, but not the number of rows, which happens again from the lazy evaluation characteristic of `dask`. This means that although we, for instance, create a new variable using some operations, it doesn't actually execute them until we use the new variable. 
For `dask` to count how many rows there are, it needs to load each partition and sum up all rows.     



In `dask` the `info()` function doesn't give us the output we know from `pandas`, but instead only gives the number of columns, first and last column name and counts each dtype. Alternatively we can do the following to get each dtype and non-null/null counts:

{{% codeblock %}}

```dask
#show types of columns
flights.dtypes

#count non-null
flights.notnull().sum().compute()

#alternatively, count null
flights.isna().sum().compute()
```

```pandas
#show types of columns
flights.dtypes

#dataframe info
flights.info()

```

{{% /codeblock %}}
_Output:_

<p align = "left">                            <p align = "center">                         <p align = "right">
<img src = "../img/output3.png" width=200">   <img src = "../img/output4.png" width=250">  <img src = "../img/output5.png" width=250">
</p>                                          </p>                                         </p>










Most of the operations are the same between the two libraries, except that in `pandas` there is no `npartitions()` function and we don't need to use `.compute()`, as explained in [Handle Large Datasets in Python](https://tilburgsciencehub.com/building-blocks/prepare-your-data-for-analysis/data-preparation/large-datasets-python/).  


### Descriptive statistics, Grouping, Filtering

We want to investigate the delays, more specifically, what is the biggest delay? What airline has the largest amount of summed delays? Are there more airlines operating in summer months than in winter?

Let's start with descriptive statistics to get a grasp of the data:

{{% codeblock %}}

```dask
#compute descriptive statistics for the whole dataframe
flights.describe().compute()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe().compute()
```

```pandas
#compute descriptive statistics for the whole dataframe
flights.describe()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe()
```
{{% /codeblock %}}

_Output:_

<p align = "center">
<img src = "../img/output6.png" width=400">
</p>

What is the largest departure delay in the data? We can find that by using:

{{% codeblock %}}

```dask
#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0).compute()
```
```pandas
#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0)
```
{{% /codeblock %}}

_Output_:
1988


What airline has the largest amount of summed delays? We can find this by computing the sum of the airline delays grouped by airlines.

{{% codeblock %}}

```dask
#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum().compute()
```

```pandas
#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum()
```
{{% /codeblock %}}

_Output:_

<p align = "center">
<img src = "../img/output7.png" width=400">
</p>

Are there more airlines operating in summer months than in winter? We start by first checking if the data contains delays for all months of the year. Then, we count the airlines by grouping them per month.

{{% codeblock %}}
```dask
#count the unique values for month column
flights['MONTH'].nunique().compute()

#group the airlines count per month
flights.groupby(by = 'MONTH')['AIRLINE'].count().compute()

#take the maximum count of grouped airlines
flights.groupby(by = 'MONTH')['AIRLINE'].count().max().compute()

```
```pandas
#count the unique values for month column
flights['MONTH'].nunique()

#group the airlines count per month
flights.groupby(by = 'MONTH')['AIRLINE'].count()

#take the maximum count of grouped airlines
flights.groupby(by = 'MONTH')['AIRLINE'].count().max()

```

{{% /codeblock %}}

_Output:_

<p align = "center">
<img src = "../img/output8.png" width=400">
</p>


### Variable creation and plotting

When plotting large datasets, we can either use packages that can handle many data points, or bring the data that we want to plot to a smaller shape that fits the memory. For this simple example we want to plot the count of airlines per month, which is not a large dataframe, so we can just use the classic `matplotlib` to make a graph.

Thus, in our answer to the question "Are there more airlines operating in summer months than in winter?", we can visualize the counts of airlines for each month with a plot:

{{% codeblock %}}
```
#create new dataframe 
monthly_flights = flights.groupby(by = 'MONTH')['AIRLINE'].count().reset_index()

#converting the dataframe from dask to pandas
monthly_flights = monthly_flights.compute()

#convert month column to int type
monthly_flights['MONTH'] = monthly_flights['MONTH'].astype(int)

#create bar plot
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (10, 7))
 
# creating the bar plot
plt.bar(monthly_flights["MONTH"], monthly_flights["AIRLINE"], color ='orange',
        width = 0.4)
 
plt.xlabel("Month")
plt.xticks(range(monthly_flights['MONTH'].nunique()+1)) #include all x values
plt.ylabel("Airline count")
plt.title("Airlines count per month")
plt.grid()
plt.rcParams.update({'text.color': "white",
                     'axes.labelcolor': "white",
                     'xtick.color': "white",
                     'ytick.color': "white" ,
                     'font.size': 13})
plt.show()
```


{{% /codeblock %}}

_Output_:

<p align = "center">
<img src = "../img/output9.png" width=400">
</p>


As such, we can see that the three months of summer register generally higher airlines count than winter months.

{{% summary %}}

`Dask` is a Python library suitable to use when dealing with larger datasets that don't fit the memory. It uses lazy evaluation, which means it doesn't actually execute operations or commands until actually necessary. Most of the functions are the same as in `pandas`, but remember to add `.compute()` after them if you actually want `dask` to compute the result at that point in your code. 

{{% /summary %}}

## See also
For more resources on `dask` check out these links:

- [Dask documentation](https://docs.dask.org/en/stable/)
- [Dask forum](https://dask.discourse.group/)
