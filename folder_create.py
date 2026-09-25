import parser
import reader
import os

pdf_path = "C:\\Users\\gasse\\Downloads\\0620_m25_qp_42.pdf"
folders_path = ""

info = reader.pdf_reader(pdf_path)
metadata_info = parser.meta_extract(info)

folders_path = f"{metadata_info['subject_name']}/{metadata_info['year']}/{metadata_info['session']}/{metadata_info['paper']}/{metadata_info['variant']}"

os.makedirs(folders_path,exist_ok=True)


if __name__ == "__main__":
    print("This is a test")
    print(folders_path)