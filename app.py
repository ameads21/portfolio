from flask import Flask, request
from flask_debugtoolbar import DebugToolbarExtension
import os
from flask_sslify import SSLify
from routes.home import home

app = Flask(__name__)
app.register_blueprint(home)

if 'DYNO' in os.environ:
    sslify = SSLify(app)