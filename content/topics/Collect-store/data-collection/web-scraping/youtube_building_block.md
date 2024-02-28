---
title: "Extract Data Using the YouTube API"
description: "Learn how to extract data from YouTube using the YouTube API."
keywords: "api, application programming interface, data collection, YouTube"
draft: false
icon: "fa-solid fa-database"
category: "reproducible"
aliases:
  - 
---

## Extracting Data Using the YouTube API

### Overview

Google has made a very accessible API for developers to extract data from different YouTube channels. There is a wide variety of data you can access through this API. The API can be used in the Python programming language, which is what this building block will focus on. 

In this article, we cover how to set up access to the YouTube API and how to access it in Python, and then we briefly explain how you can use it and how you can use the Youtube API documentation to help you use it.

### Setting up the API Access
The first thing you have to do if you want to use the YouTube API is request an API key with YouTube. There is a daily limit on how many requests a single person can make to the YouTube API hence you need a personal API key. You can request this API key through the Google Cloud platform with your Google account using the following steps.

-   Go to the [Google Cloud website](https://cloud.google.com) (make sure you are logged in to your Google account).
-   Open the console (top right of the page).
-   Create a project for your data collection (click on select a project -> new project) and select the project
-   Navigate to the page APIs and Services -> credentials
-   Create an API key (Create Credentials -> API key)

You can now copy your API key when clicking SHOW KEY. The APIs and Services page can also be used to track your used and remaining tokens. Congratulations you can now use the YouTube API.

### Accessing the API in Python

To access the YouTube API in your Python script you will need the `google-api-python-client` Python package that you can install through pip. In your Python script, you can import this package and create a service that functions as your connection to the YouTube API.

{{% codeblock %}}
```Python
from googleapiclient.discovery import build

service = build("youtube", "v3", developerKey="your_api_key")
```
{{% /codeblock %}}

Using this service, you can access a lot of data about videos, channels, and comments within YouTube. One thing to take into account though is that the API mostly works with Channel and video IDs rather than their names, hence if you want to collect data about specific YouTube channels or videos you need to find their ID first. Fortunately for YouTube videos, the ID is simply in the URL of the video. 

A typical YouTube video URL will be of the form `https://www.youtube.com/watch?v={VIDEO_ID}`. Let's consider a video from Tilburg Science Hub as an example. The video can be found [here](https://www.youtube.com/watch?v=-qOTEMVT9zM) and has video ID -qOTEMVT9zM as we can find from the URL. We can extract some basic information using the following code.

{{% codeblock %}}
```Python
from googleapiclient.discovery import build

service = build("youtube", "v3", developerKey="your_api_key")

information = service.videos().list(id='-qOTEMVT9zM', part='snippet').execute()
```
{{% /codeblock %}}

The output of the list function is a dictionary and can be printed and the information can be accessed just as with any dictionary. 

You can also request data on multiple videos at the same time by giving the function multiple video IDs as follows:

{{% codeblock %}}
```Python
from googleapiclient.discovery import build

service = build("youtube", "v3", developerKey="your_api_key")

information = service.videos().list(id='-qOTEMVT9zM, JIqPDE-lrLs', part='snippet').execute()
```
{{% /codeblock %}}

There is a maximum on the number of videos you can request in one request, you can give a list that exceeds this amount but then you will have to make multiple requests to get all the data. For example, if we want to extract information from all items in a playlist that has thousands of videos we can use the following code:

{{% codeblock %}}
```Python
from googleapiclient.discovery import build

service = build("youtube", "v3", developerKey="your_api_key")

while True:
    # Retrieve a batch of video items from the playlist
    result = service.playlistItems().list(playlistId=playlist_id,
                                       part='snippet',
                                       maxResults=100,
                                       pageToken=next_page_token).execute()

    next_page_token = res.get('nextPageToken')

    # Do something with the information extracted

    if next_page_token is None:
        break
```
{{% /codeblock %}}

### Use the Documentation

There is a lot of information you can extract using the YouTube API. It is all documented on their documentation page. The documentation page is quite technical and sometimes a little hard to read but with a little practice becomes very usable. You can find the documentation page [here](https://developers.google.com/youtube/v3/docs). 

{{% tip %}}
Not everything on the documentation page is relevant. If you want specific information go to the category that information would fall under and select 'list'. The list function is used for data extraction. Then under 'Response' you can see what the typical output of this function is. If you then select the listed Resource this will show all the information that you can get using the list method and what 'part' parameter to choose to get specific information.
{{% /tip %}}

{{% summary %}}
To use the Youtube API you first have to create an API key in Google Cloud, you can then use this API key in your Python script to set up a connection to the API. Finally using this connection you can extract a lot of different types of data from YouTube. 
{{% /summary %}}


