'''
Author: tkucherera
'''


from flask import Flask, json 
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/v1")
def home():
    response = app.response_class(
        response=json.dumps("Welcome Tinashe"),
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)