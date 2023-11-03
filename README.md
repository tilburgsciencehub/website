# Tilburg Science Hub To Flask
This is the repository thats hosts the news flask application for Tilburg Science Hub

## Install Packages
- pip install Flask-SQLAlchemy
- pip install SQLAlchemy
- pip install beautifulsoup4
- pip install nltk
- pip install markdown
- pip install Flask-Assets

## Content To Database
To create the database with all necessary data, simply go to the root folder and run the following command:

python3 content_to_db.py

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
    
## Features/Issues to Update/Implement
- [ ] make slider on mobile only move when clicked/touched
- [ ] Most read tutorials - duplicates
- [ ] scaling of tilburg science hub image on landing page off
- [ ] bug w/ slider on mobile
- [ ] About page in footer
- [ ] add reading time estimate
- [ ] Recently updated/published settings
- [ ] Cookies
- [ ] In text links with {{% cta-primary-center .. %}} do not render
- [ ] Header does not display BB's when hovering over it
- [ ] urls on homepage dont work
- [ ] Edit page url doesn't work
- [ ] Table do not render (e.g. BB on Cloud computing/ webscraping vs API's)
- [ ] ODCM tutorial does not work (specific)
- [ ] formatting does not render in {{% blocks %}} (e.g. Learn R BB)
- [ ] {{% example }} block does not render (e.g. use Scrum in your team BB)
- [ ] under automate and execute your work there is a "new" category called error handling?
- [ ] Text out of line (e.g. BB on cars/ interactive Interactive shiny COVID-19)
- [ ] external youtube link does not render {{< youtube DK7TYR68kqc iframe-video-margins >}} (BB practicing pipeline automation > verify)
- [ ] 
