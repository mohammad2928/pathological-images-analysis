from flask import Flask, render_template,request
import os
import main

app = Flask(__name__,  static_url_path = "/uploads", static_folder = "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = './uploads'

def produce_personal_html_tags(Patient_info):
    return f"""
    <ul class="list-group list-group-flush">
        <li class="list-group-item active">'Personal Informations'</li>
        <li class="list-group-item">Name: {Patient_info['Patient_name']}</li>
        <li class="list-group-item">Age: {Patient_info['Patient_age']}</li>
        <li class="list-group-item">Sex: {Patient_info["Patient_sex"]}</li>
    </ul>
    """

def produce_tumor_html_tags(tumor_info):
    return f"""
    <ul class="list-group list-group-flush">
        <li class="list-group-item active">'Tumor Informations'</li>
        <li class="list-group-item">Tumor size: {tumor_info['tumor_size']}</li>
        <li class="list-group-item">Tumor site: {tumor_info['tumor_site']}</li>
    </ul>
    """

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
        

        Patient_info, tumor_info = main.main(ocr_type, image_path)
        tumor_html_tags = produce_tumor_html_tags(tumor_info)
        personal_html_tags = produce_personal_html_tags(Patient_info)
        image_path = "/uploads/temp.png"
        return render_template(
            'index.html', Patient_info = Patient_info ,
            tumor_html_tags = tumor_html_tags,
            personal_html_tags = personal_html_tags,
            image_path=image_path,
            title="The process is finished")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


