from lxml import html
import requests


url = "https://example.com"
response  = requests.get(url)
print(response)
tree = html.fromstring(response.content)
print(tree)
link_titles = tree.xpath('//a/text()')

for title in link_titles:
    print(title)