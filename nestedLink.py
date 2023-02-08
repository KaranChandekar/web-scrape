import requests
from bs4 import BeautifulSoup

url = "https://upcity.com/seo"
request = requests.get(url)
htmlContent = request.content

soup = BeautifulSoup(htmlContent, 'html.parser')
lists = soup.find_all('div', class_='s1cv79vu')

for list in lists:
    nestedLinkUrl = list.find('a', class_='t164o0ez wwnygx3 b1otow1k').get('href')
    nestedLink = 'https://upcity.com/' + nestedLinkUrl

    request1 = requests.get(nestedLink)
    nestedHtmlContent = request1.content

    soup1 = BeautifulSoup(htmlContent, 'html.parser')
    telephone = soup1.find('small', class_='class="x1qkz07z')

    print(telephone)

    