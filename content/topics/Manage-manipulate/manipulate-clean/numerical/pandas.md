---
title: "Pandas for data manipulation in Python"
description: "Master data manipulation and analysis in Python with the pandas library."
keywords: "python, data science, data, programming, manipulation, analysis, tutorial"
draft: false
weight: 3
author: "Valerie Vossen"
aliases:
  - /learn/pandas
  - /pandas
---

## Overview

Pandas, a Python library built on top of the NumPy library, contains essential tools for anyone working with structured data in Python. It has numerous options for data manipulation and analysis tasks and this guide will provide you with the basics in 10 minutes! An introduction on the different data structures in pandas will continue into the key data manipulation techniques. 

## Import pandas

First, install pandas and numpy, using the [Install Python Packages](/get/python-packages) topic. Then import it with the following code:

{{% codeblock %}}
```python

import numpy as np
import pandas as pd

```
{{% /codeblock %}}


## Data structures in pandas

Pandas has two primary data structures: **Series** and **DataFrame**. 

### Series

The **Series** is a one-dimensional data structure, consisting of values and an index. You can create a Series using various data types, such as a list or a dictionary.

{{% codeblock %}}
```python

# List
grades = [5.5, 8.4, 9.6, 7.0, 7.5]

# Create Series from list
series = pd.Series(grades)
series

```
{{% /codeblock %}}

```python

0    5.5
1    8.4
2    9.6
3    7.0
4    7.5
dtype: float64

```

- Index

The default index is from 0 to n-1, where n is the length of the data. You can change this: for example if you want the indeces from 1 to n, or want to have different labels. 

{{% codeblock %}}
```python

# List

grades = [5.5, 8.4, 9.6, 7.0, 7.5]
series = pd.Series(grades, index = [1, 2, "3rd student", 4, 5])
series

```
{{% /codeblock %}}

```python

1              5.5
2              8.4
3rd student    9.6
4              7.0
5              7.5
dtype: float64
```

- Handling different data types

Series can handle different data types within the same structure. For example, the `grades` list now includes a string. 

{{% codeblock %}}
```python

# Including a string in the list
grades = [5.5, 8.4, "highest grade", 7.0, 7.5]

# Create Series
series = pd.Series(grades, dtype = object)

```
{{% /codeblock %}}

```python

0              5.5
1              8.4
2    highest grade
3              7.0
4              7.5
dtype: object

```

Here, the Series interprets elements as objects to accommodate the different data types (the data includes both floating-point numbers and a string). You can also specify the data type with the `dtype` parameter.

Data can also be a one-dimensional ndarray, a Python dictionary, or a scalar value. When creating a Series from a dictionary, the keys become the index and values become the data.

{{% codeblock %}}
```python

# Dictionary
grade_dict = {"Ellis": 9.6, "John": 8.5, "Casper": 5.3} 

# Create Series
series = pd.Series(grade_dict)
series

```
{{% /codeblock %}}

```python

Ellis     9.6
John      8.5
Casper    6.7
dtype: float64

```

Call `values` or `index` to see the individual component.

{{% codeblock %}}
```python

series.values

```
{{% /codeblock %}}

returns `array([9.6, 8.5, 5.3])`, and 

{{% codeblock %}}
```python

series.index

```
{{% /codeblock %}}

returns `Index(['Ellis', 'John', 'Casper'], dtype='object')`


### DataFrame

A DataFrame is a two-dimensional data structure in pandas, organized into rows and columns. Each column is essentially a pandas Series. While columns should have the same length, they can hold different data types.

You can create a DataFrame from a dictionary where keys become column names, and values form the data in those columns. 

By default, pandas intuitively generates index and column names. However, you can customize these by explicitly specifying them during DataFrame creation with the  `index` and `column` arguments. 


{{% codeblock %}}
```python
# Dictionary
grades = {
    'Name': ['Ellis', 'John', 'Casper'],
    'Midterm Grade': [9.6, 8.5, 5.3],
    'Final Grade': [9, 7, 6]
}

# Create DataFrame from Dictionary
df = pd.DataFrame(grades, 
                  index= ['Student 1', 'Student 2', 'Student 3'], 
                  columns= ['Name', 'Midterm Grade', 'Final Grade'])
df
```
{{% /codeblock %}}

```python

             Name  Midterm Grade  Final Grade
Student 1   Ellis            9.6            9
Student 2    John            8.5            7
Student 3  Casper            5.3            6

```

### Import data from another file

Instead of manually creating a DataFrame in Python, pandas provides convenient functions to import data from various file formats. 

