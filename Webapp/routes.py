from flask.helpers import flash
import flask_login
from flask_login import login_manager
from flask_login.login_manager import LoginManager
from flask_login.utils import login_required
from sqlalchemy.orm import backref, relationship
from Webapp.forms import CardForm, RegisterForm, LoginForm, CreateCardForm
from logging import debug

from flask_wtf import form
from Webapp import app, db
from flask import render_template, redirect, url_for, flash, request
from Webapp.models import Flashcard, User
from Webapp import random, copy
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    item_to_delete = Flashcard.query.get_or_404(id)

    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect(url_for("flashcards_page"))
    except:
        print("Failed to delete flashcard")


@app.route("/quiz1", methods=["GET", "POST"])
@login_required
def quiz_page():
    card_form = CardForm()
    users = User.query.all()
    data_b= Flashcard.query.all()
    create_form = CreateCardForm()
    if card_form.validate_on_submit():  # Validate when user presses submit button
        new_card = Flashcard(
            key_phrase=card_form.key_phrase.data, definition=card_form.definition.data, user_id = current_user.id
        )
        db.session.add(new_card)  # Send to database, user section
        db.session.commit()

        print(current_user.id) #Outputs what flashcard the user has added
        #p_item_object = User.query.filter_by(id=purchased_item).first
       # if p_item_object:
          #  p_item_object.user_id = current_user.id
        flash("New flashcard succesfully added!", category="success")
        return redirect(url_for("quiz_page"))
    return render_template("quiz_page.html", card_form=card_form, data_b = data_b, users = users, create_form = create_form)


@app.route("/test")
def test_page():
    flashcards = Flashcard.query.all()
    users = User.query.all()
    return render_template("test.html", flashcards=flashcards, users=users)


@app.route("/flashcards")
@login_required
def flashcards_page():
    flashcards = Flashcard.query.filter_by(user_id=current_user.id)
    return render_template("flashcards.html", flashcards=flashcards)

@app.route("/allcards")
def allcards_page():
    flashcards = Flashcard.query.all()
    users = User.query.all()
    return render_template("allcards.html", flashcards=flashcards, users = users)

@app.route("/register", methods=["GET", "POST"])  # methods allows to submit
def register_page():
    form = RegisterForm()  # imported from forms.py
    if form.validate_on_submit():  # Validate when user presses submit button
        user_to_create = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data,
        )

        db.session.add(user_to_create)  # Send to database, user section
        db.session.commit()
        flash("Account succesfully created!", category="success")
        return redirect(url_for("login_page"))
    if form.errors != {}:  # If there are no errors from validations
        for error_message in form.errors.values():
            flash(
                "There was an error with the entered data: {}".format(error_message),
                category="danger",
            )  # Flash method allows the message to be displayed on a HTML page
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(
                "Login Successful! You are logged in as: {}".format(
                    attempted_user.username
                ),
                category="success",
            )  # category="success" creates a light green box
            return redirect(url_for("home_page"))
        else:
            flash(
                "Username or Password is incorrect, please try again.",
                category="danger",
            )  # category="danger" creates a light red box
    return render_template("login.html", form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("home_page"))
