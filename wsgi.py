from flask import Flask, render_template, request

DEBUG = True

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("request.py")


@app.route("/todo", methods=["POST"])
def add_todo():
    items = request.form.values()
    return render_template("login.html", items=items)


@app.route("/todo", methods=["GET"])
def todo():
    return render_template("login.html")

