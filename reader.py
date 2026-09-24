from pypdf import PdfReader as reader

input_path = input("Please input the path of ur file (paste in full directory if not in the same folder as reader.py)")

pages = reader.pages()

for i in pages:
    text = pages.extract_text
    print(text)