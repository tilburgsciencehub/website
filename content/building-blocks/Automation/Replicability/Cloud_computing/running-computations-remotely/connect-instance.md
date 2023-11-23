---
tutorialtitle: "Running Computations Remotely"
type: "running-computations-remotely"
indexexclude: "true"
title: "Connect Instance"
description: "Learn how to run computations remotely"
keywords: "cloud computing, azure, amazon, google, virtual machine"
weight: 102
draft: false
aliases:
  - /learn/cloud/connect
  - /tutorials/more-tutorials/running-computations-remotely/connect-instance
---

# Connect Instance

Depending on your operating system and whether you chose to launch a Linux or Windows instance, follow one of the tutorials below.

## Linux instance

**Mac**
1. Click on your running EC2-instance in the console and copy the Public IPv4 DNS address (e.g., `ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com`).

2. Open the terminal and type `export HOST=<YOUR-PUBLIC-IPV4-DNS>` (see step 1) and `export KEY=<PATH_TO_KEY_PAIR_FILE>` (e.g., `/Users/Roy/Downloads/ec2-key-pair.pem`). This creates two variables, `HOST` and `KEY`, that we can reference in our terminal (e.g., if you type `$KEY` it returns the aforementioned file path).

3. Type `chmod 700 $KEY` to change the permissions of the private key file.

4. Type `SSH -i $KEY ec2-user@$HOST` to connect with the EC2-instance.

5. Type `yes` if it asks you to continue connecting and hit Enter. If done successfully, it prints the text "EC2" to the terminal followed by the AMI that you selected (e.g., Amazon Linux 2 AMI). So, in short, we connected to an EC2-instance that we can control through our terminal, however, there are no scripts or data on it yet so we first need to copy files to our instance before we can put it to work.


**Windows** 
1. Download [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) MSI Windows Installer and follow the installation wizard. If it doesn't come with the PuTTY Key Generator pre-installed, also make sure to download `puttygen.exe` from the same page. 

2. Open PuTTy Key Generator, click on "Load", and select the private key file you downloaded earlier.

3. Click on "Save private key" to convert the `*.pem` file into a `*.ppk` file.

4. Click on your running EC2-instance in the console and copy the Public IPv4 DNS address (e.g., `ec2-XX-XXX-XXX-XXX.compute-1.amazonaws.com`).

5. Open PuTTY (so not the Key Generator!) and enter the following as the host name: `ec2-user@<YOUR-PUBLIC-IPV4-DNS>`

6. In the left panel, click on Connection > SSH > Auth and click on "Browse" to add your `*.ppk` private key.


## Windows instance
![Connect Windows Instance](../img/connect-windows-instance.gif)

1. Install Windows Remote Desktop ([Windows](https://apps.microsoft.com/store/detail/microsoft-remote-desktop/9WZDNCRFJ3PS) & [Mac](https://apps.apple.com/us/app/microsoft-remote-desktop/id1295203466?mt=12). 

2. Head over to your Windows Instance in the AWS console and click on "Connect" and then "RDP Client".

3. Click on the "Download remote desktop file" button to download a rdp file.

4. Before you open the file, click on "Get password", upload the keypair (`*.pem` file), click on "Decrypt password" and copy the password.

5. Now, open the rdp file and login with the credentials (Username = "Administrator", Password = <see step 4>).
