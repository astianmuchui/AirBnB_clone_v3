#!/usr/bin/python3

"""
Index file for views
"""

from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    """
    returns a JSON string: "status": "OK"
    """
    return jsonify({"status": "OK"})
