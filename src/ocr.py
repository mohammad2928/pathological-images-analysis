from PIL import Image
import pytesseract
from parameters import pyteseract_path
import easyocr


class OCR:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = pyteseract_path

    def english_tesseract_ocr(self, img):
        # TODO: using oem, psm in tesseract config
        return pytesseract.image_to_string(img, lang="eng")

    def persian_tesseract_ocr(self, img):
        # TODO: using oem, psm in tesseract config
        config = "-l fas-tune-float"
        return pytesseract.image_to_string(img, config=config)

    def english_easyocr(self, img):
        reader = easyocr.Reader(
            ["en"]
        )  # need to run only once to load model into memory
        return reader.readtext(img, detail=0)

    def persian_easyocr(self, img):
        reader = easyocr.Reader(
            ["en", "fa"]
        )  # need to run only once to load model into memory
        return reader.readtext(img, detail=0)


if __name__ == "__main__":
    sample_image_path = "../data/sample.jpg"
    img = Image.open(sample_image_path)
    ocr = OCR()
    ocr_result = ocr.extract_text(img)
    print(ocr_result)
