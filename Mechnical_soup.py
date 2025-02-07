# import mechanicalsoup
# browser = mechanicalsoup.Browser()
# url = "http://olympus.realpython.org/login"
# page = browser.get(url)

# content = page.soup

# form = content.select("form")[0]
# form.select("input")[0]["value"] = "vrushabh"
# form.select("input")[1]["value"] = "ThunderDude"

# profile_page = browser.submit(form,page.url)
# print(profile_page)

import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)
print(profiles_page.url)