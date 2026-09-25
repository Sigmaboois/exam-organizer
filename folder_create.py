import os
import shutil


def create_exam_folder(pdf_path, metadata_info):

    folders_path = f"{metadata_info['subject_name']}/{metadata_info['year']}/{metadata_info['session']}/Paper {metadata_info['paper']}/Variant {metadata_info['variant']}"

    file_name = f"{metadata_info['subject_name']}_{metadata_info['year']}_{metadata_info['session']}_{metadata_info['paper']}_{metadata_info['variant']}.pdf"

    os.makedirs(folders_path, exist_ok=True)

    destination = os.path.join(folders_path, file_name)

    shutil.copy2(pdf_path, destination)


if __name__ == "__main__":
    print("folder_create.py")