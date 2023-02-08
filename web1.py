import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://upcity.com/seo"

with open('companyData1.csv', 'w', encoding='utf-8') as f:
            thewriter = writer(f)
            header = ['Company Name', 'Address', 'Rating', 'Recent Review', 'About', 'Website Link', 'Business Detail', 'Industries']
            thewriter.writerow(header)

            while url:
                # Make the request to the URL
                response = requests.get(url)

                # Check if the request was successful
                if response.status_code == 200:
                    htmlContent = response.content

                    soup = BeautifulSoup(htmlContent, 'html.parser')
                    lists = soup.find_all('div', class_='s1cv79vu')

                    

                    for list in lists:
                        companyName = list.find('h4', class_='business-name-tile')
                        if companyName:
                            companyName = companyName.text.replace('\n', '')
                        else:
                            companyName = ''

                        address = list.find('div', class_='address-tile')
                        if address:
                            address = address.text.replace('\n', '')
                        else:
                            address = ''

                        rating = list.find('span', class_='rating-text-tile')
                        if rating:
                            rating = rating.text.replace('\n', '')
                        else:
                            rating = ''

                        about = list.find('div', class_='s1y5ibwe')
                        if about:
                            about = about.text.replace('\n', '')
                        else:
                            about = ''

                        website = list.find('a', class_='s16kbbkb o1rs5my3 p1rbas2u b1otow1k')
                        if website:
                            website = website.get('href')
                        else:
                            website = ''

                        recentReview = list.find('div', class_='iee7gma')
                        if recentReview:
                            recentReview = recentReview.find('div', class_='inner').text.replace('\n', '')
                        else:
                            recentReview = ''

                        businessDetails = list.find('div', class_='s8lnatv')
                        if businessDetails:
                            businessDetails = businessDetails.text.replace('\n', '')
                        else:
                            businessDetails = ''

                        industries = list.find('div', class_='ifwv84l')
                        if industries:
                            industries = industries.text.replace('\n', '')
                        else:
                            industries = ''

                        info = [companyName, address, rating, recentReview, about, website, businessDetails, industries]
                        thewriter.writerow(info)


                # Find the link to the next page
                next_page_link = soup.find("a", class_="view-more-btn-link")
                if next_page_link:
                    url = 'https://upcity.com/seo' + next_page_link.get("href")
                else:
                    url = None
            else:
                print("Failed to retrieve page content")
                url = None