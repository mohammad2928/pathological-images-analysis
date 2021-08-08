from flask import Flask, render_template, request, redirect
import os
import main
from utilities import convert_line_to_meaningful
import json 


app = Flask(__name__,  static_url_path = "/uploads", static_folder = "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = './uploads'


def ulify(elements):
    string = "<ul class='list-unstyled'>\n"
    for s in elements:
        string += "<li>" + str(s) + "</li>\n"
    string += "</ul>"
    return string


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
            
            with open('keys.txt') as json_file:
                keys = json.load(json_file)
            key = request.form['key']
            key_type = request.form['key_type']
            key_section = request.form['key_section']
            help_key = request.form['help_key']
            
            if key != '':
                keys[key] = [key, key_type, key_section,  help_key]
                with open('keys.txt', 'w') as outfile:
                    json.dump(keys, outfile)
            return redirect('/')

        ocr_type = request.form['ocr_type']
        uploaded_file  = request.files['file']
        image_path = os.path.join("uploads", "temp.png")
        if uploaded_file.filename != '':
           uploaded_file .save(image_path)
        
        if uploaded_file:
            ocr_text = main.extract_ocr_text(ocr_type, image_path)
            ocr_text = [    convert_line_to_meaningful(line) for line in ocr_text]
            image_path = "/uploads/temp.png"
            return render_template(
                'index.html', 
                ocr_text=ulify(ocr_text),
                image_path=image_path,
                title="The process is finished")


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


