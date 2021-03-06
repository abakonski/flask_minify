from sys import path as sys_path
from os import path
from importlib import import_module
from flask import Flask

from .constants import HTML, JS, LESS, FALSE_LESS, JS_WITH_TYPE


sys_path.append(path.dirname(path.dirname(__file__)))
module = import_module('flask_minify')
minify = module.minify
decorator = module.decorators.minify


app = Flask(__name__)
store_minify = minify(app=app, fail_safe=False)


@app.route('/html')
def html():
    return HTML


@app.route('/bypassed')
def bypassed():
    return HTML


@app.route('/js')
def js():
    return JS


@app.route('/js_with_type')
def js_with_type():
    return JS_WITH_TYPE


@app.route('/cssless')
def cssless():
    return LESS


@app.route('/js/<addition>')
def js_addition(addition=None):
    return '''<script>
        ["J", "S"].reduce(
            function (a, r) {
                return a + r
            })
    ''' + (addition + '\n</script>')


@app.route('/cssless_false')
def cssless_false():
    return FALSE_LESS


@app.route('/html_decorated')
@decorator(html=True)
def html_decorated():
    return HTML


@app.route('/js_decorated')
@decorator(html=True, js=True)
def js_decorated():
    return JS


@app.route('/less_decorated')
@decorator(html=True, cssless=True)
def less_decorated():
    return LESS