- `read_csv()`: for importing data from CSV files
- `read_excel()`: for reading data from Excel files
- `read_html()`: to read data from HTML tables
- `read_sql()`: for importing data from SQL queries or database tables

To use these functions, provide the file path as an argument. For instance:

{{% codeblock %}}
```python

df2 = pd.read_excel("\\example_path\\file_name.xlsx")

```
{{% /codeblock %}}


## Inspecting data

To inspect your data, you can use the following functions:

- `.head()`: Displays the first few rows (default value is 5)
- `.info()`: Provides information on each column, such as the data type and the number of missing values.
- `.shape`: Returns the number of rows and columns.
- `.describe()`: Computes summary statistics for each numerical column, such as count, mean, standard deviation, minimum, 25th percentile, median, 75th percentile, and maximum.

For instance, to examine the DataFrame `df` that was created before:

{{% codeblock %}}
```python

df.shape
```
{{% /codeblock %}}

returns `(3, 3)`, indicating that `df` has 3 rows and 3 columns.

To explore specific aspects of the DataFrame, you can use `df.index`, `df.columns`, and `df.values`. For example:

{{% codeblock %}}
```python

df.index

```
{{% /codeblock %}}

returns `Index(['Student 1', 'Student 2', 'Student 3'], dtype='object')`


## Sorting data

Sorting data is the process of arranging it in a specific order. It can be useful for ...

- `sort_index()`: sort by index values along a specified axis. By default, sort data along the index axis (rows). 

- `sort_values()`: sort by values of the column specified with argument `by =`.

{{% codeblock %}}
```python

#### df!
df.sort_values(by = "Final Grade")

```
{{% /codeblock %}}

```python

             Name  Midterm Grade  Final Grade
Student 3  Casper            5.3            6
Student 2    John            8.5            7
Student 1   Ellis            9.6            9

```

The data is now sorted based on the values in the Final Grade column, with the lowest grade at the top and the highest at the bottom.


{{% codeblock %}}
```python

df.sort_values(by = "Final Grade")

```
{{% /codeblock %}}


To sorte in descending order and get the highest grade on top of the DataFrame, set ascending to `False`. 

{{% codeblock %}}
```python

df.sort_values(by = "Final Grade", ascending = False)
```
{{% /codeblock %}}

```python

             Name  Midterm Grade  Final Grade
Student 1   Ellis            9.6            9
Student 2    John            8.5            7
Student 3  Casper            5.3            6

```

## Subsetting data

To look at just one column, specify the column name within square brackets.
### short introduction missing!!

{{% codeblock %}}
```python
df["Final Grade"]
```
{{% /codeblock %}}

```python

Student 1    9
Student 2    7
Student 3    6
Name: Final Grade, dtype: int64

```

To subset multiple columns, provide a list of column names within square brackets:

{{% codeblock %}}
```python
df[["Final Grade","Name"]]
```
{{% /codeblock %}}

```python

           Final Grade    Name
Student 1            9   Ellis
Student 2            7    John
Student 3            6  Casper

```

To subset a specific row, you can use the `.loc[]` with the index label in between the square brackets.

{{% codeblock %}}
```python

df.loc['Student 1']

```
{{% /codeblock %}}

```python

Name             Ellis
Midterm Grade      9.6
Final Grade          9
Name: Student 1, dtype: object

```

To subset rows/columns based on specific conditions, you can use Boolean indexing. 
When subsetting based on multiple conditions:
- `&` (AND): BOTH conditions should hold for a row to be included.

{{% codeblock %}}
```python

# Midterm grade higher than 7 AND Final grade is 9
df[(df["Midterm Grade"] > 7) & (df["Final Grade"] == 9)]

```
{{% /codeblock %}}

```python

            Name  Midterm Grade  Final Grade
Student 1  Ellis            9.6            9

```

- `|` (OR): One or the other condition should hold for a row to be included.

{{% codeblock %}}
```python

# Midterm grade higher than 7 OR Final grade is 9
df[(df["Midterm Grade"] > 7) | (df["Final Grade"] == 9)]

```
{{% /codeblock %}}

```python
            Name  Midterm Grade  Final Grade
Student 1  Elli©            9.6            9
Student 2   John            8.5            7

```

## Adding, deleting, and renaming columns

To add a new column, assign values to a new column name. These values can be new, or calculated from the values of other columns in the DataFrame.For example, you want to have a new column with the age of each student, and one column with the mean of the Midterm and Final grade of each student.

