from flask import Flask, request,jsonify,render_template,flash,session
from werkzeug.security import check_password_hash,generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
# import jwt
import uuid
import datetime

 

app = Flask(__name__)
app.config['SECRET_KEY']="thisisecreys"
db =SQLAlchemy(app)



#user interfaces 
@app.route('/')
def index():
	return "Hello World"
#user routes
@app.route('/api/v1')
def signup():
 	return render_template('signup.html')

@app.route('/api/v2')
def login():
 	return render_template('login.html')

@app.route('/api/v3')
def make_request():
	return render_template('make_request.html')

@app.route('/api/v4')
def user_requests():
	return render_template('user_requests.html')
#admin routes
@app.route('/api/v5')
def requests():
 	return render_template('requests.html')
@app.route('/api/v6')
def resolve():
 	return render_template('resolve.html')

 # api endpoints













if __name__=='__main__':
	db.create_all()
	app.run(debug=True)