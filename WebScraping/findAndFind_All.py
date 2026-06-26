from bs4 import BeautifulSoup
import requests
url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
# print(soup)

find = soup.find('div')
findAll = soup.find('p', class_ = 'lead').text.strip()
print(findAll)

