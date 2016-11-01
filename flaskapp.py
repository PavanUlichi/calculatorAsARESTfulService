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

@app.route('/api/sub', methods=['GET'])
def get_sub():
    a = request.args.get('num1')
    a = int(a)
    b = request.args.get('num2')
    b = int(b)
    c = a-b
    return jsonify({"difference": c})

@app.route('/api/mul', methods=['GET'])
def get_mul():
    a = request.args.get('num1')
    a = int(a)
    b = request.args.get('num2')
    b = int(b)
    c = a*b
    return jsonify({"product": c})

@app.route('/api/div', methods=['GET'])
def get_div():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    c = a/b
    return jsonify({"ratio": c})

@app.route('/api', methods=['GET'])
def get_opr():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    o = request.args.get('opp')
    if(o == 'add'):
        c = a+b
    elif(o == 'sub'):
        c = a-b
    elif(o == 'mul'):
        c = a*b
    else:
        c = a/b
    return jsonify({"result": c})
    
if __name__ == '__main__':
        app.run()

