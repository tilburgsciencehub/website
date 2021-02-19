---
title: "Download Data Programmatically"
description: "Learn how to download data right from its (online) source and store it locally with code."
keywords: "download, import data, store, collect"
date: 2021-02-08
draft: false
weight: 1
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

### Downloading data from Dropbox or Google Drive

You can also use the code snippet above to download data directly from your personal Dropbox or Google Drive.

Just generate a download link for your file ([see here for Dropbox](https://help.dropbox.com/files-folders/share/view-only-access), [and here for Google Drive -- share a link to the file](https://support.google.com/drive/answer/2494822?co=GENIE.Platform%3DDesktop&hl=en#zippy=%2Cshare-a-link-to-the-file)).

All you need to do is to put your link in the code snippet above.

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
