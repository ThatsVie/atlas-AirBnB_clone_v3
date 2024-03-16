#!/usr/bin/python3
"""
Defines routes for interacting with City objects in the API
"""

from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities_by_state(state_id):
    """
    Retrieves the list of all City objects associated with a State
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities = state.cities
    cities_list = [city.to_dict() for city in cities]
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city_by_id(city_id):
    """
    Retrieves a specific City object by its ID
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_city_by_id(city_id):
    """
    Deletes a City object by its ID
    """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_new_city(state_id):
    """
    Creates a new City object
    """
    city_data = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not city_data:
        abort(400, 'Not a JSON')
    if 'name' not in city_data:
        abort(400, 'Missing name')

    city_data['state_id'] = state_id
    new_city = City(**city_data)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """
    Updates a specific City object by its ID
    """
    city_data = request.get_json()
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not city_data:
        abort(400, 'Not a JSON')

    for key, value in city_data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 200
