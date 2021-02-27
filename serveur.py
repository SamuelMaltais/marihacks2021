from os import environ
from flask import Flask, render_template

app = Flask(__name__)
app.run(environ.get('PORT'))

@app.route("/")
def home():
    return render_template(index.html)
@app.route("/getfoodbanks")
def 