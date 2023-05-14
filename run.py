# python run.py to start webapp
# run.py has pakaged everything together
from logging import debug
from Webapp import app
#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)