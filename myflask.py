
from flask import Flask #Import the Flask package

#Make an instance of the Flask class and store it in the variable 'app' 
app = Flask(__name__)

#Tell 'app' that its root folder is "/". This means that the URL of the root application is http://localhost:5000 
@app.route('/')

#myflask() is the function that will be called at http://localhost:5000 
def myflask():
  #All that myflask() does is return a string. The browser will put it on the screen.                   
  return 'My first Flask application' 

