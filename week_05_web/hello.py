from flask import Flask, escape

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, world!'


@app.route('/<username>')
def greet(username):
    return 'Hello, {}!'.format(escape(username))
