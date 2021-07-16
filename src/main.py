import cv2
from ocr import OCR
from image_preprocessing import img_preprocessing
from analyse import get_personal_info, get_tumor_info


def main():
    sample_image_path = "../data/sample.jpg"
    ocr = OCR()
    pre_processed_image = img_preprocessing(
        sample_image_path
    )  # preprocessing input image

    english_result = ocr.english_tesseract_ocr(pre_processed_image)  # English OCR
    persian_result = ocr.persian_tesseract_ocr(pre_processed_image)  # Persian OCR

    get_personal_info(persian_result.split("\n"))
    get_tumor_info(persian_result.split("\n"))


if __name__ == "__main__":
    main()
