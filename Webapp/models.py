from enum import unique
import bcrypt
from sqlalchemy.orm import backref
from Webapp import login_manager
from Webapp import Bcrypt, bcrypt
from Webapp import db
from flask_login import UserMixin #f12 to inspect class


@login_manager.user_loader # @=instances
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=20), nullable=False, unique=True) #Cannot be empty, must be unique
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False) #Two users can have the same password
    flash_card = db.relationship('Flashcard', backref='owner', lazy=True) #lazy=True makes database take all items of the user and return as a list

    @property #Sets the password variable as itself and returns it so that password.setter can take it.
    def password(self):
        return self.password
    
    @password.setter #For converting the password into a hash before storing it to the database
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password): #if the attempted password is the same as the hashed password, return True
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
        

class Flashcard(db.Model):
    flashcard_id = db.Column(db.Integer(), primary_key=True) #primary_key=True automatically sets the id starting from 1 and up incrementally.
    key_phrase = db.Column(db.String(length=1000), nullable=False, unique=True)
    definition = db.Column(db.String(length=1000), nullable=False, unique=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False) #Saves the user id of the owner

    def __repr__(self):
        return f'Flashcards {self.name}' #Makes the columns display as name
