---
title: "Task Scheduling"
description: "Execute scripts at specified intervals with cronjob and Task Scheduler"
weight: 4
keywords: "cron, cronjob, automation, task scheduler, task scheduling"
date: 2021-01-06T22:01:14+05:30
aliases:
  - "/task-scheduling"
---

## Overview

Task scheduling involves the automatic execution of scripts on your local computer. For example, you may want to run a web scraper on a daily basis without having to manually execute the script. Mac and Windows users can leverage cronjobs and the Task Scheduler respectively to automate repetitive tasks. Depending on your operating system, follow one of the guides below to learn how to configure task scheduling on your machine.

### cronjob (Mac / Linux)
Most Mac and Linux distributions come with pre-installed cron by default. This is a program that you can only access through the terminal. Before we can schedule tasks, we first need to understand the cron syntax. After all, it uses a very specific way to define the task frequency.

#### cron syntax
The syntax consists of 5 symbols - each separated by a space - which denote the minute, hour, day, month, and weekday respectively. An asterisk symbol matches any value so `* * * * *` means every minute of every hour of every day. Note that weekdays can take on a value between 0 and 6 and start on Sunday (0 = Sunday, 1 = Monday, ... etc.)

```
*    *    *    *    *  
┬    ┬    ┬    ┬    ┬
│    │    │    │    └─  Weekday  (0 - 6)
│    │    │    └──────  Month    (1 - 12)
│    │    └───────────  Day      (1 - 31)
│    └────────────────  Hour     (0 - 23)
└─────────────────────  Minute   (0 - 59)
```

If needed, you can use commas to insert more than a single digit (e.g., `15,45 * * * *` = every 15th and 45th minute every hour), dashes to define a range (e.g., `0 0-5 * * *` = 0:00, 01:00, ..., 05:00 every day), and slashes to specify the relative frequency (e.g., `*/10 * * * *` = every 10 minutes).

{{% example %}}
`30 * * * *` = every 30th minute of every hour every day    
`30 5 * * *` = at 05:30 on every day  
`30 5 1 * *` = at 05:30 the first day of the month   
`30 5 1 1 *` = at 05:30 on January 1st  
`30 5 * * 1` = at 05:30 on every Monday  
`0 0 */3 * *` = every 3 days at midnight   
`30 5 1,15 * *` = at 05:30 on every 1st and 15th day of the month     
`*/30 9-17 * * 1-5` = every 30 minutes during business hours
{{% /example %}}

#### Configuring cron jobs

1. Double-check whether your script works as expected and then save the Python script as a **`.py` file** (so not a `.ipynb` notebook!). For example, copy-paste the contents from Jupyter to Spyder. We recommend storing the script in your root directory (the parent directory of your Desktop and Documents among others) to avoid file permission issues.

2. Open the Terminal and type `crontab -e`. This opens the so-called vim editor which you can think of as a notepad within the terminal. 
3. Press `I` so that you can edit the text.
4. Insert the following syntax (always specify the full path! - see the tip below on how to obtain the Python installation path): 
```
# e.g., * * * * * /usr/bin/python3 /script.py
<CRON CODE> <PATH OF YOUR PYTHON INSTALLATION> <PATH TO PYTHON FILE>
```
5. Press Esc and type `:wq` followed by Enter to save your changes (if a window pops up choose OK). 

6. If you now run `crontab -l` your newly scheduled task should be listed. We recommend keeping an eye out whether your scheduler works as expected, especially in the beginning. If not, you can make changes to the cron file at any time. To remove all existing tasks and clean up the cron file type `crontab -r`.

{{% tip %}}
Since a single cron file can contain multiple tasks, we'd recommend putting a comment (`#...`) above each line that describes what the job is about. This serves as documentation for your future self.
{{% /tip %}}



### Task Scheduler (Windows)
Windows 10 has a built-in graphical interface for scheduling tasks which provides plenty of functionalities and options you can adjust (e.g., frequency, start and end date, battery and network settings). Although you don't have to mess around with the terminal, you do need to create a so-called BAT script that executes your Python script. Follow the steps below to get started!

1. Double-check whether your script works as expected and then save the Python script as a **`.py` file** (so not a `.ipynb` notebook!). For example, copy-paste the contents from Jupyter to Spyder.
 
2. Open Notepad and create a new file with the following contents:

{{% codeblock %}}
```python
"<PATH OF YOUR PYTHON INSTALLATION>" "<PATH TO PYTHON FILE>"
pause
```
{{% /codeblock %}}

See the tip below on how to obtain the Python installation path. For example, the first line could look like `"C\Users\Pieter\AppData\Local\Programs\Python\Python37\python.exe" "C\Users\Pieter\Desktop\scrape_websites.py"`

3. Save the file as `run_script.bat` (doubling clicking the file should run the Python script)

4. Open **Task Scheduler** (search for it in your programs list)

5. Click **Create Basic Task** and fill out a **Name** and a **Description** for your task

6. Under **Security Options** choose **"Run whether user is logged on or not"** (i.e., the script will still run if the computer is in standby mode) and tick the box **"Run with highest privileges"**

7. Create a new trigger (e.g., Daily) and set a start and end date/time

8. Create a new action **"Start a Program"** and select the `.bat` file you created earlier (e.g., `run_script.bat`)

9. On the "Conditions" tab, you may want to untick the box **"Start the task only if the computer is on AC power"** (i.e., the script still runs if your laptop is on battery power) and tick the box **"Wake the computer to run this task"** to make sure the tasks are always executed on time.

10. Click **"OK"** and fill out your password. If done correctly, your newly scheduled task should be added to the Task Scheduler Library window.

{{% tip %}}
Run the following command in, for example Spider or a Jupyter Notebook, to figure out the path of your Python installation. 
```python
import os, sys
print(os.path.dirname(sys.executable))
```
{{% /tip %}}

## See Also

- [This](https://crontab.guru) website converts cron syntax into human-readable language. For some practice, click on *random* and try to write the cron expressions yourself (without looking at the answer of course)!