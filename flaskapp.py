#!/usr/bin/python
from flask import Flask, jsonify, render_template, request
from flask import abort


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_tasks():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

