#!/usr/bin/python3

from flask import Blueprint, jsonify
from api.v1.views.index import *
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/status', strict_slashes=False)
def status():
    """
    returns a JSON string: "status": "OK"
    """
    return jsonify({"status": "OK"})
