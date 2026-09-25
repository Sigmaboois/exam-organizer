from pypdf import PdfReader as reader
import re

path = "C:\\Users\\gasse\\OneDrive\\Documents\\Practice\\Learning git\\Exam Organizer\\Demo PDFs\\9709_w20_ms_12.pdf"
pdf = reader(path)

pages = pdf.pages

for page_number, page in enumerate(pages):
    page_text = page.extract_text()
    print(page_number,page_text)