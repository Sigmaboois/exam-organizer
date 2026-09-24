from pypdf import PdfReader as reader

def meta_extract(pdf_path):

    pdf = reader(pdf_path)
    
    page_1 = pdf.pages[0]
    page_1_text = page_1.extract_text()
    lines_1 = page_1_text.split("\n")
    
    page_2 = pdf.pages[1]
    page_2_text = page_2.extract_text()
    lines_2 = page_2_text.split("\n")
    
    metadata = {
        "year":None,
        "subject_name":None,
        "subject_code":None,
        "session":None,
        "paper_type":None
    }

    for line in lines_1:
        print(line)
    
    for line in lines_2:
        print(line)
    
    return metadata

if __name__ == "__main__":
    print("This is a test\n")
    meta_extract("C:\\Users\\gasse\\OneDrive\\Documents\\Practice\\Learning git\\Exam Organizer\\9709_s25_qp_53.pdf")
