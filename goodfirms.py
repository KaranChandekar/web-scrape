import requests 
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.goodfirms.co/seo-agencies"
request = requests.get(url)
htmlContent = request.content

soup = BeautifulSoup(htmlContent, 'html.parser')
lists = soup.find_all('li', class_='service-provider')

# with open('companyData.csv', 'w', encoding='utf-8') as f:
#     thewriter = writer(f)
#     header = ['Company Name', 'Address', 'Rating', 'Recent Review', 'About', 'Website Link', 'Business Detail', 'Industries']
#     thewriter.writerow(header)
    
for list in lists:
    companyName = list.find('a', class_='c_name_head')
    if companyName:
        companyName = companyName.find('span').text.replace('\n', '')
    else:
        companyName = ''

    logo = list.find('div', class_='entity-header-wrapper')
    if logo:
        logo = logo.find('a', class_='company-logo').find('img')['src']
    else:
        logo = ''

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

    info = [companyName, address, rating, recentReview, about, website, businessDetails, industries, logo]
    # info = [img]
    print(info)
        # thewriter.writerow(info)



# case 1: 