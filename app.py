from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/recruitment", methods=["GET", "POST"])
def recruitment():
    return render_template("recruitment.html")