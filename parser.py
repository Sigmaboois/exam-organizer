from pypdf import PdfReader as reader

def meta_extract(pdf_path):

    pdf = reader(pdf_path)
    
    page_1 = pdf.pages[0]
    page_1_text = page_1.extract_text()
    lines_1 = page_1_text.split("\n")
    
    page_2 = pdf.pages[1]
    page_2_text = page_2.extract_text()
    lines_2 = page_2_text.split("\n")

    code = lines_2[1]
    code = code.split("/")
    
    metadata = {
        "year":None,
        "subject_name":None,
        "subject_code":None,
        "session":None,
        "paper_type":None,
        "paper":None,
        "variant":None
    }

    subject_name,subject_code = lines_1[3].split()
    subject_code,paper = subject_code.split("/")
    paper,variant = paper[0],paper[1]
    
    #For the paper_type key -->
    for line in lines_1:
        if "You must answer on the question paper" in line:
            metadata["paper_type"] = "QP"

    
    
    metadata["subject_name"] = subject_name
    metadata["subject_code"] = subject_code
    metadata["paper"] = paper
    metadata["variant"] = variant

    return metadata,code

if __name__ == "__main__":
    print("This is a test\n")
    metadata,code = meta_extract("C:\\Users\\gasse\\OneDrive\\Documents\\Practice\\Learning git\\Exam Organizer\\9709_s25_qp_53.pdf")
    print(metadata,"\n",code)
    