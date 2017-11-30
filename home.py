from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html') # Load index.html file

# http://127.0.0.1:5000/digit/9 outputs digit:9
'''
@app.route('/digit/<digit>')
def fname(digit): 
    return 'Digit:' + digit
'''

# File upload adapted from http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
UPLOAD_FOLDER = './uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect()
            #return uploaded_file(filename)
            #return #redirect(url_for('upload_file')) #uploaded_file(filename) #jsonify({"result": randint(0,9)}), 200 #redirect(url_for('uploaded_file' filename=filename))
    return

'''
@app.route('/uploadedImage')
def uploaded_file(filename):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #return #send_from_directory(app.config['UPLOAD_FOLDER'], filename)
'''
if __name__ == "__main__":
    app.run()