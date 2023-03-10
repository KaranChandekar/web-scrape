import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.topseos.com/rankings-of-best-seo-companies"

with open('telephone.csv', 'w', encoding='utf-8') as f:
    thewriter = writer(f)
    header = ['Company Name', 'Subtitle', 'Telephone', 'Review', 'Website Link']
    thewriter.writerow(header)

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        htmlContent = response.content

        soup = BeautifulSoup(htmlContent, 'html.parser')
        lists = soup.find_all('div', class_='statistic_row')

        for list in lists:
            companyName = list.find('a', class_='track-click $dma_class')
            if companyName:
                companyName = companyName.text.replace('\n', '')
            else:
                companyName = ''

            subtitle = list.find('span', class_='statistic_block_subtitle')
            if subtitle:
                subtitle = subtitle.text.replace('\n', '')
            else:
                subtitle = ''

            telephone = list.find('a', class_='statistic_block_link')
            if telephone:
                telephone = telephone.br.next_sibling.text.replace('\n', '')
            else:
                telephone = ''

            reviews = list.find('a', class_='statistic_block_info')
            if reviews:
                reviews = reviews.text.replace('\n', '')[:-7] + ' Reviews'
            else:
                reviews = ''

            website = list.find('a', class_='btn_action')
            if website:
                website = website.get('href')
            else:
                website = ''

            info = [companyName, subtitle, telephone, reviews, website]
            thewriter.writerow(info)
