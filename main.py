# Python task of Web Scraping

# Import BeautifulSoup, requests & re modules
from bs4 import BeautifulSoup
import requests
import re

# Dictionary to store all the extracted data from the web page
AllData = {}

# Function to access a webpage
def AccessPage(url):
    r = requests.get(url)
    return r.content            # Return the content of the page

SecurityNoticesPageContent = AccessPage("https://ubuntu.com/security/notices")

# Function that uses BeautifulSoup to scrap and parse the webpage
def BeautifyDocument(pageContent):
    soup = BeautifulSoup(pageContent, 'html5lib')
    return soup

# Store the return value of BeautifyDocument() function
SecurityPageContent = BeautifyDocument(SecurityNoticesPageContent)

# Function to extract a list of all the Security Notices Articles
def ExtractSecurityNoticesArticles():
    # Extract the div tag that wraps the main content below Navigation bar
    MainContentWrapper = SecurityPageContent.find('div', attrs={'class': 'wrapper u-no-margin--top'})

    # Extract the inner wrapper which lies within MainContentWrapper
    InnerWrapper = MainContentWrapper.find('div', attrs={'class': 'inner-wrapper'})

    # Extract Latest Notices Section
    LatestNoticesSection = InnerWrapper.find_all('section')
    
    # Extract all Security Notices articles
    AllArticles = LatestNoticesSection[2].div.div
    AllArticles = AllArticles.find_all('article')
    return AllArticles

articles = ExtractSecurityNoticesArticles()

ubuntu = "https://ubuntu.com"

# Function to store article links and names in a dictionary
def AddArticlesToDict(articles):
    articlesDict = {}
    for article in articles:
        articleLink = article.h3
        articleLink = articleLink.find('a', attrs={'href': re.compile('^/')})
        articleName = articleLink.text
        link = articleLink.get('href')
        link = ubuntu + link
        articlesDict[articleName] = link
    return articlesDict

articlesDict = AddArticlesToDict(articles)

# Store the articles into the AllData dictionary
AllData['Articles'] = articlesDict

# Extract the first article's link
firstArticleLink = articlesDict['USN-5450-1: Subversion vulnerabilities ›']

# Make a request to the web page of the first article
firstArticlePage = requests.get(firstArticleLink).content

# Parse and scrap the article page using BeautifyDocument() function
firstArticlePageContent = BeautifyDocument(firstArticlePage)

# Function to extract the release versions from the first article page
def ExtractReleases():
    releases = firstArticlePageContent.find('div', attrs={'class': 'wrapper u-no-margin--top'})
    releases = releases.find('div', attrs={'class': 'inner-wrapper'})
    releases = releases.find('section', attrs={'class': 'p-strip--suru-topped'})
    releases = releases.div.div.ul
    releases = releases.find_all('li')
    return releases

releases = ExtractReleases()

# Function to add the release version name and link in to a dictionary
def AddReleaseVersionToDict(releases):
    releasesDict = {}
    for releaseVersion in releases:
        releaseLink = releaseVersion.find('a', attrs={'href': re.compile('^/')})
        link = releaseLink.get('href')
        link = ubuntu + link
        name = releaseLink.text
        releasesDict[name] = link
    return releasesDict

releasesDict = AddReleaseVersionToDict(releases)

# Store the release versions into the AllData dictionary
AllData['Release Versions'] = releasesDict

# Function to extract packages
def ExtractPackages():
    packages = firstArticlePageContent.find('div', attrs={'class': 'wrapper u-no-margin--top'})
    packages = packages.find('div', attrs={'class': 'inner-wrapper'})
    packages = packages.find('section', attrs={'class': 'p-strip--suru-topped'})
    packages = packages.find_all('div', attrs={'class': 'row'})
    packages = packages[1].div.ul
    packages = packages.find_all('li')
    return packages

packages = ExtractPackages()

# Function to store packages in a dictionary
def AddPackagesToDict(packages):
    packagesDict = {}
    if len(packages) > 1:
        for package in packages:
            name = package.text
            packageLink = package.find('a', Attrs={'href': re.compile('^/')})
            link = packageLink.get('href')
            link = ubuntu + link
            packagesDict[name] = link
    else:
        package = packages[0]
        name = package.text
        packageLink = package.find('a', attrs={'href': re.compile('^/')})
        link = packageLink.get('href')
        link = ubuntu + link
        packagesDict[name] = link
    return packagesDict

packagesDict = AddPackagesToDict(packages)

# Store the Packages into the AllData dictionary
AllData['Packages'] = packagesDict

# Function to Extract CVE IDs
def ExtractCVE():
    ids = firstArticlePageContent.find('div', attrs={'class': 'wrapper u-no-margin--top'})
    ids = ids.find('div', attrs={'class': 'inner-wrapper'})
    ids = ids.find('section', attrs={'class': 'p-strip--suru-topped'})
    ids = ids.find_all('div', attrs={'class': 'row'})
    ids = ids[2].div
    ids = ids.find_all('p')
    del ids[0]
    del ids[-1]
    return ids

ids = ExtractCVE()

# Function to add ids into dictionary
def AddIdToDict(ids):
    id_dict = {}
    for id in ids:
        id_link = id.find('a', attrs={'href': re.compile('^/')})
        name = id_link.text
        link = id_link.get('href')
        link = ubuntu + link
        id_dict[name] = link
        return id_dict

id_dict = AddIdToDict(ids)

# Store the CVE IDs into the AllData dictionary
AllData['CVE IDs'] = id_dict

print(AllData)