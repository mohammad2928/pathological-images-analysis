from flask import Flask, render_template,request
import os
import time
import main

app = Flask(__name__,  static_url_path = "/uploads", static_folder = "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = './uploads'


@app.route('/',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', title="no file attached")

        ocr_type =request.form['ocr_type']
        uploaded_file  = request.files['file']
        image_path = os.path.join("uploads", "temp.png")
        if uploaded_file.filename != '':
           uploaded_file .save(image_path)
        
        if ocr_type == "tesseract":
            Patient_info, tumor_info = main.main(ocr_type, image_path)
            image_path = "/uploads/temp.png"
            print(image_path)
            return render_template(
                'index.html', Patient_info = Patient_info ,
                tumor_info = tumor_info, image_path = image_path,
                title="The process is finished")
        if ocr_type == "easyocr":
            Patient_info, tumor_info = main.main(ocr_type, image_path)
            image_path = "/uploads/temp.png"
            return render_template('index.html', Patient_info = Patient_info ,
            tumor_info = tumor_info, image_path = image_path,
            title="The process is finished")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


