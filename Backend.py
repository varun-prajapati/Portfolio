#pip3 install flask
from flask import Flask, render_template
import os

#when run with python, __name__ is assigned value __main
app = Flask(__name__)

#decorator mapping path '/' to function named home


@app.route("/")
def aboutme():
    return render_template("aboutme.html")

@app.route("/background/")
def background():
    return render_template("background.html")

@app.route("/projects/")
def projects():
    return render_template("projects.html")

@app.route("/academics/")
def academics():
    return render_template("academics.html")

if __name__=="__main__":
    app.run(debug=True)
