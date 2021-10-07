# This script generates a search-index.json file used in our GitHub worflow
import re, os, json, pandas as pd

def list_files(filepath, filetype):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    return(paths)


def search_item(word, header):
    r = re.compile(word)
    content = list(filter(r.match, header))[0]
    content = content[len(word) + 2:]
    return content.strip('"').strip("'")

def structure_markdown(df, path):
    # Split markdown in header and body
    max_index = df[1:].index('---') + 1
    header = df[1:max_index]
    body_list = df[max_index + 1:]
    body = " ".join(body_list)

    # Define regular expression patterns
    code_block = re.compile("{{% codeblock %}}(.+?){{% /codeblock %}}")
    headers = re.compile("#{2,6}\s(.+)")

    # Separate code, headers, and content
    body_no_code = re.sub(code_block, "", body)
    body_no_headers = " ".join([word for word in body_list if not re.search(headers, word)])

    return {
        "objectID": path,
        "title": search_item("title", header),
        "draft": search_item("draft", header),
        "description": search_item("description", header),
        "keywords": search_item("keywords", header),
        "code": re.findall(code_block, body),
        "headers": [re.search(headers, word).group(1) for word in body_list if re.search(headers, word)],
        "content": re.sub(code_block, "", body_no_headers)
    }

def export_data(file_paths):
    json_data = []

    for path in file_paths:
        f = open(path, 'r')
        df = f.read().split('\n')
        try:
            json_data.append(structure_markdown(df, path))
        except:
            print("Skipped file:", path) # skipped files
    return json_data


# Generate list of all markdown files
file_paths = list_files(".", ".md")
json_data = export_data(file_paths)

# Filter out draft objects
json_data_without_draft = []

for item in json_data:
    if item['draft']=='true':
        print('Excluding draft file:', item['title'])
        continue
    json_data_without_draft.append(item)


with open('search-index.json', 'w') as outfile:
    json.dump(json_data_without_draft, outfile)
