import sqlite3
import os
import re
import shutil
import logging
from PIL import Image, UnidentifiedImageError

# Create the database and table
conn = sqlite3.connect('tsh.db')
cursor = conn.cursor()

# Create the topics table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY,
        title TEXT,
        level INTEGER,
        parent INTEGER,
        path TEXT,
        draft TEXT
    )
''')

# Create the articles table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        parent INTEGER,
        description TEXT,
        path TEXT,
        keywords TEXT,
        date TEXT,
        date_modified TEXT,
        draft TEXT,
        weight INTEGER,
        author TEXT,
        content TEXT
    )
''')

# Create the contributors table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contributors (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description_short TEXT,
        description_long TEXT,
        skills TEXT,
        linkedin TEXT,
        facebook TEXT,
        twitter TEXT,
        email TEXT,
        image TEXT,
        status TEXT,
        path TEXT,
        content TEXT
    )
''')

# Create the blogs table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS blogs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        path TEXT,
        date TEXT,
        date_modified TEXT,
        draft TEXT,
        content TEXT
    )
''')

# Commit the creation of tables
conn.commit()

# Define the content directory
script_directory = os.path.dirname(os.path.realpath(__file__))
content_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "content")
topic_folder = os.path.join(content_directory, 'topics')

# Insert or update a topic in the database
# Parameters:
# - cursor: SQLite cursor object
# - title (str): The title of the topic
# - level (int): The level of the topic in the hierarchy
# - parent (int): The parent ID of the topic
# - path (str): The path of the topic
# - draft (str): The draft status of the topic
# Returns:
# - int: The ID of the inserted or updated topic
def insert_topic_into_db(cursor, title, level, parent, path, draft):
    try:
        cursor.execute("SELECT 1 FROM topics WHERE path = ?", (path,))
        exists = cursor.fetchone()

        if exists:
            cursor.execute("UPDATE topics SET title = ?, level = ?, parent = ?, draft = ? WHERE path = ?", 
                           (title, level, parent, draft, path))
        else:
            cursor.execute("INSERT INTO topics (title, level, parent, path, draft) VALUES (?, ?, ?, ?, ?)", 
                           (title, level, parent, path, draft))
            
        conn.commit()

        cursor.execute("SELECT id FROM topics WHERE path = ?", (path,))
        topic_id = cursor.fetchone()[0]

        logging.info(f"Inserted/Updated topic, ID: {topic_id}")
    except Exception as e:
        logging.error(f"Database error: {e}")
        raise

    return topic_id

