---
title: "Read & Write Data From APIs"
description: "Learn how to store your API data locally and read in the data for future use."
keywords: "api, application programming interface, read, write, export"
#weight: 5
#date: 2020-11-11T22:02:51+05:30
draft: false
aliases:
  - /collect-data/read-write-data-api
---

## Overview
After you have requested data from an API and extracted the required fields, you often want to convert the data into a format that is compatible with other software programs (e.g., Excel and R). A popular file format for tabular data is a Comma Separated Value (CSV) because it is simple, widespread, and compatible with most platforms. CSV files are file formats that contain plain text values separated by commas and can be opened by almost any spreadsheet program. In other cases, you may solely want to store the raw JavaScript Object Notation (JSON) data as a backup (simply because you don't know exactly what fields you'll need).


## Code
### Write Data to CSV
To faciliate writing to a CSV file, we'll make use of the `csv` library. If you want to add to an existing CSV file - rather than overwriting it - use the `a` flag (append) instead of the `w` flag (write).

{{% codeblock %}}
```Python
import csv
with open("<FILENAME>.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter = ";")
    writer.writerow(["<COLUMN_1>", "<COLUMN_2>"])
    for content in all_data:
        writer.writerow([<DATAFRAME>["<COLUMN_1>"], <DATAFRAME>["<COLUMN_2>"])
```
{{% /codeblock %}}

{{% tip %}}
If your data is already stored as a [pandas](https://pandas.pydata.org) DataFrame you can easily export it as follows: `<DATAFRAME>.to_csv("<FILENAME>.csv", index=False)`.
{{% /tip %}}


### Read CSV Data
The `read.csv()` method from the `pandas` library automatically converts the data into a DataFrame which provides rich functionalities for data analysis.
{{% codeblock %}}
```Python
import pandas as pd
df = pd.read_csv("<FILENAME>.csv", sep=";")
```
{{% /codeblock %}}

{{% tip %}}
If you encounter CSV files with a custom delimiter (i.e., symbol used to separate the data into rows and columns), you can explicitly indicate that with the `sep` parameter. For example, in this case the interpreter expects that data fields have been separated by semi-colons (`;`).
{{% /tip %}}


### Write Data to JSON
The `json` packages makes exporting raw JSON data (`JSON_FILE`) straightforward:

{{% codeblock %}}
```Python
import json
with open("<NAME_OF_JSON_EXPORT>.json", "w") as outfile:
    json.dump(<JSON_FILE>, outfile)
```
{{% /codeblock %}}


### Read JSON Data
In a similar way, you can import the JSON files with the same library.

{{% codeblock %}}
```Python
import json
with open("<NAME_OF_JSON_EXPORT>.json") as f:
    data = json.load(f)
```
{{% /codeblock %}}
