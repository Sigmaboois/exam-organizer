from pypdf import PdfReader as reader

input_path = input("Please input the path of ur file (paste in full directory if not in the same folder as reader.py)")

pdfreader = reader(input_path)
pagesinpdf = pdfreader.pages

for page in pagesinpdf:
    text = page.extract_text()
    print(text)