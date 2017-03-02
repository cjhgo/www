#coding: utf-8
#created at 17-3-2 11:12

from flask import Flask
from flask.templating import render_template
from settings import API_HOST

app = Flask(__name__, template_folder="templates")


@app.template_global(name="api_host")
def api_host():
    return API_HOST


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/keywords")
def keywords():
    return render_template("keywords.html")

if __name__ == "__main__":
    app.run(port=7000, debug=True)