# Insert or update an article in the database
# Parameters:
# - cursor: SQLite cursor object
# - type (str): The type of the article
# - title (str): The title of the article
# - parent (int): The parent ID of the article
# - description (str): The description of the article
# - path (str): The path of the article
# - keywords (str): The keywords associated with the article
# - date (str): The publication date of the article
# - date_modified (str): The modification date of the article
# - draft (str): The draft status of the article
# - weight (int): The weight of the article for ordering
# - author (str): The author of the article
# - content (str): The content of the article
# Returns:
# - None -> Insert/update article into db
def insert_article_into_db(cursor, type, title, parent, description, path, keywords, date, date_modified, draft, weight, author, content):
    cursor.execute("SELECT 1 FROM articles WHERE path = ?", (path,))
    exists = cursor.fetchone()
    
    if exists:
        cursor.execute("""
            UPDATE articles 
            SET type = ?, title = ?, parent = ?, description = ?, keywords = ?, date = ?, 
                date_modified = ?, draft = ?, weight = ?, author = ?, content = ? 
            WHERE path = ?
            """, (type, title, parent, description, keywords, date, date_modified, draft, weight, author, content, path))
        print("Artikel bijgewerkt.")
    else:
        cursor.execute("""
            INSERT INTO articles (type, title, parent, description, path, keywords, date, date_modified, draft, weight, author, content) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (type, title, parent, description, path, keywords, date, date_modified, draft, weight, author, content))

# Insert or update a contributor in the database
# Parameters:
# - cursor: SQLite cursor object
# - name (str): The name of the contributor
# - description_short (str): Short description of the contributor
# - description_long (str): Long description of the contributor
# - skills (str): Skills of the contributor
# - linkedin (str): LinkedIn profile URL of the contributor
# - facebook (str): Facebook profile URL of the contributor
# - twitter (str): Twitter profile URL of the contributor
# - email (str): Email of the contributor
# - image (str): Image URL of the contributor
# - status (str): Status of the contributor
# - path (str): Path of the contributor
# - content (str): Content of the contributor
# Returns:
# - None -> Insert/update contributor in db
def insert_or_update_contributor(cursor, name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content):
    name = name if name else None
    description_short = description_short if description_short else None
    description_long = description_long if description_long else None
    skills = skills if skills else None
    linkedin = linkedin if linkedin else None
    facebook = facebook if facebook else None
    twitter = twitter if twitter else None
    email = email if email else None
    image = image if image else None
    status = status if status else None
    path = path if path else None
    content = content if content else None

    cursor.execute("SELECT 1 FROM contributors WHERE path = ?", (path,))
    exists = cursor.fetchone()
    
    if exists:
        cursor.execute('''
            UPDATE contributors SET name = ?, description_short = ?, description_long = ?, skills = ?, linkedin = ?, facebook = ?, twitter = ?, email = ?, image = ?, status = ?, content = ?
            WHERE path = ?
        ''', (name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, content, path))
    else:
        cursor.execute('''
            INSERT INTO contributors (name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content))

# Insert or update a blog in the database
# Parameters:
# - cursor: SQLite cursor object
# - title (str): The title of the blog
# - description (str): The description of the blog
# - path (str): The path of the blog
# - date (str): The publication date of the blog
# - date_modified (str): The modification date of the blog
# - draft (str): The draft status of the blog
# - content (str): The content of the blog
# Returns:
# - None -> Insert/update blog into db
def insert_or_update_blog(cursor, title, description, path, date, date_modified, draft, content):
    title = title if title else None
    description = description if description else None
    path = path if path else None
    date = date if date else None
    date_modified = date_modified if date_modified else None
    draft = draft if draft else None
    content = content if content else None

    cursor.execute("SELECT 1 FROM blogs WHERE path = ?", (path,))
    exists = cursor.fetchone()
    
    if exists:
        cursor.execute('''
            UPDATE blogs SET title = ?, description = ?, date = ?, date_modified = ?, draft = ?, content = ?
            WHERE path = ?
        ''', (title, description, date, date_modified, draft, content, path))
    else:
        cursor.execute('''
            INSERT INTO blogs (title, description, path, date, date_modified, draft, content)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, description, path, date, date_modified, draft, content))

# Parse a Markdown file to extract metadata
# Parameters:
# - file_path (str): The path to the Markdown file
# Returns:
# - tuple: A tuple containing the title, description, and draft status
def parse_md_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        title = re.search(r'title: "(.*?)"', content)
        description = re.search(r'description: "(.*?)"', content)
        draft = re.search(r'draft: (.*?)\n', content)

        # Extract values, return None if not found
        title_value = title.group(1) if title else None
        description_value = description.group(1) if description else None
        draft_value = draft.group(1) if draft else None

        return title_value, description_value, draft_value

# Process an article from a Markdown file and insert it into the database
# Parameters:
# - md_file_path (str): The path to the Markdown file
# - parent_id (int): The parent ID of the article
# Returns:
# - None -> Insert article into db
def process_article(md_file_path, parent_id):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        content = md_file.read()
        title = re.search(r'title: "(.*?)"', content)
        description = re.search(r'description: "(.*?)"', content)
        draft = re.search(r'draft: (.*?)\n', content)
        keywords = re.search(r'keywords: "(.*?)"', content)
        date = re.search(r'date: (\d{4}-\d{2}-\d{2})', content)
        date_modified = re.search(r'date_modified: (\d{4}-\d{2}-\d{2})', content)
        weight = re.search(r'weight: (\d+)', content)
        author = re.search(r'author: "(.*?)"', content)

        # Extract article content
        match = re.search(r'---(.*?)---(.*)', content, re.DOTALL)
        if match:
            file_content = match.group(2).strip()
        else:
            file_content = None

        # Insert data into articles table
        insert_article_into_db(cursor, 'topic', title.group(1) if title else None, parent_id,
                               description.group(1) if description else None, os.path.basename(md_file_path).replace('.md', ''),
                               keywords.group(1) if keywords else None, date.group(1) if date else None,
                               date_modified.group(1) if date_modified else None, draft.group(1) if draft else None,
                               int(weight.group(1)) if weight else None, author.group(1) if author else None, file_content)

import sqlite3
import os
import re
import shutil
import logging

# Loop through topics and fill the database
# Parameters:
# - root_path (str): The root directory path to start the traversal
# Returns:
# - None
def fill_database(root_path):
    exclude = {'img', 'images', 'data'}
    path_to_id = {}

    for path, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in exclude]
        level = path.count(os.sep) - root_path.count(os.sep)
        parent_path = os.path.dirname(path)
        parent_id = path_to_id.get(parent_path, None)
        folder_name = os.path.basename(path)

        index_file = os.path.join(path, '_index.md')
        if os.path.exists(index_file):
            title, description, draft = parse_md_file(index_file)
            folder_id = insert_topic_into_db(cursor, title, level, parent_id, folder_name, draft)
            path_to_id[path] = folder_id

            for file in os.listdir(path):
                if file != '_index.md' and file.endswith('.md'):
                    md_file_path = os.path.join(path, file)
                    process_article(md_file_path, folder_id)

# Check if the file is an image
# Parameters:
# - filename (str): The name of the file to check
# Returns:
# - bool: True if the file is an image, False otherwise
def is_image(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in image_extensions

# Check if the file is not an image or Markdown
# Parameters:
# - filename (str): The name of the file to check
# Returns:
# - bool: True if the file is not an image or Markdown, False otherwise
def is_not_image_or_md(filename):
    _, ext = os.path.splitext(filename)
    return not (ext.lower() in image_extensions or ext.lower() == '.md')

# Execute loop through topics and fill the database
fill_database(topic_folder)

# Fetch and process examples
examples_root_folder = os.path.join(content_directory, 'examples')
for md_file_name in os.listdir(examples_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(examples_root_folder, md_file_name)

        path = md_file_name.replace('.md', '').lower()

        # Initialize variables
        description = None
        title = None
        keywords = None
        date = None
        date_modified = None
        draft = None
        author = None
        content = None 

        # Read the contents of the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # YAML
            for line in md_file:
                if line.startswith('description:'):
                    description = line.strip().replace('description:', '', 1).replace('"','').strip()
                elif line.startswith('title:'):
                    title = line.strip().replace('title:', '', 1).replace('"','').strip()
                elif line.startswith('keywords:'):
                    keywords = line.strip().replace('keywords:', '', 1).replace('"','').strip()
                elif line.startswith('date:'):
                    date = line.strip().replace('date:', '', 1).strip()
                elif line.startswith('date_modified:'):
                    date_modified = line.strip().replace('date_modified:', '', 1).strip()
                elif line.startswith('draft:'):
                    draft = line.strip().replace('draft:', '', 1).strip()
                elif line.startswith('author:'):
                    author = line.strip().replace('author:', '', 1).replace('"','').strip()
                elif line.startswith('weight:'):
                    weight = line.strip().replace('weight:', '', 1).replace('"','').strip()
        
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # Fetch content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                file_content = match.group(2)
                content = file_content
            else:
                content = None

        # Insert data into the articles table
        insert_article_into_db(cursor, 'examples', title if title else None, None,
                               description if description else None, os.path.basename(md_file_path).replace('.md', ''),
                               keywords if keywords else None, date if date else None,
                               date_modified if date_modified else None, draft if draft else None,
                               int(weight) if weight else None, author if author else None, content if content else None)

# Fetch and process contributors
contributors_root_folder = os.path.join(content_directory, 'contributors')
for md_file_name in os.listdir(contributors_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(contributors_root_folder, md_file_name)

        # Initialize variables
        name = None
        description_short = None
        description_long = None
        skills_list = []
        skills = None
        skills_started = False
        linkedin = None
        facebook = None
        twitter = None
        email = None
        image = None
        status = None
        content = None
        path = None
        
        # Read the contents of the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # YAML
            for line in md_file:
                if line.startswith('name:'):
                    name = line.strip().replace('name:', '', 1).replace('"','').strip()
                    path = name.replace(' ','-').lower()
                elif line.startswith('description_short:'):
                    description_short = line.strip().replace('description_short:', '', 1).replace('"','').strip()
                elif line.startswith('description_long:'):
                    description_long = line.strip().replace('description_long:', '', 1).replace('"','').strip()
                elif 'linkedin' in line.strip().lower() and line.strip().startswith('link:'):
                    linkedin = line.strip().replace('link:', '', 1).strip()
                elif 'facebook' in line.strip().lower() and line.strip().startswith('link:'):
                    facebook = line.strip().replace('link:', '', 1).strip()
                elif 'twitter' in line.strip().lower() and line.strip().startswith('link:'):
                    twitter = line.strip().replace('link:', '', 1).strip()
                elif line.startswith('email:'):
                    email = line.strip().replace('email:', '', 1).replace('"','').strip()
                elif line.startswith('image:'):
                    image = line.strip().replace('image:', '', 1).replace('"','').strip()
                elif line.startswith('status:'):
                    status = line.strip().replace('status:', '', 1).replace('"','').strip()
                elif line.strip().startswith('skills:'):
                    skills_started = True
                elif skills_started and line.strip().startswith('-'):
                    skill = line.strip().lstrip('-').strip()
                    skills_list.append(skill)
                elif skills_started and not line.strip().startswith('-') and not line.strip().startswith('skills:'):
                    skills_started = False
                
        skills = ', '.join(skills_list)
        
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # Fetch content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                content = match.group(2)
            else:
                content = None

        # Insert or update contributor data in the contributors table
        insert_or_update_contributor(cursor, name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content)

# Fetch and process blogs
blog_root_folder = os.path.join(content_directory, 'blog')
for md_file_name in os.listdir(blog_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(blog_root_folder, md_file_name)

        path = md_file_name.replace('.md', '').lower()

        # Initialize variables
        description = None
        title = None
        date = None
        date_modified = None
        draft = None
        content = None 

        # Read the contents of the Markdown file
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # YAML
            for line in md_file:
                if line.startswith('description:'):
                    description = line.strip().replace('description:', '', 1).replace('"','').strip()
                elif line.startswith('title:'):
                    title = line.strip().replace('title:', '', 1).replace('"','').strip()
                elif line.startswith('date:'):
                    date = line.strip().replace('date:', '', 1).strip()
                elif line.startswith('date_modified:'):
                    date_modified = line.strip().replace('date_modified:', '', 1).strip()
                elif line.startswith('draft:'):
                    draft = line.strip().replace('draft:', '', 1).strip()
        
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            # Fetch content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                file_content = match.group(2)
                content = file_content
            else:
                content = None

        # Insert or update blog data in the blogs table
        insert_or_update_blog(cursor, title, description, path, date, date_modified, draft, content)

# Commit the changes to the database and close the connection
conn.commit()
conn.close()

# Define the image directory
img_directory = os.path.join(script_directory, "static/img")

# Define valid image extensions
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mov']

# Create image directory if it does not exist
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

# Loop through the content directory and convert/copy images to the image directory
for root, _, files in os.walk(content_directory):
    for filename in files:
        src_filepath = os.path.join(root, filename)
        
        if is_image(filename):
            try:
                # Define the destination filepath with .webp extension
                dst_filename = os.path.splitext(filename)[0] + '.webp'
                dst_filepath = os.path.join(img_directory, dst_filename)
                
                # Open and convert the image to webp
                with Image.open(src_filepath) as img:
                    img.save(dst_filepath, 'webp')

                print(f"Converted {src_filepath} to {dst_filepath}")

            except UnidentifiedImageError:
                print(f"UnidentifiedImageError: Cannot identify image file {src_filepath}")
            except Exception as e:
                print(f"Error processing {src_filepath}: {e}")

# Define the directory for other files
files_directory = os.path.join(script_directory, "static/files")

# Create files directory if it does not exist
if not os.path.exists(files_directory):
    os.makedirs(files_directory)

# Initialize a set to keep track of unique file extensions
unique_extensions = set()

# Loop through the content directory and copy non-image, non-Markdown files
for root, _, files in os.walk(content_directory):
    for filename in files:
        if is_not_image_or_md(filename):
            src_filepath = os.path.join(root, filename)
            dst_filepath = os.path.join(files_directory, filename)
            
            os.makedirs(os.path.dirname(dst_filepath), exist_ok=True)
            
            # Check if the destination file already exists
            if os.path.exists(dst_filepath):
                continue
            else:
                shutil.copy(src_filepath, dst_filepath)
                print(f"Bestand gekopieerd: {dst_filepath}")
                # Add the file extension to the set of unique extensions
                unique_extensions.add(os.path.splitext(filename)[1].lower())

# Convert the set of unique extensions to a list for output
unique_extensions_list = list(unique_extensions)
print(f"Unieke bestandsextensies van gekopieerde bestanden: {unique_extensions_list}")
