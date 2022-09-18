---
title: "BLADE for Cloud Computing"
description: "A free cloud solution from Tilburg University for heavy computation tasks."
keywords: "cloud, virtual computers, BLADE, infrastructure, parallel, research cloud"
weight: 2
draft: false
author: "Roshini Sudhaharan"
authorlink: "https://nl.linkedin.com/in/roshinisudhaharan"
aliases:
  - /configure/research-cloud
---
# BLADE: Overview
Blade Computing is a service by Tilburg University's Library and IT Services (LIS) and finds its origins in TiSEM's Finance department.

The environment consists of powerful servers on which researchers can interactively work on data and run statistical computations. This is a Windows-based environment, which looks and feels like a regular Windows desktop.

It's accessible through a web portal. When logged on to the blade 24 CPUs and 384 GB of memory are available. Furthermore, the blade is equipped with SSDs to speed up your I/O.


<p align = "center">
<img src = "../blade.png" width="500">
<figcaption> Pros and Cons of Using Blade </figcaption>
</p>

### How to access Blade?

You can [request access to Blade](https://servicedesk.uvt.nl/tas/public/ssp/content/detail/knowledgeitem?unid=db72c119bf344fb78a196d5b6c669ecc) via the IT Service Desk and filling in a form. Access for external researchers is possible. The guest researcher needs to have a Tilburg University username, and a so-called PNIL-account (staff-not-on-payroll).
These accounts can be requested at the HRM department.

Once your request is approved, you can access Blade:

- On a **Windows, macOS, ChromeOS or Linux** computer enter the following [URL](https://rdweb.campus.uvt.nl/RDWeb/webclient/) in a recent version of your web browser and sign in with your TiU credentials.

**If this doesn't work**, proceed with the following:

- On a **Windows** computer use the following [URL](https://rdweb.campus.uvt.nl/RDWeb/webclient/) in web browser and sign in with your TiU credentials (campus\TiU username)

- On a **macOS** computer use Microsoft Remote Desktop Client for Mac (install from App Store), use this web feed [URL](https://rdweb.campus.uvt.nl/RDWeb/feed/webfeed.aspx) and sign in with your TiU credentials (campus\TiU username)


{{% tip %}}
You can download a one-page PDF quickstart guide [here](https://servicedesk.uvt.nl/tas/public/dispatcherpublicservlet/D4HMCQZAZ8JTL47KA4RA9NZ1U7MELV69YKH0W3ZRSZN33/One-Page-Quickstart-Guide%20RDP%20client%20-%20TiU%20BladeComputing.pdf).
{{% /tip %}}

{{% warning %}}
**Scheduled maintenance**

Every **Friday after the 2nd Tuesday of the month** the TiU Blades will be put offline for maintenance. You will receive an email reminder each month.

Do **NOT** run your analyses when maintenance is performed, because unsaved work will be lost.

Moreover, each month during the maintenance period, **all personal data stored locally on Blade on scratch drives (D:) will be erased!** Therefore, you should back up your files before.
{{% /warning %}}

### Where to Save your Files?
**M / S / T drive**
- Use M / S / T disc for storing data that must be retained.

**D drive (Scratch)**
- Use only the D-disk (Scratch) for temporary data storage.
During standard (monthly) maintenance, the D drive is deleted.

**C drive**
- The C drive is only intended for the Operating System and Applications.

**E drive**
- The E-disk has been used since 12-10-2018 to store the local user profiles. (This is because of possible filling up of the C-drive and thus undermining the entire server).
- The E-disk contains the user profiles (with, for example, python packages). This E-disk is automatically deleted on restart.

# Additional resources

## SURFsara's LISA cluster: Overview
If Blade Computing is not sufficient then the LISA Cluster may offer a solution.
Hundreds of servers can be accessed via a so-called queue system. The execution of a calculation task can be assigned to multiple servers. As soon as the number of required servers is available, the assignment is executed.

Some of the servers are linked to each other via a so-called high-speed link (infiniband). This part of the LISA Cluster is a good choice for executing an assignment that requires a great deal of communication between servers.
The support desk of SurfSARA can support in use. The support desk has templates and sample applications and offers workshops for beginners.

### Pros
- Hundreds of servers are available (cluster).
- Access to a huge amount of software.
- Users do not have to share the resources but have exclusive access.

### Cons
- Steep learning curve. Knowledge is required to be able to build an efficient job.
- No direct access to the joint network of Tilburg University.
- There may be a queue and thus waiting time.
- Less interactive because of the queue principle.

### How to access LISA cluster?
You can [request access to LISA](https://servicedesk.uvt.nl/tas/public/ssp/content/serviceflow?unid=8607361336ec4bcf8989e82f168602e7&openedFromService=true) via the IT Service Desk and filling in a form.

Once your request is approved, you can connect to LISA:

**Windows**

- There is more than one way to make a connection, we take PuTTY. If that program is not present on your system, you should install it now: go to the PuTTY download page and download putty.exe. Start PuTTY and fill in under 'Host Name (or IP address)'

- lisa.surfsara.nl
Check the 'Connection type' radio button labelled 'SSH', and click the 'Open' button.

**Linux**

Open a terminal window (for Ubuntu users: you find that here: 'Accessories - Terminal'). In that terminal window, type:

- ssh <your_username>@lisa.surfsara.nl

If the ssh command cannot be found, install the ssh-client. For Ubuntu users:

- sudo apt-get install OpenSSH-client

**MacOS**

Open a terminal window (You find that here: 'Applications - Utilities - Terminal'). In that terminal window, type:

- ssh <your_username>@lisa.surfsara.nl

## SURFsara's Cartesius Cluster: Overview
Cartesius is a supercomputer in the true sense of the word. All servers in the cluster are linked with high-speed connections to form a very large computer. Cartesius is best suited for calculations in which the individual components (functions and procedures) have a great interdependence.
A so-called Graphical Processing Unit (GPU) is also offered in this environment. In some cases, for example with Floating Point calculations, running a program on a Graphics adapter is much more efficient than on a computer processor.

### Pros
- The most rapid solution.
- Graphical Processing Unit (GPU) available.
- A huge amount of software.
- Users do not have to share resources but have exclusive access.

### Cons
- Steep learning curve. Knowledge is required to be able to build an efficient job.
- No direct access to the joint network of Tilburg University.
- There may be a queue and thus waiting time.
- Less interactive because of the queue principle.

You can find more information about the Cartesius cluster and how to connect to it on the [IT Service Desk](https://servicedesk.uvt.nl/tas/public/ssp/content/detail/service?unid=d3f67e5b448d4f629aa68ec1ac9578ce).
