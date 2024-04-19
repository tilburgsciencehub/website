---
title: "SQLite: a Database for Your Research Data"
description: ""
keywords: "research data storage, efficiency, SQL database"
#date: 2021-02-08
draft: false
weight: 2
author: "Maliheh Mahlouji"
aliases:
---

## Overview

In this article, we will introduce SQLite, an easy-to-use database for research data storage.
If you are not yet sure whether you need a database for your research data, 
you can read our article on [data storage options](https://tilburgsciencehub.com/topics/collect-store/data-storage/databases/csv-vs-database/).

## What is SQLite?

SQLite is a SQL library that implements a self-contained, 
serverless, zero-configuration SQL database engine. 
It is widely used in mobile applications and embedded systems. 
SQLite is a good choice for research data storage because it is lightweight, fast, and easy to use. 
It is also open-source and free to use. 

SQLite is architecturally different from traditional SQL databases, such as PostgreSQL or MySQL. For starters, it is a library that links to your application; not a standalone server that you connect to. Therefore, you don't need to install a separate server to use SQLite.
The entire database can be stored in a single file on disk which makes it easy to move the database around and share it with others, via email, flash drive, etc.

## When to choose other databases over SQLite?

If your data meets one of the below conditions, then SQLite might not be the best choice for you. We recommend using a more robust database like PostgreSQL, MySQL, or MariaDB.
- your data is already on a remote server, 
- you have loads of concurrent writers (because SQLite locks the table when writing),
- gazillion transactions per second (for the same reason as above),
- extremely large datasets (due to its single-file architecture)
{{% warning %}}
SQLite does not support stored procedures, triggers, or user-defined functions. In addition, since it is just a file, it doesn't come with all security features that a server-based database would have.
{{% /warning %}}
## How to use SQLite in R?

With the following code snippet, you can create a SQLite database in R.
{{% codeblock %}}

```R
# Install the RSQLite package once
install.packages('RSQLite', repos='http://cran.us.r-project.org')
--------------------------------

library(RSQLite)
library(DBI)

# Connect to an existing SQLite database file or create a new one
con <- dbConnect(SQLite(), "mydatabase.db")

```
{{% /codeblock %}}

Then you can use the connection object `con` to interact with the database.

Below you can see how to use SQL command to create a table, insert data to it, and then query that data. Query results are returned as a dataframe in R.


{{% codeblock %}}

```R
# Create a table
dbExecute(con, "CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data into the table
dbExecute(con, "INSERT INTO mytable (name, age) VALUES ('John', 30)")
dbExecute(con, "INSERT INTO mytable (name, age) VALUES ('Alice', 25)")

# Retrieve data from the table
result <- dbGetQuery(con, "SELECT * FROM mytable")
print(result)
```
{{% /codeblock %}}

If you have your initial data as CSV file, you can simply read it into a dataframe and then save it to a SQLite table.
Make sure to create a table following a code similar to above before writing the data to it.

{{% codeblock %}}

```R
# Connect to SQLite database
con <- dbConnect(SQLite(), "mydatabase.db")

# Read the CSV file into a dataframe
new_data <- read_csv("data.csv")

# Append data to an existing table in SQLite database
dbWriteTable(con, "mytable", new_data, append = TRUE)

```
{{% /codeblock %}}

Finally, don't forget to close the connection when you are done with it.
{{% codeblock %}}

```R
# Close the connection
dbDisconnect(con)
```
{{% /codeblock %}}