#!/usr/bin/python3
"""
Defines routes for interacting with Amenity objects in the API
"""

from flask import jsonify, abort, request
from models import storage
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def list_amenities():
    """
    Retrieves the list of all Amenity objects
    """
    amenities = []
    for amenity in storage.all(Amenity).values():
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenity_by_id(amenity_id):
    """
    Retrieves a specific Amenity object by its ID
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        return jsonify(amenity.to_dict())
    #  if amenity not found based on ID, abort with 404 error
    abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity_by_id(amenity_id):
    """
    Deletes a specific Amenity object by its ID
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity:
        storage.delete(amenity)
        storage.save()
        #  Converts empty dict into JSON response
        return jsonify({})
    abort(404)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_new_amenity():
    """
    Creates a new Amenity object
    """
    #  When server receives requset, it will execute function
    #  and create new Amenity object based on extracted data
    data = request.get_json(silent=True)
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    #  Create new instance of 'Amenity'
    #  Sets attributes based on key-value pairs in data dict
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def update_amenity(amenity_id):
    """
    Updates a specific Amenity object by its ID
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200
