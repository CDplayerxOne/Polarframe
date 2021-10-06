from flask import Blueprint
from flask import render_template

views = Blueprint(__name__, "views")


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/cdplayerx1")
def cdplayerx1():
    return "hello"
