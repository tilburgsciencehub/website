import logging
import os
import googleapiclient.discovery
import json
from google.oauth2 import service_account
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

VIEW_ID = "265450145"
MAX_PAGES = 10
SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]
SCRIPT_DIR = os.path.dirname(__file__)
SERVICE_ACCOUNT_FILE = "service_account.json"
JSON_FILE = os.path.join(SCRIPT_DIR, SERVICE_ACCOUNT_FILE)

credentials = service_account.Credentials.from_service_account_file(
    JSON_FILE, scopes=SCOPES
)

analytics = googleapiclient.discovery.build(
    serviceName="analyticsreporting", version="v4", credentials=credentials,
)


def get_report():
    body = {
        "reportRequests": [
            {
                "viewId": VIEW_ID,
                "dateRanges": [{"startDate": "14daysAgo", "endDate": "today"}],
                "metrics": [{"expression": "ga:users"}],
                "dimensions": [
                    {"name": "ga:pagePath"},
                    {"name": "ga:pageTitle"}
                ],
                "orderBys": [{"fieldName": "ga:users", "sortOrder": "DESCENDING"}],
            }
        ]
    }
    return analytics.reports().batchGet(body=body).execute()


def get_popular_pages(response):
    print("Fetching popular pages...")
    popular_pages = []
    reports = response.get("reports", [])
    if reports:
        report = reports[0]
        for row in report.get("data", {}).get("rows", []):
            if (row["dimensions"][0] != "/"):
                path = row["dimensions"][0]
                title = row["dimensions"][1].replace(
                    '- Tilburg Science Hub', '').strip()
                data = {"path": path, "title": title}
                popular_pages.append(data)
    filtered = [page for page in popular_pages]
    if len(filtered) > MAX_PAGES:
        filtered = filtered[:MAX_PAGES]
    return filtered

# Fetch Description
# page_path: url of the page to retrieve the description from


def fetch_og_description(page_path):
    # Fetch the webpage's HTML and extract the og:description using BeautifulSoup
    url = "https://tilburgsciencehub.com" + page_path
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        meta_tag = soup.find("meta", attrs={"property": "og:description"})
        if meta_tag:
            return meta_tag.get("content", "")
    return ""

# Collect Top 5 From BB or Tutorials
# response: result from get_report()
# path_prefix: "building_blocks" or "tutorials"


def fetch_cards_popular_pages(response, path_prefix):
    print(f"Fetching popular {path_prefix}...")
    popular_pages = []
    reports = response.get("reports", [])
    if reports:
        report = reports[0]
        for row in report.get("data", {}).get("rows", []):
            page_path = row["dimensions"][0]
            page_title = row["dimensions"][1]
            parts = page_title.split(" - ")
            if len(parts) > 1:
                page_title = parts[0]
            else:
                page_title = page_title
            page_description = fetch_og_description(page_path)
            # Eerst een lijst maken van alle page_titles in popular_pages
            existing_titles = [page['title'] for page in popular_pages]
            if page_path.startswith(path_prefix) and page_path != path_prefix and page_title != "(not set)" and page_title not in existing_titles and 'contribute-to-tilburg-science-hub' not in page_path:
                popular_pages.append(
                    {"path": page_path, "title": page_title, "description": page_description})
    filtered = popular_pages[:5]
    return filtered

# Retrieve Sitemap
# url: root url of the website


