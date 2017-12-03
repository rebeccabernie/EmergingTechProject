from flask import Flask, request, json, jsonify
import base64
from PIL import Image
from PIL import ImageOps as io

import runMnist as rm

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

    # Configure the image - longwinded way but works and is easier to read
    colour = Image.open("img.png") # Open the saved image
    sized = io.fit(colour, (28, 28)) # Rezise it
    grey = sized.convert("L") # Convert it to grayscale

    # Image needs to be black -or- white, use a lambda function to loop through each pixel of the image
    # If the pixel (x) is less than 128 set it to black (0,0,0), if greater set to white (255,255,255)
    im = grey.point((lambda x: 0 if x<128 else 255), '1') # Mode 1 (black/white)
    im.save('img.png') # Save the new image

    savedImg = Image.open("img.png") # Save the new version of the image

    prediction = rm.predict(savedImg) # Run prediction function in runMnist.py
    #print(prediction)
    
    return jsonify(prediction = str(prediction[0])) # Return the result of the prediction function to the ajax call in index.html

if __name__ == "__main__":
    app.run(debug=True) # debug=True auto re-runs the program when changes to any file are saved