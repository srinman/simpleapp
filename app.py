import os
import json
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/index.html')
def welcome_page():
    return render_template('index.html')
