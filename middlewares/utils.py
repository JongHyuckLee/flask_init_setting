# -*- coding: utf-8 -*-
from flask import Flask, abort


class Util:
    def check_get_method(router_function):
        def check(*args, **kwargs):  #1
            if kwargs['method'] == 'GET':
                return router_function(*args, **kwargs)  #2
            else:
                abort(405)
        return check

    def check_post_method(router_function):
        def check(*args, **kwargs):  #1
            if kwargs['method'] == 'POST':
                return router_function(*args, **kwargs)  #2
            else:
                abort(405)
        return check
