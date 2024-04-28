from flask import Flask, render_template, request, redirect, url_for, abort
from flask_assets import Environment, Bundle
from datetime import datetime
from functions import build_data_dict, fetch_contributions_for_the_single_contributor, generate_table_of_contents, get_breadcrumbs, find_related_articles, calculate_reading_time, fetch_meta_data, recently_published
import os
from models import db, articles, Contributors, blogs, Topics
from html_parser import htmlize
from sqlalchemy import func

# Initialize App
app = Flask(__name__, static_url_path='/static')

# DB
db_filename = 'tsh.db'  # Adjust the filename if needed
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), db_filename))
db_uri = f'sqlite:///{db_path}'  # Construct the URI

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['CACHE'] = False
app.config['ASSETS_DEBUG'] = True

# Initialize SQLAlchemy with the app
db.init_app(app)

# Assets
assets = Environment(app)

# Build & Register SCSS Bundle
scss_bundle = Bundle(
    'scss/bootstrap.scss',  
    output='css/main.css',
    filters='scss',
)

assets.register('scss_all', scss_bundle)

# custom filter for dates
@app.template_filter('formatdate')
def formatdate(value, format="%Y-%m-%d"):
    if value is None:
        return ""
    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
    return date.strftime(format)

# Home Page
@app.route('/')
def home():

    # Meta Data
    data_object = {'title' : 'Home'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    recent_articles = recently_published(articles, Topics)

    return render_template('index.html', assets=assets, data_dict=data_dict, meta_data=meta_data, recent_articles=recent_articles)

# Single Example
@app.route('/examples/<article_path>')
def example(article_path):
    data_dict = build_data_dict(Topics, articles)
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    article = articles.query.filter_by(path=article_path).first()
    meta_data = fetch_meta_data(article)
    if article:
        example = article
        content = htmlize(example.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('examples-single.html', breadcrumbs=breadcrumbs, assets=assets, example=example, current_url=current_url, data_dict=data_dict, table_of_contents=table_of_contents, content=content, meta_data=meta_data)

# Single Blog
@app.route('/blog/<blog_path>')
def blogs_single(blog_path):
    data_dict = build_data_dict(Topics, articles)
    breadcrumbs = get_breadcrumbs()
    blog_query = None
    blog_data = None
    blog_query = blogs.query.filter_by(path=blog_path).first()
    meta_data = fetch_meta_data(blog_query)
    if blog_query:
        blog_data = blog_query
        content = htmlize(blog_query.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('blog-single.html', assets=assets, breadcrumbs=breadcrumbs, blog=blog_data, data_dict=data_dict, table_of_contents=table_of_contents, content=content, meta_data=meta_data)

# Still needs metadata!
# List Topics
@app.route('/topics')
def topics_list():
    data_dict = build_data_dict(Topics, articles)
    return render_template('topics-list.html', assets=assets, data_dict=data_dict)

# Still needs metadata!
# First Level Topic
@app.route('/topics/<first_level_topic_path>/')
def topics_first_level(first_level_topic_path):
    data_dict = build_data_dict(Topics, articles)
    
    return render_template('first-level-topic.html', assets=assets, data_dict=data_dict, topic_path=first_level_topic_path)

# Still needs metadata!
# Second Level Topic
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/')
def topics_second_level(first_level_topic_path,second_level_topic_path):
    data_dict = build_data_dict(Topics, articles)
    
    return render_template('second-level-topic.html', assets=assets, data_dict=data_dict, topic_path=first_level_topic_path, sec_level_topic_path=second_level_topic_path)

# Still needs metadata!
# Third Level Topic
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/<third_level_topic_path>/')
def topics_third_level(first_level_topic_path,second_level_topic_path, third_level_topic_path):
    data_dict = build_data_dict(Topics, articles)
    
    return render_template('third-level-topic.html', assets=assets, data_dict=data_dict, topic_path=first_level_topic_path, sec_level_topic_path=second_level_topic_path, third_level_topic_path=third_level_topic_path)

# Single Article (Topic)
@app.route('/topics/<first_level_topic_path>/<second_level_topic_path>/<third_level_topic_path>/<article_path>/')
def topic_single(first_level_topic_path, second_level_topic_path, third_level_topic_path, article_path):
    data_dict = build_data_dict(Topics, articles)
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    article = articles.query.filter_by(path=article_path).first()
    meta_data = fetch_meta_data(article)
    related_articles = None
    if article:
        related_articles = find_related_articles(article_path, articles, Topics)
        content = htmlize(article.content)
        table_of_contents = generate_table_of_contents(content)
        if (len(content) > 0):
            reading_time = calculate_reading_time(article.content)

    return render_template('topic-single.html', breadcrumbs=breadcrumbs, assets=assets, article=article, current_url=current_url, data_dict=data_dict, table_of_contents=table_of_contents, content=content, reading_time=reading_time, meta_data=meta_data, related_articles=related_articles)

# List Examples
@app.route('/examples')
def examples():

    # Meta Data
    data_object = {'title' : 'Examples'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    print(data_dict)
    return render_template('examples-list.html', assets=assets, data_dict=data_dict, meta_data=meta_data)

# List Blogs
@app.route('/blog')
def blog():

    # Meta Data
    data_object = {'title' : 'Blog'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    blogs_data = blogs.query.all()

    # Lus door de lijst en formatteer de datum in elk item
    for blog in blogs_data:
        if blog.date:
            # Scheid de tijdzone-informatie
            date_parts = blog.date.split("+")
            date_without_timezone = date_parts[0]

            # Converteer naar een datumobject
            date_object = datetime.strptime(
                date_without_timezone, "%Y-%m-%dT%H:%M:%S")

            # Formateer de datum naar het gewenste formaat
            blog.formatted_date = date_object.strftime("%B %d, %Y")
        else:
            blog.formatted_date = None

    return render_template('blog-list.html', assets=assets, data_dict=data_dict, blogs_data=blogs_data, meta_data=meta_data)

# About
@app.route('/about')
def about():

    # Meta Data
    data_object = {'title' : 'About Us'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    return render_template('about.html', assets=assets, data_dict=data_dict, meta_data=meta_data)

# Contribute
@app.route('/contribute')
def contribute():

    # Meta Data
    data_object = {'title' : 'Contribute to TSH'}
    meta_data = fetch_meta_data(data_object)

    return redirect('topics/collaborate-share/project-management/engage-open-science/contribute-to-tilburg-science-hub/contribute/')

# Contribute
@app.route('/search')
def search():

    # Meta Data
    data_object = {'title' : 'Search'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    return render_template('search.html', assets=assets, data_dict=data_dict, meta_data=meta_data)

# Contributors
@app.route('/contributors')
def contributors():

    # Meta Data
    data_object = {'title' : 'Contributors'}
    meta_data = fetch_meta_data(data_object)

    data_dict = build_data_dict(Topics, articles)
    contributors_list = Contributors.query.all()
    return render_template('contributors-list.html', assets=assets, data_dict=data_dict, contributors_list=contributors_list, meta_data=meta_data)

# Still needs metadata!
# Single Contributor
@app.route('/contributors/<contributor_path>')
def contributor(contributor_path):
    data_dict = build_data_dict(Topics, articles)
    contributor_single = Contributors.query.filter_by(
        path=contributor_path).first()
    
    if contributor_single is None:
        abort(404)
    
    contributions = fetch_contributions_for_the_single_contributor(contributor_single, articles, Topics)

    return render_template('contributors-single.html', assets=assets, data_dict=data_dict, contributor_single=contributor_single, contributions=contributions)

# Still needs metadata!
# Error Handler 404
@app.errorhandler(404)
def page_not_found(e):
    data_dict = build_data_dict(Topics, articles)
    return render_template('404.html', assets=assets, data_dict=data_dict), 404

if __name__ == '__main__':
    app.run(debug=True)
