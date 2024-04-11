import random
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
import flask
from db import *

app = Flask(__name__)

app.secret_key = 'thatsSecret';
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods = ['POST','GET'])
def index():
 if(flask.request.method == "POST"):
    
    userEmail = request.form["email"];
    userPassword = request.form["password"]; 
    loginError = 0
        
    if(userEmail == row[4] and userPassword == row[5]):
        

        session["userEmail"] = userEmail
      

       
      
        return render_template('profile.htm',login = userEmail); 

    else:

       loginError = 1
    
       return render_template('index.htm',loginError = loginError);

 else:
  return render_template('index.htm');
    
     
@app.route('/profile', methods = ['POST','GET'])   
def profile():



  return render_template('profile.htm');

@app.route('/logout', methods = ['POST','GET'])   
def logOut():
  
  killSession = session.clear();

  return redirect('http://127.0.0.1:5000/',killSession);

if __name__ == '__main__':  
   app.run(debug=True)