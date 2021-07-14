import cv2
from parameters import erotion_kernel, delation_kernel
import pytesseract

def get_rotate_size(osd):
    osd_lines = osd.split('\n')
    rotate_size = 0
    for line in osd_lines:
        if line.startswith("Rotate: "):
            rotate_size = line.split(" ")[1]
    return rotate_size


def convert_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray 


def rotation(gray):
    while 1:
        osd = pytesseract.image_to_osd(gray)
        if int(get_rotate_size(osd)):
            gray = cv2.rotate(gray, cv2.cv2.ROTATE_90_CLOCKWISE)
        else:
            break
    return gray

def binarization(gray):
    _, thresh = cv2.threshold(gray, 135, 240, cv2.THRESH_BINARY)
    return thresh


def do_erotion(thresh):
    erosion = cv2.erode(thresh, erotion_kernel, iterations = 1)
    return erosion

def do_delation(thresh):
    delation = cv2.dilate(thresh, delation_kernel, iterations = 1) 
    return delation
