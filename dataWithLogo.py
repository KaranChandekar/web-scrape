import requests 
from bs4 import BeautifulSoup
from csv import writer
import os

url = "https://www.semrush.com/agencies/list/seo/"

if not os.path.exists('images'):
    os.makedirs('images')

with open('dataWithLogo.csv', 'w', encoding='utf-8') as f:
    thewriter = writer(f)
    header = ['Company Name', 'About', 'Logo']
    thewriter.writerow(header)

    while url:
        # Make the request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            htmlContent = response.content

            soup = BeautifulSoup(htmlContent, 'html.parser')
            lists = soup.find_all('article', class_='___SBoxSizing_8om4t_gg_ Iwvz1NUd')

            for list in lists:
                companyName = list.find('span', class_='___SText_is0jf_gg_ _size_400_is0jf_gg_ __fontWeight_is0jf_gg_')
                if companyName:
                    companyName = companyName.text.replace('\n', '')
                else:
                    companyName = ''

                about = list.find('p', class_='l3GSkPAx ___SText_is0jf_gg_ _size_200_is0jf_gg_')
                if about:
                    about = about.text.replace('\n', '')
                else:
                    about = ''
                
                logo = list.find('img', class_='_2ioAjkxV')
                if logo:
                    logo = logo['src']
                else:
                    logo = ''

                try:
                    if logo:
                        logo_filename = f"images/{companyName}.jpg"
                        logo_response = requests.get(logo)
                        with open(logo_filename, "wb") as logo_file:
                            logo_file.write(logo_response.content)
                except OSError as e:
                    print(f"Error occured while saving image for {companyName}: {e}")
                
                info = [companyName, about, logo_filename]
                thewriter.writerow(info)

        # Find the link to the next page
        next_page_link = soup.find("a", class_="___SNextPage_1sarh_gg_")
        if next_page_link:
            url = 'https://www.semrush.com' + next_page_link.get("href")
        else:
            url = None
            break
    else:
        print("Failed to retrieve page content")
        url = None
