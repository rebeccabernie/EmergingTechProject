from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json
import os, base64
from werkzeug.utils import secure_filename
from PIL import Image

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

    #print(str(img['base64'])) # Print base64 value in json

    base64Img = img['base64'] # Convert base64 value in json to a string
    print(type(base64Img))
    imgData = base64Img.split(',')[1]

    with open("img.png", "wb") as f:
        f.write(base64.b64decode(imgData))


    # image = Image.fromstring('RGB',(200,200),base64.b64decode(base64Img))
    # image.save("img.png")

    #new = decode_base64(bytes(base64Img)) # Pass to decoding method, back to bytes for splitting
    #imgData = base64.b64decode(base64Img).split(',')[1] # Split the decoded data - "data:image/jpeg;base64" causes errors, use the second element 
    #imgData = base64.b64decode(base64Img, validate=False).split(',')[1]
    #print(imgData)

    #res = open('img.png', 'wb') # create a writable image and write the decoding result
    #res.write(imgData)
    
    #print("img file written")

    return json.dumps(img)

def decode_base64(data):
    # Handles padding errors - adapted from https://stackoverflow.com/a/9807138/7232648
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += '='* (4 - missing_padding)

    return str(base64.b64decode(data)) # Return the decoded data

if __name__ == "__main__":
    app.run(debug=True)