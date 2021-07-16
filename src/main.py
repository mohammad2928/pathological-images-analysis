from ocr import OCR
from image_preprocessing import img_preprocessing
from analyse import get_personal_info, get_tumor_info
import multiprocessing



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


def main():
    sample_image_path = "../data/sample.jpg"
    ocr = OCR()
    pre_processed_image = img_preprocessing(
        sample_image_path
        )  # preprocessing input image

    ocr_types = {
    'persain_easyocr': ocr.persian_easyocr,
    'english_easyocr': ocr.english_easyocr,
    'persian_tesseract_ocr': ocr.persian_tesseract_ocr,
    'english_tesseract_ocr': ocr.english_tesseract_ocr,  
        }
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    multi_process(ocr_types, pre_processed_image, return_dict)

    get_personal_info(return_dict['persian_tesseract_ocr'].split("\n"))
    get_tumor_info(return_dict['persian_tesseract_ocr'].split("\n"))


if __name__ == "__main__":
    main()
