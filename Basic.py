from urllib.request import urlopen

url = "https://example.com/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# get_title = html.find('<p>')
start_index = html.find('<p>') + len('<p>')
end_index = html.find('</p>')

print("Start Index: ", start_index)
print("End Index: ", end_index)

print("--------------------------------")

get_content = html[start_index:end_index]
print("Content: \n",get_content)
