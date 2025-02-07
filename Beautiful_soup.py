from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://example.com"
url_open = urlopen(url)
data_url = url_open.read().decode('utf-8')

# print without beautifulsoup
# print(data_url)
print("----------------------")

# print with beautifulsoup
formated_data = BeautifulSoup(data_url,'html.parser')
# print(formated_data)
print(formated_data.title.string)