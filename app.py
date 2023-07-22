import os
import json
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get('OPENAI_API_KEY')
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", None)

@app.route('/')
@app.route('/index.html')
def welcome_page():
    return render_template('index.html')
