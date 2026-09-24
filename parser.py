from pypdf import PdfReader as reader

def meta_extract(pdf_path):

    # INITIALIZATION OF ALL VARIABLES BEFORE BEING ASSIGNED
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
        "paper_type":None,
        "paper":None,
        "variant":None
    }

    #END OF INITIALIZATION
    #______________________________________________________________________________________________________________

    #For the paper_type key -->
    for line in lines_1:
        if "You must answer on the question paper" in line:
            metadata["paper_type"] = "QP"
        elif "MARK SCHEME" in lines_1:
            metadata["paper_type"] = "MS"
    
    # Extraction based on the fact that paper_type = QP
    if metadata["paper_type"] ==  "QP": 
        code = lines_2[1]
        code = code.split("/")
        year_expression = code[5]
        yearsplitted = year_expression.split()
        year = yearsplitted[2]
        subject_name,subject_code = lines_1[3].split()
        subject_code,paper = subject_code.split("/")
        paper,variant = paper[0],paper[1]

        metadata["session"] = code[2]
        metadata["subject_name"] = subject_name
        metadata["subject_code"] = subject_code
        metadata["paper"] = paper
        metadata["variant"] = variant
        metadata["year"] = year

    return metadata

if __name__ == "__main__":
    print("This is a test\n")
    metadata= meta_extract("9709_w20_ms_12.pdf")
    print(metadata)
    