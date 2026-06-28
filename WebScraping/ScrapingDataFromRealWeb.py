from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

#ต้องใส่  header เพราะเว็ปนั้นต้องการป้องกันการใช้ bot เข้ามาในเว็ป
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')

#<table class="wikitable sortable jquery-tablesorter">
# table = soup.find_all('table')[0]

table = soup.find('table', class_='wikitable sortable')

# print(table)

#------------------Get Title------------------
world_table = table.find_all('th')
# print(world_table)

world_table_titles= [title.text.strip() for title in world_table]
# print(world_table_titles)


#------------------Pull Columns------------------
df = pd.DataFrame(columns =world_table_titles)


#------------------Pull Data------------------
columns_data = table.find_all('tr')
for row in columns_data[1:]:
    row_data = row.find_all('td')
    individual_row_data= [data.text.strip() for data in row_data]
    
    lenght =len(df)
    df.loc[lenght] = individual_row_data

print(df)

df.to_csv(r'C:/Users/tame_/OneDrive/Desktop/Data Analyst/Python/Python-Data-Analysis/WebScraping/Companies.csv', index= False)