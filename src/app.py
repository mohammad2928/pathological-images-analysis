from flask import Flask, render_template, request, redirect
import os
import main
from utilities import convert_line_to_meaningful
import json 
from analyse import PersonalInformation, ResultInformation

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

def show_result(text_dict):
    out = ""
    for k,v in text_dict.items():
        if v != "":
            out += "<p class='text-center'> {} : {} </p> ".format(k,v)
    return out

@app.route('/',methods = ['GET','POST'])
def send():
    with open('keys.txt') as json_file:
        keys = json.load(json_file)
    if request.method == 'POST':
        if 'file' not in request.files:
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
            ocr_lines = main.extract_ocr_text(ocr_type, image_path)
            ocr_text = [    convert_line_to_meaningful(line) for line in ocr_lines]
            image_path = "/uploads/temp.png"
            personal_info = PersonalInformation()
            result_info = ResultInformation()
            print(ocr_text)
            out_text = {
                'name': personal_info.get_name(ocr_text),
                'age': personal_info.get_age(ocr_text),
                'sex': personal_info.get_sex(ocr_text),
            }
            for k,v in keys.items():
                if v[1] == "number":
                    out_text[k] = result_info.get_number_result(ocr_text, v[0])
                else:
                    out_text[k] = result_info.get_text_result(ocr_text, v[0])
            return render_template(
                'index.html', 
                result = show_result(out_text),
                ocr_text=ulify(ocr_text),
                image_path=image_path,
                title="The process is finished")


    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


