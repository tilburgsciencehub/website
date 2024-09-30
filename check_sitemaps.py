import xml.etree.ElementTree as ET
from urllib.parse import urlparse

# Function to extract URL paths from a sitemap
def extract_url_paths(sitemap):
    tree = ET.parse(sitemap)
    root = tree.getroot()
    url_paths = set()

    # Iterate over all <url> tags and extract the <loc> contents (URLs)
    for url in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
        loc = url.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
        parsed_url = urlparse(loc)
         # Normalize the path: convert to lowercase and remove trailing slash if present
        normalized_path = parsed_url.path
        # if normalized_path != '/':  # Keep the root slash if it's just "/"
        #     normalized_path = normalized_path.rstrip('/')
        url_paths.add(normalized_path)

    return url_paths

# Load the two sitemaps
sitemap1_paths = extract_url_paths("sitemap1.xml")  # URLs from tilburgsciencehub.com
sitemap2_paths = extract_url_paths("sitemap2.xml")  # URLs from flask.tilburgsciencehub.com

# Find URLs that are in sitemap1 (first domain) but not in sitemap2 (second domain)
missing_in_sitemap2 = sitemap1_paths - sitemap2_paths

# Print differences
if missing_in_sitemap2:
    print("URLs in sitemap1 but not in sitemap2 (only paths after the domain):")
    for path in missing_in_sitemap2:
        print(path)
else:
    print("All URLs from sitemap1 are present in sitemap2.")
