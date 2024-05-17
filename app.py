from flask import Flask,request

from controllers.summarize import summarize
from controllers.classification import classifications
from controllers.extractText import extract
from controllers.ranking import ranking

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Flask server running"

@app.route('/extract',methods=['POST'])
def extractText():
    return extract(request)

@app.route('/summarize',methods=['POST'])
def summarize_route():
    return summarize(request)

@app.route('/categorize',methods=['POST'])
def classify_route():
    return classifications(request)

@app.route('/rank',methods=['POST'])
def rank_route():
    return ranking(request)