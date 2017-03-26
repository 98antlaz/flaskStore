from flask import Flask, render_template, request, url_for
from dbhandler import dbhandler as db

app = Flask(__name__)

"""
TODO:
> Finish modal inputs
> Create a DB handler
> > Connect store.py to DB handler (send and receive data)
> Showcase products in configure
> Add edit/delete functionality
"""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/configure", methods=["GET", "POST"])
def configure():
    products = db().getProducts()
    if(request.method == "POST"):
        if("create" in request.form):
            print(request.form["name"]) #Prints name input value
    return render_template("configure.html", products = products)

if(__name__ == "__main__"):
    app.run()
