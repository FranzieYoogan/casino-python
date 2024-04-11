import random
from flask import Flask, render_template, request, session
from flask_session import Session
import flask
from db import *

app = Flask(__name__)

app.secret_key = 'thatsSecret';

@app.route("/", methods = ['POST','GET'])
def index():
 if(flask.request.method == "POST"):
    
    userEmail = request.form['email'];
    userPassword = request.form['password']; 
    loginError = 0
        
    if(userEmail == row[4] and userPassword == row[5]):
        session["email"] = userEmail;
        
      
        return render_template('index.htm',login = session["email"]); 

    else:

       loginError = 1
    
       return render_template('index.htm',loginError = loginError);

 else:
  return render_template('index.htm');
    
     
      



if __name__ == '__main__':  
   app.run(debug=True)