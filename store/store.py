from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/configure")
def configure():
    return render_template("configure.html")

if(__name__ == "__main__"):
    app.run()
