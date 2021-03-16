---
title: "Download Data Programmatically"
description: "Learn how to download data right from its (online) source and store it locally with code."
keywords: "download, import data, store, collect"
date: 2021-02-08
draft: false
weight: 1
aliases:
  - /store/data
  - /store/data-programmatically
---

## Overview

Download a file from a URL and store it on your local machine. That way, it's super easy for *others* to run your workflow (e.g., team members), or to refresh the data once it's been udpated. All you need to do is rerun your code - that's it!

## Code

Here's an example of how to download data from within R.

{{% codeblock %}}
```R
download_data <- function(url, filename, filepath) {
  # create directory
  dir.create(filepath)
  # download file
  download.file(url = url, destfile = paste0(filepath, filename))
}

download_data(url = "http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2020-12-12/visualisations/reviews.csv", filename = "airbnb_listings.csv", filepath = "data/")
```
{{% /codeblock %}}

## Advanced Use Cases

### Running the download code from the terminal

If you want to download data to work on it in a data pipeline, it's useful to include the download snippet in a source file (e.g., `download.R`). You can then save the script, and run it from the terminal (e.g., as part of a `make` workflow).

In your command line/terminal, you can enter:

{{% codeblock %}}
```bash
R --vanilla < download.R
```
{{% /codeblock %}}

### Download data to different directories

Keep in mind that the `filepath` is dependent on the location from where your R script is called. The use of absolute directory names (e.g., `c:/research/project`) should be avoided so that the code remains portable to other computers and work environments.

### Open (rather than download) data

The code snippet above just *downloads* the data from the web, but does not yet open it in R. If the target data is in tabular format (i.e., has rows and columns), you could directly load it into R using the `read.table` function.

{{% codeblock %}}
```R
airbnb <- read.table("http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2020-12-12/visualisations/reviews.csv", sep = ',', header = TRUE)
```
{{% /codeblock %}}

### Downloading data from Google Drive

The Google Drive API offers a way to programatically download and upload files through, for example, a Python script. Keep in mind that this only works for files stored in your own Google Drive account (i.e., your own files and those shared with you).


{{% warning %}}
Unfortunately, the procedure described in the first code snippet does not work for Google Drive sharing links. The steps below may require some set-up time and technical know-how, but they can be re-used for a variety of cloud services. 
{{% /warning %}}


#### Google Cloud Platform
Like Amazon and Microsoft, Google offers cloud services (e.g., databases and compute resources) which you can configure through an [online console](https://console.cloud.google.com/home). In Google Cloud Platform you can also enable services like the Google Drive API, which we'll make use of here. Follow the steps below to get started.

{{% tip %}}
Google offers a 90-day trial with a €300 credit to use, but you can keep on using the Drive API after that because it's free to use. In other words, you can following along without filling out any creditcard or debit card details.
{{% /tip %}}

1. Sign in to [Google Cloud Platform](https://console.cloud.google.com/home) and agree with the terms of use (if necessary). 

2. Click on "Create New Project", give it a project name (e.g., `GoogleDriveFiles`), and click on "Create".

![new-project](../images/new_project.png)


3. Next, we need to set-up a so-called OAuth2 client account which is a widely used protocol for authentication and authorization of API services. 
   * In the left-side bar click on "APIs & Services" > "OAuth consent screen".
   * Set the user type to "External" and click on "Create".
   * Give your app a name (can be anything) and fill out a support and developer email address. Click "Save and continue" (it may sometimes throw an app error, then just try again!).
   * Click "Save and continue" twice and then "Back to dashboard".
   * Click on "Publish app" and "Confirm".
   * In the left sidebar, click on "Credentials" and then "Create Credentials" > "OAuth client ID" > "Desktop app" and click on "Create". It will show you your client ID and client secret in a pop-up screen. Rather than copying them from here, we will download a JSON file that contains our credentials. Click on "OK" and then on the download symbol: 
![download-credentials](../images/download_credentials.png)

   * Rename the file to `client_secret.json` and store it in the same folder as the scripts you'll use to download and upload the files.
  
4.  By default, the Google Drive API is not activated, so search for it in search bar and click on "Enable".  

5. Download the following [Python script](https://github.com/RoyKlaasseBos/tsh-website/blob/master/content/building-blocks/store-and-document-your-data/store-data/google_drive.py) ("Raw" > "Save as") and put it in the same directory as the client secret.

6. Run the folllowing command to install the Google Client library:  

{{% codeblock %}}
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
{{% /codeblock %}}

7. Create a new Python script (or Jupyter Notebook) and run the following code to set-up an API connection.

#### API Connection

{{% codeblock %}}
```python
import io, os
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.http import MediaFileUpload
from google_drive import create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
```
{{% /codeblock %}}

The first time a new window may pop up that asks you to authenticate yourself with your Google account. Click on "Allow".  
![authenticate](../images/authenticate_Drive.png)

Depending on whether you'd like to download or upload a file, follow one of both approaches: 

#### Download a file
{{% codeblock %}}
```python
request = service.files().get_media(fileId="<FILE_ID>")
fh = io.BytesIO()

downloader = MediaIoBaseDownload(fd=fh, request=request)

done = False

while not done: 
    status, done = downloader.next_chunck()
    print("Download progress {0}".format(status.progress() * 100))
    
fh.seek(0)

with open("<FILE_NAME.extension>", 'wb') as f:
    f.write(fh.read())
    f.close()
```
{{% /codeblock %}}

* You can find the `<FILE_ID>` by navigating towards the file in your browser and clicking on "Open in new window". The URL then contains the file ID you need. For example, the file ID of `https://drive.google.com/file/d/XXXXXX/view` is `XXXXXX`.  
![open_new_window](../images/open_new_window.png)

* Larger files may be split up in separate chuncks. The progress will be printed to the console.

* To save the file in a subdirectory, you can use the following syntax: `os.path.join("./<SUBDIRECTORY>", "<FILE_NAME.extension>")` within the `open()` function.


#### Upload a file
{{% codeblock %}}
```python
file_metadata = {
    "name": "<FILE_NAME.extension>",
    "parents": ["<FOLDER_ID>"]
}

media = MediaFileUpload("<FILE_NAME.extension>", mimetype="<MIME_TYPE>")

service.files().create(
    body = file_metadata,
    media_body = media,
    fields='id'
).execute()
```
{{% /codeblock %}}

* The `<FOLDER_ID>` can be obtained in a similar way as the `<FILE_ID`>: navigate towards the folder where you'd like to save the file and look for the identifier within the URL.

* The `MediaFileUpload()` function assumes that the file supposed to be uploaded is stored in the current directory. If not, add the subdirectory in which the file is stored to the path.

* `<MIME_TYPE>` informs Google Drive about the type of file to be uploaded (e.g., `csv`, `jpg`, `txt`). You can find a list with common MIME types over [here](https://learndataanalysis.org/commonly-used-mime-types/). For example, for a csv-file it is: `text/csv`.

