from pypdf import PdfReader as reader

def meta_extract(pdf_path):

    # INITIALIZATION OF ALL VARIABLES BEFORE BEING ASSIGNED
    pdf = reader(pdf_path)
    
    page_1 = pdf.pages[0]
    page_1_text = page_1.extract_text()
    lines_1 = page_1_text.split("\n")
    
    last_page = pdf.pages[-1]
    last_page_text = last_page.extract_text()
    last_lines = last_page_text.split("\n")
    
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
        elif "MARK SCHEME" in line:
            metadata["paper_type"] = "MS"
    
    # Extraction based on the fact that paper_type = QP
    if metadata["paper_type"] ==  "QP": 
        code = last_lines[1]
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

    elif metadata["paper_type"] == "MS":
        
        # Subject Name Extraction from MS
        subject_name_splitted = lines_1[12].split()
        subject_name = subject_name_splitted[0]
        metadata["subject_name"] = subject_name

        # Subject Code Extraction from MS
        subject_code_splitted = subject_name_splitted[1].split("/")
        subject_code = subject_code_splitted[0]
        metadata["subject_code"] = subject_code

        # Paper and variant extraction
        paper_variant = subject_code_splitted[1]
        paper = paper_variant[0]
        variant = paper_variant[1]
        metadata["paper"] = paper
        metadata["variant"] = variant

    return metadata

if __name__ == "__main__":
    print("This is a test\n")
    metadata= meta_extract("9709_w20_ms_12.pdf")
    print(metadata)
    