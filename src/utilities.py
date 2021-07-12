
import cv2
from parameters import erotion_kernel

def convert_to_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray 


def binarization(gray):
    _, thresh = cv2.threshold(gray, 135, 240, cv2.THRESH_BINARY)
    return thresh


def do_erotion(thresh):
    erosion = cv2.erode(thresh, erotion_kernel, iterations = 1)
    return erosion


