# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the required packages:
# pip install requests
# pip install bs4
# pip install html5lib

import requests 
from bs4 import BeautifulSoup
url = "https://www.webfx.com/"

# Step 1: Get the HTML of the website
request = requests.get(url)
htmlContent = request.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal

# Commanly used types of objects:
# 1. Tag  --> print(type(title))
# 2. NavigableString --> print(type(title.string))
# 3. BeautifulSoup --> print(type(soup))
# 4. Comment


# Get the title of the website
title = soup.title

# Get all the paragraphs from the website
paras = soup.find_all('p')
# print(paras)

# Get all the anchor tags from the website
anchors = soup.find_all('a')
# print(anchors)

# Get all the links from the website
all_links = set()
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://www.webfx.com/" + link.get('href')
        all_links.add(link)
        print(linkText)


# Get first element in the html
# print(soup.find('p'))

# Get class of the any html element
# print(soup.find('p')['class'])

## Find all the elements with same class name
# print(soup.find_all('p', class_='description'))

# Get the text from the elements/tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())


