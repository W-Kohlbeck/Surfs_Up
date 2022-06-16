# import flask dependency
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# create flask routes


@app.route('/')
def hello_world():
    return 'Hello World'
