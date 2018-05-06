from flask import Flask, abort, render_template, request
from werkzeug.routing import BaseConverter

import os, glob, sys, importlib


app = Flask(__name__)


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route('/')
def index():
    return "test"


@app.route('/<regex("[\S]{0,12}"):dirs>/', methods=['GET'])
def mapping_dirs(dirs):
    directories = [os.path.basename(directory) for directory in glob.glob('%s/%s/*' % (app.root_path, 'routes'))
                   if os.path.isdir(directory)]
    if dirs in directories:
        module_from = 'routes.%s.%s_route' % (dirs, dirs)
        module = importlib.import_module(module_from)

        return getattr(module, 'index')()
    else:
        abort(404)


@app.route('/<regex("[\S]{0,12}"):dirs>/<regex("[\S]{0,12}"):route>/', methods=['GET', 'POST'])
def mapping_routes(dirs, route):

    directories = [os.path.basename(directory) for directory in glob.glob('%s/%s/*' % (app.root_path, 'routes'))
                   if os.path.isdir(directory)]
    if dirs in directories:
        module_from = 'routes.%s.%s_route' % (dirs, dirs)
        module = importlib.import_module(module_from)
        routes = [route for route in dir(module) if '__' not in route]
        if route not in routes:
            abort(400)
        return getattr(module, route)(method=request.method)
    else:
        abort(404)


@app.route('/<regex("[\S]{0,12}"):dirs>/<regex("[\S]{0,12}"):route>/<regex("[\S]{0,12}"):param>/', methods=['GET', 'POST'])
def mapping_param(dirs, route, param):

    directories = [os.path.basename(directory) for directory in glob.glob('%s/%s/*' % (app.root_path, 'routes'))
                   if os.path.isdir(directory)]
    if dirs in directories:
        module_from = 'routes.%s.%s_route' % (dirs, dirs)
        module = importlib.import_module(module_from)
        routes = [route for route in dir(module) if '__' not in route]
        if route not in routes:
            abort(400)

        return getattr(module, route)(param, method=request.method)
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
