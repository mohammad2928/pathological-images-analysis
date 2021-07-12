import cv2
from ocr import OCR
from utilities import convert_to_gray, binarization, do_erotion

if __name__ == '__main__':
    sample_image_path = "../data/sample.jpg" 
    img = cv2.imread(sample_image_path)

    # pre-processing phase
    gray = convert_to_gray(img)
    thresh = binarization(gray)
    erotion = do_erotion(thresh)

    # OCR part
    ocr = OCR()
    ocr_result = ocr.extract_text(erotion)
    print(ocr_result)