def get_sitemap(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            sitemap_content = response.content
            sitemap_root = ET.fromstring(sitemap_content)
            urls = [loc.text for loc in sitemap_root.findall(
                ".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
            return urls
        else:
            print(
                f"Failed to retrieve sitemap. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sitemap: {e}")
        return []

# type_page: Building Block or Tutorial
# category_slug: The Name of the Category


def get_tsh_sitemap_category(type_page, category_slug):
    sitemap_url = "https://tilburgsciencehub.com/sitemap.xml"
    urls = get_sitemap(sitemap_url)
    common_part = 'https://tilburgsciencehub.com/'+type_page+'/'+category_slug+'/'

    url_list = []
    for url in urls:
        if url.startswith(common_part):
            trimmed_url = url[len(common_part):]
            if trimmed_url.count('/') == 1:
                path = common_part + trimmed_url
                trimmed_url = trimmed_url.replace('/', '')
                trimmed_url = trimmed_url.replace('-', ' ')
                title = trimmed_url.title()
                data_dict = {"path": path, "title": title}
                url_list.append(data_dict)

    return url_list

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
    for dirpath, _, filenames in os.walk(os.path.join(root_folder, ('content/topics'))):
        for filename in filenames:
            if filename.endswith('.md'):
                # Append the full path of the .md file to the list
                md_files.append(os.path.join(dirpath, filename))

    for dirpath, _, filenames in os.walk(os.path.join(root_folder, ('content/topics'))):
        for filename in filenames:
            if filename.endswith('.md'):
                # Append the full path of the .md file to the list
                md_files.append(os.path.join(dirpath, filename))

    return md_files

# Get the Data for a Category
# md_files: the results from get_md_files()
# category_input: name of the category


def get_category_files(md_files, category_input):

    category_list = []

    for file in md_files:
        with open(file, 'r') as f:
            content = f.read()

        # Find the front matter section in the .md file
        front_matter_start = content.find('---')
        front_matter_end = content.find('---', front_matter_start + 3)

        # Extract the front matter content
        front_matter = content[front_matter_start + 3:front_matter_end].strip()

        # Split the front matter into lines
        front_matter_lines = front_matter.split('\n')

        # Initialize the category, title, description, and path variables
        category = None
        title = None
        description = None
        path = None
        indexpage = ""

        # Find the "category" and "indexPage" keys in the front matter and get their values
        for line in front_matter_lines:
            if 'category:' in line:
                category = line.split(':', 1)[1].strip().strip('"')
            elif 'indexPage:' in line:
                indexpage = line.split(':', 1)[1].strip().strip('"')

        # If the category is "reproducible", find the "title", "description", "icon", "aliases" keys
        if category == category_input:

            # Set Icon Empty
            icon = ""

            # Loop Through each Line
            for line in front_matter_lines:
                if 'title:' in line:
                    title = line.split(':', 1)[1].strip().strip('\"')
                elif 'description:' in line:
                    description = line.split(':', 1)[1].strip().strip('\"')
                elif 'icon:' in line:
                    icon = line.split(':', 1)[1].strip().strip('\"')
                elif 'aliases:' in line:
                    # Find the end of the aliases section
                    aliases_end = front_matter_lines.index(line) + 1

                    # Get the value of the last alias (if available) and remove the '- ' prefix
                    for i in range(aliases_end, len(front_matter_lines)):
                        if front_matter_lines[i].strip() != '':
                            path = front_matter_lines[i].strip().lstrip('- ')

            # Add the index page to the path if available and not empty
            if indexpage:
                path = f"{path}{indexpage}"

            # Put the file location, title, description, and path in Dict
            data_dict = {"title": title, "path": path,
                         "description": description, "icon": icon}
            category_list.append(data_dict)

    return category_list

# Create Populard Cards JSON
# input_categories: Names of the input categories separated by comma


def create_popular_cards_json(input_categories):

    # Split the input_categories string by comma to get individual category names
    category_names = input_categories.split(',')

    # Get all MD files
    md_files = get_md_files()

    # Create a dictionary to store the category variables
    category_vars = {}

    # Loop through input categories and create variables
    for category_name in category_names:
        category_var = get_category_files(md_files, category_name)
        category_vars[category_name] = category_var

    # Create the categories output dictionary
    categories_output = category_vars

    # Get Analytics, Populate popular tutorials and building blocks
    response = get_report()
    tutorials = fetch_cards_popular_pages(response, "/topics/")
    building_blocks = fetch_cards_popular_pages(response, "/topics/")

    # Create Dictionary
    data_dict = {
        "tutorials": tutorials,
        "building_blocks": building_blocks,
        "categories": categories_output
    }

    print('Created Dict')

    return data_dict


def main():

    logging.info('Python HTTP trigger function processed a request.')

    # Navigate to the root folder (one level up from the current notebook file)
    notebook_path = os.path.dirname(__file__)
    root_folder = os.path.join(notebook_path, 'static')
    os.chdir(root_folder)

    response = get_report()
    pages = get_popular_pages(response)

    with open('pages.json', 'w') as f:
        json.dump(pages, f)

    popular_cards = create_popular_cards_json('reproducible,learn')
    cards_file_path = os.path.join(root_folder, 'cards.json')

    # Write Popular Cards to the 'cards.json' file in the 'static' folder
    with open(cards_file_path, 'w') as f:
        json.dump(popular_cards, f)

    print('JSON created')


if __name__ == "__main__":
    main()
