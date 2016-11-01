#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from flask import abort


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    return render_template('index.html')

@app.route('/api/add', methods=['GET'])
def get_add():
    a = request.args.get('num1')
    a = int(a)
    b = request.args.get('num2')
    b = int(b)
    c = a+b
    return jsonify({"sum": c})
    
if __name__ == '__main__':
        app.run()

