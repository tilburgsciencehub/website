---
title: "Automating Reports With Quarto"
description: " "
keywords: "Quarto, quarto, interactive, dashboard, report, automating, presentation, document, markdown, set-up, install, guide, command line, interface, tool, command line interface, CLI"
draft: false
author: "Valerie Vossen"
weight: 5
aliases:
  - /quarto-reports
---

## Overview

[Quarto](https://quarto.org/) is an open-source scientific and technical publishing system that enables you to create and share interactive documents, presentations, dashboards and reports. This topic demonstrates the process of creating a report with streaming data directly extracted from an API.

An example report is created with data collected from the API of the [music-to-scrape website](), with Python. This report is automated, thus updated weekly to the most recent data.


{{% tip %}}

To get started with Quarto, refer to these articles first:

- [Quarto setup guide](/quarto-setup) for detailed instructions on installing Quarto
- [Create your first document with Quarto](/quarto-use)

{{% /tip %}}


## Example: Generating a report with Quarto


As an example, we create a Quarto report with streaming that. Specifically, the goal is to give a summary of the top 5 artists streamed that week, and their number of plays. This report should automatically update in a new week. 

Specifically, with Python code, we extract data from the API to a Pandas dataframe. This dataframe is printed and shows the top 5 artists of that specific week, with the total plays. After, an interactive visualization is created, all outputted in a single HTML document. The table and chart automatelly update with new data!


{{% tip %}}

To follow this example, preview the [Quarto document]() yourself.
This is the output: [HTML output file]()

{{% /tip %}}

The following steps create the Quarto document:

### Extracting the data 

First, we extract the streaming data from the API. 


{{% codeblock %}}
```python
# Import the required libraries
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime 
import plotly.express as px

# Function to get top 5 artists with total plays

def get_top_artists_dataframe():
    # Specify the URL of the API
    api_url = "https://api.music-to-scrape.org"
    
    # Send an HTTP GET request to the API
    response = requests.get(api_url+'/charts/top-artists')
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the chart data and timestamps
        artists_data = data.get('chart', [])
        unix_start = data.get('unix_start')

               # Convert the unix_start timestamp to a datetime object
        start_date = datetime.utcfromtimestamp(unix_start)
        week_number = start_date.isocalendar().week
        
        # Create lists to hold artist names and plays
        artist_names = []
        total_plays = []
        
        # Populate the lists with data
        for item in artists_data:
            artist_names.append(item['name'])
            total_plays.append(item['plays'])
        
        # Create a DataFrame from the lists
        df = pd.DataFrame({
            'Artist': artist_names,
            'Total Plays': total_plays,
            'Week Number': week_number
        })
        return df
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None

# Dataset 
get_top_artists_dataframe()

```
{{% /codeblock %}}

The following dataset is created:

{{% table %}}

| Artist                      | Total Plays | Week Number |
|-----------------------------|-------------|-------------|
| The Jackson Southernaires    | 51          | 34          |
| Stevie Ray Vaughan           | 49          | 34          |
| SNOWPATROL                   | 45          | 34          |
| Sugar Minott                 | 44          | 34          |
| Nick Cave & The Bad Seeds    | 37          | 34          |

{{% /table %}}


## Visualizing the data

The data is visualized with an interactive bar plot, which can be outputted in a Quarto file as well:

{{% codeblock %}}
```python
def interactive_bar_plot(df):
    if df is not None:

        # Get week number from the DataFrame (to include in dynamic title)
        week_number = get_top_artists_dataframe()["Week Number"].iloc[0]

        # Sort the DataFrame by 'Total Plays' in descending order 
        df = df.sort_values(by='Total Plays', ascending=False)

        # Create an interactive bar chart with Plotly
        fig = px.bar(get_top_artists_dataframe(), x='Total Plays', y='Artist', 
                 title=f'Total Plays for Top 5 Artists - Week {week_number}',
                 labels={'Total Plays':'Total Plays'},
                 hover_data={'Artist':True, 'Total Plays':True, 'Week Number':False})

        fig.update_layout(xaxis_title='Artist', yaxis_title='Total Plays',
                      xaxis_tickangle=-45, template='plotly_white')
        fig.show()

# Create plot with recent data extracted from API
interactive_bar_plot(get_top_artists_dataframe())

```
{{% /codeblock %}}

This is a screenshot of the interactive barplot:

<p align = "center">
<img src = "../images/quarto-barplot.png" width="200">
</p>


## Automating the workflow

- Use of task schedulers (e.g. `cron` jobs for Linux/Mac, Task Scheduler for Windows) to run Quarto scripts at regular intervals.

- Automating Data Refresh and Report Generation:
Setting up scripts to scrape data, analyze it, and regenerate the report automatically.

