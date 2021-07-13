# Pathological-images-analysis-
Analysis of Pathological Images, is an open-source project to analyze pathological images and extract as much information from them as possible. 
Also, it tries to use the extracted information to show the types of tumors and other issues. in the following the steps of the project is shown.

![no-image](https://raw.githubusercontent.com/mohammad2928/pathological-images-analysis/main/docs/images/pathalogical-image-analysis.svg)

1: **Preprocessing**

In this step, noise, background, and useless information are removed from input images. 

For example, after pre-processing source image (A), converted to (B). 

A: source image 

![source image](https://raw.githubusercontent.com/mohammad2928/pathological-images-analysis/main/docs/images/source.jpg)

B: pre-processed image

![pre-processed image](https://raw.githubusercontent.com/mohammad2928/pathological-images-analysis/main/docs/images/pre-processed.jpg)


2: **OCR**

In this phase, all texts are extracted from the pre-processed image.

OCR engines:

1. [tesseract](https://github.com/madmaze/pytesseract)
2. [easyocr](https://github.com/JaidedAI/EasyOCR/tree/master/easyocr/character) 


Notes:

1. In the first running some models will be downloaded.

For each image two types of ocr will be extended:

    1. English OCR
    2. Persian ocr
 


3- **Analysis**

In the last step, the extracted information is analyzed to show the issues. 


## Installation

1- Create an virtual enviorment (You can use anaconda or virtualenv) and active the enviornment.

2- Clone the project

```
clone https://github.com/mohammad2928/pathological-images-analysis.git
```

3- cd TO-PROJECT-FILES-FOLDER;

4- pip install -r reqierments.txt

(If you are living in the IRAN, for installation maybe you need to use a VPN.)

5- Head over to https://github.com/UB-Mannheim/tesseract/wiki and get the 32-bit or 64-bit version depending on your system architecture and install it like as other programs. 
(Or you can use direct path in your codes), you can use installation file in ~/data/ folder.

## Usage 

```
cd src
python src/main.py

```
