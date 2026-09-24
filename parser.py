from pypdf import PdfReader as reader

def meta_extract(pdf_path):

    pdf = reader(pdf_path)
    page_1 = pdf.pages[0]
    page_1_text = page_1.extract_text()
    lines = page_1_text.split("\n")
    metadata = {
        "year":None,
        "subject_name":None,
        "subject_code":None,
        "session":None,
        "paper_type":None
    }

    for line in lines:
        print(line)

    return metadata

if __name__ == "__main__":
    print("This is a test\n")
    meta_extract("C:\\Users\\gasse\\OneDrive\\Documents\\Practice\\Learning git\\Exam Organizer\\9709_s25_qp_53.pdf")
