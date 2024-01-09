#!/usr/bin/python3

"""
Index file for views
Here all the api routes are stored
and defined
"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def status():
    """
    returns a JSON string: "status": "OK"
    """
    return jsonify({"status": "OK"})

@app_views.route('/stats', strict_slashes=False)
def stats():
    """
    retrieves the number of each objects by type
    """
    from models import storage
    stats = {"amenities": storage.count("Amenity"),
             "cities": storage.count("City"),
             "places": storage.count("Place"),
             "reviews": storage.count("Review"),
             "states": storage.count("State"),
             "users": storage.count("User")}
    return jsonify(stats)
