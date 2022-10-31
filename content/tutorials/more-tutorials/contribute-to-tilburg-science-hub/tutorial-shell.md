INSTRUCTIONS:
- This is a template. Please replace the content while keeping this structure.
- Make sure to read our contribution guide to learn how to submit your content to Tilburg Science Hub.
- Always start your file with the parameters shown below. Keep the double quotes as shown.
- Do NOT use #Titles lines (with a single #) in your article. Instead, use the title parameters shown below.
- Please provide up to 10 keywords for each tutorial page in the appropriate parameter. Metadata should provide information on the role and usage of this tutorial (e.g., "data collection, data analysis, article writing")
- IMPORTANT! Replace the # of the weight parameter with an integer (no quotes are needed). This number indicates the relative position of this page within the tutorial hierarchy. The ordering of all pages inside a tutorial folder is based on their weight. Pages with lower weight appear at the top.
- IMPORTANT! Remove the indexexclude: "true" line from the FIRST page of your tutorial. All subsequent pages should have it instead.
- If your tutorial is only one page long, remove the indexexclude: "true" line, create a folder named like your "type" below, and save your page as "index.md" inside that folder.
- If you want to be credited, fill in the author and authorlink fields below. If you want to remain anonymous, delete those.
- Provide at least one short link for each of your tutorial pages. Combine an action verb and a noun like this: /verb/noun (ex. /install/python).
- Write the most important keyword of your page once bold in the text
- Remove these instructions before submitting. Your article should start with the three dashes --- and the following parameters.
---
tutorialtitle: "Your Building Block Title (50-70 characters + most important keyword must be in the title atleast once)"
type: "your-building-block-title (spaces replaced with - and no capitals)"
title: "Your building block title (50-70 characters)"
description: "A brief description of this tutorial page (130–160 characters + most important keyword must be in the descripion atleast once)."
keywords: "any, relevant, keywords, separated, by, commas, like, this" 
date: YYYY-MM-DD 
weight: # 
indexexclude: "true" 
author: "Your Name" 
authorlink: "A link to your personal webpage" 
aliases:
  - /verb/noun
  - /do/this
  - /get/that
  - add as many as you want, but at least one
---

## Overview

Provide a brief overview of the issue to solve, or why this is a best practice. Explain the goal of this step and how it connected to the previous ones. Optionally, if you have assigned a task in the previous chapter, provide the solution at the beginning of this one.

## The task

Explain the solution step by step. If there's code involved, explain small snippets first and add more to build the final code, which you can display at the end of the chapter.

### Step 1

#### Step 1.1

Use subheaders if needed.

## Code <!-- Provide your code in all the relevant languages and/or operating systems and specify them after the three back ticks. Do NOT remove {{% codeblock %}} -->

{{% codeblock %}} <!-- You can provide more than one language in the same code block -->

[python-link](code.py) <!-- OPTIONAL: You can also provide your code as a downloadable file (useful for very long codes). Make sure you place this file in the same folder. Specify in [square brackets] the language followed by "-link" as shown here.-->


```python
# some Python code here
print("Hello, world!")
```

```R
# some R code here
cat('Hello, world!')
```

{{% /codeblock %}}

## Next steps

Explain briefly how to bring this to the next level, provide useful resources, and announce what will come in the following chapter.

{{% tip %}}

**This is a tip.**

You can use special formatting options to highlight some paragraphs in your article.

{{% /tip %}}

{{% warning %}}

And this is a warning.

{{% /warning %}}

## (Optional) Knowledge check

Challenge your audience with a small test, quiz or task. You can provide the (written or video) answer in the next chapter.

{{% summary %}}

Lastly, consider including a brief summary to wrap up your article.

{{% /summary %}}
