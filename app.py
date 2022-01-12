import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import pandas as pd

#app = Flask(__name__, static_url_path='/C:/Users/v-jakodw/Downloads/HTML_Kit/static')
#app = Flask(__name__, static_url_path='/static')
app = Flask(__name__)

@app.route('/')
def home():
    #return 'Hello World'
    return render_template('home.html')
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    return 'Hello World'   
  

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.get_json(force=True)   

    output = 'Hello World'  
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)