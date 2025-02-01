# -*- coding: utf-8 -*-
"""
Created on Sun May 19 16:26:43 2024

@author: yunteng

pip install Flask

"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__);

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/getRoute/<user>")
def getRouteValue(user):
    return "Hello " + user

@app.route('/shutdown', methods=['POST'])
def shutdown():
    authcode = request.values.get('AUTHCODE')
    if (authcode == 'shutdown'):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        
        return 'Server shutting down...'
    else: 
        return 'Please enter authrization code to stop server'
    
    

@app.route("/getData", methods=['POST'])
def getData():
    data = request.values.get('DATA')
    return "接收到剛剛輸入的"+data

@app.route("/getJSONData", methods=['POST'])
def getJSONData():
    # 根據Content-Type判斷是否為application/json
    if request.is_json:
        data = request.get_json()
        result = data.get('DATA')
    else:
        result = 'None'
    return "接收到剛剛輸入的"+result

@app.route("/responseData", methods=['GET'])
def responseData():
    resdata = {
        'callback': "response data",
        'arraydata': [
            1,
            2,
            'hello'
        ]
    }
    
    return jsonify(resdata)



app.run();