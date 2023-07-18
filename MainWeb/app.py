#Main code. All this was for testing. But I recommend changing because this might have faulty code
import jinja2
from flask import Flask, flash, redirect, render_template, request, session

# Configs app
app = Flask(__name__)

# I assume the user will be redirected to login page once they enter web. Plz inform me if you decide on something else
@app.route("/")
def index():
    return render_template("index.html")
