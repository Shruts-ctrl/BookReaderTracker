#from crypt import methods
from crypt import methods
import os
from flask import Flask, url_for, redirect
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null
import jinja2 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///datadb.sqlite3"
db= SQLAlchemy()
db.init_app(app)
app.app_context().push()

@app.route('/', methods= ["GET", "POST"])
def home():
    return render_template("login.html")

@app.route('/<string:username>/home', methods= ["GET", "POST"])
def dashboard():
    if request.method== 'GET':
        return render_template("dashboard.html")

    if request.method== 'POST':
        pass

if __name__ == '__main__':
    print("Working")
    app.run(host="0.0.0.0", port= 8080, debug= True)
