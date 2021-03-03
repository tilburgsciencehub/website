---
title: "Use AWS S3 Buckets"
description: "This block explains how to list contents, download content from and upload content to a AWS S3 bucket."
keywords: "aws, s3, boto3, python, bucket"
date: 2021-02-17
weight: 2
author: "Nazli Alagöz"
authorlink: "https://www.tilburguniversity.edu/staff/n-m-alagoz"
share: false
aliases:
  - "/use/aws-s3"
---

## Overview <!-- Goal of the Building Block -->

[Amazon Simple Storage Service](https://aws.amazon.com/s3/) (AWS S3) is an industry-leader object storage service that allows you to store and retrieve any kind of files fast, securely and anywhere in the world - basically Dropbox on steroids. It can be used for a range of use cases, from websites to backup and archives. It can also be particularly useful for research projects - storing a huge amount of raw data, for instance.

If you are using AWS S3 to store data necessary for your research and want to incorporate downloading and uploading your data files to AWS S3 into a [`make`](/building-blocks/configure-your-computer/automation-and-workflows/make/) script, it is useful to use a code script to interact with your AWS S3 bucket instead of the command line. Keep reading to learn how to do it.

{{% tip %}}
**Some terminology**

You will often read about AWS S3 "buckets". What are they?
Put simply, a bucket is a container for objects (files) stored in Amazon S3. Every object must be contained in a bucket. A single user can have as many buckets as they want. Inside a bucket, you can create as many folders you want.
{{% /tip %}}

{{% warning %}}
You need to have access to an AWS S3 bucket and have the credentials to run the following code.

Whenever you interact with AWS, you must specify your security credentials to verify who you are and whether you have permission to access the resources that you are requesting. For instance, if you want to download a file from an AWS S3 bucket, your credentials must allow that access.

Learn more about AWS credentials [here](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html).
{{% /warning %}}

## Code

We show you how to very simply upload and download files to a S3 bucket with [boto3]().

First off, install boto3 - the AWS SDK for Python - via [pip](/building-blocks/configure-your-computer/statistics-and-computation/python-packages/):

```bash
pip install boto3
```

### Establish a connection
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
{{% codeblock %}}

```python
# List objects in your AWS bucket and print them
objects = s3.list_objects(Bucket = your_aws_bucket_name)
print(objects)
```

{{% /codeblock %}}

### List the names of the objects in bucket contents
{{% codeblock %}}

```python
# List the names of the objects in bucket contents
for object in objects["Contents"]:
    print(object["Key"])
```

{{% /codeblock %}}

### Upload a file
{{% codeblock %}}

```python
# To upload a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html
filetoupload = open("hello.txt", "w")

# Upload the file to S3
s3.upload_file(filetoupload, your_aws_bucket_name, "remote-object-name.txt")
```

{{% /codeblock %}}

### Download a file
{{% codeblock %}}

```python
# Download a file
# Source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html
s3.download_file(your_aws_bucket_name, "remote-object-name.txt", "local-file-name.txt")
```

{{% /codeblock %}}

## See also

- Learn more about [AWS S3](https://aws.amazon.com/s3)
- Learn more about [`boto3`](https://aws.amazon.com/s3), the AWS SDK for Python
- Learn more on how to upload files with [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html)
- Learn more on how to download files with [`boto3`](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-download-file.html)

{{% summary %}}

In this article, we showed you how to use Python to automate your uploads to and downloads from AWS S3. Hopefully, this is helpful to you.

{{% /summary %}}
