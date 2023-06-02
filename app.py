from flask import Flask, render_template, send_from_directory, url_for
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from src.mainProgram import *


app= Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'
app.config['UPLOADED_PHOTOS_DEST']='uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

options={
    "textDetectionOptions":['paddleOCR', 'YOLO'],
    "textRecognitionOptions": ['paddleOCR', 'somethingmore']
}

class UploadForm(FlaskForm):
    photo= FileField(
        validators=[
            FileAllowed(photos, 'Only images are allowed'),
            FileRequired('File field should not be empty')
        ]
    )
    submit=SubmitField('Upload')

@app.route('/uploads/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

@app.route('/', methods= ['GET','POST'])
def upload_image():
    form = UploadForm()
    if form.validate_on_submit():
        filename= photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        print(str(app.config['UPLOADED_PHOTOS_DEST']+ filename))
        texts = get_text(url = os.path.join(app.config['UPLOADED_PHOTOS_DEST'],filename))
    else:
        file_url=None
        texts=""
    

    return render_template('index.html', form=form, file_url=file_url, options = options, texts= texts)

@app.route('/faq', methods=['GET'])
def get_faq_page():
    return render_template("faq.html")


if __name__=='__main__':
    app.run(debug=True, port = 8000)
