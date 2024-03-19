#!/usr/bin/python3
"""
Defines routes for interacting with User objects in the API
"""
from flask import jsonify, request, abort
from models import storage
from models.user import User
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def list_users():
    """
    Retrieves a list of all User objects
    """
    users = []
    for user in storage.all(User).values():
        users.append(user.to_dict())
    return jsonify(users)


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_users_by_id(user_id):
    """
    Retrieves a specific User object by its ID
    """
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user_by_id(user_id):
    """
    Deletes a specific User object by its ID
    """
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({})
    abort(404)


@app_views.route('/users', methods=['POST'], strict_slashes=False)
#  When POST request received, this function will be executed
def create_new_user():
    """
    Creates a new User object
    """
    data = request.get_json(silent=True)
    if not data:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')

    new_user = User(**data)

    storage.new(new_user)
    storage.save()

    #  Return new User object
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """
    Updates a specific User object by its ID
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json(silent=True)
    if not data:
        abort(400, 'Not a JSON')
    #  Remove keys that are ignored
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    #  Returns JSON response with the details of the updated user object
    return jsonify(user.to_dict()), 200
