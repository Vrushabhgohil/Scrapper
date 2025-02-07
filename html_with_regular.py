from urllib.request import urlopen
import re

url = "https://example.com"
url_open = urlopen(url)

url_data=url_open.read().decode('UTF-8')
# print(url_data)

# get title using regular expression
regex = '<title>.*?</title>'
find_data = re.search(regex,url_data,re.IGNORECASE)

# Print with the html tags
print(find_data.group())
print("-------------------")

# print without html tags 
group_data = find_data.group()
remove_tags =  re.sub('<.*?>',"",group_data)
print("After Remove: ",remove_tags)