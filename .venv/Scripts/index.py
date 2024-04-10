import random
from flask import Flask, render_template, request
import flask
from db import *

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
   if(flask.request.method == "POST"):
    show = 0;
    showError = 0
    userEmail = request.form['email'];
    userPassword = request.form['password'];
        
    if(userEmail == row[4] and userPassword == row[5]):
      show = 1;

    
    return render_template('index.htm',show = show); 

   else:
    showError = 1
    show = 0
    return render_template('index.htm',showError = showError)
 
    
     
      



if __name__ == '__main__':  
   app.run(debug=True)