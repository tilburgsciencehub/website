---
title: "Learn with open-interpreter"
description: "Explanation and usage of Decision Trees in R"
keywords: "open-interpreter, terminal, cmd, webscraping, web scraping, learning"
draft: false
weight: 2
author: "Niels Rahder"
authorlink: "https://www.linkedin.com/in/nielsrahder" 
---
  
  # Overview 
  
  ## What is open-interpreter?
  
Open-interpreter is a program that allows large language models (like Chat-GPT4 or Code Llama) to run code locally on your machine. This allows users of the program to issue commands and interact with their terminal/cmd in natural language.

The program is (besides really powerful) also incredibly useful for learning how to complete certain projects with your computer. 

Examples of tasks open-interpreter can achieve are: 
  - Change settings on your device 
  - Analyze/Visualize data sets
  - Retrieve information from the internet (via web scrapers)
  - Creating websites
  - Translating videos
  - And much more!
  
In this tutorial, we will guide you through the required software, demonstrate how to install the interpreter, and show you how to harness the interpreter's capabilities to enhance your proficiency in terminal/cmd and web scraping.


  ## Installation
  
As an open-source project the entire code is available on this [repository](https://github.com/KillianLucas/open-interpreter).   
In order to work with open-interpreter you need at least `python 3.10` installed on your system, and preferably an [Open-AI API key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key). <br> <br>
Open-Interpreter is installed with the following command: 

{{% codeblock %}}
```bash 
pip install interpreter
```
{{% /codeblock %}}

After which you can call the program using the command below:

{{% codeblock %}}
```bash 
interpreter
```
{{% /codeblock %}}

And you will see the following screen:

<img 
src="../images/terminal_interpreter.png" 
alt="Screenshot of Open-Interpreter terminal interface." 
width="3000">

Following this, you can choose to work with the recommended Chat-GPT4, which offers advanced language processing and requires a paid API-key, or opt for Code Llama, which runs locally on your machine for free, though at the time of writing, it's a bit buggy and less capable.

{{% tip %}}
When you are working with the chat-GPT4 API you can save you API key with the following commands:
- for Mac/Linux `export OPENAI_API_KEY=your_api_key` 
- For Windows `setx OPENAI_API_KEY your_api_key`
{{% /tip %}}

Now that you have successfully installed open-interpreter, we can start working with it! We will first look at how it can aid you in learning terminal controls, after which we'll dive into web scraping. 

  ## Examples on the how to use open-interpreter

  ### terminal controls 
  
Learning to navigate the terminal/cmd can be challenging, however with open-interpreter you can ask the software what you want to do in natural langue and it will display the steps and the required code for you. This way learning to navigate the terminal/cmd becomes easier and more natural. 
  
  #### example

Let's say are a NASA enthusiast and you want to learn more about the perseverance rover, in order to aid you study you want to check the following [website](https://mars.nasa.gov/mars2020/) and find if the word "Perseverance" is present in the code. Following this you want to store the number of occurrences of the word on the website in a separate text file. <br> 

However you are not entirely sure on how to perform this via the terminal/cmd, so you ask open-interpreter for help via the following prompt:

<img
src = "../images/Mars_Interpreter.png" 
alt = "screenshot of prompt for terminal commands."
width = "3000">

As you can see the program first comes up with a plan to create a directory, download the webpage via `wget`, check for the occurrence of Perseverance, and create a new file. 
Following which it asks you if it can executes the following commands: 

{{% codeblock %}}
```bash 
mkdir mars2020_analysis 
curl 'https://mars.nasa.gov/mars2020/' -o ./mars2020_analysis/mars2020.html 
grep -o -i perseverance ./mars2020_analysis/mars2020.html | wc -l 
echo '74' > ./mars2020_analysis/perseverance_count.txt                                                                                                                    
```
{{% /codeblock %}}

When you run the code in your terminal it will do exactly as asked! 
  
  ### web scraping
  
Open-interpreter is also suited for creating web scrapers (and learning how to create them yourself!). The program will explain the code in easy to understand pieces, making it accessible even for those new to web scraping.  


  #### example

Let's say you are also enthusiastic about books and want to collect the top 10 books from the Poetry category on [books-to-scrape](https://books.toscrape.com/). After collecting information about the title, price and in-store availability you want to have this data stored in a new-line separated JSON file. 
When you are not entirely sure on how to do it you can now just ask open-interpreter to do it for you, and the program will guide you trough all the necessary steps as well as execute the code!
<br>
In the example below you can see how open-interpreter again comes up with a plan to collect and store this data for you:


<img
src = "../images/WS_prompt_open_interpreter.png"
alt = "screenshot of prompt for web scraping."
width = "3000">

<br>

After coming up with the plan on how to extract the code the program writes the code in Python using the `BeautifulSoup` and `Request` libraries (When the program notices that you have not yet installed these, it will do that for you!) 


{{% codeblock %}}
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
{{% /codeblock %}}


After fetching the HTML content, moving to the Poetry section, and extracting the relevant data open-interpreter retrieves the title and the price for each book, stores this in a list and writes that to a JSON file. 

 ## summary
In summary, open-Interpreter not only provides an intuitive and powerful interface for integrating the prowess of language models into coding and web tasks but also serves as a valuable learning platform. Whether you're navigating the intricacies of the terminal, diving deep into web scraping, or embarking on a journey to enhance your digital skills, this tool acts as the bridge between human instruction and machine capability, making learning more interactive and efficient.


{{% warning %}}
When you are working with open-interpreter it will continuously ask you for permission to execute code. You can circumvent this by running `interpreter -y` or `set interpreter.auto_run = True`. This however calls for more caution when requesting commands that interact with files or system settings. 
{{% /warning %}}



{{% warning %}}

When using open-interpreter for tasks like summarizing files, it's important to note that the file needs to be sent to the OpenAI server, which could potentially raise privacy concerns for some users. However, for tasks related to data operations, everything stays securely on your own system. To ensure that all processes remain local and do not involve external servers, you can utilize Code Llama to execute tasks exclusively on your system.

__Please exercise caution and consider your privacy preferences when using open-interpreter for various tasks.__

{{% /warning %}}



  