{{% codeblock %}}
```python

df["Age"] = [19, 22, 21]
df["Mean Grade"] = (df["Midterm Grade"] + df["Final Grade"]) / 2
df

```
{{% /codeblock %}}

The two new column are added:

```python

             Name  Midterm Grade  Final Grade  Age  Mean Grade
Student 1   Ellis            9.6            9   19        9.30
Student 2    John            8.5            7   22        7.75
Student 3  Casper            5.3            6   21        5.65

```

To delete the Age column again, you can use `.drop()`. 
`axis=1` indicates that it's operating along columns. Note that the original DataFrame is not modified in place unless you set the inplace parameter to True:

{{% codeblock %}}
```python

df.drop('Age', axis = 1, inplace = True)
df

```
{{% /codeblock %}}


```python

             Name  Midterm Grade  Final Grade  Mean Grade
Student 1   Ellis            9.6            9        9.30
Student 2    John            8.5            7        7.75
Student 3  Casper            5.3            6        5.65

```

Rename column?


## Transposing data

With `.T` behind the DataFrame name, you change the axis: the columns and the indeces are switched.

{{% codeblock %}}
```python

df.T

```
{{% /codeblock %}}

```python

              Student 1 Student 2 Student 3
Name              Ellis      John    Casper
Midterm Grade       9.6       8.5       5.3
Final Grade           9         7         6
Age                  19        22        21
Mean Grade          9.3      7.75      5.65

```

## Handling missing data

Handling missing data is a crucial aspect of data analysis. In any real-world dataset, missing values are common and can impact the accuracy of your analysis. First, we create an example DataFrame with missing values.

{{% codeblock %}}
```python

data = {'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Eva'],
        'Age': [25, np.nan, 30, 22, 35],
        'Score': [90, 85, np.nan, 78, np.nan]}

df = pd.DataFrame(data)

```
{{% /codeblock %}}

```python

      Name   Age  Score
0    Alice  25.0   90.0
1      Bob   NaN   85.0
2  Charlie  30.0    NaN
3      NaN  22.0   78.0
4      Eva  35.0    NaN

```

- Detect missing data with `.isna().sum()`

{{% codeblock %}}
```python

df.isna().sum()

```
{{% /codeblock %}}

```python

Name     1
Age      1
Score    2
dtype: int64

```
This displays the number of missing values per column.

- Remove missing data with `.dropna()`

This function drops any rows that have missing data.
`df.dropna(axis=0)` removes rows with any missing values, and `df.dropna(axis=1)` removes columns.

{{% codeblock %}}
```python

df_droprow = df.dropna(axis = 0)
df_droprow

```
{{% /codeblock %}}

```python

  Name   Age  Score
0  Alice  25.0   90.0

```

Only the first does not contain missing values and is left in the new DataFrame.

{{% codeblock %}}
```python

df_dropcolumn =  df.dropna(axis = 1)
df_dropcolumn

```
{{% /codeblock %}}

```python

Empty DataFrame
Columns: []
Index: [0, 1, 2, 3, 4]

```

All columns contained missing values, so none are left.

- Filling missing data

Use `.fillna()` to fill missing values with a specific value that you specify inbetween the brackets. For example, fill the missing values with the mean of each column:

{{% codeblock %}}
```python

df.fillna(df.mean()) 

```
{{% /codeblock %}}

```python

      Name   Age      Score
0    Alice  25.0  90.000000
1      Bob  28.0  85.000000
2  Charlie  30.0  84.333333
3      NaN  22.0  78.000000
4      Eva  35.0  84.333333

```

Or you can use `method ='ffill'` or `method ='bfill'` to fill missing values with the previous or next valid value. For example:

{{% codeblock %}}
```python

df.fillna(method ='ffill')
```
{{% /codeblock %}}

```python


      Name   Age  Score
0    Alice  25.0   90.0
1      Bob  25.0   85.0
2  Charlie  30.0   85.0
3  Charlie  22.0   78.0
4      Eva  35.0   78.0

```

## Grouping

It is often useful to split the data set into groups based on specific criteria and apply a function to each group independently. Grouping allows for that.

### Splitting into groups

To split your data into gorups based on particular criteria or columns, you can use the `groupby()` method.

First, make an example DataFrame:




### GroupBy operations

Once you have your data grouped, you can perform different operations within each group, like aggregation, transformation, and filtration, to extract meaningful information from your dataset.
- Aggregation

.agg

- Transformation

.transform


- Filtration

Filtering groups


## Pivot tables


## Multi-level indexing




## Descriptive statistics


## Combining dataframes: merging and joining


## Data visualization


link to matplotlib topic


