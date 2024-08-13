---
title: "Open Anonymisation tools"
description: "Review of different open tools that can be used for anonymisation of qualitative data."
keywords: ""
draft: false
weight: 1
author: "Tiernan O'Sullivan"
aliases:
  - /open-anonymisation-tools
  - /anonymisation-tools
---

## Overview

Anonymisation of qualitative data is an important step in making data reusable and abiding by commitments to research participants.

In this article we explain how to install and use three open source tools for manipulating qualitative data, which you may find useful when creating an anonymized or pseudonymized version of your research data. 


## AnonymoUUs

Developed by Utrecht University,  the AnonymoUUs Python package is used in identifying and replacing strings in multiple files and folders at once. To use the tool, you specify a replacement mapping - a set of keywords to replace and the substitutes that will replace them - and the name of a file tree or zipped archive where you want the package to make replacements.  AnonymoUUs will open each file in the tree, and will substitute any found keyword in the files. As well as this, the package will change the text in file/folder paths. 

If you have multiple files which contain personal data, such as a person’s name or ID, you can use this package to substitute that the personal data with a different string. For example, you can use the package to review a number of files and folders to identify specific personal names and replace them with pseudonyms. 

The package has a number of methods that allow you to substitute a string in this way and it has been developed to work with text in different filetypes, provided that there is UTF-8 encoding.  

### Key points
- AnonymoUUs is a Python package that provides methods for replacing text in files and folders.  

- It can process text-based files like .txt, .html, .json, and .csv. 

- It supports (nested) zip archives, which will be unpacked and processed in a temp folder, and zipped again.

- It provides options to use a dictionary, a CSV file, or a function for the replacement mapping

- It can overwrite file contents or create a modified copy in a new location.

- It can handle file and folder path substitutions in addition to file contents.

### Installation

To install AnonymoUUs, you can use the following command:

{{% codeblock %}} 
```python


pip install anonymoUUs


```
{{% /codeblock %}}

### Replacing Text with AnonymoUUs

To replace text using AnonymoUUs: 
- you must specify keywords - what text string(s) or patterns of text should be changed - and substitutes - what text should replace each keyword or pattern.
- You must indicate what folders or files the operation should run on. 

AnonymoUUs has three methods generating a replacement mapping. 




### Replacing text using a dictionary: 
A dictionary is written in python using the curly brackets:

example_dictionary = {keys: values}

In this scenario, the dictionary keys will represent the text you want to replace and the values represent the pseudonyms or replacement text. 

We can instruct the program to follow these key-values pairings to substitute text in a single file or in a group of files. We can overwrite the file or create a modified copy in a new location.


```python

from anonymouus import Anonymize

# Create a dictionary whose key-value pairs map to text and substitute
dictionary = {
    "Alex Taylor": "Arizona Worker 1", 
    "Emily Walker": "Arizona Worker 2",
    "Frank Burchess" : "Atacama Worker 1"
    } 

# Creating an instance of the class Anonymize
anonymize_dict = Anonymize(dictionary)

# Process the files in 'interview_transcripts'and 
# write a copy to the location 'pseudonymised_files'
original_file = '/Users/osulliva/Documents/interview_files'
new_file = '/Users/osulliva/Desktop/pseudonymised_files'

anonymize_dict.substitute(original_file, new_file)
```
###

In this example:
- We imported the class Anonymize from anonymoUUS. 
- We created a dictionary that linked the text we want to replace, with the text that should replace it. 
- We created an instance of the Anonymize class called 'anonymize_dict'so that we could later use the method anonymize_dict.substitute()
- We assigned the file path of the original text document to the variable 'original_file'
- We assigned the file path of the new folder to the variable 'new_File'
- We ran the substitute method which open and read all documents in 'original_file' and wrote replacements, substituting text according to our dictionary, in the location 'new_file'.

### Replacing text using a CSV file

In the previous example, the keys and values of a dictionary written in the python console instructed what keywords to replace and the substitutions to use for each keyword. 
Rather than writing a dictionary in the console, we can create a csv file that records the text and its replacement. 
AnonymoUUs will will interpret a csv file as a dictionary of keywords and their substitutes. 
- When AnonymoUUs reads a csv file it assumes it consists of two columns
- The left column is treated as the keys, and the right column is treated as the values. 
- It is necessary to include column headers

In this way, it is possible to write the list of keywords and substitutes elsewhere and keep your code shorter. 

{{% codeblock %}} 
```python
from anonymouus import Anonymize

# select a csv file to be used as the dictionary of 
# keywords and substitutes
csv = '/Users/osulliva/Documents/interview_substitutions.csv'
anonymize_csv = Anonymize(csv)

# write a copy with the substitutes to the location 'pseudonymised_files'
original_file = '/Users/osulliva/Documents/interview_files'
new_file = '/Users/osulliva/Documents/pseudonymised_files'

anonymize_csv.substitute(original_file, new_file)


```
{{% /codeblock %}}



### Replacing text using a function

It is possible to use a function as the mapping in the substitute method. 
In the example below, we will review the contents of a spreadsheet to remove references to specific ages, and assign labels based on the age of the participant. We will use the regular expression '\b\d{2}\b' to match with two digit numbers. 

{{% codeblock %}} 
```python
from anonymouus import Anonymize

#Make a function to substitute two digit numbers with an age band
def map_to_age_band(matched_text):
    number = int(matched_text)
    if 10 <= number < 20:
        return '[between 10 and 20]'
    elif 20 <= number < 30:
        return '[between 20 and 30]'
    elif 30 <= number < 40:
        return'[between 30 and 40]'
    elif 40 <= number < 50:
        return '[between 40 and 50]'
    else:
        return '[over 50]'
    

# Create an Anonymize instance
anon = Anonymize(map_to_age_band, pattern=r'\b\d{2}\b')

input_file = 'C:\\Users\\osulliva\\Documents\\interview_files\\interviewee_profile.csv'
replacement_file = 'C:\\Users\\osulliva\\Documents\\interview_files\\inteviewees_with_age_bands.csv'

# Call the substitute method to replace ages in the old file and save to the replacement file
anon.substitute(input_file, replacement_file)
```
{{% /codeblock %}}

More examples of functions written for AnonymoUUs can be found on the GitHub page.