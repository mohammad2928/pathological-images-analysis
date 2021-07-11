from PIL import Image
import pytesseract
from parameters import pyteseract_path

class OCR:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = pyteseract_path

    def extract_text(self, img):
        return pytesseract.image_to_string(img, lang='eng')

if __name__ == '__main__':
    sample_image_path = "../data/sample.jpg" 
    img = Image.open(sample_image_path)
    ocr = OCR()
    ocr_result = ocr.extract_text(img)
    print(ocr_result)