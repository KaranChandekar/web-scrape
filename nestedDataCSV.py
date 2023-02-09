import requests 
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.semrush.com/agencies/list/seo/"

with open('nestedAboutData.csv', 'w', encoding='utf-8') as f:
    thewriter = writer(f)
    header = ['Company Name', 'Location', 'About']
    thewriter.writerow(header)

    while url:
        # Make the request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            htmlContent = response.content

            soup = BeautifulSoup(htmlContent, 'lxml')

            articles = soup.find_all('article', class_='___SBoxSizing_8om4t_gg_ Iwvz1NUd')
            for article in articles:
                parent_a_tag = article.find_parent('a')
                if parent_a_tag:
                    href = parent_a_tag['href']
                    individual_page_request = requests.get('https://www.semrush.com' + href)
                    individual_page_content = individual_page_request.content
                    individual_page_soup = BeautifulSoup(individual_page_content, 'lxml')

                    CompanyNameParentTag = individual_page_soup.find('a', class_='___SLink_1omwd_gg_ ___SLink_1k80k_gg_ ___SText_is0jf_gg_ _size_500_is0jf_gg_ __bold_is0jf_gg_')

                    CompanyName = CompanyNameParentTag.find('span', class_='___SText_1omwd_gg_').text

                    location = individual_page_soup.find('p', class_='___SText_is0jf_gg_ _size_300_is0jf_gg_ __noWrap_is0jf_gg_')
                    location = location.text if location else ""

                    aboutDiv = individual_page_soup.find('div', class_='_37KbW3oD')      
                    about = aboutDiv.text.strip() if aboutDiv else ""
                    
                    data = [CompanyName, location, about]
                    thewriter.writerow(data)

        # Find the link to the next page
        next_page_link = soup.find("a", class_="___SNextPage_1sarh_gg_")
        if next_page_link:
            url = 'https://www.semrush.com' + next_page_link.get("href")
        else:
            url = None
    else:
        print("Failed to retrieve page content")
        url = None        