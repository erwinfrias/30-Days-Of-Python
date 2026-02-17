# =============================
# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
# =============================

import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

data = {}

# Extract all sections with headings and paragraphs/lists
for section in soup.find_all(["h2", "h3"]):
    title = section.get_text(strip=True)
    content = []

    for sibling in section.find_next_siblings():
        if sibling.name in ["h2", "h3"]:
            break
        if sibling.name == "p":
            content.append(sibling.get_text(strip=True))
        if sibling.name == "ul":
            for li in sibling.find_all("li"):
                content.append(li.get_text(strip=True))

    if content:
        data[title] = content

# Save to JSON
with open("bu_facts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("BU facts saved successfully.")


# =============================
# Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
# =============================


# =============================
# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
# =============================

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# First main table
table = soup.find("table", {"class": "wikitable"})

headers = []
for th in table.find_all("th"):
    header_text = th.get_text(strip=True)
    headers.append(header_text)

rows = table.find_all("tr")[1:]

presidents = []

for row in rows:
    cols = row.find_all(["td", "th"])
    if len(cols) >= 5:
        president = {
            "Number": cols[0].get_text(strip=True),
            "Name": cols[1].get_text(strip=True),
            "Term": cols[2].get_text(strip=True),
            "Party": cols[4].get_text(strip=True)
        }
        presidents.append(president)

# Save JSON
with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4)

print("US presidents saved successfully.")