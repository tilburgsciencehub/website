---
title: "Manage memory and storage in your Google Cloud VM" 
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

After [configuring our Virtual Machine](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/config-vm-gcp/) in Google Cloud, we might be in the need to handle heavy files or prevent memory issues when running your code in the instance.

In this building block, you will learn how to:

- 
-
-

## Connect the Docker container within your instance to a Google Cloud Storage bucket 

Your docker-compose file likely provides Docker with the necessary instructions to employ [Docker volumes](https://docs.docker.com/storage/volumes/) to save any output file or data that you produce while working in your environment's container. If this is the case you may be also interested in connecting such volume to Google cloud storage so you don't have to manually download the output to your machine and make it easier to share and make available to your team.

To do this, first of all you will need to install [GCSFuse](https://github.com/GoogleCloudPlatform/gcsfuse) in your instance by running the following code:

{{% warning %}}
 
Carry out the following steps while your environment is not running. For that press "ctrl + c" to shut down Jupyter notebook and then run `docker compose stop` in your instance to stop the execution of the container. 

{{% /warning %}}

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

Now navigate to the directory of your instance which is connected to the container by the volume and create a new directory inside of it to be the one connected with your bucket. After you can run the following:

{{% codeblock %}}
```bash
$ sudo gcsfuse -o allow_other your-bucket volume_path/new_dir/
```
{{% /codeblock %}}

This code will tell GCSFuse to synchronize your new directory within the path with your bucket and allow your container to access it. After this, you just have to store any output produced in your environment in this new directory that you just created in your instance a few moments ago (Referred to in the previous code block as "new_dir") and it will be immediately available to you in your GCS bucket.

{{% tip %}}

Bear in mind that the absolute path to your bucket-sinchronized directory is not the same for your instance and for your container given that containers have independent file systems. However, its relative path will be the same to that where the Docker volume is mounted.

{{% /tip %}}

## Import heavy files: Use Google Colab as a bridge

In the moment you open your Jupyter notebook window with the instance running, you'll see its directory is empty. Is it the time to import the files we want to work with. 

The common way would be to import then via the **Upload file** button on the top-right corner of our commands prompt. Nonetheless, if the files are heavy, this would either take an eternity or probably incurre in a connection error after some time. Hence, What can we do? We can use **Google Colab** as a bridge to send the files from **Google Drive** into our **GCS bucket**!

It is suggested to utilize the same account for all Google tools. Doing so simplifies the authentication process and prevents potential permission issues, fostering a more seamless workflow.

{{% tip %}}
**Copy all directories you need**

When syncronizing the bucket with your directory inside the container, if your bucket contains other directories as well, the command `$ sudo gcsfuse -o allow_other your-bucket volume_path/new_dir/` might not copy those directories. 

Try `$ sudo gcsfuse --implicit-dirs -o allow_other your-bucket volume_path/new_dir/` to make sure the implicit directories are also included, if you want them to.

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

Next, we set our **project ID**. This is the identifier corresponding to your **GCS bucket** that you intend to populate with files:

{{% codeblock %}}
```python
project_id = 'your_project_id'
!gcloud config set project {project_id}

```
{{% /codeblock %}}

The `gcloud config set project {project_id}` command configures the gcloud command-line tool to use the specified **project ID** by default.

Finally, we define our bucket's name and use the `gsutil -m cp -r` command to recursively copy the directory you're interested on sending from our mounted **Google Drive** to our specified **GCS bucket**:

{{% codeblock %}}
```python
bucket_name = 'your_bucket_name'
!gsutil -m cp -r <copy your directory path here>/* gs://{bucket_name}/
```
{{% /codeblock %}}

The output of this last cell will say at the end *"Operation completed..."*.

Now your data should be available in your **GCS bucket** and can be accessed from your Google Cloud instance. Refresh your bucket webpage and confirm it.

After following the steps outlined so far, you will be able to import your files and execute your code within the Docker container.

{{% tip %}}
**GPUs ready?**

To ensure that GPUs are accessible for your tasks, you can use specific commands depending on the framework you're using. 

For instance, in `PyTorch`, the command `torch.cuda.is_available()` can be used to check if CUDA (GPU acceleration) is currently available, returning a boolean value.
{{% /tip %}}

## Handling memory allocation issues

Regardless of how powerful your machine is, it's not immune to running out of memory, especially when dealing with intensive computational tasks and large datasets. 

These situations can give rise to runtime errors when the CPU cannot allocate the required memory. While you could remedy this by using more powerful hardware, this isn't always an affordable or practical solution.

### Monitor resources usage

A crucial part of managing any computational task is continuously monitoring your system's resource usage. This way, you can promptly identify potential bottlenecks and inefficiencies and address them proactively.

In Linux-based environments, such as **Ubuntu**, [htop](https://github.com/htop-dev/htop) and [nvtop](https://github.com/Syllo/nvtop) are two widely used tools for tracking CPU and GPU usage, respectively.

`htop` is an interactive process viewer and system monitor. It's similar to the `top` command but provides a more visually appealing and human-readable format.
In fact, it allows us to sort by the task we're most interested in monitoring by pressing `F6`, among other interesting features.

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

- **Parallelizing your Work:** Divide the task among multiple identical instances, each running a part of the code. This approach is particularly useful when your code involves training or using multiple machine learning models. For example, if you have three BERT models to run, you could use three instances.

Remember that beyond these strategies, it's always possible to leverage the scalability and flexibility of cloud services such as Google Cloud. These services allow for a dynamic allocation of resources according to your needs. 

{{% summary %}}
- **Google Cloud VM Setup:**

    - Register on Google Cloud.
    - Create a Virtual Machine that satisfies your computational power needs.

- **Enable reproducibility and large files handling:**

    - Install Docker on the VM to aim for reproducibility.
    - Authenticate in Colab, set project ID, and bucket name.
    - Use Google Colab to move files from Google Drive to GCS.

- **Memory Management:**

    - Monitor with `htop` (CPU) and `nvtop` (GPU).
    - Check CUDA availability for GPU tasks.
    - Implement batching, efficient data structures and algorithms, and use job parallelization to handle memory issues.

{{% /summary %}}

## Additional Resources

- PyTorch [Documentation](https://pytorch.org/)
- Memory management [Python documentation](https://docs.python.org/3/c-api/memory.html)