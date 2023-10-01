---
title: "Bring AI to your command line/terminal"
description: "How to use open interpreter to bring AI to your command line/terminal"
keywords: "open interpreter, terminal, cmd, command line, webscraping, web scraping, learning"
draft: false
weight: 2
author: "Niels Rahder"
authorlink: "https://www.linkedin.com/in/nielsrahder" 
---
  
# Overview 

## What is open interpreter?

The open interpreter project allows large language models (like Chat-GPT4 or Code Llama) to **run code locally** on your computer. This allows you to "remote control" your own computer in *natural language* via the terminal/command.

Examples of tasks you can use open interpreter for are:
  - Change settings on your device 
  - Analyze/Visualize data sets
  - Retrieve information from the internet (e.g., via web scrapers)
  - Create websites
  - Translate videos
  - ...and much more!
  
In this building block, we will help you install open interpreter, and then demonstrate how to use it. Finally, we provide an example on how to use open interpreter for web scraping.

## Installation
  
As an open-source project, the entire code is available on this [repository](https://github.com/KillianLucas/open-interpreter). To work with open interpreter, you need at least `python 3.10` installed on your system, and preferably an [Open-AI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key) (if you want to use GPT-4 as your preferred LLM).

Installed open interpreter via the following command:

{{% codeblock %}}
```bash 
pip install interpreter
```
{{% /codeblock %}}

Then, you can open interpreter via the command line:

{{% codeblock %}}
```bash 
interpreter
```
{{% /codeblock %}}

You will then see the following screen:

<img 
src="../images/terminal_interpreter.png" 
alt="Screenshot of Open Interpreter terminal interface." 
width="3000">

Following this, you can choose to work with GPT-4 (a commercial large language model, requiring you to provide a for-pay API key), or use the open source large language model Code Llama (which will run for free on your machine - though a bit buggy at the time of writing).

{{% tip %}}
When you are working with the Open AI's GPT-4 API, you can store you API key with the following commands:
- for Mac/Linux: `export OPENAI_API_KEY=your_api_key` 
- For Windows: `setx OPENAI_API_KEY your_api_key`
{{% /tip %}}

Now that you have successfully installed open interpreter, we can start working with it! We will first look at how it can aid you in learning terminal controls, after which we'll dive into web scraping. 

## Examples on the how to use open interpreter

### Control your terminal

Learning how to navigate the terminal/command prompt can be challenging. Hwever with open interpreter, you can simply **say what you want to do in natural language**, and open interpreter will display (and execute) the required steps. This way, learning how to use the terminal becomes easier and way more natural!

{{% tip hint %}}
__Example on how to control your terminal__

Let's say are a NASA enthusiast and you want to learn more about the perseverance rover. To collect some data, you would like to check how often the word "perseverance" is listed on [this website](https://mars.nasa.gov/mars2020/). Afterwards, you want to store the number of words in a separate text file.

You know that it's best to do this via the command line - particularly because you want to scale this up to many more websites in the future. To learn how to do it via the command prompt, you can simply ask open interpreter for help via the following prompt:

```
> Create a directory, download this file (https://mars.nasa.gov/mars2020/), 
  check for the word "perseverance' and create a new file with the number of 
  times the word occurs.

Sure, in order to download the webpage, check for the word "perseverance", 
and create a new file with the number of occurrences, we will stick with 
the following plan:

1. Create a new directory in your current working directory.
2. DownLoad the given URL's HIML content into a file in the newly created directory.
3. Read the downloaded HIM tIle and count the number at accurrences at The Ward DersPVerance
4. Write the count into a new file.
```

As you can see the program first comes up with a plan to create a directory, download the webpage via `wget`, check for the occurrence of Perseverance, and create a new file. 
Afterwards, open interpeter asks whether it can execute the following commands: 


```bash 
mkdir mars2020_analysis 
curl 'https://mars.nasa.gov/mars2020/' -o ./mars2020_analysis/mars2020.html 
grep -o -i perseverance ./mars2020_analysis/mars2020.html | wc -l 
echo '74' > ./mars2020_analysis/perseverance_count.txt                                                                                                               
```

When you run the code in your terminal it will do exactly as asked! 
  
{{% /tip %}}


### Web scraping
  
Open interpreter is also suited for creating web scrapers (and learning how to create them yourself!). The program will explain the code in easy to understand pieces, making it accessible even for those new to web scraping.  

{{% tip hint %}}
__Using open interpreter to scrape the web__

Let's say you are also enthusiastic about books and want to collect the top 10 books from the Poetry category on [books-to-scrape](https://books.toscrape.com/). After collecting information about the title, price and in-store availability you want to have this data stored in a new-line separated JSON file. 
When you are not entirely sure on how to do it you can now just ask open interpreter to do it for you, and the program will guide you trough all the necessary steps as well as execute the code!

In the example below, you can see how open interpreter again comes up with a plan to collect and store this data for you:

```
> Go to https://books.toscrape.com/ and get me the top 10 books in the Poetry section. 
  I want you to store the title, price, and in-store availability as a new-line 
  seperated JSON file.

Sure, I will implement the steps as below:
1. Access the website and fetch its HTML content.
2. Parse the HTML content from the homepage to get the URL of the poetry section.
3. Visit the poetry section's URL and extract the details of the first 10 books with their title, price, and availability status.
4. Store these details for each book as new-line separated JSON data.
```

After coming up with the plan on how to extract the code the program writes the code in Python using the `BeautifulSoup` and `request` libraries (When the program notices that you have not yet installed these, it will do that for you!) 

```python    
import json
import requests
from bs4 import BeautifulSoup      

# Scrape information for books on page
url = 'https://books.toscrape.com/catalogue/category/books/poetry_23/index.html'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
books_html = soup.find_all('article', class_='product_pod')                                                                                                                

for book_html in books_html:
    # Parse book title and price
    title = book_html.h3.a['title']
    price = book_html.find('p', class_='price_color').text                                                                                                               
    
    # Parse availability
    availability_html = book_html.find('p', class_='instock availability')
    availability = availability_html.text.strip()                                                                                                                                                                                                                             
    # Store book data in list
    books.append({'title': title, 'price': price, 'availability': availability})                                                                                           
    
# Write data to file
with open('/Users/Niels/Documents/Top_10_Poetry_Books.json', 'w') as f:
    for book in books:
        json.dump(book, f)
        f.write('\n')  
```



After fetching the HTML content, moving to the Poetry section, and extracting the relevant data, open interpreter retrieves the title and the price for each book, stores this in a list and writes that to a JSON file. 

{{% /tip %}}

## Summary

Open interpreter provides an intuitive and powerful interface for letting large language models run directly on your computer - allowing them to execute commands (rather than forcing you into copy-pasting them from ChatGPT).

As such, it enables controlling the computer using natural language commands. Fnctions range from device settings adjustments to web scraping.
  


{{% warning %}}
When you are working with open interpreter, it will continuously ask you for permission to execute code. You can circumvent this by running `interpreter -y` or `set interpreter.auto_run = True`. This, however, calls for more caution when requesting commands that interact with files or system settings. 
{{% /warning %}}


{{% warning %}}

When using open interpreter for tasks like summarizing files, it's important to note that the file needs to be sent to the OpenAI server, which could potentially raise privacy concerns for some users. However, for tasks related to data operations, everything stays securely on your own system. To ensure that all processes remain local and do not involve external servers, you can utilize Code Llama to execute tasks exclusively on your system.

__Please exercise caution and consider your privacy preferences when using open interpreter for various tasks.__

{{% /warning %}}



  





