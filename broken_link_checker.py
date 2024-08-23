from usp.tree import sitemap_tree_for_homepage
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
from datetime import datetime
import os

# # Lists & Other Necessities

# Domain
fullDomain = 'https://tilburgsciencehub.com'

#Sitemap listpages
listPages_Raw = []
listPages = []

#Links on pages
externalLinksListRaw = []
uniqueExternalLinks = []

#broken link list
brokenLinksList = []
brokenLinksDict = {'link':[],'statusCode':[]}

#broken link location list
brokenLinkLocation = []

#set user agent
user_agent = {'User-agent': 'Mozilla/5.0'} 

#git token by git secret
token = os.environ['GIT_TOKEN']

#git headers authorization
headers = {"Authorization" : "token {}".format(token)}

#Generate target repositoryURL using Github API
username = 'tilburgsciencehub'
Repositoryname = 'website'
url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)

#github table setup
tablehead = "| URL | Broken Link | Anchor | Code |" + "\n" + "| ------------- | ------------- | ------------- | ------------- |" + "\n"

# # Functions

#Put all pages from sitemap in listPages_Raw
def getPagesFromSitemap(fullDomain):
    listPages_Raw.clear()
    tree = sitemap_tree_for_homepage(fullDomain)
    for page in tree.all_pages():
        listPages_Raw.append(page.url)

# Go through List Pages Raw output a list of unique pages links
def getListUniquePages():
    listPages.clear()
    
    for page in listPages_Raw:
        
        if page in listPages:
            
            pass

        else:
            
            listPages.append(page)

#get all links per page and insert url, dest. url & anchor text in externalLinksListRaw
def ExternalLinkList(listPages, fullDomain):
    
    externalLinksListRaw.clear()
    
    for url in listPages:
        request = requests.get(url, headers=user_agent)
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        list_of_links = soup.find_all("a")
        
        
        for link in list_of_links:

            try:
                
                if link["href"].startswith("#") or link["href"].startswith("mail"):

                    pass

                else:
                    
                    if link["href"] == '':
                        externalLinksListRaw.append([url,'Same destination as page',link.text])
                        
                    elif link["href"].startswith("/"):
                        
                        linkhrefadjust = link["href"][1:]
                        domain = fullDomain
                        urlcomp = domain + linkhrefadjust
                        externalLinksListRaw.append([url,urlcomp,link.text])
                    
                    elif link["href"].startswith("../"):
                        
                        if link["href"].startswith("../../"):
                            
                            if link["href"].startswith("../../../"):
                                subsetlinkhref = link["href"].replace("../", '')
                                lastpartdomain = url.rsplit('/')[-4] + '/' + url.rsplit('/')[-3] + '/' + url.rsplit('/')[-2] + '/'
                                subseturl = url.replace(lastpartdomain, '')
                                newlink = subseturl + subsetlinkhref
                                externalLinksListRaw.append([url,newlink,link.text])
                            
                            else:
                                subsetlinkhref = link["href"].replace("../", '')
                                lastpartdomain = url.rsplit('/')[-3] + '/' + url.rsplit('/')[-2] + '/'
                                subseturl = url.replace(lastpartdomain, '')
                                newlink = subseturl + subsetlinkhref
                                externalLinksListRaw.append([url,newlink,link.text])
                            
                        else:    
                            
                            subsetlinkhref = '/' + link["href"].replace("../", '')
                            lastpartdomain = '/' + url.rsplit('/')[-2] + '/'
                            subseturl = url.replace(lastpartdomain, '')
                            newlink = subseturl + subsetlinkhref
                            externalLinksListRaw.append([url,newlink,link.text])
                        
                    elif link["href"].startswith("./../"):
                
                        subsetlinkhref = link["href"].replace("./../", '')
                        lastpartdomain = url.rsplit('/')[-2] + '/'
                        subseturl = url.replace(lastpartdomain, '')
                        newlink = subseturl + subsetlinkhref
                        externalLinksListRaw.append([url,newlink,link.text])
                        
                    elif '.py' in link["href"] and 'http://' not in link["href"]:
                        
                        pass
                        
                    
                    else: 
                        
                        externalLinksListRaw.append([url,link["href"],link.text])
                    
            except:

                pass

