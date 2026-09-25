import requests as req
import json
import bs4 as bt
import re

codepattern = r"\d{4}"
target_url = "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-advanced/cambridge-international-as-and-a-levels/subjects/?utm_source=chatgpt.com"

scraped = req.get(target_url)
scraped_text = scraped.text

subjects_file = "subjects.json"
soup = bt.BeautifulSoup(scraped_text,"html.parser")

extracted = soup.find_all("a",attrs={"data-href":True})

codesearch = re.search(codepattern,extracted)
print(type(codesearch))