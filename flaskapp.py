#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from flask import abort
from flask import Response

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/', methods=['GET','POST'])
def get_tasks():
    return render_template('index.html')

@app.route('/api/rsdl', methods=['GET'])
def get_xml():
    xml = render_template('READ.xml')
    return Response(xml, mimetype='text/xml')

@app.route('/api/add', methods=['GET','POST'])
def get_add():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    c = a+b
    return jsonify({"result": c})

@app.route('/api/sub', methods=['GET','POST'])
def get_sub():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    c = a-b
    return jsonify({"result": c})

@app.route('/api/mul', methods=['GET','POST'])
def get_mul():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    c = a*b
    return jsonify({"result": c})

@app.route('/api/div', methods=['GET','POST'])
def get_div():
    a = request.args.get('num1')
    a = float(a)
    b = request.args.get('num2')
    b = float(b)
    c = a/b
    return jsonify({"result": c})
    
if __name__ == '__main__':
        app.run()