# Go through externalLinksListRaw output and create a list(uniqueExternalLinks) of unique pages links
def getUniqueExternalLinks(externalLinksListRaw):

    uniqueExternalLinks.clear()
    
    for link in externalLinksListRaw:
        
        if link[1] in uniqueExternalLinks:
            
            pass

        else:
            
            uniqueExternalLinks.append(link[1])

#identify Broken Links
def identifyBrokenLinks(uniqueExternalLinks):
    
    brokenLinksList.clear()
    
    count = 0
    length_uniqueExternalLinks = len(uniqueExternalLinks)

    for link in uniqueExternalLinks:
        
        count = count + 1
        
        print("Checking external link #",count," out of ",length_uniqueExternalLinks,".")
        
        try:
            # Stel een time-out van 10 seconden in
            statusCode = requests.get(link, headers=user_agent, timeout=10).status_code
            
            if statusCode == 404:
                brokenLinksDict['link'].append(link)
                brokenLinksDict['statusCode'].append(statusCode)
                brokenLinksList.append(link)
                
            elif statusCode != 404 and statusCode > 399 and statusCode < 452:
                brokenLinksDict['link'].append(link)
                brokenLinksDict['statusCode'].append(statusCode)
                brokenLinksList.append(link)
            
            else:
                pass
            
        except requests.exceptions.Timeout:
            print(f"Skipping {link} due to timeout.")
        
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Identify Unique Broken Links and Matches them to Original List of All External Links
def matchBrokenLinks(brokenLinksList,externalLinksListRaw):
    
    brokenLinkLocation.clear()
    
    for link in externalLinksListRaw:
        
        if link[1] in brokenLinksList:
                    
            brokenLinkLocation.append([link[0],link[1],link[2]])
            
        else:
            
            pass

    dataframeFinal = pd.DataFrame(brokenLinkLocation,columns=["URL","Broken_Link_URL","Anchor Text"])
    dataframeFinal2 = pd.DataFrame(brokenLinksDict)
    EndDataFrame = dataframeFinal.merge(dataframeFinal2, left_on='Broken_Link_URL', right_on ='link', how='outer')
    del EndDataFrame['link']
    EndDataFrame = EndDataFrame[EndDataFrame['statusCode'] != 200]

    return EndDataFrame
    
def push_issue_git(EndDataFrame):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    titleissue = 'Broken/Error Links on ' + dt_string

    df_duplicates = EndDataFrame.reset_index()
    df = df_duplicates.drop_duplicates()

    table = ''
    if len(df.index) > 0:
        for index, row in df.iterrows():
            anchortext = row['Anchor Text'].replace("\n", '') if '\n' in row['Anchor Text'] else row['Anchor Text']
            tablebody = f"| {row['URL']} | {row['Broken_Link_URL']} | {anchortext} | {row['statusCode']} |\n"
            table = table + tablebody

        tablecomp = tablehead + table
        issuebody = f"Today, a total of {len(df.index)} link errors have been found. The following links have been found containing errors:\n{tablecomp}"

        data = {"title": titleissue, "body": issuebody}

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            if response.status_code == 201:
                print('Issue created successfully')
            else:
                print(f'Failed to create issue: {response.status_code} - {response.text}')
        except Exception as e:
            print(f'An error occurred: {str(e)}')

    else:
        print('No broken links found')


# # Execute Functions
getPagesFromSitemap(fullDomain)
getListUniquePages()
ExternalLinkList(listPages, fullDomain)
getUniqueExternalLinks(externalLinksListRaw)
identifyBrokenLinks(uniqueExternalLinks)
EndDataFrame = matchBrokenLinks(brokenLinksList,externalLinksListRaw)
push_issue_git(EndDataFrame)
