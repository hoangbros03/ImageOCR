from flask import Flask, render_template, send_from_directory, url_for, abort, request
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
import sys
sys.path.append("models/mmocr")
from src.mainProgram import *
from src.models.models_list import text_detection_dict, text_recognition_dict

app= Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'
app.config['UPLOADED_PHOTOS_DEST']='uploads'
UPLOAD_THRESHOLD = 3

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

options=get_options()

# To limit upload times
ip_dict = {}

class UploadForm(FlaskForm):
    photo= FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit=SubmitField('Upload')

def get_ip():
    '''
    To get ip of user
    '''
    return request.remote_addr

@app.before_request
def record_ip():
    '''
    To record ip to ip_dict for further actions
    '''
    ip_address = get_ip()
    print(ip_address)
    if ip_address not in ip_dict:
        ip_dict[ip_address] = 0
        

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods= ['GET','POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        if ip_dict[get_ip()] >= UPLOAD_THRESHOLD:
            file_url=None
            texts = "Sorry, you have exceeded your upload limit"
        else:
            filename= photos.save(form.photo.data)
            file_url = url_for('get_file', filename=filename)
            print(str(app.config['UPLOADED_PHOTOS_DEST']+ filename))
            texts = get_text(url = os.path.join(app.config['UPLOADED_PHOTOS_DEST'],filename))
            ip_dict[get_ip()]+=1
    else:
        file_url=None
        texts=""
    

    return render_template('index.html', form=form, file_url=file_url, options = options, texts= texts, count_times = ip_dict[get_ip()], threshold = UPLOAD_THRESHOLD)

@app.route('/faq', methods=['GET'])
def get_faq_page():
    return render_template("faq.html")

@app.route('/404', methods=['GET'])
@app.errorhandler(404)
def get_notfound_page(e = "ok", limit= False):
    return render_template("404.html"), {"Refresh": "5; url=/"}


if __name__=='__main__':
    app.run(debug=True, port = 8000)
