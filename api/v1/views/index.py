#!/usr/bin/python3
"""
This module defines endpoints for retrieving API status and statistics
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def api_status():
    """
    Retrieve the status of the API

    Returns:
        JSON response indicating the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def api_stats():
    """
    Retrieve statistics about the API

    Returns:
        JSON response containing statistics for each model class
    """
    model_classes = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }

    stats = {key: storage.count(value) for key, value in model_classes.items()}
    return jsonify(stats)
