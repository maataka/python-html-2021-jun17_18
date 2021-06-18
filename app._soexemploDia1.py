from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World PY dia 2 parte da tarde"