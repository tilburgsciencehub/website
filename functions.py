from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func
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

    return data_dict

# Recursive loop to find full path
def get_full_topic_path(parent_topic_id, Topics):
    topic = Topics.query \
        .with_entities(Topics.id, Topics.title, Topics.path, Topics.parent) \
        .filter_by(id=parent_topic_id) \
        .first()

    if not topic:
        return None
    
    if not topic.parent:
        return {
            "title": topic.title,
            "path": topic.path
        }

    parent_topic = get_full_topic_path(topic.parent, Topics)
    if parent_topic:
        full_path = f"{parent_topic['path']}/{topic.path}"
        return {
            "title": topic.title, 
            "path": full_path
        }
    return {
        "title": topic.title,
        "path": topic.path
    }

def recently_published(articles, Topics):
    base_url = request.host_url.rstrip("/")
    recent_articles_query = articles.query \
        .with_entities(articles.title, articles.path, articles.parent) \
        .order_by(func.coalesce(articles.date_modified, articles.date).desc()) \
        .limit(4) \
        .all()

    recent_articles_dict = []

    for article in recent_articles_query:
        title = article.title
        article_path = article.path
        article_parent = article.parent

        parent_topic_path = get_full_topic_path(article_parent, Topics)

        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{article_path}"
            full_dict = {"title": title, "path": full_path}
            recent_articles_dict.append(full_dict)
        else:
            full_path = f"{base_url}/{article_path}"
            recent_articles_dict.append({"title": title, "path": full_path})

    return recent_articles_dict

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

# Function for breadcrumbs
def get_breadcrumbs():
    base_url = request.host_url.rstrip("/")  # Haalt het domein en schema dynamisch op en verwijdert de trailing slash
    current_url = request.url
    path = current_url.replace(base_url, "")
    url_parts = path.strip("/").split("/")  # Verwijder leading/trailing slashes voor correct splitsen
    breadcrumbs = [{"name": "Home", "url": base_url}]

    # Bouw de breadcrumb-items op basis van de delen van de URL
    for i in range(1, len(url_parts)):
        breadcrumb = {
            "name": url_parts[i].replace("-", " ").title(),
            "url": f"{base_url}/{'/'.join(url_parts[:i + 1])}/"  # Gebruik f-string voor duidelijkheid
        }
        breadcrumbs.append(breadcrumb)

    return breadcrumbs


# Generate related articles
def find_related_articles(article_path, articles, Topics):
    # Stap 1: Vind het huidige artikel
    current_article = articles.query.filter_by(path=article_path).first()

    if not current_article:
        return []  
    
    related_articles_query = articles.query \
        .filter(articles.parent == current_article.parent, articles.id != current_article.id) \
        .limit(3) \
        .all()

    base_url = request.host_url.rstrip("/")
    top_related_articles = []

    for article in related_articles_query:
        parent_topic_path = get_full_topic_path(article.parent, Topics)
        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{article.path}"
        else:
            full_path = f"{base_url}/{article.path}"

        top_related_articles.append({
            "title": article.title,
            "path": full_path,
            "keywords": article.keywords,
            "description": article.description
        })

    return top_related_articles

def fetch_meta_data(data_object):
    meta_data = {}

    # Controleer of data_object een dictionary is
    if isinstance(data_object, dict):
        # Gebruik de get methode voor dictionaries
        title = data_object.get('title')
        description = data_object.get('description')
        keywords = data_object.get('keywords')
    else:
        # Gebruik getattr voor objectattributen, met een standaardwaarde van None als het attribuut niet bestaat
        title = getattr(data_object, 'title', None)
        description = getattr(data_object, 'description', None)
        keywords = getattr(data_object, 'keywords', None)

    # Voeg de waarden toe aan meta_data als ze bestaan (niet None en niet leeg)
    if title:
        meta_data['title'] = title
    if description:
        meta_data['description'] = description
    if keywords:
        meta_data['keywords'] = keywords

    return meta_data
    
def fetch_contributions_for_the_single_contributor(Contributor, Articles, Topics):
    base_url = request.host_url.rstrip("/")
    contributions = Articles.query.filter_by(author=Contributor.name).with_entities(Articles.id, Articles.title, Articles.path, Articles.parent).all()
    contributions_with_full_path = []

    for contribution in contributions:
        parent_topic_path = get_full_topic_path(contribution.parent, Topics)
        if parent_topic_path:
            full_path = f"{base_url}/{parent_topic_path['path']}/{contribution.path}"
        else:
            full_path = f"{base_url}/{contribution.path}"
        
        contributions_with_full_path.append({
            "id": contribution.id,
            "title":contribution.title,
            "path": full_path
        })
    return contributions_with_full_path

    


