---
title: "Handle memory and storage within your Google Cloud instance" 
description: "After configuring a Google Cloud instance with GPUs, learn to import heavy files from Google Drive and handling memory issues"
keywords: "Docker, Environment, Python, Jupyter notebook, Google cloud, Cloud computing, Cloud storage, GPU, Virtual Machine, Instance, Memory, Bucket, Storage"
weight: 3
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2023-09-16 
aliases: 
  - /handle/memory-storage-issues
---

## Overview

This building block builds upon the foundational steps outlined in [Configure a VM with GPUs in Google Cloud](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/config-vm-gcp/).

After configuring our instance, we may find the necessity to manage large files proficiently or to circumvent memory issues that could potentially arise during code execution within the instance.

In this guide, you will learn how to:

- Connect our Docker container with Google Cloud Storage using GCSFuse.
- Use Google Colab for seamless file transfers between Google Drive and Google Cloud Storage.
- Manage and monitor resources in Linux environments to prevent memory allocation issues.

## Connect the Docker container to a GCS bucket 

[Storage buckets](https://cloud.google.com/storage/docs/buckets) are the native storage units of the Google Cloud platform. Linking them to your virtual machine offers integrated and efficient data management, simplifying scaling, backup, and access from anywhere in the Google Cloud infrastructure, eliminating, for example, the need to perform manual uploads/downloads via the Google Cloud's browser interface.

To do this, first of all, you will need to install [GCSFuse](https://github.com/GoogleCloudPlatform/gcsfuse) in your instance by running the following code:

{{% codeblock %}}
```bash
#1
$ export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

#2
$ sudo apt-get update

#3
$ sudo apt-get install gcsfuse
```
{{% /codeblock %}}

Now, create a new directory in your virtual machine, which will be the one connected to your bucket. After that, you can run the following, substituting 'YOUR_BUCKET' with the name of the storage bucket you wish to connect with your instance, and 'PATH_TO/NEW_DIRECTORY' to the path of the newly created directory that will host that connection:

{{% codeblock %}}
```bash
$ sudo gcsfuse -o allow_other YOUR_BUCKET PATH_TO/NEW_DIRECTORY
```
{{% /codeblock %}}

This code will tell GCSFuse to synchronize your new directory with your bucket. Then, you would be able to store any output produced in your projects in this new directory that you just created in your instance and it will be immediately at your disposal within your GCS bucket, and vice versa.


## Import large files: Use Google Colab as a bridge

The transfer and management of large files can be challenging due to extended upload/download durations. Yet, having connected your Google Cloud virtual machine to your storage buckets, you can swiftly transfer files that you already have hosted on **Google Drive** and **GCS Buckets** (and in turn to your virtual machine as well) using **Google Colab** as a bridge. This bypasses the need to manually Download/Upload files from Drive to your local machine and then to your cloud instance, potentially saving you significant amounts of time in the process.

It is suggested to utilize the same account for all Google tools. Doing so simplifies the authentication process and prevents potential permission issues, fostering a more seamless workflow.

{{% tip %}}
**Copy all directories you need**

When synchronizing the bucket with your directory inside the container, if your bucket contains other directories as well, the command `$ sudo gcsfuse -o allow_other your-bucket volume_path/new_dir/` might not copy those directories. 

Try `$ sudo gcsfuse --implicit-dirs -o allow_other your-bucket volume_path/new_dir/` to make sure the implicit directories are also included if you want them to.

{{% /tip %}}

To start with, make sure your bucket is created. To do so, you can follow [these](https://cloud.google.com/storage/docs/creating-buckets)  short guidelines.

To continue, launch a notebook in **Google Colab**, preferably the one you plan to run on your instance later. This approach helps you maintain a record of the code you've used. 

Subsequently, to mount your **Google Drive** to this notebook, use the following code:

{{% codeblock %}}
```python
from google.colab import drive
drive.mount('/content/gdrive')

```
{{% /codeblock %}}

Next, we authenticate our user:

{{% codeblock %}}
```python
from google.colab import auth
auth.authenticate_user()

```
{{% /codeblock %}}

After, we set our **project ID**. This is the identifier corresponding to your **GCS bucket** that you intend to populate with files:

{{% codeblock %}}
```python
project_id = 'your_project_id'
!gcloud config set project {project_id}

```
{{% /codeblock %}}

The `gcloud config set project {project_id}` command configures the gcloud command-line tool to use the specified **project ID** by default.

Finally, we define our bucket's name and use the `gsutil -m cp -r` command to recursively copy the directory you're interested in sending from our mounted **Google Drive** to our specified **GCS bucket**:

{{% codeblock %}}
```python
bucket_name = 'your_bucket_name'
!gsutil -m cp -r <copy your directory path here>/* gs://{bucket_name}/
```
{{% /codeblock %}}

The output of this last cell will say at the end *"Operation completed..."*.

Now your data should be available in your **GCS bucket** and can be accessed from your Google Cloud instance. Refresh your bucket webpage and confirm it.

After following the steps outlined so far, you will be able to import your files and execute your code within the Docker container.

## Handling memory allocation issues

Regardless of how powerful your machine is, it's not immune to running out of memory, especially when dealing with intensive computational tasks and large datasets. 

These situations can give rise to runtime errors when the CPU cannot allocate the required memory. While you could remedy this by using more powerful hardware, this isn't always an affordable or practical solution.

### Monitor resources usage

A crucial part of managing any computational task is continuously monitoring your system's resource usage. This way, you can promptly identify potential bottlenecks and inefficiencies and address them proactively.

In Linux-based environments, such as **Ubuntu**, [htop](https://github.com/htop-dev/htop) and [nvtop](https://github.com/Syllo/nvtop) are two widely used tools for tracking CPU and GPU usage, respectively.

`htop` is an interactive process viewer and system monitor. It's similar to the `top` command but provides a more visually appealing and human-readable format.
It allows us to sort by the task we're most interested in monitoring by pressing `F6`, among other interesting features.

<p align = "center">
<img src = "../img/htop1.png" width="1000" style="border:1px solid black;">
<figcaption> htop command top-display of vCPUs resources usage </figcaption>
</p>
<p align = "center">
<img src = "../img/htop2.png" width="1000" style="border:1px solid black;">
<figcaption> htop command down-display running tasks sorted by memory consumption </figcaption>
</p>

To install `htop` in your VM instance, you can use the following command:

{{% codeblock %}}
```bash
$ sudo apt install htop
# or:
$ sudo apt-get install htop
```
{{% /codeblock %}}

You can then run `htop` by simply typing `htop` in your terminal.

Similarly, `nvtop` stands for **NVIDIA GPUs TOP**. It's an interactive [NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#ubuntu-lts) usage viewer for Unix-like systems, including **Ubuntu**, and it's a must-have tool for anyone using GPU-accelerated tasks.

<p align = "center">
<img src = "../img/nvtop-user.png" width="700" style="border:1px solid black;">
<figcaption> nvtop command display of GPUs resources usage</figcaption>
</p>

You can install nvtop using the following commands:

{{% codeblock %}}

```bash
$ sudo apt install nvtop
# or:
$ sudo apt-get install nvtop
```
{{% /codeblock %}}

With `nvtop`, you can monitor GPU usage by typing `nvtop` into your terminal.

Use `htop` and `nvtop` to keep an eye on your resource usage. If you notice your system is running out of memory or your GPU utilization is too high, it's a good idea to take steps to address the issue before it leads to a crash.

### Practical approaches 

There are several practical solutions to avoid running out of memory. These are some common strategies:

- **Batching:** Break your task into smaller, more manageable chunks, or batches. This strategy works well with large datasets. 

{{% example %}}
In **PyTorch**, the `DataLoader` class can implement batching. An illustration of creating a `DataLoader` for a text dataset, using a tokenizer for a **BERT** model, is shown below:

    from torch.utils.data import Dataset, DataLoader

    class TextDataset(Dataset):
        def __init__(self, texts, tokenizer, max_length):
            self.texts = texts
            self.tokenizer = tokenizer
            self.max_length = max_length

        def __len__(self):
            return len(self.texts)

        def __getitem__(self, idx):
            text = self.texts[idx]
            encoding = self.tokenizer(
                text,
                max_length=self.max_length,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )
            return encoding

    # Create Dataset instance
    dataset = TextDataset(full_df['commenttext'].tolist(), tokenizer, max_length)

    # Configure your batch size according to your hardware resources
    batch_size = 32

    # DataLoader parameter shuffle is set to false by default to avoid mixing values
    dataloader = DataLoader(dataset, batch_size=batch_size)

    # Change path to read the saved models from data/Labeled_Responses/Models

    # Load model
    bert_sc_pa = BertForSequenceClassification.from_pretrained(
        dir +'/model_BERT_pa1')

    # Inference
    bert_sc_pa.eval()
    predictions_pa = []

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].squeeze()
            attention_mask = batch['attention_mask'].squeeze()
            
            output = bert_sc_pa(input_ids=input_ids, attention_mask=attention_mask)
            
            scores = output.logits
            predicted_pa = torch.argmax(scores, dim=1).cpu().numpy()
            predictions_pa.extend(predicted_pa)

{{% /example %}}

{{% tip %}}

Adjusting the `batch_size` parameter balances memory usage against processing time. A smaller `batch_size` reduces memory usage but may increase processing time.

{{% /tip %}}

- **Efficient Data Structures and Algorithms:** A wise choice in data structures and algorithm design can substantially cut down memory usage. The selection depends on your data's nature and your go-to operations. 

{{% example %}}
Take hash tables as an example, they boast constant time complexity for search operations, becoming a superior option for substantial datasets. 

In Python, this translates to choosing dictionaries over lists when wrestling with large datasets:

<p align = "center">
<img src = "../img/timeit.png" width="600" style="border:1px solid black;">
<figcaption> Dictionaries are more efficient data structures than lists</figcaption>
</p>

{{% /example %}}

- **Parallelizing your Work:** Divide the task among multiple identical instances, each running a part of the code. This approach is particularly useful when your code involves training or using multiple machine-learning models. For example, if you have three BERT models to run, you could use three instances.

Remember that beyond these strategies, it's always possible to leverage the scalability and flexibility of cloud services such as Google Cloud. These services allow for a dynamic allocation of resources according to your needs. 

{{% summary %}}

- **GCS buckets for large file handling:**

    - Connect your Docker container with your GCS bucket
    - Use Google Colab to move files from Google Drive to the bucket.

- **Memory Management:**

    - Monitor with `htop` (CPU) and `nvtop` (GPU).
    - Implement batching, efficient data structures and algorithms, and use job parallelization to handle memory issues.

{{% /summary %}}

## Additional Resources

- Google Cloud [Memory-Optimized](https://cloud.google.com/compute/docs/memory-optimized-machines) machines
- Memory management [Python Documentation](https://docs.python.org/3/c-api/memory.html)
- Machine type [recommendations for VM instances](https://cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances)