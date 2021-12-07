import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nonfiction")
def nonfic():
    return render_template("nonfic.html")


@app.route("/fantasy")
def fantasy():
    return render_template("fantasy.html")


@app.route("/philosophy")
def philosophy():
    return render_template("philosophy.html")


@app.route("/mystery")
def mystery():
    return render_template("mystery.html")


@app.route("/shop")
def shop():
    return render_template("shop.html")


if __name__ == "__main__":
    app.run(
        host = os.environ.get("IP", "0.0.0.0"),
        port = int(os.environ.get("PORT", "5000")),
        debug = True)