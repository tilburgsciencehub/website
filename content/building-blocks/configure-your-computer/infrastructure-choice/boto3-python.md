---
title: "Using AWS S3 with Python"
description: "This block explains how to list contents, download content from and upload content to a AWS S3 bucket."
keywords: "aws, python, data"
date: 2021-02-17
weight: 1
---

## Overview <!-- Goal of the Building Block -->

If you are using AWS S3 to store data necessary for your research and want to incorporate downloading and uploading your data files to AWS S3 into a MAKE script, it is useful to use a Python script to interact with your AWS S3 bucket instead of the command line.

You need to have access to an AWS S3 bucket and have the credentials that is required in the code. Next, the sample code chuck to do very simple downloading and uploading files to a AWS S3 Bucket is shown.


## Code

{{% codeblock %}} <!-- You can provide more than one language in the same code block -->

```python
# Import the necessary packages
import boto3

# Make sure you have reading and writing privileges on AWS user settings
# Define credentials
your_aws_access_key_id = "" #enter your AWS Access Key
your_aws_secret_access_key = "" #enter your AWS Secret Key
your_aws_region_name = "" #enter your AWS bucket region


# Create an S3 client
s3 = boto3.client('s3',
    region_name= your_aws_access_key_id,
    aws_access_key_id= your_aws_secret_access_key,
    aws_secret_access_key= your_aws_region_name)

your_aws_bucket_name = "" # specify the bucket you use


# List objects in your AWS bucket and print them
objects = s3.list_objects(Bucket = your_aws_bucket_name)
print(objects)

# List the names of the objects in bucket contents
for object in objects['Contents']:
    print(object['Key'])

# To upload a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
filetoupload = open('hello.txt', 'w')

# Upload the file to S3
s3.upload_file('hello_downloaded.txt',your_aws_bucket_name, 'hello-remote.txt')

# Download a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
s3.download_file(your_aws_bucket_name,'hello-remote.txt','hello_downloaded.txt')
```


{{% /codeblock %}}

{{% summary %}}

In this article, we showed you how to use Python to automate your uploads to and downloads from AWS S3. Hopefully, this is helpful to you.

{{% /summary %}}
