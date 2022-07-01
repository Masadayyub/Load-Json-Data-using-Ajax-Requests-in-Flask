from flask import Flask, render_template

lab1 = Flask(__name__)
@lab1.route("/")
def index():  
    return render_template("index.html")