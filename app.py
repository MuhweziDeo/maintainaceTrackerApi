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
@app.route('/signup')
def signup():
 	return render_template('signup.html')

@app.route('/login')
def login():
 	return render_template('login.html')

@app.route('/make_request')
def make_request():
	return render_template('make_request.html')

@app.route('/user_requests')
def user_requests():
	return render_template('user_requests.html')

#admin routes
@app.route('/requests')
def requests():
 	return render_template('requests.html')
@app.route('/resolve')
def resolve():
 	return render_template('resolve.html')

 # api endpoints
 
# USERS

@app.route('/api/v1/users/requests', methods=['GET'])
def get_all_requests():
	# get all requests of logged in users
	return ''

@app.route('/api/v1/users/requests/<request_id>', methods=['GET'])
def get_one_request(request_id):
	# get a single request
	return ''

@app.route('/api/v1/users/request', methods=['POST'])
def create_request():
	# create a request
	data=request.get_json()
	
	return ''

@app.route('/api/v1/users/requests/<request_id>', methods=['PUT'])
def modify_request(request_id):
	# modify a request
	return ''











if __name__=='__main__':
	db.create_all()
	app.run(debug=True)