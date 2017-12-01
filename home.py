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
    print("img received")
    #print(img) # Outputs JSON data to console, test if base64 transferred
    #imgdata = base64.b64decode(img)
    #filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    #with open(filename, 'wb') as f:
    #    f.write(imgdata)

    newstrimg = str(img).replace('[{}]','')
    print(newstrimg)

    #with open('img', 'w') as outfile:
        #json.dump(img, outfile)
        
    #newjpgtxt = open('img',"rb").read()
    #print(newjpgtxt)

    #new = base64.decodestring(bytes('img', "utf-8"))
    #image_result = open('img.png', 'wb') # create a writable image and write the decoding result
    #image_result.write(new)
    
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