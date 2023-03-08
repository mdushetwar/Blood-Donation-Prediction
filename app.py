# Importing main Libraries
from flask import Flask, render_template, jsonify, request
import pandas
import numpy
import pickle

# Creating Flask app
app= Flask(__name__)

@app.route('/')
def Home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
