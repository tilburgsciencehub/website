import requests
from bs4 import BeautifulSoup
from usp.tree import sitemap_tree_for_homepage
import pandas as pd
from urllib.parse import urljoin
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from datetime import datetime
import os
import json

# Variables
fullDomain = os.environ('FULL_DOMAIN')
aws_access_key_id = os.environ('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ('AWS_SECRET_ACCESS_KEY')
aws_region = os.environ('AWS_REGION')
aws_bucket = os.environ('AWS_BUCKET')
username = os.environ('GIT_USERNAME')
repositoryname = os.environ('GIT_REPOSITORY')
token = os.environ['GIT_TOKEN']

# Settings for Git Issue
user_agent = {'User-agent': 'Mozilla/5.0'} 
headers = {"Authorization" : "token {}".format(token)}
url = "https://api.github.com/repos/{}/{}/issues".format(username,repositoryname)

# Functie om alle pagina's van de sitemap in een lijst te plaatsen
def getUniquePagesFromSitemap(fullDomain):
    listPages_Raw = []
    listPages = []
    
    # Haal alle pagina's op uit de sitemap
    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPages_Raw.append(page.url)
    
    # Voeg unieke pagina's toe aan de lijst
    for page in listPages_Raw:
        if page not in listPages:
            listPages.append(page)
    
    return listPages

# Functie om gebroken afbeeldingen te controleren
def checkBrokenImages(url):
    broken_images = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        img_url = img.get('src')
        if img_url:
            # Zorg ervoor dat de URL volledig is
            img_url = urljoin(url, img_url)
            img_response = requests.head(img_url)
            if img_response.status_code != 200:
                broken_images.append(img_url)
    return broken_images

# Functie om te lange titels te controleren
def checkTooLongTitles(listPages, max_length=60):
    too_long_titles = []
    for url in listPages:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text.strip()
        if len(title) > max_length:
            too_long_titles.append(url)
    return too_long_titles

# Functie om lege meta descriptions te controleren
def checkEmptyMetaDescriptions(listPages):
    empty_meta_descriptions = []
    for url in listPages:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if not meta_desc or not meta_desc.get('content').strip():
            empty_meta_descriptions.append(url)
    return empty_meta_descriptions

# Functie om te lange meta descriptions te controleren
def checkTooLongMetaDescriptions(listPages, max_length=160):
    too_long_meta_descriptions = []
    for url in listPages:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and len(meta_desc.get('content').strip()) > max_length:
            too_long_meta_descriptions.append(url)
    return too_long_meta_descriptions

# Functie om lege alt-teksten te controleren
def checkEmptyAltText(url):
    empty_alt_texts = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt') or not img.get('alt').strip():
            empty_alt_texts.append(img.get('src'))
    return empty_alt_texts

# Functie om titels en meta descriptions te verzamelen
def collectTitlesAndMetaDescriptions(listPages):
    title_meta_data = []
    for url in listPages:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').text.strip() if soup.find('title') else ''
        meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
        meta_desc = meta_desc_tag['content'].strip() if meta_desc_tag and meta_desc_tag.get('content') else ''
        
        title_meta_data.append({
            'URL': url,
            'Title': title,
            'Meta Description': meta_desc
        })
    
    return pd.DataFrame(title_meta_data)

# Functie om dubbele titels en meta descriptions te controleren
def checkDuplicateTitlesAndMetaDescriptions(df):
    duplicates = []

    # Check for duplicate titles
    title_duplicates = df[df.duplicated(['Title'], keep=False) & df['Title'].str.strip().ne('')]
    grouped_titles = title_duplicates.groupby('Title')
    for title, group in grouped_titles:
        urls = group['URL'].tolist()
        for url in urls:
            duplicates.append({'URL': url, 'Duplicate Type': 'Title', 'Matching URLs': ', '.join([u for u in urls if u != url])})

    # Check for duplicate meta descriptions
    meta_desc_duplicates = df[df.duplicated(['Meta Description'], keep=False) & df['Meta Description'].str.strip().ne('')]
    grouped_meta_desc = meta_desc_duplicates.groupby('Meta Description')
    for meta_desc, group in grouped_meta_desc:
        urls = group['URL'].tolist()
        for url in urls:
            duplicates.append({'URL': url, 'Duplicate Type': 'Meta Description', 'Matching URLs': ', '.join([u for u in urls if u != url])})

    # Check for both duplicate title and meta description
    both_duplicates = df[df.duplicated(['Title', 'Meta Description'], keep=False) & df['Title'].str.strip().ne('') & df['Meta Description'].str.strip().ne('')]
    grouped_both = both_duplicates.groupby(['Title', 'Meta Description'])
    for (title, meta_desc), group in grouped_both:
        urls = group['URL'].tolist()
        for url in urls:
            duplicates.append({'URL': url, 'Duplicate Type': 'Both', 'Matching URLs': ', '.join([u for u in urls if u != url])})

    return pd.DataFrame(duplicates).drop_duplicates()

def upload_file_to_s3(file_name, bucket, object_name=None, aws_access_key_id=None, aws_secret_access_key=None, aws_region=None):
    """
    Upload een bestand naar een S3-bucket.

    :param file_name: Bestandspad naar het te uploaden bestand.
    :param bucket: Naam van de S3-bucket.
    :param object_name: S3-objectnaam. Als niet opgegeven, wordt file_name gebruikt.
    :param aws_access_key_id: AWS access key ID. Als niet opgegeven, wordt uit omgeving gehaald.
    :param aws_secret_access_key: AWS secret access key. Als niet opgegeven, wordt uit omgeving gehaald.
    :param aws_region: AWS regio. Als niet opgegeven, wordt standaard regio gebruikt.
    :return: True als upload succesvol is, anders False.
    """
    # Gebruik standaard object_name als deze niet is opgegeven
    if object_name is None:
        object_name = file_name

    # Maak een S3-client aan
    try:
        if aws_access_key_id and aws_secret_access_key and aws_region:
            s3_client = boto3.client(
                's3',
                region_name=aws_region,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key
            )
        else:
            s3_client = boto3.client('s3')
    except NoCredentialsError:
        print("Credentials not available.")
        return False

    # Upload het bestand
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Bestand '{file_name}' succesvol geüpload naar '{bucket}/{object_name}'.")
        return True
    except FileNotFoundError:
        print(f"Bestand '{file_name}' niet gevonden.")
        return False
    except NoCredentialsError:
        print("Geen geldige AWS-credentials gevonden.")
        return False
    except ClientError as e:
        print(f"Fout bij het uploaden: {e}")
        return False

def push_issue_git(file_url):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    titleissue = 'Broken/Error Links on ' + dt_string
    issuebody = f"A new SEO Report has been created. It can be found over here: {file_url} "
    data = {"title": titleissue, "body": issuebody}

    try:
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 201:
            print('Issue created successfully')
        else:
            print(f'Failed to create issue: {response.status_code} - {response.text}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')


# Controleer alle URLs en verzamel de resultaten
def analyzeWebsite(fullDomain, aws_bucket=None, aws_access_key_id=None, aws_secret_access_key=None, aws_region=None):
    urls = getUniquePagesFromSitemap(fullDomain)
    
    results = []
    
    x = 0
    print('-----------------')
    print('Start SEO Checks')
    for url in urls[:50]:
        x += 1
        print('-----------------')
        print('Url ' + str(x))
        broken_images = checkBrokenImages(url)
        print('Images done')
        empty_alt_texts = checkEmptyAltText(url)
        empty_meta_desc = checkEmptyMetaDescriptions([url])
        print('Alt and meta done')
        too_long_titles = checkTooLongTitles([url])
        too_long_meta_desc = checkTooLongMetaDescriptions([url])
        print('Size checks done')
        
        results.append({
            'URL': url,
            'Broken Images': len(broken_images),
            'Empty Alt Texts': len(empty_alt_texts),
            'Empty Meta Descriptions': len(empty_meta_desc),
            'Too Long Titles': len(too_long_titles),
            'Too Long Meta Descriptions': len(too_long_meta_desc),
        })
        print('-----------------')
    
    # Collect per Page results
    df = pd.DataFrame(results)

    # Collect titles and meta descriptions for duplicate check
    title_meta_df = collectTitlesAndMetaDescriptions(urls[:50])
    duplicate_df = checkDuplicateTitlesAndMetaDescriptions(title_meta_df)
    
    with pd.ExcelWriter('seo_report_combined.xlsx') as writer:
        df.to_excel(writer, sheet_name='SEO Report', index=False)
        duplicate_df.to_excel(writer, sheet_name='Duplicate Titles & Meta', index=False)

    date = datetime.now().strftime("%Y-%m-%d")
    filename = f'reports/seo-report-{date}.xlsx'

    upload_success = upload_file_to_s3('seo_report_combined.xlsx', aws_bucket, filename, aws_access_key_id, aws_secret_access_key, aws_region)
    
    if upload_success:
        s3_url = f"https://{aws_bucket}.s3.{aws_region}.amazonaws.com/{filename}"
        print(f"Excel-bestand succesvol geüpload naar S3. URL: {s3_url}")
    else:
        print("Fout bij het uploaden van Excel-bestand naar S3.")

    return df, duplicate_df

df, duplicate_df = analyzeWebsite(fullDomain, aws_bucket, aws_access_key_id, aws_secret_access_key, aws_region)