---
title: "Style and Writing Guide"
description: "When contributing content to our platform, please follow our style and writing guidelines."
keywords: "style, styling, guideline, writing"
weight: 1
draft: false
---

## Develop content for our target audience

When contributing content to our platform, please address at least one of our target groups.

1. __Students and novice researchers__ who look for material developed, curated, and rigorously tested by professors and experienced users, ensuring them about quality and usability. Users may not know yet what (and why) they should learn the Tilburg Science Hub way of working. These users need to be onboarded first and guided through our content.

2. __(Advanced) researchers and professors__ who look for useful material developed by their peers. These users have identified a problem, but need code snippets to use in their projects. Researchers seek to avoid mistakes that others have made before them, and look to get inspired by their colleagues. They may also use our platform to share their solutions to problems (e.g., in the form of building blocks or tutorials).

3. __Teams and small businesses__ who wish to get inspired by how scientists work on on data-intensive projects. Tilburg Science Hub offers tools and knowledge to help teams work together better, more efficiently. Our content can be adopted by individual team members (i.e., adoption doesn't disturb the way of working of other team members), or jointly by a team (i.e., the entire team commits to the Tilburg Science Hub way of working). <!--Businesses can also request a paid custom consultancy to implement reproducible workflows in their own processes.-->

4. __Data science enthusiasts__ who encounter our site when working on their projects. We strive to become a key learning resource in the data science community.

## Keep in mind our key goals

Our platform focuses on __usability__ (i.e., ability to quickly copy-paste code or download templates), __speed__ (i.e., loading time), and __attractiveness__ (i.e., visual appeal, “state-of-the-art” look, good writing).

Our platform is a (classical) two-sided market.

1. We attract __novice and expert users__ that *use* our content in their work, and

2. We build a __community of content creators__ that have an outspoken vision on how to conduct science efficiently.

All of our content is licensed under the Creative Commons License, CC-BY-NC 4.0. In other words, it can be reused by anybody for non-commercial purposes, but needs to be properly cited.

<!--
### Use cases for experienced users and novices:
TSH communicates content expertise and content depth that is appealing to advanced users. At the same time, it appeals to novices who use TSH to (i) understand what is potentially wrong in their current workflow; (ii) understand the advantages of our proposed one; (iii) understand what is needed to get started and what they need to learn; (iv) learn the concepts and put them into practice with templates, examples, and exercises.

Students and professors:
TSH seeks to build a community of professors and scholars who use reproducible science in their daily work and want to contribute (with their own code). These professors build content that is useful for their students. Also, they share content that they can use to kick-start their own projects without "reinventing the wheel".

New users and returning ones:
Ideally, TSH is ranked high on search engines to attract new users. It also becomes part of the curriculum at various schools. For returning users, it becomes the essential bookmark tab they often resort to, knowing they will find the information they need to run their projects.
-->

## Specific instructions

### Adopt our style of communication

We are glossy and nerdy. We are welcoming, competent and helpful. We seek to cheerfully inform our users. We communicate concisely.

Will you blend in?

### Language

Please develop your content in English.

### Start your content with our templates

Please use our templates when developing new building blocks or tutorials.

### Contribute via Git Pull Requests

Please fork our site, and develop your content in a new branch. When you're done, make a pull request, explain briefly what you've done (and why), and we're going to review your code and add it to the site.

### Styling your content

Your content is written in markdown, and is automatically rendered in our house style.

You can also make use of code highlighting and admonitions.

#### Code highlighting

We currently support code highlighting for bash, R, Python and STATA. Want to add another language? Create an issue on our GitHub repository.

#### Highlighting boxes

We support four kind of highlighting boxes.

{{% tip %}}

This is a tip

{{% /tip %}}


{{% warning %}}
This is a warning

{{% /warning %}}

{{% summary %}}
This is a summary

{{% /summary %}}

{{% example %}}
This is an example

{{% /example %}}

#### Writing tips

- Use the second person ("you") when speaking to our or talking about our users
- Content creators may refer to themselves in the first person ("I" in single-author articles, or "we" in multiple-author articles). Do remember to keep the focus on our users.
- Avoid personal references: e.g., in my career, on a project I run.
- We encourage the use of contractions: e.g., it’s, you’ll, you’re, we’re, let’s.
- We prefer shorter words over longer alternatives.
  - e.g., "helps" is better than "facilitates"
  - e.g., "uses" is better than "utilizes"
- Use an active voice wherever possible.
- Write conversationally: prepositions are okay to end sentences with. And another thing. You can even start sentences with "And" or "But."
- Be informal, but being clear is more important than being entertaining!
- Get to the point fast.
- Frame sentences positively: use positive language (e.g., be more efficient, write better code...), rather than negative language (e.g., avoid mistakes...).
- Avoid slang.
- Avoid jargon. We know it's difficult for you academics out there.
- Use `#`, `##`, `###`, `####` for headers, not a standard line on **bold**. Use `**` only for bolded words or short sentences when you want to stress a concept. Learn more about markdown syntax [here](https://www.markdownguide.org/basic-syntax/).
- Be consistent and double-check your file before sending!

{{% warning %}}
**The naming of your file matters!**

We use the filename, which is different from the actual article's title, to extract information and display the current path within the navigation menu and on the breadcrumb trails. Please, choose your filename carefully!
{{% /warning %}}
