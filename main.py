# Python Webscraping Task (Ubuntu Security Notices)
from xml.dom.minidom import Attr
from bs4 import BeautifulSoup
import requests
import re

url = "https://ubuntu.com/security/notices"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify)
section = soup.find('section', attrs={'class': 'p-strip'})
row = section.find('div', attrs={'class':'row'})
col = row.find('div', attrs={'class':'col-9'})
SecurityNotice1 = col.find('article', attrs={'class':'notice'})
link = SecurityNotice1.h3.find('a', attrs={'href': re.compile('^/')})
notice_path = link.get('href')
url1 = "https://ubuntu.com"
notice_link = url1 + notice_path
noticePage = requests.get(notice_link)
soupPage = BeautifulSoup(noticePage.content, 'html5lib')
soupPageDiv = soupPage.find('div', attrs={'class': 'wrapper u-no-margin--top'})
innerWrapper = soupPageDiv.find('div', attrs={'class': 'inner-wrapper'})
releases = innerWrapper.section.div.div.ul.li
releaseVersion = releases.a.text
data = {}
data['Release Version'] = releaseVersion
packages = innerWrapper.section
packageDiv = packages.find_all('div')
packageDiv = packageDiv[2]
packageDivLi = packageDiv.ul.li
packageLink = packageDivLi.find('a', attrs={'href': re.compile('^/')})
packageLink = packageLink.get('href')
packageLink = url1 + packageLink
data['Package Link'] = packageLink
references = innerWrapper.section
referenceDiv = references.find_all('div')
referenceDiv = referenceDiv[5]
referenceParas = referenceDiv.find_all('p')
referencePara1 = referenceParas[1]
referencePara2 = referenceParas[2]
referenceLink1 = referencePara1.find('a', attrs={'href': re.compile('^/')})
referenceLink1 = referenceLink1.get('href')
referenceLink1 = url1 + referenceLink1
referenceLink2 = referencePara2.find('a', attrs={'href': re.compile('^/')})
referenceLink2 = referenceLink2.get('href')
referenceLink2 = url1 + referenceLink2
cve_ids = [referenceLink1, referenceLink2]
data['CVE_ID1'] = cve_ids[0]
data['CVE_ID2'] = cve_ids[1]
print(data)