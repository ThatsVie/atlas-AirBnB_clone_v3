#!/usr/bin/python3
"""
Defines routes for interacting with 'Place' objects in the API
"""
from flask import jsonify, request, abort
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
def get_places_by_city(city_id):
    """
    Retrieves the list of all Place objects associated with a City
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    #  Retrieve all place objects associated with city_id
    #  Creates list of dictionaries of each place object
    places = [place.to_dict() for place in city.places]
    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'],
                 strict_slashes=False)
def get_places_by_id(place_id):
    """
    Retrieves a Place object based off of its place ID
    """
    place = storage.get(Place, place_id)
    if place:
        return jsonify(place.to_dict())
    abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place_by_id(place_id):
    """
    Deletes a specific Place object based off its ID
    """
    place = storage.get(Place, place_id)
    if place:
        storage.delete(place)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
def create_new_place(city_id):
    """
    Creates a new Place object associated with a City
    """
    #  Retrieve proper City object of which new Place object
    #  will be associated
    city = storage.get(City, city_id)
    if city is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, 'Not a JSON')

    required_attributes = ['user_id', 'name']
    for attribute in required_attributes:
        if attribute not in data:
            #  If user_id or name missing from JSON data, will return error
            abort(400, f'Missing {attribute}')

    user_id = data['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)

    new_place = Place(**data)
    #  Assign city_id extracted from URL parameter
    new_place.city_id = city_id
    storage.new(new_place)
    storage.save()

    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """
    Updates the attributes of a Place based on its ID
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    data = request.get_json(silent=True)
    if not data:
        abort(400, 'Not a JSON')

    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)

    storage.save()

    return jsonify(place.to_dict()), 200
