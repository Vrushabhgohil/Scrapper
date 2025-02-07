import re
from urllib.request import urlopen

url = "https://example.com/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# get_title = html.find('<p>')
start_index = html.find('<h1>') + len('<h1>')
end_index = html.find('</h1>')

print("Start Index: ", start_index)
print("End Index: ", end_index)

print("--------------------------------")

get_content = html[start_index:end_index]
print("Content: \n",get_content)


replace_answer = re.sub("Example.*" , "Of Domain",get_content)
print("Replace Content: ",replace_answer)