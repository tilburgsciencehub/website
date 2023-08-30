---
title: "Configure a VM with GPUs in Google Cloud" 
description: "Learn how to configure code in a Google Cloud instance with GPUs, importing heavy files from Google Drive and handling memory issues"
keywords: "Docker, Environment, Python, Jupyter notebook, Google cloud, Cloud computing, Cloud storage, GPU, Virtual Machine, Instance, Memory"
weight: 2
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2023-06-05 #updated 2023-08-23
aliases: 
  - /run/vm-on-google-cloud
  - /handle/memory-issues
  - /import/heavy-files
---

## Overview

In this building block, you will discover how to create and configure a simple and robust VM instance in [Google Cloud](https://cloud.google.com/?hl=en), designed to overcome memory or power constraints limitations. Say goodbye to obstacles and embrace seamless computing.

With this guide you'll see how to:

- Establish a VM instance in Google Cloud with optimized configurations.
- Use [Docker](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/docker/) and Google Colab for a reproducible environment and efficient file handling.
- Monitor system resources and implement strategies to handle memory challenges.

## Initialize a new instance

### Create a Google Cloud account

First of all, we will need to have a Google Cloud account and a project created in order to create an instance. After this is done, we can go to the welcome page and click on **"Create a VM"**.

<p align = "center">
<img src = "../img/welcome1.png" width="600" style="border:1px solid black;">
<figcaption> Click in "Create a VM"</figcaption>
</p>

### Set up your Virtual Machine

You will be directed to the instance configuration page. Here, you will need to enter details for your instance. This includes the **instance name**, **labels**, **region**, **zone**, and **machine configuration**.

You'll encounter four primary machine categories to select from:

- **General-purpose:** Offers the best balance between price and performance, making it suitable for a wide range of workloads. It provides a cost-effective solution without compromising efficiency.

- **Compute-optimized:** Delivers the highest performance per core on Compute Engine, specifically designed for compute-intensive tasks. It excels in scenarios that require substantial computational power, ensuring faster processing and reduced execution times.

- **Memory-optimized:** Specifically designed for memory-intensive workloads, this category offers a higher memory capacity per core compared to other machine families. With the ability to support up to 12 TB of memory, it empowers applications that heavily rely on data storage and manipulation, enabling efficient data processing and analysis.

- **Accelerator-optimized (GPUs):** The perfect choice for massively parallelized Compute Unified Device Architecture ([CUDA](https://developer.nvidia.com/cuda-zone#:~:text=CUDA%C2%AE%20is%20a%20parallel,harnessing%20the%20power%20of%20GPUs.)) compute workloads, such as machine learning and high-performance computing. This category is specifically tailored for workloads that demand GPU acceleration, ensuring exceptional performance for tasks that require substantial graphical processing power and parallel computing capabilities.

{{% warning %}}

**Save on unnecessary costs!** 

GPU-enabled VMs are vital for deep learning tasks like language models. However, for other uses, GPUs are redundant and increase expenses. 

See an example on how suboptimal GPU usage can slow compute time [here](https://rstudio-pubs-static.s3.amazonaws.com/15192_5965f6c170994ebb972deaf18f1ddf34.html).

{{% /warning %}}

A good choice to balance between price and performance could be selecting an **NVIDIA T4 n1-standard-8** machine. It's packed with 30GB of RAM and a GPU. If we would need more vCPUs or memory, we can improve it by selecting a customized version, under the **"Machine type"** header.


<p align = "center">
<img src = "../img/machine-config.png" width="700" style="border:1px solid black;">
<figcaption> Adjust the machine configuration to your needs</figcaption>
</p>

While we won't dive into all the configuration bells and whistles here, remember Google Cloud is your playground for [custom-tailoring your instance](https://cloud.google.com/compute/docs/machine-resource) just the way it better suits your needs.

{{% tip %}}

**Balance your budget and computational needs**

In the top right corner, you'll see a real-time **pricing summary**. As you adjust your instance's configuration, you'll be able to find the optimal setup that suits your specific requirements.

<p align = "center">
<img src = "../img/price-vm.png" width="350" style="border:1px solid black;">
<figcaption> Pricing summary</figcaption>
</p>

{{% /tip %}}

As we scroll-down through the configuration process, we'll skip to [Boot Disk settings](https://cloud.google.com/compute/docs/disks). 

Think of your boot disk as your instance's storage locker - here, you get to pick its type (standard or SSD), size, and the VM image (Operating System) you want to load on it. 

A bigger boot disk equals more space for data and apps. So, if you're playing with chunky datasets, you'll want to upgrade your storage. In our case, we'll crank up the boot disk size to 100GB, which is a good starting point. In fact, boosting your storage won't be very costly.

<p align = "center">
<img src = "../img/boot-disk-config.png" width="400" style="border:1px solid black;">
<figcaption> Boot disk configuration summary</figcaption>
</p>


If you're considering integrating GPUs into your instance, it's recommended to switch the default boot disk from **Debian** to **Ubuntu**.

**Ubuntu** simplifies the installation of proprietary software drivers and firmware, making the process of installing necessary [NVIDIA drivers](https://docs.nvidia.com/datacenter/tesla/tesla-installation-notes/index.html#ubuntu-lts) for GPU utilization significantly smoother. This could save you time and effort in the long run.


As you scroll down, you will find the [Firewall Rules](https://cloud.google.com/compute/docs/samples/compute-firewall-create) section. Here, you will see the default settings that manage your network traffic flow. HTTP or HTTPS? Go for HTTPS whenever you can. It's the safer bet, wrapping your data transfers in an encryption layer for added security. 

However, many developers activate both HTTP and HTTPS for broader compatibility, handling secure (HTTPS) and insecure (HTTP) requests alike. But let's keep it modern and secure, HTTPS should be your go-to, especially when handling sensitive data.

{{% warning %}}
**Custom firewall rules?**

Beyond the standard rules, you can also craft custom firewall rules in **Google Cloud**. These can be shaped to match your individual security needs and traffic flow. But be cautious, as incorrect firewall configurations can either expose your instance to threats or obstruct valid traffic.

{{% /warning %}}

Since we're not handling sensitive data in this example, we'll be activating both.

<p align = "center">
<img src = "../img/firewall-rules-config.png" width="500" style="border:1px solid black;">
<figcaption> Firewall rules </figcaption>
</p>

After fine-tuning your instance's setup and firewall rules, you can go ahead and establish the instance. Take into account that the instance will start automatically after you create it. So if you won't inmediatly need it make sure you stop it.

## Establish your environment using Docker

Your next task involves setting up a reproducible environment on your instance, for which we'll be utilizing [Docker](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/docker/). If you're not already acquainted with it, we strongly recommend visiting this [building block](https://tilburgsciencehub.com/building-blocks/automate-and-execute-your-work/reproducible-work/google_cloud_docker/). This guide provides a comprehensive step-by-step walkthrough that you need to follow to progress further.

It's worth noting that the supplementary information provided there regarding the association of our instance with **Google Cloud Storage (GCS)** buckets using `GCFuse` commands is essential for our current use-case.

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

## Extra: Handling memory allocation issues

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

## Additional Resources

- Google Cloud Compute Engine [guides](https://cloud.google.com/compute/docs/instances)
- PyTorch [Documentation](https://pytorch.org/)
- CUDA Toolkit [download](https://developer.nvidia.com/cuda-toolkit)
- Memory management [Python documentation](https://docs.python.org/3/c-api/memory.html)

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