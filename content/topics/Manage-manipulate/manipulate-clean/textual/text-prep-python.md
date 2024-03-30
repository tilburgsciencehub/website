---
title: "Text Pre-processing in Python" 
description: "Dive into the world of text preprocessing with Python! Learn how to clean, tokenize, and visualize text data for your NLP projects using popular libraries such as pandas, spaCy, and matplotlib"
weight: 2
author: "Fernando Iscar"
authorlink: "https://www.linkedin.com/in/fernando-iscar/"
draft: false
date: 2023-03-29
aliases: 
  - /text-python
---

# Overview

The ability to process and analyze text data is increasingly important in the era of big data. From social media analytics to customer feedback analysis, the insights gained from text data can inform decision-making and reveal trends. However, raw text data is often messy and unstructured. Preprocessing this data into a clean format is essential for effective analysis.

This tutorial introduces the fundamental techniques of text preprocessing in Python, utilizing the [pandas](https://pandas.pydata.org/) library for data manipulation, [spaCy](https://spacy.io/) for tokenization and lemmatization, and [matplotlib](https://matplotlib.org/) for data visualization. By the end of this guide, you'll be equipped with some fundamental skills to prepare text data for a Natural Language Processing (NLP) project.


# Getting Started

In this tutorial, we will explore the process of loading, cleaning, and preprocessing text data from subReddit descriptions. SubReddits are specific communities within the larger [Reddit platform](https://edu.gcfglobal.org/en/thenow/what-is-reddit/1/#), focusing on various topics such as machine learning or personal finance.

## Natural Language Processing (NLP)

When building machine learning models, we typically work with numeric features as models only understand numerical data. However, there are cases where our features are in categorical text format. In such situations, we need to preprocess and encode these features into numerical format, often referred to as vectors, using techniques like Label Encoding or One Hot Encoding.

The main challenge arises when our entire feature set is in text format, such as product reviews, tweets, or comments. How do we train our machine learning model with text data? As we know, machine learning algorithms only work with numeric inputs.

NLP is a branch of Artificial Intelligence (AI) that enables computers to understand, interpret, manipulate, and respond to human language. In simple terms, NLP allows computers to comprehend human language.

In order to effectively preprocess text data, it is important to understand key techniques such as tokenization, stemming, and lemmatization. These techniques play a crucial role in breaking down text into smaller units, reducing words to their base form, and producing valid words respectively.

### Tokenization

Tokenization is the process of breaking down a text into smaller units called tokens. These tokens can be words, sentences, or even characters, depending on the level of granularity required. Tokenization is an essential step in text preprocessing as it forms the basis for further analysis and manipulation of text data.

{{% example %}}

{{% codeblock %}}
```python
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Here's an example of tokenization: breaking down text into individual words!"

# Tokenize the text
doc = nlp(text)

# Extract tokens
tokens = [token.text for token in doc]

print(tokens)
```
{{% /codeblock %}}

The `output` will be a list of tokens: `["Here", "'s", "an", "example", "of", "tokenization", ":", "breaking", "down", "text", "into", "individual", "words", "!"]`. Notice how punctuation and spaces are treated as separate tokens, which is typical in word tokenization.

{{% /example %}}

### Stemming

Stemming is a technique used to reduce words to their base or root form, known as the stem. It involves removing suffixes and prefixes from words to obtain the core meaning. Stemming helps in reducing the dimensionality of text data and can be useful in tasks such as information retrieval and text classification.

{{% example %}}

{{% codeblock %}}
```python
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize the stemmer
stemmer = PorterStemmer()

# Sample text
text = "The boys are playing football. One boy is injured."

# Tokenize the text
tokens = word_tokenize(text)

# Stem each token
stemmed_tokens = [stemmer.stem(token) for token in tokens]

print(stemmed_tokens)

```
{{% /codeblock %}}

The `output` might look like `['The', 'boy', 'are', 'play', 'footbal', '.', 'One', 'boy', 'is', 'injur', '.']`, demonstrating how stemming simplifies words to their roots, albeit not always in a grammatically correct form.

{{% /example %}}

### Lemmatization

Lemmatization, unlike stemming, reduces words to their base or dictionary form, known as the lemma. It involves a more sophisticated analysis of a word's morphology to arrive at its simplest form, which ensures that the result is a valid word.

{{% example %}}

{{% codeblock %}}
```python
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "The boys are playing football. One boy is injured."

# Tokenize and lemmatize the text
doc = nlp(text)

# Extract lemmatized tokens
lemmatized_tokens = [token.lemma_ for token in doc]

print(lemmatized_tokens)

```
{{% /codeblock %}}

The `output` will be: `['the', 'boy', 'be', 'play', 'football', '.', 'one', 'boy', 'be', 'injure', '.']`. Here, verbs like "are" and "is" are lemmatized to "be", and "injured" to "injure", ensuring the result is grammatically viable.

{{% /example %}}


