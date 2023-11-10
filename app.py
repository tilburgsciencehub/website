from flask import Flask, render_template, request, redirect, url_for
from flask_assets import Environment, Bundle
from datetime import datetime
from functions import build_data_dict, generate_table_of_contents, get_breadcrumbs, find_related_articles
import os
from models import db, categories, articles, Contributors, blogs
from html_parser import htmlize

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
    'scss/bootstrap.scss',  # Change this to your main SCSS file
    output='css/main.css',   # Change this to your desired output CSS file
    filters='scss',
)

assets.register('scss_all', scss_bundle)

# Home Page


@app.route('/')
def home():
    data_dict = build_data_dict(categories, articles)

    return render_template('index.html', assets=assets, data_dict=data_dict)

# Single Building Block


@app.route('/building-blocks/<category_path>/<child_category_path>/<article_path>')
def building_block(category_path, child_category_path, article_path):
    data_dict = build_data_dict(categories, articles)
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    category = categories.query.filter_by(path=category_path).first()
    if category:
        child_category = categories.query.filter_by(
            path=child_category_path, parent=category.id).first()
        if child_category:
            article = articles.query.filter_by(
                path=article_path, parent=child_category.id).first()
            if article:
                top_related_articles = find_related_articles(article.keywords, articles, categories, article.id)
                buildingblock = article
                content = htmlize(article.content)
                table_of_contents = generate_table_of_contents(content)

    return render_template('building-block-single.html', assets=assets, breadcrumbs=breadcrumbs, buildingblock=buildingblock, current_url=current_url, data_dict=data_dict, table_of_contents=table_of_contents, content=content, top_related_articles=top_related_articles)

# Single Tutorial


@app.route('/tutorials/<category_path>/<child_category_path>/<article_path>')
def tutorial(category_path, child_category_path, article_path):
    data_dict = build_data_dict(categories, articles)
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    parts = current_url.split('/')
    current_tutorial_url = '/'.join(parts[:-1])
    article = None
    category = categories.query.filter_by(path=category_path).first()
    if category:
        child_category = categories.query.filter_by(
            path=child_category_path, parent=category.id).first()
        if child_category:
            articles_child_category = articles.query.filter_by(
                parent=child_category.id).order_by(articles.weight.asc()).all()
            article = articles.query.filter_by(
                path=article_path, parent=child_category.id).first()

            if article:
                tutorial = article
                content = htmlize(article.content)
                table_of_contents = generate_table_of_contents(content)

                if (article.weight != None):
                # Get the previous article
                    previous_article = articles.query \
                        .filter(articles.parent == child_category.id, articles.weight == (article.weight - 1)) \
                        .first()

                    # Get the next article
                    next_article = articles.query \
                        .filter(articles.parent == child_category.id, articles.weight == (article.weight + 1)) \
                        .first()
                else:
                    previous_article = None
                    next_article = None

    return render_template('tutorials-single.html', breadcrumbs=breadcrumbs, assets=assets, tutorial=tutorial, current_url=current_url, data_dict=data_dict, table_of_contents=table_of_contents, articles_child_category=articles_child_category, previous_article=previous_article, next_article=next_article, current_tutorial_url=current_tutorial_url, content=content)

# Single Example


@app.route('/examples/<article_path>')
def example(article_path):
    data_dict = build_data_dict(categories, articles)
    breadcrumbs = get_breadcrumbs()
    current_url = request.url
    article = None
    article = articles.query.filter_by(path=article_path).first()
    if article:
        example = article
        content = htmlize(example.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('examples-single.html', breadcrumbs=breadcrumbs, assets=assets, example=example, current_url=current_url, data_dict=data_dict, table_of_contents=table_of_contents, content=content)


# Single Blog
@app.route('/blog/<blog_path>')
def blogs_single(blog_path):
    data_dict = build_data_dict(categories, articles)
    breadcrumbs = get_breadcrumbs()
    blog_query = None
    blog_data = None
    blog_query = blogs.query.filter_by(path=blog_path).first()
    if blog_query:
        blog_data = blog_query
        content = htmlize(blog_query.content)
        table_of_contents = generate_table_of_contents(content)

    return render_template('blog-single.html', assets=assets, breadcrumbs=breadcrumbs, blog=blog_data, data_dict=data_dict, table_of_contents=table_of_contents, content=content)

# List Tutorials


@app.route('/tutorials')
def tutorials():
    data_dict = build_data_dict(categories, articles)
    return render_template('tutorials-list.html', assets=assets, data_dict=data_dict)

# List Examples


@app.route('/examples')
def examples():
    data_dict = build_data_dict(categories, articles)
    return render_template('examples-list.html', assets=assets, data_dict=data_dict)

# List Building Blocks


@app.route('/building-blocks')
def buildingblocks():
    data_dict = build_data_dict(categories, articles)
    return render_template('building-blocks-list.html', assets=assets, data_dict=data_dict)

# List Blogs


@app.route('/blog')
def blog():
    data_dict = build_data_dict(categories, articles)
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

    return render_template('blog-list.html', assets=assets, data_dict=data_dict, blogs_data=blogs_data)

# About


@app.route('/about')
def about():
    data_dict = build_data_dict(categories, articles)
    return render_template('about.html', assets=assets, data_dict=data_dict)

# Contribute


@app.route('/contribute')
def contribute():
    return redirect('/tutorials/more-tutorials/contribute-to-tilburg-science-hub/contribute')

# Contribute


@app.route('/search')
def search():
    data_dict = build_data_dict(categories, articles)
    return render_template('search.html', assets=assets, data_dict=data_dict)

# Contributors


@app.route('/contributors')
def contributors():
    data_dict = build_data_dict(categories, articles)
    contributors_list = Contributors.query.all()
    return render_template('contributors-list.html', assets=assets, data_dict=data_dict, contributors_list=contributors_list)

# Single Contributor


@app.route('/contributors/<contributor_path>')
def contributor(contributor_path):
    data_dict = build_data_dict(categories, articles)
    contributor_single = Contributors.query.filter_by(
        path=contributor_path).first()
    return render_template('contributors-single.html', assets=assets, data_dict=data_dict, contributor_single=contributor_single)


if __name__ == '__main__':
    app.run(debug=True)
