---
title: "Use AWS S3 Buckets"
description: "This block explains how to list contents, download content from and upload content to an AWS S3 bucket with boto3."
keywords: "aws, s3, boto3, python, bucket, list contents, upload, dowload, automate"
#date: 2021-02-17
weight: 1
author: "Nazli Alagöz"
authorlink: "https://www.tilburguniversity.edu/staff/n-m-alagoz"
aliases:
  - "/use/aws-s3"
---

## Overview

Discover how to leverage the power of Amazon Simple Storage Service (AWS S3) to store and retrieve files in a fast and secure manner. In this building block, we'll explore how to establish a connection to an AWS S3 bucket, list the objects within it, and upload or download files using Python and the boto3 package. These skills will empower you to seamlessly integrate AWS S3 into your research workflows, boosting your data management capabilities.

## AWS S3 Buckets 

[Amazon Simple Storage Service](https://aws.amazon.com/s3/) (AWS S3) is an industry-leader object storage service that allows you to store and retrieve any kind of files fast, securely and anywhere in the world - basically Dropbox on steroids. It can be used for a range of use cases, from websites to backups and archives. It can also be particularly useful for research projects - storing a huge amount of raw data, for instance.

In AWS S3, storage units are referred to as **buckets**. Essentially, a bucket is a container for objects (files). Every object in S3 must reside within a bucket. Users have the flexibility to create as many buckets as they need. Moreover every bucket can contain as many folders as desired. 

If you are using AWS S3 to store data necessary for your research and want to incorporate downloading and uploading your data files to AWS S3 into a [`make`](/building-blocks/configure-your-computer/automation-and-workflows/make/) script, it is useful to use a code script to interact with your AWS S3 bucket instead of the command line. Keep reading to learn how to do it.

{{% warning %}}
You need to have access to an AWS S3 bucket and have the credentials to run the following code.

Whenever you interact with AWS, you must specify your security credentials to verify who you are and whether you have permission to access the resources that you are requesting. For instance, if you want to download a file from an AWS S3 bucket, your credentials must allow that access.

Learn more about AWS credentials [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
{{% /warning %}}

## Handle AWS S3 through Python

The following code snippets show how to set up a connection with AWS S3 using Python with boto3, to then carry out some useful related operations including how to list files in your bucket, as well as upload and download them.

The first step would be to install boto3 - the AWS SDK for Python - via [pip](/building-blocks/configure-your-computer/statistics-and-computation/python-packages/):

{{% codeblock %}}
```bash
pip install boto3
```
{{% /codeblock %}}

### Set up a connection with AWS S3

With boto3 installed, your next step will be to establish a connection with S3.

{{% codeblock %}}

```python
# Import the necessary packages
import boto3

# Define credentials and make sure you have reading and writing privileges on AWS user settings
your_aws_access_key_id = "" # Enter your AWS Access Key
your_aws_secret_access_key = "" # Enter your AWS Secret Key
your_aws_region_name = "" # Enter your AWS bucket region


# Create an S3 client
s3 = boto3.client("s3",
    region_name = your_aws_region_name,
    aws_access_key_id = your_aws_access_key_id,
    aws_secret_access_key = your_aws_secret_access_key)

your_aws_bucket_name = "" # Specify the bucket you use
```

{{% /codeblock %}}

### List objects in your AWS bucket and print them

With your connection ready, the following code snippet will list the objects present in your bucket.

{{% codeblock %}}

```python
# List objects in your AWS bucket and print them
objects = s3.list_objects(Bucket = your_aws_bucket_name)
print(objects)
```

{{% /codeblock %}}

### List the names of the objects in bucket contents

While the previous code snippet returns a list of the objects in your bucket alongside some other relevant information and metadata, if you are interested in retrieving filenames only, you can use the following snippet instead.

{{% codeblock %}}

```python
# List the names of the objects in bucket contents
for object in objects["Contents"]:
    print(object["Key"])
```

{{% /codeblock %}}

### Upload a file

You can use the following code snippet to upload files to your bucket through Python.

{{% codeblock %}}

```python
# To upload a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
filetoupload = "hello.txt"

# Upload the file to S3
s3.upload_file(filetoupload, your_aws_bucket_name, "remote-object-name.txt")
```

{{% /codeblock %}}

### Download a file

Conversely, the code snippet below allows you to download files from your bucket.

{{% codeblock %}}

```python
# Download a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
s3.download_file(your_aws_bucket_name, "remote-object-name.txt", "local-file-name.txt")
```

{{% /codeblock %}}

## See also

- Learn more about [AWS S3](https://aws.amazon.com/s3)
- Learn more about [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), the AWS SDK for Python
- Learn more on how to upload files with [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
- Learn more on how to download files with [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html)

{{% summary %}}

- AWS S3 is a reliable and flexible storage service that supports a variety of use cases, including research projects.

- Boto3 simplifies the process of interacting with AWS S3 buckets using Python, enabling automation of file uploads and downloads and more.

- You can employ the `list_objects` function to retrieve information from the objects in your bucket.

- Uploading files to an S3 bucket can be done with the `upload_file` function, specifying the file and target object name.

- Downloading files from an S3 bucket is straightforward with the `download_file` function, specifying the bucket, object name, and desired local file name.

{{% /summary %}}
