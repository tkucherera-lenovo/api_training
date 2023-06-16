'''
Author: tkucherera
api implimantation 
check scalability 
'''


from flask import Flask, json, request
from flask_cors import CORS
from  redis_caching import Cache 
import time
from utilities.power import get_node_total_power

app = Flask(__name__)
CORS(app)
caching = Cache()  
        

@app.route("/api/v1")
def home():  
    # try to cache the info if it is the first time 
    try:
        response_line = caching.read("tom")
        if response_line is None:
            no_cache = True
        else:
            response_line = 'cache:  ' + response_line
            no_cache = False
    except:
        no_cache = True

    # read the text file
    if no_cache:
        with open('data.txt', mode='r') as f:
            lines = f.readlines()
            response_line = lines[0]
        caching.write("tom", response_line)
        response_line = lines[0]
        no_cache = False
    response = app.response_class(
        response=json.dumps(response_line),
        status=200,
        mimetype='application/json',
    )
    return response

@app.route('/api/v1/temperature', methods=['GET','POST'])
def temperature(temp):
    if request.method == "POST":
        return ""
    
    elif request.method == "GET":
        return ""
    else:
        pass 

@app.route("/api/v1/humidity", methods=['GET', 'POST'])
def humidity(hum):
    if request.method == "POST":
        return ""
    
    elif request.method == "GET":
        return ""
    else:
        pass 

@app.route("/api/v1/power/<node>", methods=['GET', 'POST'])
def power(node):
    if request.method == "POST":
        return ""
    
    elif request.method == "GET":
        node_tot_power = get_node_total_power(node)
        response = app.response_class(
        response=json.dumps(node_tot_power),
        status=200,
        mimetype='application/json',
    )
        return response
    else:
        pass 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)