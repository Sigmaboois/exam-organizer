import reader
import parser
import folder_create
import generate_subjects


def main():

    path = input("Please input the exam file path:\n")

    generate_subjects.generate_file()

    extracted_pdf = reader.pdf_reader(path)

    parsed_pdf = parser.meta_extract(extracted_pdf)

    folder_create.create_exam_folder(path, parsed_pdf)


if __name__ == "__main__":
    main()