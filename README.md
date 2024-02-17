# Tilburg Science Hub To Flask
This is the repository thats hosts the news flask application for Tilburg Science Hub

## Install Packages
```
pip install Flask-SQLAlchemy
pip install SQLAlchemy
pip install beautifulsoup4
pip install nltk
pip install markdown
pip install Flask-Assets
```

## Content To Database
To create the database with all necessary data, simply go to the root folder and run the following command:

```python3 content_to_db.py```

## Start Up Flask Application
After successfully creating the database, you are ready to start up the flask application. To do so run the following command in the root folder:

flask run

## Updated & Implemented
- [x] Fix Authors
- [x] Related Articles
- [x] Blogs
    - [x] List
    - [x] Add to db
    - [x] Single
- [x] Breadcrumbs
- [x] In text links with {{% cta-primary-center .. %}} do not render -> shortcode added to parser
- [x] Header does not display BB's when hovering over it -> first item added classes active
- [x] urls on homepage cards dont work -> removed backslash at the end
- [x] Edit page url doesn't work -> url fixed
- [x] ODCM tutorial does not work (specific) -> pagination problem (empty weight), issue solved
- [x] formatting does not render in {{% blocks %}} (e.g. Learn R BB/ set up docker) -> adjust formatting in tips, example, warning.
- [x] {{% example }} block does not render (e.g. use Scrum in your team BB) -> implemented example
- [x] under automate and execute your work there is a "new" category called error handling? -> this is an error in the index.md of that file. For some reason it contains 2 draft parameters, which ofcourse results in problems. 
- [x] videos are not able to play (BB configuring git) -> corrected video parsing and move video files to img
- [x] symbols (e.g. $\alpha$) do not render -> issue with katex, fixed, stil a problem in content, documented in section "Issues related to content".
- [x] formulas in {{}} {{}} also do not render (both in BB on fixed effects) -> issue with katex, fixed.
- [x] << katex >> also does not render (BB sample size on webscrapers) -> issue with katex, fixed.
- [x] external youtube link does not render {{< youtube DK7TYR68kqc iframe-video-margins >}} (BB practicing pipeline automation > verify)
- [x] Text out of line (e.g. BB on cars/ interactive Interactive shiny COVID-19)
- [x] #'s in a ``` block get converted to headers instead of to just small text within the block (BB configure git/ reschedule tasks) -> created a fallback codeblock such as in the current website
- [x] remove google console bugs (js bugs mainly)
- [x] make slider on mobile only move when clicked/touched -> implemented from main
- [x] Most read tutorials - duplicates -> implemented from main
- [x] scaling of tilburg science hub image on landing page off -> implemented from main
- [x] bug w/ slider on mobile -> implemented from main
- [x] About page in footer -> implemented from main
- [x] Recently updated/published settings -> works now with date and date_modified.
- [x] About menu in header -> Added al necessary pages
- [x] add reading time estimate -> implemented
- [x] Cookies -> Fixed, we only need a basic analytics script.
- [x] Code Block 
- [x] Dual Code Blocks 
- [x] Copy Button in Codeblock
    
## Features/Issues to Update/Implement
- [ ] MetaData
- [ ] Implement New Basic Web Analytics Cookies
- [ ] Bullet points do not render correctly (e.g., Random Effects Model)
- [ ] $ formulas do not render correctly (e.g., Random Effects Model)
- [ ] tables do not display correctly (e.g., Random Effects Model, Configure Python virtual environments)
- [ ] Reproducible Research (homepage) link does not work
- [ ] Contributors links of people that do not do have a contributors page result in an error
- [ ] font size is off (Scrape static websites)
- [ ] Time of writing does not display nicely (e.g. Use Google Colab to RUn Python in the Cloud (2022-04-08T10:01:14+05:30)
- [ ] Title does not display properly (e.g., Confgure Python virtual environments)
- [ ] Codechunks not correctly displayed (No ```) (R Coding Style Guidelines)
- [ ] \ formulas do not display correctly (XGboost)
- [ ] {{< katex }} does not display correctly (Calculate Sample Sizes for web scrapers)
- [ ] PDF-file download button does not render (Bookdown Thesis Template)
- [ ] code chunk without content (Run RStudio on AWS docker)
- [ ] Buttons (Twitter, FB etc) are spread out, when there is no date (Download Data Programmatically)
- [ ] Use 'X' button instead of Twitter?
- [ ] BASH no correctly specified in chunk (Debugging Makefiles with Remake)
- [ ] Image does not load (prob mis specified path) (About TSH)
- [ ] Email does not display properly & multiple "parts" of text (About TSH)
- [ ] Contibutors are displayed multiple times (Meet our contributors)
- [ ] Presentation slides are not available (Blog - Introducing TSH at the Open to Complexity Symposium)
- [ ] Blog posts are displayed 3 times
- [ ] Link to emperical research projects (Homepage - bottom) does not work
- [ ] None of the tutorials are accessible from the bottom of the homepage (darkblue)
- [ ] Building blocks from the bottom to the page link to the "Building Blocks" page instead of to the individual BB themselves
- [ ] Link (How to install LateX) does not work (set up LaTeX)
- [ ] Tutorials seem to fall of screen (when opening tutorials from header)
- [ ] Related posts have the sampe post multiple times (e.g., Exclude files from versioning)

 
## Issues related to content
- [ ] The way people use katex is inconsistent which gives problems during rendering. Some people forget to add the $ sign in front and at the end of a variable, which was not really an issue for some reason in Hugo, but in Flask this makes applying these Katex Formulas why harder. We should fix the katex boxes in content and make sure it is used correctly in all content.
- [ ] Tables currently to complex to parse to html by hardcoding. The most effective way would be to convert them all to html with ChatGPT (tried it, is very easy and quickly done) and add context to the styleguide on how people can add a html table (very easy and logical). Another option would to self design a new structure for a table. We should discuss this with Hannes.
- [] Some articles have lists without an enter (break) in front of it. The markdown package then cannot convert them to html lists.
- [ ] In Task Scheduling BB: someone wrote the following:

```
# e.g., * * * * * /usr/bin/python3 /script.py
<CRON CODE> <PATH OF YOUR PYTHON INSTALLATION> <PATH TO PYTHON FILE>
```

and also in a codeblock. It would be more efficient to change this since html sees < > as tag elements, which it now tries to autocomplete, instead as interpreting it as a string. The autocomplete process is something outside of my control (happens by browser).
- [ ] All Codeblock languages should be shown as follows ```Stata, so in the same line straight after the three signs, without any other signs such as - or others.
