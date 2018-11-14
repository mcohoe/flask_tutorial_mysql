from datetime import datetime
from flaskblog import login_manager
from flask_login import UserMixin
from flask import flash
import pymysql

@login_manager.user_loader
def load_user(user_id):
    user = User('','','')
    user.get_user_by_id(user_id)
    return user

class User(UserMixin):

	id = -1
	username = ''
	email = ''
	image_file = ''
	password = ''
	
	def __init__(self, username, email, password):
	    self.id = -1
	    self.username = username
	    self.email = email
	    self.image_file = 'default.jpg'
	    self.password = password
		
	def get_user_by_email(self, email):
	    conn = pymysql.connect(host='localhost', port=3306, user='flaskblog_user', passwd='test', db='flaskblog_db')
	    cur = conn.cursor()
	    cur.execute("SELECT * FROM users WHERE email = %s", (email))
	    data = cur.fetchall()
	    if data:
		    self.id = data[0][0]
		    self.username = data[0][1]
		    self.email = email
		    self.image_file = data[0][3]
		    self.password = data[0][4]
	    else:
		    self.id = -1
		    self.username = ''
		    self.email = ''
		    self.image_file = ''
		    self.password = ''
			
	def get_user_by_id(self, id):
	    conn = pymysql.connect(host='localhost', port=3306, user='flaskblog_user', passwd='test', db='flaskblog_db')
	    cur = conn.cursor()
	    cur.execute("SELECT * FROM users WHERE id = %s", (id))
	    data = cur.fetchall()
	    if data:
		    self.id = data[0][0]
		    self.username = data[0][1]
		    self.email = data[0][2]
		    self.image_file = data[0][3]
		    self.password = data[0][4]
	    else:
		    self.id = -1
		    self.username = ''
		    self.email = ''
		    self.image_file = ''
		    self.password = ''
			
	def get_user_by_username(self, username):
		conn = pymysql.connect(host='localhost', port=3306, user='flaskblog_user', passwd='test', db='flaskblog_db')
		cur = conn.cursor()
		cur.execute("SELECT * FROM users WHERE username = %s", (username))
		data = cur.fetchall()
		if data:
			self.id = data[0][0]
			self.username = username
			self.email = data[0][2]
			self.image_file = data[0][3]
			self.password = data[0][4]
		else:
		    self.id = -1
		    self.username = ''
		    self.email = ''
		    self.image_file = ''
		    self.password = ''
	
	def add_user(self):
	    conn = pymysql.connect(host='localhost', port=3306, user='flaskblog_user', passwd='test', db='flaskblog_db')
	    cur = conn.cursor()
	    cur.execute("SELECT MAX(id) FROM users")
	    data = cur.fetchall()
	    if data[0][0]:
		    id = data[0][0] + 1
	    else:
		    id = 1
	    cur.execute("INSERT INTO users(id, username, email, image_file, password) VALUES(%s, %s, %s, %s, %s)", (id, self.username, self.email, self.image_file, self.password))
	    conn.commit()
		



   
