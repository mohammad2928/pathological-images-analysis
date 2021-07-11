from PIL import Image
from parameters import pyteseract_path
from ocr import OCR

if __name__ == '__main__':
    sample_image_path = "../data/sample.jpg" 
    img = Image.open(sample_image_path)
    ocr = OCR()
    ocr_result = ocr.extract_text(img)
    print(ocr_result)