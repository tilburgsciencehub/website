---
title: "Learn Regular Expressions"
description: "Learn how to formulate powerful string search queries with regular expressions."
keywords: "regular expressions, regex, strings, string processing, characters, regexp, search pattern, string searching"
#date: 2020-11-11T22:02:51+05:30
draft: false
#weight: 3
aliases:
  - /learn/regex
  - /learn/regular-expressions
---

## What are regular expressions?

Regular expressions provide a concise language for describing patterns in strings. They make finding information easier and more efficient. That is, you can often accomplish with a single regular expression what would otherwise take dozens of lines of code. And while you can often come a long way with the default `strip()` and `replace()` functions, they have their own set of limitations. For example, how do you extract emails or hashtags from a text? Or how do you strip away HTML tags from the web page source code? Regular expressions fill this void and are a powerful skill for any data scientist's toolkit!

{{% warning %}}
At first sight, regular expressions can look daunting but don't be put off! In this building block, we break down the syntax into tangible pieces so that you can get up to speed step by step.

{{% /warning %}}


## Code

### Match Characters
The `re` Python library contains a variety of methods to identify, split, and replace strings. The `findall()` function returns all matching cases that satisfy a character pattern. Each pattern starts with `r"` followed by one or more symbols. Please note that "regular" characters can be chained together with these symbols. For example, `r"\d\ds"` refers to 2 digits (`\d`) followed by a lower case letter `s`. The equivalent in "R" is found in the library `stringr` by means of the `str_match_all` function. In Stata the function `regexm` can be employed. However, it only reports a value equal to 1 if the expression is true and 0 otherwise.

| Symbol     |       |            |                                     |                    |
| ---------- | ----- | ---------- | ----------------------------------- | ------------------ |
| **Python** | **R** | **Stata**  | **Definition**                      | **Example**        |
| `\d`       | `\\d` | `[0-9]`    | digit                               | 0, 1... 9          |
| `\s`       | `\\s` | (a space)  | whitespace                          | (a space)          |
| `\w`       | `\\w` | `[a-zA-Z]` | single letter, number of underscore | a, 4, _            |
| `.`        | `\.`  | `.`        | any character                       | b, 9, !, (a space) |


{{% tip %}}
 Want to find all but a certain character? Use capital letters for the symbols instead. For instance, `\\D` in R, matches all but a single digit.
{{% /tip %}}

{{% warning %}}
In "Stata" regular expressions are much less flexible. However, they are still widely used for more specific purposes. In this sense, we provide different examples of regex usage for Stata.
{{% /warning %}}

The four examples below illustrate how to combine these symbols to extract various characters from `my_string`.

{{% codeblock %}}

```python
import re
my_string = "The 80s music hits were much better than the 90s."

# a single digit: ['8', '0', '9', '0']
print(re.findall(r"\d", my_string))

# double digits: ['80', '90']
# hereafter we learn how to write this more concisely using quantifiers
print(re.findall(r"\d\d", my_string))

# combinations of 3 characters (even if it's not a complete word)
# ['The', '80s', 'mus', 'hit', 'wer', 'muc', 'bet', 'ter', 'tha', 'the', '90s']
print(re.findall(r"\w\w\w", my_string))

# combinations of 3 characters that start and end with a space (note: the first "The" is skipped!): [' 80s ', ' the ']
print(re.findall(r"\s\w\w\w\s", my_string))
```

```R
library(stringr)
my_string = "The 80s music hits were much better than the 90s."

# a single digit: ['8', '0', '9', '0']
str_match_all(my_string, "\\d")

# double digits: ['80', '90']
# hereafter we learn how to write this more concisely using quantifiers
str_match_all(my_string, "\\d\\d")

# combinations of 3 characters (even if it's not a complete word)
# ['The', '80s', 'mus', 'hit', 'wer', 'muc', 'bet', 'ter', 'tha', 'the', '90s']
str_match_all(my_string, "\\w\\w\\w")

# combinations of 3 characters that start and end with a space (note: the first "The" is skipped!): [' 80s ', ' the ']
str_match_all(my_string, "\\s\\w\\w\\w\\s")
```
```
- Stata-
gen str my_string = "The 80s music hits were much better than the 90s."
# a single digit: '1' (as there are 4 digits, it will refer to the first one found)

```
{{% /codeblock %}}


### Quantifiers
In the examples above, we explicitly formulated a pattern of 1, 2, or 3 characters but in many cases this is unknown. Then, quantifiers can offer some flexibility in defining a search pattern of 0, 1, or more occurences of a character. Note that the symbols always refer to the character preceding it. For example, `r"\d+"` means one or more digits. The following quantifiers work for all python, R and Stata.

| Symbol | Definition | Example |
|:---- | :---- | :---- |
| `?` | zero or one | `colou?r` (you want to capture both `color` and `colour`) |
| `*` | zero or more | `\d\.\d*` (a single digit followed by zero or more decimals - e.g., 5.34, 8., 3.1)|
| `+`  | one or more  | `#\w+` (e.g., Twitter hashtags)|
| `{n,m}`  | between n and m | `\d{2}-\d{2}-\d{4}` (dates e.g., 05-03-2021)|


