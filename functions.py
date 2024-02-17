from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_, not_
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from flask import request
import math
from collections import defaultdict

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Get reading time estimate
def calculate_reading_time(content):
    
    if (content != None):
        words = content.split()

        # Calculate the reading time (in minutes) assuming 200 words per minute
        reading_time = len(words) / 200

        # Round up the reading time to the nearest whole minute
        reading_time = math.ceil(reading_time)

        return reading_time
    
    else:

        return 0

def urlize(text):
    # Remove leading and trailing whitespace
    text = text.strip()

    # Replace hyphens and underscores with spaces
    text = text.replace('-', ' ').replace('_', ' ')

    # Split the text into words
    words = text.split()

    # Capitalize the first letter of each word, excluding common stop words
    words = [word.capitalize() if word.lower(
    ) not in stop_words else word for word in words]

    # Join the words back together with hyphens
    text = ' '.join(words)

    text = text[0].capitalize() + text[1:]

    return text

def build_data_dict(topics, articles):
    data_dict = {}
    topics_data = topics.query.all()
    topic_dict = defaultdict(lambda: defaultdict(list))

    for topic in topics_data:
        topic_dict[topic.level][topic.parent].append(topic)

    def serialize_article(article):
        return {
            'id': article.id,
            'title': article.title,
            'path': article.path,
            'description': article.description,
            'reading_time': calculate_reading_time(article.content)
        }

    def build_structure(level, parent, articles):
        if level not in topic_dict:
            return []
        return [
            {
                'id': topic.id,
                'title': topic.title,
                'path': topic.path,
                'parent': topic.parent,
                'level': topic.level,
                'draft': topic.draft,
                'childtopics': build_structure(level + 1, topic.id, articles),
                'articles': [serialize_article(article) for article in articles.query.filter_by(parent=topic.id).all()]
            }
            for topic in topic_dict[level][parent]
        ]
    
    # Fetch articles for examples
    articles_examples = articles.query.filter_by(type='examples').all()
    for article in articles_examples:
        article.reading_time = calculate_reading_time(article.content)
    
    data_dict['topics'] = build_structure(1, 1, articles)
    data_dict['examples'] = articles_examples
    print(data_dict['topics'])

    return data_dict

# Generate table of contents

def generate_table_of_contents(content_html):
    # Parse de HTML-content met BeautifulSoup
    soup = BeautifulSoup(content_html, 'html.parser')

    # Zoek naar alle h2 en h3 elementen in de content
    headings = soup.find_all(['h2', 'h3'])

    # Bouw de inhoudsopgave op basis van de gevonden headings
    table_of_contents = []

    current_h2 = None
    for heading in headings:
        # Bepaal het niveau van de heading (h2 of h3)
        level = heading.name

        # Haal de tekst van de heading op
        text = heading.text.strip()

        # Genereer een anchor (id) op basis van de tekst van de heading
        anchor = text.lower().replace(' ', '-')

        if level == 'h2':
            current_h2 = {'text': text, 'anchor': anchor, 'subheadings': []}
            table_of_contents.append(current_h2)
        elif level == 'h3' and current_h2 is not None:
            current_h2['subheadings'].append({'text': text, 'anchor': anchor})

    return table_of_contents

# Functie om breadcrumbs op te halen


def get_breadcrumbs():
    base_url = "http://127.0.0.1:5000"
    current_url = request.url
    path = current_url.replace(base_url, "")
    url_parts = path.split("/")
    breadcrumbs = [{"name": "Home", "url": base_url}]

    # Bouw de breadcrumb-items op basis van de delen van de URL
    for i in range(1, len(url_parts)):
        breadcrumb = {
            "name": url_parts[i].replace("-", " ").title(),
            "url": base_url + "/".join(url_parts[:i + 1]) + "/"
        }
        breadcrumbs.append(breadcrumb)

    return breadcrumbs

# Generate related articles


def find_related_articles(keywords, articles, categories, id):
    keyword_list = keywords.split()

    # Find keywords in the 'keywords' or 'content' columns of the articles
    related_articles = articles.query.filter(
        or_(
            articles.keywords.ilike('%{}%'.format(keyword)) for keyword in keyword_list
        ),
        or_(
            articles.content.ilike('%{}%'.format(keyword)) for keyword in keyword_list
        ),
        not_(articles.id == id)
    ).all()

    # Order Based on Appearances
    related_articles.sort(key=lambda article: sum(keyword_list.count(
        keyword) for keyword in article.keywords.split() + article.content.split()), reverse=True)

    # Top 5
    top_related_articles = related_articles[:5]

    for top_article in top_related_articles:
        url = None
        if (top_article.type == 'building-blocks') or (top_article.type == 'tutorials'):
            child_category = categories.query.filter_by(id=top_article.parent).first()
            if child_category:
                category = categories.query.filter_by(id=child_category.parent).first()
                if category:
                    child_category_path = child_category.path
                    category_path = category.path
                    url = top_article.type + '/' + category_path + '/' + \
                        child_category_path + '/' + top_article.path

            # Add Url to Article
            top_article.url = url

    return top_related_articles

