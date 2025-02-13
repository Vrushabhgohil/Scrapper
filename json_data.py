from bs4 import BeautifulSoup
import requests
import json

url = "https://www.screener.in/company/RELIANCE/consolidated/"  #place url from we want to fetch data
res = requests.get(url=url)
# res.status_code
soup = BeautifulSoup(res.content,'html.parser')

table = soup.find('table',{'class': 'data-table'}) #get table
title = table.find('td',{'class':"text"}) # title of the table
print(title.text.strip())
rows = table.find_all('th') #store headings of all the rows
header = [header.text.strip() for header in rows]
final_data = []
table_data=table.find_all('tr')[1:] #fetch all the tr without first one
for row in table_data:
    cols = row.find_all('td') #fetch all the table data
    row_data = {}
    for i,col in enumerate(cols):
        row_data[header[i]] = col.text.strip()
    final_data.append(row_data)
json_data = json.dumps(final_data, indent=4)
print(json_data)
