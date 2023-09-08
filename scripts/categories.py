import os
import spacy
import json
import datetime

# Retrieve MD Files
def get_md_files():
    # Get the absolute path of the current notebook file
    notebook_path = os.path.abspath('')
    
    # Navigate to the root folder (one level up from the current notebook file)
    root_folder = os.path.abspath(os.path.join(notebook_path, '..'))
    os.chdir(root_folder)

    # Create a list to store the paths of .md files
    md_files = []

    # Iterate through all subdirectories and find .md files
    for dirpath, _, filenames in os.walk(os.path.join(root_folder, ('content/building-blocks'))):
        for filename in filenames:
            if filename.endswith('.md'):
                # Append the full path of the .md file to the list
                md_files.append(os.path.join(dirpath, filename))

    for dirpath, _, filenames in os.walk(os.path.join(root_folder, ('content/tutorials'))):
        for filename in filenames:
            if filename.endswith('.md'):
                # Append the full path of the .md file to the list
                md_files.append(os.path.join(dirpath, filename))

    return md_files

def get_title_files(md_files):

    title_list =[]

    for file in md_files:
        with open(file, 'r') as f:
            content = f.read()

        page_type = None

        if 'tutorials' in file:
            page_type = 'tutorial'
        elif 'building-blocks' in file:
            page_type = 'building-block'
        elif 'examples' in file:
            page_type = 'example'
        else:
            page_type = 'unknown'

        # Find the front matter section in the .md file
        front_matter_start = content.find('---')
        front_matter_end = content.find('---', front_matter_start + 3)

        # Extract the front matter content
        front_matter = content[front_matter_start + 3:front_matter_end].strip()

        # Split the front matter into lines
        front_matter_lines = front_matter.split('\n')

        data = {}

        # Find the "category" and "indexPage" keys in the front matter and get their values
        for line in front_matter_lines:
            if 'title:' in line and 'tutorialtitle' not in line and '_index.md' not in file:
                data['title'] = line.split(':', 1)[1].strip().strip('"')
                
            elif 'aliases:' in line:
                # Find the end of the aliases section
                aliases_end = front_matter_lines.index(line) + 1

                # Get the value of the last alias (if available) and remove the '- ' prefix
                for i in range(aliases_end, len(front_matter_lines)):
                    if front_matter_lines[i].strip() != '':
                        data['path'] = front_matter_lines[i].strip().lstrip('- ')

        if data:
            data['page_type'] = page_type
            title_list.append(data)

    return title_list

def get_related_items(titles, categories):
    # Load the spaCy model
    nlp = spacy.load('en_core_web_sm')

    # Dictionary to store categorized titles
    categorized_titles = {}

    # Process each title dictionary and categorize it
    for title_data in titles:
        title = title_data.get('title', '').lower()  # Get the title from the dictionary
        doc = nlp(title)
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in title:
                    if category not in categorized_titles:
                        categorized_titles[category] = []
                    categorized_titles[category].append(title_data)

    # Print the categorized titles (replace only the second for loop)
    for category, titles in categorized_titles.items():
        current_datetime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime('%Y-%m-%dT%H:%M:%S%z')
        
        # Initialize the Markdown content for the category
        category_md_content = f'---\ntitle: "{category}"\ndescription: "Leave empty for now"\nweight: 3\ndate: {current_datetime}\ndraft: false\naliases:\n  - /custom-categories/{category.lower().replace(" ", "-")}\nitems:\n'
        
        # Add titles and details to the category Markdown content
        for title_data in titles:
            title = title_data['title']
            path = title_data['path']
            page_type = title_data['page_type']
            category_md_content += f'  - title: "{title}"\n    path: "{path}"\n    type: "{page_type}"\n'
        
        category_md_content += f'---\n'

        # Create a Markdown file for the category and write the content
        category_md_filename = f'{category.replace(" ", "-").lower()}.md'
        main_path = 'content/custom-categories/' + category_md_filename
        with open(main_path, 'w') as md_file:
            md_file.write(category_md_content)
            print(f"Created '{category_md_filename}'")

files = get_md_files()
titles = get_title_files(files)

with open('scripts/categories.json', 'r') as json_file:
    categories = json.load(json_file)

get_related_items(titles, categories)