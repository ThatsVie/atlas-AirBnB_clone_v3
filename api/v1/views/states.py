#!/usr/bin/python3
"""
Defines routes for interacting with State objects in the API
"""

from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def list_states():
    """
    Retrieves all State objects.

    Returns:
        JSON representation of all State objects
    """
    #  Create 'states' dict and places all State objects from state into dict
    states = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_by_id(state_id):
    """
    Retrieves a specific State object by its ID.

    Args:
        state_id (str): The ID of the State object to retrieve.

    Returns:
        JSON representation of the retrieved State object.
        If no State with the given ID is found, returns a 404 error.
    """
    #  Calls get() method and retrieves State obj with given ID
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    #  Convert state's attributes into dict format and returns as JSON response
    return jsonify(state.to_dict())


@app_views.route(
    "/states/<state_id>",
    methods=["DELETE"],
    strict_slashes=False
)
def delete_state_by_id(state_id):
    """
    Deletes a State object by its ID.

    Args:
        state_id (str): The ID of the State object to delete.

    Returns:
        An empty JSON response with status code 200 upon successful deletion.
        If no State with the given ID is found, returns a 404 error.
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    storage.delete(state)
    storage.save()
    #  Converts empty dict into JSON response, returns 'OK' status code
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_new_state():
    """
    Creates a new State object.

    Returns:
        JSON representation of newly created State object with status code 201.
        If request does not contain JSON data or is missing 'name' attribute,
        returns a 400 error.
    """
    #  With addition of silent=True, if request does not contain
    #  valid data, it will return 'None' instead of kicking error
    data = request.get_json(silent=True)
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    #  Create new State obj and passes key/value pairs from 'data' dict
    #  into the State constructor
    new_state = State(**data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """
    Updates a specific State object by its ID.

    Args:
        state_id (str): The ID of the State object to update.

    Returns:
        JSON representation of the updated State object with status code 200.
        If no State with the given ID is found or the request does not contain
        JSON data, returns a 404 or 400 error, respectively.
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, "Not a JSON")
    for key, value in data.items():
        #  Avoids directly modifying specific attributes
        if key not in ["id", "created_at", "updated_at"]:
            #  Sets attributes on new State based on user input
            setattr(state, key, value)
    storage.save()
    return jsonify(state.to_dict()), 200
