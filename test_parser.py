from pypdf import PdfReader as reader

path = "C:\\Users\\gasse\\OneDrive\\Documents\\Practice\\Learning git\\Exam Organizer\\Demo PDFs\\9709_m25_ms_12 (1).pdf"
pdf = reader(path)

for page_number in [0,-1]:
    page = pdf.pages[page_number]
    page_text = page.extract_text()
    lines = page_text.split("\n")
    print(f"-----Page Number {page_number + 1}-------")

    for line_number, line in enumerate(lines):
        print(line_number,line)

#C:\Users\gasse\OneDrive\Documents\Practice\Learning git\Exam Organizer\9709_w20_ms_12.pdf