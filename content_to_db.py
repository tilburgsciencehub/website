import sqlite3
import os
import re
import shutil

# Create the database and table
conn = sqlite3.connect('tsh.db')
cursor = conn.cursor()

# Create the categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        type TEXT,
        title TEXT,
        weight INTEGER,
        parent INTEGER,
        description TEXT,
        path TEXT,
        draft TEXT,
        indexpage TEXT
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
               
# Create tables commit
conn.commit()

# Bepaal de huidige directory van het script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Voeg de map "content" toe aan het pad
content_directory = os.path.join(script_directory, "content")

# Fetch Tutorials and Building Blocks
for type in ['tutorials', 'building-blocks']:

    root_folder = os.path.join(content_directory, type)

    stack = [(root_folder, None, 0)]

    while stack:
        folder_path, parent_id, weight = stack.pop()
        
        for folder_name in os.listdir(folder_path):
            exclude_folders = ['images', 'img']
            if folder_name not in exclude_folders:
                folder_path_full = os.path.join(folder_path, folder_name)
                description = None
                title = None
                keywords = None
                date = None
                date_modified = None
                draft = None
                author = None
                content = None 
                indexpage = None

                if os.path.isdir(folder_path_full):
                    # Try to read the _index.md file
                    index_md_path = os.path.join(folder_path_full, '_index.md')
                    if os.path.exists(index_md_path):
                        with open(index_md_path, 'r', encoding='utf-8') as index_file:
                            for line in index_file:
                                # Check if the line starts with 'description:'
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
                                elif line.startswith('indexPage:'):
                                    indexpage = line.strip().replace('indexPage:', '', 1).replace('"','').strip()
                    path = folder_name
                    if (weight < 2):
                        cursor.execute('''
                            INSERT INTO categories (type, title, weight, parent, description, path, draft, indexpage)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (type, title, weight, parent_id, description, path, draft, indexpage))

                        if (weight == 1):

                            parent_id_article = cursor.lastrowid
                            
                            for md_file_name in os.listdir(folder_path_full):
                                if md_file_name != '_index.md' and md_file_name.endswith('.md'):
                                    # Construct the full path of the Markdown file
                                    md_file_path = os.path.join(folder_path_full, md_file_name)

                                    path = md_file_name.replace('.md', '').lower()

                                    #Init Vars
                                    description = None
                                    title = None
                                    keywords = None
                                    date = None
                                    date_modified = None
                                    draft = None
                                    article_weight = None
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
                                                article_weight = line.strip().replace('weight:', '', 1).strip()
                                    
                                    with open(md_file_path, 'r', encoding='utf-8') as md_file:
                                        
                                        # Fetch Content
                                        md_file_content = md_file.read()
                                        match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
                                        if match:
                                            file_content = match.group(2)
                                            content = file_content

                                    # Execute an SQL INSERT statement to add data to the 'articles' table
                                    cursor.execute('''
                                        INSERT INTO articles (type, title, parent, description, path, keywords, date, date_modified, draft, weight, author, content)
                                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                    ''', (type, title, parent_id_article, description, path, keywords, date, date_modified, draft, article_weight, author, content))

                    # Get the ID of the last inserted row
                    last_row_id = cursor.lastrowid

                    # Add subfolders to the stack
                    stack.append((folder_path_full, last_row_id, weight + 1))

# Fetch Examples
examples_root_folder = os.path.join(content_directory, 'examples')
for md_file_name in os.listdir(examples_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(examples_root_folder, md_file_name)

        path = md_file_name.replace('.md', '').lower()

        #Init Vars
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
        
        with open(md_file_path, 'r', encoding='utf-8') as md_file:
            
            # Fetch Content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                file_content = match.group(2)
                content = file_content

        # Execute an SQL INSERT statement to add data to the 'articles' table
        cursor.execute('''
            INSERT INTO articles (type, title, description, path, keywords, date, date_modified, draft, author, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', ('examples', title, description, path, keywords, date, date_modified, draft, author, content))

# Fetch Contributors
contributors_root_folder = os.path.join(content_directory, 'contributors')
for md_file_name in os.listdir(contributors_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(contributors_root_folder, md_file_name)

        #Init Vars
        name = None
        description_short = None
        description_long = None
        skills_list = []
        skills = None
        skills_started = False
        skills_ended = False
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
            
            # Fetch Content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                content = match.group(2)

        # Execute an SQL INSERT statement to add data to the 'articles' table
        cursor.execute('''
            INSERT INTO contributors (name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, description_short, description_long, skills, linkedin, facebook, twitter, email, image, status, path, content))

# Fetch Blogs
blog_root_folder = os.path.join(content_directory, 'blog')
for md_file_name in os.listdir(blog_root_folder):
    if md_file_name != '_index.md' and md_file_name.endswith('.md'):
        # Construct the full path of the Markdown file
        md_file_path = os.path.join(blog_root_folder, md_file_name)

        path = md_file_name.replace('.md', '').lower()

        #Init Vars
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
            
            # Fetch Content
            md_file_content = md_file.read()
            match = re.match(r'---(.*?)---(.*)', md_file_content, re.DOTALL)
            if match:
                file_content = match.group(2)
                content = file_content

        # Execute an SQL INSERT statement to add data to the 'articles' table
        cursor.execute('''
            INSERT INTO blogs (title, description, path, date, date_modified, draft, content)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, description, path, date, date_modified, draft, content))

# Submit to Database
conn.commit()
conn.close()

## Copy All images to img folder
img_directory = os.path.join(script_directory, "static/img")

## IMAGES AND VIDS
if not os.path.exists(img_directory):
    os.makedirs(img_directory)

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.mov']

def is_image(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in image_extensions

# Loop door de bestanden in de bronmap (content_directory) en submappen
for root, _, files in os.walk(content_directory):
    for filename in files:
        src_filepath = os.path.join(root, filename)
        
        # Controleer of het bestand een afbeelding is op basis van de extensie
        if is_image(filename):
            dst_filepath = os.path.join(img_directory, filename)
            
            # Kopieer het afbeeldingsbestand van de bronmap naar de doelmap en vervang indien nodig
            shutil.copy(src_filepath, dst_filepath)

print("Conversion Of Content Successful.")