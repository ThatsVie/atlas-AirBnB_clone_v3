#!/usr/bin/python3
"""
Defines routes for interacting with 'Review' objects in the API
"""
from flask import jsonify, request, abort
from models import storage
from models.review import Review
from models.place import Place
from models.user import User
from api.v1.views import app_views

@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews_by_place(place_id):
    """
    Retrieves list of all Review objects associated with given Place
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    
    reviews = [reviews.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_review_by_id(review_id):
    """
    Retreives single Review object based on its ID
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id', methods=['DELETE'],
                 strict_slashes=False)
def delete_review_by_id(review_id):
    """
    Deletes a specific Review object based on its ID
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_new_review(place_id):
    """
    Creates new Review object associated with a given Place
    """
    place = storage.get(Place, place_id)
    if Place is None:
        abort(404)
    
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    
    required_attributes = ['user_id', 'text']
    for attribute in required_attributes:
        if attribute not in data:
            abort(400, f'Missing {attribute}')

    #  Retrieve user associated with given user_id from storage
    user_id = data['user_id']
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    
    new_review = Review(**data)
    #  Assign place_id extracted from URL
    new_review.place_id = place_id
    storage.new(new_review)
    storage.save()

    return jsonify(new_review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_review(review_id):
    """
    Updates the attributes of a Rebiew based on its ID
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    
    storage.save()

    return jsonify(review.to_dict()), 200
    
