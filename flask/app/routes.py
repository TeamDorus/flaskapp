from flask import render_template, url_for, redirect, flash
from app import app
import os



@app.route("/")
@app.route("/home/")
def index():
    return render_template("index.html", active="Home")




@app.route("/test/")
def test():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")
    if app_name:
        outstr = f"Hello from {app_name} running in a Docker container behind Nginx!"
    else:
        outstr = "Hello from Flask"

    return render_template("test.html", active="Test", msg=outstr)