{{% codeblock %}}
```python
import re
my_string = "The 80s music hits were much better than the 90s."

# all words: ['The', '80s', 'music', 'hits', 'were', 'much', 'better', 'than', 'the', '90s']
print(re.findall(r"\w+", my_string))

# one or more digits followed by a s: ['80s', '90s']
print(re.findall(r"\d+s", my_string))

# words that are preceded or followed by more than one whitespace (i.e., to identify unnecessary spaces)
print(re.findall(r"\s{2,}\w+\s{2,}", my_string))
```

```R
library(stringr)
my_string = "The 80s music hits were much better than the 90s."

# all words: ['The', '80s', 'music', 'hits', 'were', 'much', 'better', 'than', 'the', '90s']
str_match_all(my_string, "\\w+")

# one or more digits followed by a s: ['80s', '90s']
str_match_all(my_string, "\\d+s")

# words that are preceded or followed by more than one whitespace (i.e., to identify unnecessary spaces)
str_match_all(my_string, "\\s{2,}\\w+\\s{2,}")
```
{{% /codeblock %}}


### Alternates

| Symbol | Definition | Example |
|:---- | :---- | :---- |
| `a|b|c`  | or  | `color|colour`  |
| `[abc]` | one of | `[$€]` (a dollar or euro currency sign)|
| `[^abc]` | anything but  | `[^q]` (any character except q) |
| `[a-z]` | range  | `[a-zA-Z]+` (i.e., one or more lower or upper case letters) or `[0-9]` (digits)|


{{% codeblock %}}
```python
my_string = "The 80s music hits were much better than the 90s."

# words that consist solely of lower case letters
# [' music', ' hits', ' were', ' much', ' better', ' than', ' the']
print(re.findall(r"\s[a-z]+", my_string))

# one or more letters followed by a space, one or more digits, and a letter s: ['The 80s', 'the 90s']
print(re.findall(r"[a-zA-Z]+\s\d+s", my_string))
```

```R
my_string = "The 80s music hits were much better than the 90s."

# words that consist solely of lower case letters
# [' music', ' hits', ' were', ' much', ' better', ' than', ' the']
str_match_all(my_string, "\\s[a-z]+")

# one or more letters followed by a space, one or more digits, and a letter s: ['The 80s', 'the 90s']
str_match_all(my_string, "[a-zA-Z]+\\s\\d+s")
```
{{% /codeblock %}}


### Groups
More often than not, you want to capture text elements and use it for follow-up analyses. However, not every element of a pattern may be necessary. Groups, denoted by parentheses `()`, indicate the pieces that should be kept, and each match is stored as a list of tuples.


{{% codeblock %}}
```python
import re
my_string = "Lara has 2 sisters who also study in Tilburg. Mehmet has 1 sister who was born last year. Sven has 19 cousins who are all older than him."

# store the person's name, the digit, and the number of relatives.
# [('Lara', '2', 'sisters'), ('Mehmet', '1', 'sister'), ('Sven', '19', 'cousins')]
family = re.findall(r"([a-zA-Z]+)\s\w+\s(\d+)\s(\w+)", my_string)

# next, you can reference elements like you're used to, for example:
print(family[0][2])  # gives 'sisters'
```
```R
library(stringr)
my_string = "Lara has 2 sisters who also study in Tilburg. Mehmet has 1 sister who was born last year. Sven has 19 cousins who are all older than him."

# store the person's name, the digit, and the number of relatives.
# [('Lara', '2', 'sisters'), ('Mehmet', '1', 'sister'), ('Sven', '19', 'cousins')]
family = str_match_all(my_string, "([a-zA-Z]+)\\s\\w+\\s(\\d+)\\s(\\w+)")

# next, you can reference elements like you're used to, for example:
 print(family[[1]][[1,4]])  # gives 'sisters'
```
{{% /codeblock %}}

### Text in Between Characters
Regular expressions can also be used to extract text in between characters. For instance, using the same string as before, if we want to extract the number of cousins that Sven has we can employ the following code.

{{% codeblock %}}
```python
import re
my_string = "Lara has 2 sisters who also study in Tilburg. Mehmet has 1 sister who was born last year. Sven has 19 cousins who are all older than him."

found = re.findall("Sven has(.+?)cousins", my_string)
print(found)
```
```R
library(stringr)
my_string = "Lara has 2 sisters who also study in Tilburg. Mehmet has 1 sister who was born last year. Sven has 19 cousins who are all older than him."

found = str_match_all(my_string, "Sven has(.+?)cousins")
print(found[[1]][[1,2]])
```

{{% /codeblock %}}

### Split & Replace Data

Regular expressions can also be used to split (`re.split()` in python and `strsplit` in R ) or replace (`re.sub()` in python and `gsub` in R) characters. While the built-in `split()` function can split on a single character (e.g., `;`), it cannot deal with a multitude of values. The same holds for Python's `replace()` function. The same goes for the analogous R functions.

