---
tutorialtitle: "Contribute to Tilburg Science Hub"
type: "contribute-to-tsh"
indexexclude: "true"
title: "Style and Writing Guide"
description: "When contributing content to our platform, please follow our style and writing guidelines."
keywords: "style, styling, guideline, contribute, writing"
weight: 1005
draft: false
aliases:
  - /contribute/style-guidelines
---

## Style Guidelines

### Adopt Our Style of Communication

We are glossy and nerdy. We are welcoming, competent and helpful. We seek to cheerfully inform our users. We communicate concisely.

Will you blend in?

### Language

Please develop your content in English.

### Start Your Content With Our Templates

Please use our [building block templates](https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/topics/more-tutorials/contribute-to-tilburg-science-hub/building-block-shell.md) or [tutorial template](https://raw.githubusercontent.com/tilburgsciencehub/tsh-website/master/content/topics/more-tutorials/contribute-to-tilburg-science-hub/tutorial-shell.md) when developing new building blocks or tutorials.

<!-- ### Contribute via Git Pull Requests

Please fork our site, and develop your content in a new branch. When you're done, make a pull request, explain briefly what you've done (and why), and we're going to review your code and add it to the site. -->

### Style Your Content

Your content is written in [Markdown](https://guides.github.com/features/mastering-markdown/), and is automatically rendered in our house style.

You can also make use of code highlighting and admonitions.

#### Code Highlighting

In addition to the standard way of formatting code in Markdown, code snippets can be displayed in special boxes that highlight the code based on the programming language.

Provide your code in all the relevant languages and/or operating systems and specify them after the three back ticks. Wrap all of your snippets (in different languages) inside a codeblock shortcode (see our templates for more info on this, or simply look at the Markdown file of this page to see how we render the codeblock below).

{{% codeblock %}}
```python
# some Python code here
print("Hello, world!")
```

```R
# some R code here
cat('Hello, world!')
```
{{% /codeblock %}}

{{% warning %}}

Our platform natively supports only a limited set of programming languages for which it can provide automatic syntax highlighting in code boxes, like Python and R. You can find a list of all the currently supported languages **[here](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages)**.

Usually, you specify the intended language right after the first three back ticks.

![Some R code](../r-codeblock.png)

But what if you want to **provide some code in a language that is not on that list?** That's the case of Stata code, for instance.

In that case, you need to omit the language right after the three back ticks. This will disable syntax highlighting. Anyway, you can then specify the programming language to let the reader know which one it is, as shown here:

![Some Stata code](../stata-codeblock.png)

{{% /warning %}}

#### LaTeX Integration & Math Formulas

You can include mathematical notation via our KaTeX integration. You can learn more on how to use it [here](https://themes.gohugo.io/theme/hugo-book/docs/shortcodes/katex/).

If you use KaTeX more than once within the same Markdown file, there's no need to write the shortcode again. Simply place your math formulas:
- within single dollar signs for inline math: `$f(x)=x^2$` yields:
{{< katex >}}f(x)=x^2{{< /katex >}}
- within double dollar signs for display: `$$f(x)=x^2$$` yields: $$f(x)=x^2$$

#### Highlighting Boxes

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

#### How to handle wide tables

If you're using wide tables, they may appear broken on smaller screens like mobile phones. Therefore, you should always wrap your tables within the `wide-table` shortcode.

This will make sure that the right edge of the table fades out on small screens and they become scrollable on the horizontal axis. The following is an example of a wide table:

{{% wide-table %}}
|  |  |  |  |  |  |  
|-------------|-------------|------------|------------|---------------|---------------|
| $\alpha$    | `\alpha`    | $\beta$    | `\beta`    | $\gamma$      | `\gamma`      |
| $\delta$    | `\delta`    | $\epsilon$ | `\epsilon` | $\varepsilon$ | `\varepsilon` |
| $\zeta$     | `\zeta`     | $\eta$     | `\eta`     | $\theta$       | `\theta`      |
| $\vartheta$ | `\vartheta` | $\iota$    | `\iota`    | $\kappa$      | `\kappa`      |
| $\lambda$   | `\lambda`   | $\mu$      | `\mu`      | $\nu$         | `\nu`         |
| $\xi$       | `\xi`       | $\pi$      | `\pi`      | $\varpi$      | `\varpi`      |
| $\rho$      | `\rho`      | $\varrho$  | `\varrho`  | $\sigma$      | `\sigma`      |
| $\tau$      | `\tau`      | $\upsilon$ | `\upsilon` | $\phi$        | `\phi`        |
| $\varphi$   | `\varphi`   | $\chi$     | `\chi`     | $\psi$        | `\psi`        |
| $\omega$    | `\omega`    |
{{% /wide-table %}}

{{% tip %}}

Click **[here](https://github.com/tilburgsciencehub/website/blob/master/content/topics/more-tutorials/contribute-to-tilburg-science-hub/style-guide.md)** to check out the Markdown file of this page to learn how these shortcodes are used in the text.

{{% /tip %}}

#### Adding Footnotes
Footnotes [^1] let you reference relevant information without disrupting the flow of what you're trying to say. Need to make use of footnotes? Here is how to add them in Markdown:
```
Footnotes[^1] let you (...)
[^1]: My reference
```
[^1]: [Footnotes in Markdown](https://github.blog/changelog/2021-09-30-footnotes-now-supported-in-markdown-fields/)
### Writing Instructions

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
- Capitalize Your Headings Like This. But don't do that for articles and prepositions.
- Avoid headings to start with articles and "How to...". Of course we're telling you how to do it.
- Use `##`, `###`, `####` for headers, not a standard line on **bold**. Use `**` only for bolded words or short sentences when you want to stress a concept. Learn more about markdown syntax [here](https://www.markdownguide.org/basic-syntax/).
- Do **NOT** use `#` for headers. Instead, use the appropriate `title` flag for your main header.
- Suggest at least one short link for your article! Combine an action verb and a noun like this: /VERB/NOUN (/do/this, /learn/that, /get/me). Ex. https://tilburgsciencehub.com/get/python. You will find these instructions in the contribution template.
- Be consistent and double-check your file before sending!

{{% tip %}}
If you want to be credited for your work, don't forget to fill in the `author` and `authorlink` fields at the top of our templates with your name and a link to your personal webpage, respectively.
{{% /tip %}}

{{% warning %}}
**The naming of your file matters!**

We use the filename, which is different from the actual article's title, to extract information and display the current path within the navigation menu and on the breadcrumb trails. Please, choose your filename carefully!

Generally speaking, it's a good idea to name your file exactly like your main title, but using all lowercase letters and separating words with a `-`.

**Example**:

    Title: Automation with GNU Make
    Filename: automation-with-gnu-make.md
{{% /warning %}}

### Add the correct tags
Every page has at the top of the code tags which, among others, help index the page. 
```
---
tutorialtitle: "Web Scraping and API Mining [a good title] " 
type: "web-scraping [very short title ~2/3 words with no capitols nor spaces]" 
title: "Web Scraping and API Mining [the same good title]" 
description: "[a short, relevant summary of what a particular page is about]"
keywords: "scrape, webscraping, beautifulsoup .. [relevant keywords to the page]" 
weight: 1 [to determine the position in the navigation 1 at the top 99 at the bottom] 
draft: false [false when finished, true when it is still a draft]
aliases: [other urls which lead to this page]
  - /learn/web-scraping-and-api-mining [first alias is the short link]
  - /topics/more-tutorials/web-scraping/web-scraping-tutorial/
---
```

## Develop content for our target audience

When contributing content to our platform, please address at least one of our target groups.

1. __Students and novice researchers__ who look for material developed, curated, and rigorously tested by professors and experienced users, ensuring them about quality and usability. Users may not know yet what (and why) they should learn the Tilburg Science Hub way of working. These users need to be onboarded first and guided through our content.

2. __(Advanced) researchers and professors__ who look for useful material developed by their peers. These users have identified a problem, but need code snippets to use in their projects. Researchers seek to avoid mistakes that others have made before them, and look to get inspired by their colleagues. They may also use our platform to share their solutions to problems (e.g., in the form of building blocks or tutorials).

3. __Teams and small businesses__ who wish to get inspired by how scientists work on on data-intensive projects. Tilburg Science Hub offers tools and knowledge to help teams work together better, more efficiently. Our content can be adopted by individual team members (i.e., adoption doesn't disturb the way of working of other team members), or jointly by a team (i.e., the entire team commits to the Tilburg Science Hub way of working). <!--Businesses can also request a paid custom consultancy to implement reproducible workflows in their own processes.-->

4. __Data science enthusiasts__ who encounter our site when working on their projects. We strive to become a key learning resource in the data science community.

{{% warning %}}

**Keep in mind our key goals**

Our platform focuses on __usability__ (i.e., ability to quickly copy-paste code or download templates), __speed__ (i.e., loading time), and __attractiveness__ (i.e., visual appeal, “state-of-the-art” look, good writing).

Our platform is a (classical) two-sided market.

1. We attract __novice and expert users__ that *use* our content in their work, and

2. We build a __community of content creators__ that have an outspoken vision on how to conduct science efficiently.
{{% /warning %}}

{{% warning %}}
**License**

Text and content are licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/). In other words, our content can be reused by anybody for non-commercial purposes, but needs to be properly cited.

[![Creative Commons Licence](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0)

{{% /warning %}}

<!--
### Use cases for experienced users and novices:
TSH communicates content expertise and content depth that is appealing to advanced users. At the same time, it appeals to novices who use TSH to (i) understand what is potentially wrong in their current workflow; (ii) understand the advantages of our proposed one; (iii) understand what is needed to get started and what they need to learn; (iv) learn the concepts and put them into practice with templates, examples, and exercises.

Students and professors:
TSH seeks to build a community of professors and scholars who use reproducible science in their daily work and want to contribute (with their own code). These professors build content that is useful for their students. Also, they share content that they can use to kick-start their own projects without "reinventing the wheel".

New users and returning ones:
Ideally, TSH is ranked high on search engines to attract new users. It also becomes part of the curriculum at various schools. For returning users, it becomes the essential bookmark tab they often resort to, knowing they will find the information they need to run their projects.
-->
