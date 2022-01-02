from flask import Flask
from convert import convert

app = Flask(__name__)

@app.route("/")
def root(): 
    return convert()