{{% codeblock %}}
```python
import re
my_string = 'Last year was our most profitable year thus far. Our year-on-year growth grew by 14% to $10B!'

# split on both "! and ".":
# ['Last year was our most profitable year thus far',' Our year-on-year growth grew by 14% to $10B','']
re.split(r"[!.]", my_string)

# hide confidential data:
# 'Last year was our most profitable year thus far. Our year-on-year growth grew by X% to $XB!'
re.sub(r"\d+", "X", my_string)
```
```R
library(stringr)
my_string = 'Last year was our most profitable year thus far. Our year-on-year growth grew by 14% to $10B!'

# split on both "! and ".":
# ['Last year was our most profitable year thus far',' Our year-on-year growth grew by 14% to $10B','']
strsplit(my_string, "[!.]")

# hide confidential data:
# 'Last year was our most profitable year thus far. Our year-on-year growth grew by X% to $XB!'
gsub("\\d+", "X", my_string)
```
{{% /codeblock %}}

### Web Scraping

In addition to Beautifulsoup, you can apply regular expressions to parse HTML source code. Say the source code of a webpage consists of a book title, description, and a table:

```python
html_code = '''
<h2>A Light in the Attic</h2>
<p>It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers.</p>
<table class="table table-striped">
    <tr>
        <th>UPC</th><td>a897fe39b1053632</td>
    </tr>
    <tr>
        <th>Price (incl. tax)</th><td>Â£51.77</td>
    </tr>
    <tr>
        <th>Availability</th>
        <td>In stock (22 available)</td>
    </tr>
    <tr>
        <th>Number of reviews</th>
        <td>0</td>
    </tr>
</table>
'''
```

Then, we can easily capture the text between two tags, a part of a row, or a specific section of the source code. Since the HTML code is split across multiple lines, the regex code `.+` does not work as expected: it only matches characters on the first line. If you print the `html_code` to the console, you also find that each line is separated by a newline separator (\n). As a workaround, you can use the following set `[\s\S]+` to capture both spaces (\s) and non-spaces (\S = letters, digits, etc.). Note that in the examples below, we rely on groups `()` to only select the elements we are after.

{{% codeblock %}}
```python
# title: ['A Light in the Attic']
re.findall(r"<h2>(.+)</h2>", html_code)

# availability: ['22']
re.findall(r"(\d+) available", html_code)

# <h2> and <p> sections
re.findall(r"[\s\S]+</p>", html_code)

# table section
re.findall(r"<table[\s\S]*", html_code)
```
```R
# title: ['A Light in the Attic']
str_match_all(html_code, "<h2>(.+)</h2>" )

# availability: ['22']
str_match_all(html_code, "(\\d+) available" )

# <h2> and <p> sections
str_match_all(html_code, "<[\\s\\S]+</p>" )

# table section
str_match_all(html_code, "<table[\\s\\S]*" )

{{% /codeblock %}}

## Advanced Use Cases

**Greedy vs non-greedy**  
By default, regular expressions follow a greedy approach which means that they match as many characters as possible (i.e., returns the longest match found). Let´s have a look at an example to see what this means in practice. Say that we want to extract the contents of `my_string` and thus remove the HTML tags.

Therefore, we replace the two paragraph tags (`<p>` and `</p>`) with an empty string. Surprisingly, it returns an empty string (`''`), why is that? After all, we would expect to see: `This is a paragraph enclosed by HTML tags.`.

It turns out that the `>` in `<.+>` refers to the `</p>` tag (instead of `<p>`). As a result, the entire sentence is replaced by an empty string! Fortunately, you can force the expression to match as few characters as needed (a.k.a. non-greedy or lazy approach) by adding a `?` after the `+` symbol.

{{% codeblock %}}
```python
import re
my_string = '<p>This is a paragraph enclosed by HTML tags.</p>'

# greedy approach: ''
re.sub(r"<.+>", "", my_string)

# non-greedy approach: 'This is a paragraph enclosed by HTML tags.'
re.sub(r"<.+?>", "", my_string)
```
```R
library(stringr)
my_string = '<p>This is a paragraph enclosed by HTML tags.</p>'

# greedy approach: ''
gsub("<.+>", "", my_string)

# non-greedy approach: 'This is a paragraph enclosed by HTML tags.'
gsub("<.+?>", "", my_string)
```
{{% /codeblock %}}


## See Also
* As you may have figured out by now, formulating regular expressions is often a matter of trial and error. An [online regex editor](https://regexr.com) that interactively highlights the phrases your regular expression captures can therefore be extremely helpful.

* Frequent applications of regular expressions are extracting dates and emails (and checking for validity), parsing webpage source data, and natural language processing. [This](https://www.analyticsvidhya.com/blog/2020/01/4-applications-of-regular-expressions-that-every-data-scientist-should-know-with-python-code/) blog post demonstrates how you can implement these ideas.

* This building block deliberately only revolved around the most common regex operations, but there are many more symbols and variations. [This](https://www.programiz.com/python-programming/regex) tutorial provides a more comprehensive list of commands (incl. examples!).
