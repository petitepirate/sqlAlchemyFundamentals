"""Demo app using SQLAlchemy."""

from flask_debugtoolbar import DebugToolbarExtension
from flask import Flask, request, redirect, render_template
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/")
def list_pets():
    """List pets and show add form."""

    pets = Pet.query.all()
    return render_template("list.html", pets=pets)
