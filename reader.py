from pypdf import PdfReader as reader


def pdf_reader(pdf_path):

    page_texts = []

    pdfreader = reader(pdf_path)
    pagesinpdf = pdfreader.pages

    for page in pagesinpdf:

        text = page.extract_text()

        page_texts.append(text)

    return page_texts


if __name__ == "__main__":

    path = input("Input the PDF path:\n")

    pdf_reader(path)