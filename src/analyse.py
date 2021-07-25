# analyse modules
# extracted information is:
# personal information, Clinical information
# persoanl information: ['name', 'نام'], ['age', 'سن'], ['sex', 'جنسیت']]
# clinical information
# tumor information: tumor size, tumor configuration
import re
from utilities import convert_line_to_meaningful

class PersonalInformation:
    def __init__(self):
        self.sex_names = ["مرد", "زن", "male", "female"]

    def get_name(self, ocr_lines):
        name = ""
        for line in ocr_lines:
            line = convert_line_to_meaningful(line)
            if "نام" in line or "name" in line:
                name = line[:]
                name.replace('name','')
                name.replace('نام', '')
                return name
        return name

    def get_age(self, ocr_lines):
        age = ""
        for line in ocr_lines:
            line = convert_line_to_meaningful(line)
            if "سن" in line or "age" in line:
                tokens = line.split(" ")
                for token in tokens:
                    try:
                        age = int(token)
                        return age
                    except:
                        continue
        return age

    def get_sex(self, ocr_lines):
        sex = ""
        for line in ocr_lines:
            line = convert_line_to_meaningful(line)
            if "جنس" in line or "sex" in line or "sex" in line:
                tokens = line.split(" ")
                for token in tokens:
                    if token.lower() in self.sex_names:
                        return token
        return sex


class TumorInformation:
    def __init__(self):
        pass

    def get_tomur_size(self, ocr_lines):
        tomur_size = ""
        for line in ocr_lines:
            line = line.lower()
            line = convert_line_to_meaningful(line)
            if "tumor" in line and "size" in line:
                for token in line.split():
                    if bool(re.search(r"\d", token)):
                        return token
        return tomur_size

    def get_tomur_site(self, ocr_lines):
        tomur_site = ""
        for line in ocr_lines:
            line = line.lower()
            line = convert_line_to_meaningful(line)
            if "tumor" in line and "site" in line:
                line = line.replace("tumor", "")
                line = line.replace("site", "")
                line = line.replace(":", "")
                line = line.replace("-", "")
                return line
        return tomur_site


def get_personal_info(ocr_lines):
    personal_info = PersonalInformation()
    Patient_name = personal_info.get_name(ocr_lines)
    Patient_age = personal_info.get_age(ocr_lines)
    Patient_sex = personal_info.get_sex(ocr_lines)
    patient_information = {
        "Patient_name":Patient_name,
        "Patient_age":Patient_age,
        "Patient_sex":Patient_sex,
    }
    return patient_information


def get_tumor_info(ocr_lines):
    tumor_info = TumorInformation()
    tumor_size = tumor_info.get_tomur_size(ocr_lines)
    tumor_site = tumor_info.get_tomur_site(ocr_lines)
    tumor_information = {
        "tumor_size":tumor_size,
        "tumor_site":tumor_site,
    }
    return tumor_information
