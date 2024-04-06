import random
from flask import Flask, render_template, request
import flask
from db import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.htm');



if __name__ == '__main__':  
   app.run(debug=True)