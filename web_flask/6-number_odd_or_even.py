#!/usr/bin/python3
'''
A simple Flask web application.
'''
from flask import Flask, render_template

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
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>')
def python_page(text='is_cool'):
    '''
    The python page.
    '''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def is_number(n):
    '''
    Display "n is a number" only if n is an integer.
    '''
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
    '''
    Display an HTML page with "Number: n" inside an H1 tag in the BODY, if n is an integer.
    '''
    return render_template('number_template.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    '''
    Display an HTML page with "Number: n is even|odd" inside an H1 tag in the BODY, if n is an integer.
    '''
    if n % 2 == 0:
        return render_template('number_odd_or_even.html', n=n, result="even")
    else:
        return render_template('number_odd_or_even.html', n=n, result="odd")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
