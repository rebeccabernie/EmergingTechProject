from flask import Flask, render_template, request, redirect, url_for, send_from_directory, json
import os, base64
from werkzeug.utils import secure_filename
from PIL import Image

import mnist

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html') # Load index.html file

# Save the image
@app.route('/save', methods=['POST'])
def save():
    img =  request.json
    #print("img received")

    base64Img = img['base64'] # Convert base64 value in json object to a string
    #print(type(base64Img)) # Type checking
    imgData = base64Img.split(',')[1] # Split the data into two, use second element (i.e. get rid of the "data:image/png;base64,", only need what's after that - https://stackoverflow.com/a/27604370/7232648

    with open("img.png", "wb") as f: # Create a writeable file called img.png
        f.write(base64.b64decode(imgData)) # Decode the data and write to an image

    mnist.test()
    
    #print("img file written")
    return json.dumps(img)

if __name__ == "__main__":
    app.run(debug=True)