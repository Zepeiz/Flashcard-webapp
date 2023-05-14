# Flashcard web application built with python flask, SQLAlchemy, and SQLite
A school project made in 2021. A web application with SQLite backend that supports user account registeration, login, and the ability to create, delete, view, and share key:definition flashcards with other users on the platform. <br />
 Currently runs on local host, could be changed in the future and be useful in a classroom setting where the teacher is the host and controls the database, students can each make and manage their own flashcards, while also being able to see all flashcards by other users as well that is stored in the database.
## Installation:
### Windows: 
pip install virtualenv <br />
python -m venv c:\path\to\myenv <br />

## Starting python virtual environment:
### Windows: 
myenv/Scripts/activate <br />

**After the env is running:** <br />
pip install flask <br />
pip install python-dotenv <br />
pip install Flask-SQLAlchemy <br />
pip install email_validator <br />
pip install flask-wtf <br />
pip install flask_bcrypt <br />
pip install flask_login <br />

**Running the server:** <br />
python run.py <br />

# Preview
![Alt text](/readme_Images/homePage.png "Home page") <br />

![Alt text](/readme_Images/register_page.png "Register page") <br />
Password length must be at least 6.
![Alt text](/readme_Images/login_page.png "Login page") <br />

![Alt text](/readme_Images/create_flashcard.png "Create flashcards") <br />

![Alt text](/readme_Images/all_cards.png "See all flashcards") <br />
Here you can see flashcards made by other users.
![Alt text](/readme_Images/database.png "Temporary page to view entire database") <br />
Don't worry, all passwords are encrypted using Bcrypt :)
