"""Main module for the application."""
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://maija:risla47@localhost/ohtu'
app.config['SECRET_KEY'] = 'sjdiwbfkewndpw556802jdwbdqdwp'
import routes  # nopep8
