# -*- coding: utf-8 -*-
from flask import Flask, abort, render_template
from werkzeug.routing import BaseConverter
from middlewares.utils import Util


def index():
    return render_template('users/index.html')


@Util.check_get_method #1
def sign_in(method):
    return 'test'


@Util.check_post_method #1
def sign_up(method=''):
    return 'test'


