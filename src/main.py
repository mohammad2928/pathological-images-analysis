from ocr import OCR
from image_preprocessing import img_preprocessing
from analyse import get_personal_info, get_tumor_info
import multiprocessing
from parameters import pyteseract_path
import pytesseract


def do_ocr(ocr_type, pre_processed_image, return_dict):
    ocr = OCR()
    ocr_text = ocr_type(pre_processed_image)
    name = str(ocr_type).split('.')[1]
    name = name.split(' ')[0]
    return_dict[name] = ocr_text


def multi_process(ocr_types, pre_processed_image, return_dict):
    jobs = []
    for i in ocr_types.values():
        p = multiprocessing.Process(target=do_ocr, args=(i, pre_processed_image, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()


def get_ocr_types(ocr_type):
    ocr = OCR()
    if ocr_type == "tesseract":
        ocr_types = {
        'persian_tesseract_ocr': ocr.persian_tesseract_ocr
            }
    elif ocr_type == "easyocr":
        ocr_types = {
        'persain_easyocr': ocr.persian_easyocr
            }
    return ocr_types


def extract_ocr_text(ocr_type, sample_image_path):
    pytesseract.pytesseract.tesseract_cmd = pyteseract_path
    pre_processed_image = img_preprocessing(
        sample_image_path
        )  # preprocessing input image
    ocr_types = get_ocr_types(ocr_type)

    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    multi_process(ocr_types, pre_processed_image, return_dict)
    if ocr_type == "tesseract":
        return return_dict.get('persian_tesseract_ocr').split('\n')    
    elif ocr_type == "easyocr":
        return return_dict.get('persian_easyocr')


if __name__ == "__main__":
    sample_image_path = "../data/sample.jpg"
    extract_ocr_text(ocr_type="tesseract", sample_image_path="../data/sample.jpg")
