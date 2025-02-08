import mechanicalsoup
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/profiles"
login_page = browser.get(url)
login_html = login_page.soup


# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"


# profiles_page = browser.submit(form, login_page.url)
links =login_page.soup.select("a")
for link in links:
    address = url + link["href"]
    text = link.text
    print(f"{text}: {address}")

# Aphrodite: http://olympus.realpython.org/profiles/aphrodite
# Poseidon: http://olympus.realpython.org/profiles/poseidon
# Dionysus: http://olympus.realpython.org/profiles/dionysus