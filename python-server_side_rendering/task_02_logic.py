#!/usr/bin/python3#!/usr/bin/python3
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def item():
    with open('items.json') as j_file:
        data = json.load(j_file)
        list_items = data.get("items", [])

    return render_template('items.html', items=list_items)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)