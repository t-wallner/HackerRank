""" Bottle is a fast, simple and lightweight micro web-framework for Python. It is distributed as a single file module
    and has no dependencies other than the Python Standard Library.
    Run this script or paste it into a Python console,
    then point your browser to http://localhost:8080/hello/world. That’s it."""

from bottle import get, post, run, template

# These are all GETS by default
@get('/')
def _route():
    return '<h3> Welcome to my first web page made with bottle</h3>'


@get('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@get('/login')
def login():
    return '<div> On Login Page </div>'


@get('/article/<id>')
def article(id):
    return '<h3> You are viewing article {} </h3>'.format(id)

# These are POST
@post('/posted')
def do_post():
    return '<p>Testing post.</p>'


if __name__ == "__main__":
    run(host='localhost', port=8080)