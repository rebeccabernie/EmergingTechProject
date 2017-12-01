from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json
import os, base64
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html') # Load index.html file

# Save the image
@app.route('/save', methods=['POST'])
def save():
    #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    img =  request.json
    #print("img received")

    #newstrimg = str(img).replace('[{}]','')
    #print(str(img['base64'])) # Print base64 value in json

    base64img = str(img['base64'])
    #newbase64 = base64img.replace('[{}]','')
    

    new = base64.decodestring(bytes(base64img, "utf-8"))
    image_result = open('img.png', 'wb') # create a writable image and write the decoding result
    image_result.write(new)
    
    print("img file written")
    return json.dumps(img)

'''
@app.route('/uploadedImage')
def uploaded_file(filename):
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #return #send_from_directory(app.config['UPLOAD_FOLDER'], filename)
'''
if __name__ == "__main__":
    app.run()