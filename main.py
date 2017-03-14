#coding: utf-8
#created at 17-3-2 11:12

import json
from flask import Flask, request
from flask.templating import render_template
from settings import API_HOST

app = Flask(__name__, template_folder="templates")


@app.template_global(name="api_host")
def api_host():
    return API_HOST


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/keywords")
def keywords():
    return render_template("keywords.html")

@app.route("/coder")
def coder():
    return render_template("coder.html")

@app.route("/temp")
def temp():
    return render_template("temp.html")


@app.route("/notes")
def notes():
    return render_template("notes.html")

if __name__ == "__main__":
    app.run(port=7000, debug=True)