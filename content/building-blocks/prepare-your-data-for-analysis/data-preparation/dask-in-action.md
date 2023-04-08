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

## How to use Dask in a simple analytics task
To illustrate how to use Dask, we provide a practical example of an analytics task applied on a large dataset. We use a flights dataset, available at [Kaggle.com](https://www.kaggle.com/datasets/usdot/flight-delays), containing over 5M flight delays and cancellations from 2015. When loaded with `pandas`, the dataframe occupies more than 1.3GB of memory, which would make operations rather slow. Let's see how to load it with `dask` and how to perform some basic operations on it. For all operations we also provide the equivalent `pandas` code for comparison.

### Loading the data 

The first thing we need to do is import the `dask` library and load the data. 

{{% codeblock %}} 

[python-link](code.py) <!-- OPTIONAL: You can also provide your code as a downloadable file (useful for very long codes). Make sure you place this file in the same folder. Specify in [square brackets] the language followed by "-link" as shown here.-->


```dask
# import the Dask DataFrame module
import dask.dataframe as dd

#read the downloaded csv file
flights = dd.read_csv('../flights.csv', assume_missing=True, dtype={'CANCELLATION_REASON': 'object'})
```

```pandas
# import the Dask DataFrame module
import pandas as pd

#read the downloaded csv file
flights = pd.read_csv('../flights.csv')

```

{{% /codeblock %}}

The arguments `assume_missing` and `dtype` are added because of the following error occurred later on in the code: `ValueError: Mismatched dtypes found in pd.read_csv/pd.read_table`. The reason for this is that `dask` attempts to infer the types of all columns by reading a sample of the data from the start of the file. Sometimes it happens that the type of a column is different later in the file, which causes the error. By specifying `assume_missing=True` when reading the file, all integer columns that aren't specified in `dtype` are assumed to contain missing entries, thus are converted to float. Another way to avoid the issue is to specify the type each column should have using `dtype`.

{{% tip %}}

If you don't mention these arguments when reading the data and it raises the error, Python will give you a longer explanation for what causes the error and a possible solution to fixing it. This is what it looks like:
```
The following columns also raised exceptions on conversion:

- CANCELLATION_REASON
  ValueError("could not convert string to float: 'A'")

Usually this is due to dask's dtype inference failing, and
*may* be fixed by specifying dtypes manually by adding:

dtype={'AIR_TIME': 'float64',
       'ARRIVAL_DELAY': 'float64',
       'ARRIVAL_TIME': 'float64',
       'CANCELLATION_REASON': 'object',
       'DEPARTURE_DELAY': 'float64',
       'DEPARTURE_TIME': 'float64',
       'ELAPSED_TIME': 'float64',
       'TAXI_IN': 'float64',
       'TAXI_OUT': 'float64',
       'WHEELS_OFF': 'float64',
       'WHEELS_ON': 'float64'}

to the call to `read_csv`/`read_table`.

```

{{% /tip %}}

### Inspecting the data

Now that we loaded the data, let's see how it looks like and find some basic info about it.

{{% codeblock %}}

```dask
#check number of partitions
flights.npartitions

#display dataframe
flights.compute()

#display dataframe columns
flights.columns

#check shape of dataframe
flights.shape  #outputs delayed object
flights.shape[0].compute() #actually calculates number of rows

#the info() function doesn't give us the output we know from pandas, but instead only gives the number of columns, first and last column name and counts each dtype; alternatively we can do the following to get each dtype and non-null counts

#show types of columns
flights.dtypes

#count non-null
flights.notnull().sum().compute()

#alternatively, count null
flights.isna().sum().compute()
```


```pandas
#display dataframe
flights

#display dataframe columns
flights.columns

#check shape of dataframe
flights.shape 

#show types of columns
flights.dtypes

#dataframe info
flights.info()

```

{{% /codeblock %}}

Most of the operations are the same between the two libraries, except that in `pandas` there is no `npartitions()` function and we don't need to use `.compute()`, as explained in [Handle Large Datasets in Python](https://tilburgsciencehub.com/building-blocks/prepare-your-data-for-analysis/data-preparation/large-datasets-python/).  When running the code we can notice that the function `shape` doesn't display the expected output we know from `pandas`, but gives this: `(Delayed('int-4b01ce40-f552-432c-b591-da8955b3ea9c'), 31)`. We can only see the number of columns, but not the number of rows, which happens again from the lazy evaluation characteristic of `dask`. For `dask` to count how many rows there are, it needs to load each partition and sum up all rows.     


### Descriptive statistics, Grouping, Filtering

Now let's see some basic operations to manipulate the dataframe. In general, these are the same command as in `pandas` with the added `compute()` function at the end. 

{{% codeblock %}}

```dask
#compute descriptive statistics for the whole dataframe
flights.describe().compute()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe().compute()

#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0).compute()

#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum().compute()

#count the unique values from a column
flights['MONTH'].nunique().compute()

#display the flights from a certain month, here July
flights[flights['MONTH'] == 7].compute()

#group the airlines count per month
flights.groupby(by = 'MONTH')['AIRLINE'].count().compute()

```


```pandas
#compute descriptive statistics for the whole dataframe
flights.describe()

#alternatively, for just one column
flights['ARRIVAL_DELAY'].describe()

#compute the max value of a column
flights['DEPARTURE_DELAY'].max(axis = 0)

#sum the total delay per airline with groupby
flights.groupby(by = 'AIRLINE')['AIRLINE_DELAY'].sum()

#count the unique values from a column
flights['MONTH'].nunique()

#display the flights from a certain month, here July
flights[flights['MONTH'] == 7]

#group the airlines count per month
flights.groupby(by = 'MONTH')['AIRLINE'].count()

```

{{% /codeblock %}}

### Variable creation and plotting

When plotting large datasets, we can either use packages that can handle many data points, like [hvplot](https://pyviz-dev.github.io/hvplot/user_guide/Introduction.html) or [datashader](https://datashader.org/), or bring the data that we want to plot to a smaller shape that fits the memory. For this simple example we want to plot the count of airlines per month, which is not a large dataframe, so we can just use the classic `matplotlib` to make a graph.


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
monthly_flights.plot.bar(x = "MONTH", y='AIRLINE', figsize=(10,7), 
            title='Airlines count per month', xlabel="Month", 
            ylabel="Airline count", rot = 0, grid = True)
```


{{% /codeblock %}}



{{% summary %}}

`Dask` is a Python library suitable to use when dealing with larger datasets that don't fit the memory. It uses lazy evaluation, which means it doesn't actually execute operations or commands until actually necessary. Most of the functions are the same as in `pandas`, but remember to add `.compute()` after them if you actually want `dask` to compute the result at that point in your code. 

{{% /summary %}}

## See also
For more resources on `dask` check out these links:

- [Dask documentation](https://docs.dask.org/en/stable/)
- [Dask forum](https://dask.discourse.group/)
