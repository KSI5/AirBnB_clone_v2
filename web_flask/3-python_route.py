#!/usr/bin/python3
'''
A simple Flask web application.
'''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
'''The Flask application instance.'''
app.url_map.strict_slashes = False

@app.route('/')
def index():
    '''The home page.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'

@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(escape(text.replace('_', ' ')))

@app.route('/python/')
@app.route('/python/<text>')
def python_page(text='is_cool'):
    '''The python page.'''
    return 'Python {}'.format(escape(text.replace('_', ' ')))

@app.route('/number/<int:n>')
def is_number(n):
    '''Display "n is a number" only if n is an integer.'''
    return '{} is a number'.format(escape(n))

@app.route('/number_template/<int:n>')
def number_template(n):
    '''Display an HTML page with "Number: n" inside an H1 tag in the BODY, if n is an integer.'''
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
