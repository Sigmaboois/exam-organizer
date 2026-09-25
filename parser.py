import re
import json


def meta_extract(info):

    pages_text = ""

    for page in info:

        pages_text += page + "\n"

    pages_lines = pages_text.split("\n")

    metadata = {
        "year": None,
        "subject_name": None,
        "subject_code": None,
        "session": None,
        "paper_type": None,
        "paper": None,
        "variant": None
    }

    for line in pages_lines:

        if "You must answer on the question paper" in line:

            metadata["paper_type"] = "QP"

        elif "MARK SCHEME" in line:

            metadata["paper_type"] = "MS"

    if metadata["paper_type"] == "QP":

        code_pattern = r"\d{4}/\d{2}/[A-Z]/[A-Z]/\d{2}"

        for line in pages_lines:

            match = re.search(code_pattern, line)

            if match:

                code = match.group().split("/")

                break

        paper_variant = code[1]

        paper, variant = paper_variant[0], paper_variant[1]

        if code[2] == "M":

            session = "May-June"

        elif code[2] == "F":

            session = "February-March"

        else:

            session = "October-November"

        year = f"{str(20) + code[4]}"

        metadata["subject_code"] = code[0]
        metadata["paper"] = paper
        metadata["variant"] = variant
        metadata["session"] = session
        metadata["year"] = year

    elif metadata["paper_type"] == "MS":

        subpattern = r"\d{4}/\d{2}"
        sessionpattern = r"[A-Za-z]+/[A-Za-z]+\s*\d{4}"

        for line in pages_lines:

            ismatch = re.search(subpattern, line)

            if ismatch:

                subcode = ismatch.group().split("/")

                break

        for line in pages_lines:

            issession = re.search(sessionpattern, line)

            if issession:

                subsession = issession.group().split()

                break

        metadata["subject_code"] = subcode[0]

        paper_variant = subcode[1]

        paper, variant = paper_variant[0], paper_variant[1]

        metadata["paper"] = paper
        metadata["variant"] = variant

        if subsession[0] == "October/November":

            session = "October-November"

        elif subsession[0] == "May/June":

            session = "May-June"

        else:

            session = "February-March"

        metadata["session"] = session
        metadata["year"] = subsession[1]

    with open("subjects.json", "r") as file:

        subjects_code = json.load(file)

        metadata["subject_name"] = subjects_code[metadata["subject_code"]]

    return metadata