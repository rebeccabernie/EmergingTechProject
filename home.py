from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file('index.html') # Load index.html file

@app.route('/<digit>')
def fname(digit): 
    return 'Digit:' + digit

if __name__ == "__main__":
    app.run()