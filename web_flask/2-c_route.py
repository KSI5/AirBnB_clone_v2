#!/usr/bin/python3
'''
A simple Flask web application.
'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    '''
    The home page.
    '''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''
    The hbnb page.
    '''
    return 'HBNB'

@app.route('/c/<text>')
def c_page(text):
    '''
    The c page.
    '''
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))

@app.route('/python/')
@app.route('/python/<text>')
def python_page(text='is_cool'):
    '''
    The python page.
    '''
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
