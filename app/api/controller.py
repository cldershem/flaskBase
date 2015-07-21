#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
api.controller.py
~~~~~~~~~~~~~~~~~

Controller for the api

:copyright: (c) 2015 by Cameron Dershem.
:license: see TOPMATTER
:source: github.com/cldershem/$SOME_REPO
"""
from flask import Blueprint, jsonify


mod = Blueprint('api', __name__, url_prefix='/api/v1/')


class Response():
    """
    """
    def __init__(self, success=False, data=None, error=None):
        self.success = success
        self.data = data
        self.error = error

    def to_json(self):
        return jsonify(self.__dict__)

    def __repr__(self):
        return "<Response success={}, data={}, error={}>".format(
            self.success, self.data, self.error)


@mod.route('/')
def api():
    result = Response(
        success=False,
        error="API not yet implemented"
        )
    return result.to_json()
