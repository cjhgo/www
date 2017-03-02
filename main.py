#coding: utf-8
#created at 17-3-2 11:12

from flask import Flask
from flask.templating import render_template


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=7000, debug=True)