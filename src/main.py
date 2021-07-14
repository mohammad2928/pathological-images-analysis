import cv2
from ocr import OCR
from image_preprocessing import convert_to_gray, binarization, do_erotion, do_delation
from image_preprocessing import rotation

if __name__ == '__main__':
    # sample_image_path = "../data/sample.jpg" 
    sample_image_path = "../data/sample2.jpeg"
    ocr = OCR()

    img = cv2.imread(sample_image_path)

    # pre-processing phase
    gray = convert_to_gray(img)
    gray = rotation(gray) # rotate if needed
    thresh = binarization(gray)
    delation = do_delation(thresh)
    erotion = do_erotion(delation)

    # OCR part
    english_result = ocr.english_tesseract_ocr(erotion)
    print(english_result)

    persian_result = ocr.persian_tesseract_ocr(erotion)
    print(persian_result)
