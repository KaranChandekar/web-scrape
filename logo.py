import requests 
from bs4 import BeautifulSoup
from csv import writer

url = "https://digitalagencynetwork.com/agencies/usa/seo/"
request = requests.get(url)
htmlContent = request.content
print(htmlContent)


soup = BeautifulSoup(htmlContent, 'html.parser')
lists = soup.find_all('li', class_='columns small-12 medium-6')
print(lists)

# with open('companyData.csv', 'w', encoding='utf-8') as f:
#     thewriter = writer(f)
#     header = ['Company Name', 'Address', 'Rating', 'Recent Review', 'About', 'Website Link', 'Business Detail', 'Industries']
#     thewriter.writerow(header)
    
for list in lists:
    companyName = list.find('a', class_='h4 thb-post-title')
    if companyName:
        companyName = companyName.text.replace('\n', '')
    else:
        companyName = ''

    logo = list.find('div', class_='entity-header-wrapper')
    if logo:
        logo = logo.find('a', class_='company-logo').find('img')['src']
    else:
        logo = ''

    about = list.find('div', class_='s1y5ibwe')
    if about:
        about = about.text.replace('\n', '')
    else:
        about = ''

    website = list.find('a', class_='h4 thb-post-title')
    if website:
        website = website.get('href')
    else:
        website = ''

    info = [companyName, about, website, logo]
    # print(info)
        # thewriter.writerow(info)

