from flask import Flask, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import os
from flask_sslify import SSLify
from routes.home import home

app = Flask(__name__)
app.register_blueprint(home)
app.config['SECRET_KEY'] = os.environ.get('SECRET-KEY', 'This is a secret key')

if 'DYNO' in os.environ:
    sslify = SSLify(app)
