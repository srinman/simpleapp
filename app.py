import os
import json
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/')
@app.route('/index.html')
def welcome_page():
    return render_template('indexv1.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')