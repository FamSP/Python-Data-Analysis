#C:\Users\HP-NPRU\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install beautifulsoup4
#C:\Users\HP-NPRU\AppData\Local\Python\pythoncore-3.14-64\python.exe -m pip install requests

from bs4 import BeautifulSoup
import requests
url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html' )

print(soup)