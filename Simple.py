from bs4 import BeautifulSoup
import requests

with open("Simple.html") as htmlFile:
    soup = BeautifulSoup(htmlFile, "lxml")

# print(soup.prettify)
title = soup.title
print(title)
all_h1 = soup.find_all('h1')
for i in all_h1:
    print(i.text)