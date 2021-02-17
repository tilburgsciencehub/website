---
title: "Using AWS S3 with Python"
description: "This block explains how to list contents, download content from and upload content to a AWS S3 bucket."
keywords: "aws, python, data"
date: 2021-02-17
weight: 1
---

## Overview <!-- Goal of the Building Block -->

Provide a brief overview of the issue to solve, or describe why this is a best practice.

Add any special requirements or attach a dummy data set if needed.


## Code <!-- Provide your code in all the relevant languages and/or operating systems and specify them after the three back ticks. Do NOT remove {{% codeblock %}} -->

{{% codeblock %}} <!-- You can provide more than one language in the same code block -->

[python-link](code.py) <!-- OPTIONAL: You can also provide your code as a downloadable file (useful for very long codes). Make sure you place this file in the same folder. Specify in [square brackets] the language followed by "-link" as shown here.-->


```python
# Import the necessary packages
import boto3

# Make sure you have reading and writing privileges on AWS user settings
# Define credentials
your_aws_access_key_id = "" #enter your AWS Access Key here
your_aws_secret_access_key = "" #enter your AWS Secret Access Key here
your_aws_region_name = "" #enter your AWS bucket region here


# Create an S3 client
s3 = boto3.client('s3', region_name= your_aws_access_key_id,
                  aws_access_key_id= your_aws_secret_access_key,
                  aws_secret_access_key= your_aws_region_name)

your_aws_bucket_name = "" # specify the bucket you want to use


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

Lastly, include a brief summary to wrap up your article.

{{% /summary %}}
