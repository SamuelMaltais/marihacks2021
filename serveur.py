from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.run(environ.get('PORT'))

@app.route("/")
def home():
    return ren
@app.route("/getfoodbanks")
def 