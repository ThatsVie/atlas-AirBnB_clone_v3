#!/usr/bin/python3
"""Main module for the API"""

from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# Register blueprint for API endpoints
app.register_blueprint(app_views)

# Enable CORS
# Specifies the URL paths for which CORS should be enabled
# Enabled for all resources and allows requests from any origin
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.errorhandler(404)
def handle_not_found_error(error):
    """
    Handle 404 Not Found errors
    """
    #  Ensures that 404 status code on error is JSON-formatted
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown(exception):
    """
    Close the SQLAlchemy session after each request
    """
    storage.close()


if __name__ == "__main__":
    # Run the API application
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", 5000))
    app.run(host=host, port=port, threaded=True)
