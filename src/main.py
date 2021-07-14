import cv2
from ocr import OCR
from image_preprocessing import convert_to_gray, binarization, do_erotion, do_delation
from image_preprocessing import rotation
from analyse import PersonalInformation, TumorInformation


def get_personal_info(ocr_lines):
    personal_info = PersonalInformation() 
    Patient_name = personal_info.get_name(ocr_lines)
    Patient_age = personal_info.get_age(ocr_lines)
    Patient_sex = personal_info.get_sex(ocr_lines)
    patient_information = f"""
               Patient information
        name: {Patient_name}
        age: {Patient_age}
        sex: {Patient_sex}
        """ 
    print(patient_information)


def img_preprocessing(sample_image_path):
    img = cv2.imread(sample_image_path)

    # pre-processing phase
    gray = convert_to_gray(img)
    gray = rotation(gray) # rotate if needed
    thresh = binarization(gray)
    delation = do_delation(thresh)
    erosion = do_erotion(delation)
    return erosion


def get_tumor_info(ocr_lines):
    tumor_info = TumorInformation()
    tumor_size = tumor_info.get_tomur_size(ocr_lines)
    tumor_site = tumor_info.get_tomur_site(ocr_lines)
    tumor_information = f"""
                Tumor information
        tumor size: {tumor_size}
        tumor site: {tumor_site}
        """ 
    print(tumor_information)


if __name__ == '__main__':
    # sample_image_path = "../data/sample.jpg" 
    sample_image_path = "../data/sample.jpg"
    ocr = OCR()
    # preprocessing input image
    pre_processed_image = img_preprocessing(sample_image_path)

    # OCR part
    english_result = ocr.english_tesseract_ocr(pre_processed_image)
    persian_result = ocr.persian_tesseract_ocr(pre_processed_image)

    # analyse part
    get_personal_info(persian_result.split("\n"))
    get_tumor_info(persian_result.split("\n"))