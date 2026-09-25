import requests as req
import json
from bs4 import BeautifulSoup as bt
import re

def generate_file():
    codepattern = r"\d{4}"
    target_url = "https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-advanced/cambridge-international-as-and-a-levels/subjects/?utm_source=chatgpt.com"

    scraped = req.get(target_url)
    scraped_text = scraped.text

    subjects_file = "subjects.json"
    soup = bt(scraped_text,"html.parser")

    extracted = soup.find_all("a",attrs={"data-href":True})

    subjects = {
        
    }
    for line in extracted:
        extracted_line = line.text

        codesearch = re.search(codepattern,extracted_line)
        extracted_name_temp = extracted_line[:codesearch.start()].strip()
        extracted_code = codesearch.group()

        subject_code = extracted_code

        if "-" in extracted_name_temp:
            extracted_name = extracted_name_temp.split("-")
            del extracted_name[1]
            subject_name = extracted_name[0].rstrip()
        else:
            subject_name = extracted_name_temp
        subjects[subject_code] = subject_name.strip()

    with open(subjects_file,"w") as file:
        json.dump(subjects,file)
if __name__ == "__main__":
    generate_file()