# pathological-images-analysis-
Analysis of Pathological Images, is an open-source project to analyze pathological images and extract as much information from them as possible. 
Also, it tries to use the extracted information to show the types of tumors and other issues. in the following the steps of the project is shown.

![no-image]("https://github.com/mohammad2928/pathological-images-analysis/docs/images/pathalogical-image-analysis.pdf")

Preprocessing:
In this step, noise, background and useless informations removed from input images. 

OCR:
In theis phase, all texts extracted from the images. 

Analysis:
In the last step, the extracted information analized for show the issues. 
        

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