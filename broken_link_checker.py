# # Libraries
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

    for link in uniqueExternalLinks[:200]:
        
        count = count + 1
        
        print("Checking external link #",count," out of ",length_uniqueExternalLinks,".")
        
        try:
        
            statusCode = requests.get(link, headers=user_agent).status_code
            
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
            
        except:
            
            brokenLinksDict['link'].append(link)
            brokenLinksDict['statusCode'].append(statusCode)
            brokenLinksList.append(link)

# Identify Unique Broken Links and Matches them to Original List of All External Links
def matchBrokenLinks(brokenLinksList,externalLinksListRaw):

    global EndDataFrame
    
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
    
def push_issue_git():
    
    #set dt_string with current date/time
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S") 

    #github issue title
    titleissue = 'Broken/Error Links on ' + dt_string

    #reset EndDataFrame index to itterate through
    df3 = EndDataFrame.reset_index()  # make sure indexes pair with number of rows
    
    #empty table for git issue
    table = ''
    if len(df3.index) > 0:
        #for each row in df3, add new row in git table
        for index, row in df3.iterrows():
            if '\n' in row['Anchor Text']:
                anchortext = row['Anchor Text'].replace("\n", '')
                tablebody = '|' + row['URL'] + '|' + row['Broken_Link_URL'] + '|' + anchortext + '|' + str(row['statusCode']) + '|' + '\n'
                table = table + tablebody

            else:
                tablebody = '|' + row['URL'] + '|' + row['Broken_Link_URL'] + '|' + row['Anchor Text'] + '|' + str(row['statusCode']) + '|' + '\n'
                table = table + tablebody

        #create content of issue
        tablecomp = tablehead + table
        issuebody = 'Today, a total of ' + str(len(df3.index)) + ' link errors have been found. The following links have been found containing errors:' + '\n' + tablecomp

        #defining data to push to git issue
        data = {"title": titleissue, "body": issuebody}

        #Post issue message using requests and json
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 201:
            print('Issue created successfully')
        else:
            print(f'Failed to create issue: {response.status_code} - {response.text}')

        
    else:
        print('No broken links found')
        pass

# # Execute Functions


getPagesFromSitemap(fullDomain)
getListUniquePages()
ExternalLinkList(listPages, fullDomain)
getUniqueExternalLinks(externalLinksListRaw)
identifyBrokenLinks(uniqueExternalLinks)
matchBrokenLinks(brokenLinksList,externalLinksListRaw)
push_issue_git()
