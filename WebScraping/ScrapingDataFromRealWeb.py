from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

headers = {'User-Agent': 'Mozilla/5.0'}
#ต้องใส่  header เพราะเว็ปนั้นต้องการป้องกันการใช้ bot เข้ามาในเว็ป
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
