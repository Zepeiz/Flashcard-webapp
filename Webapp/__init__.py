# Initialize pakager file
from enum import unique
import os
import re
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random, copy
from flask_bcrypt import Bcrypt, bcrypt
from flask_login import LoginManager, login_manager
from os import path

DB_NAME = 'database.db'
file_path = os.path.abspath(os.getcwd())+DB_NAME
db = SQLAlchemy()


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path  # Connects with the database
app.config['SECRET_KEY'] = 'f27147030183d991bbcfbb48' #Randomly generated 12bit hexadecimal value

db.init_app(app)

bcrypt = Bcrypt(app) #Hashing passwords in database instead of storing as plain text
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = 'info'
from Webapp import routes 
from Webapp import models

with app.app_context():
    db.create_all()

