from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from converter import TextToMorse
import requests

app = Flask(__name__)
cv = TextToMorse()
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/convert", methods=['POST'])
def convert():
    text = request.form["text"]
    morse = cv.converter(text)
    return f"<h1>{morse}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
