from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment
VALID_API_KEY = os.getenv('VALID_API_KEY')

# Middleware for authenticating the API key
@app.before_request
def authenticate_api_key():
    # Skip authentication for specific routes like '/ping'
    if request.endpoint == 'ping':
        return
    
    # Check if the API key is passed in the payload or headers
    api_key = request.headers.get("X-API-Key")

    # If the API key is missing or invalid
    if api_key != VALID_API_KEY:
        return jsonify({"error": "unauthorized"}), 401


# Not authenticated route
@app.route('/ping')
def ping():
    return "", 200

# Authenticated route with an empty body and 200 status code
@app.route('/test-auth')
def test_auth():
    return "", 200

# Authenticated route with a JSON response and 200 status code
@app.route('/test-auth-response')
def test_auth_response():
    return jsonify({"message": "hello world"}), 200

if __name__ == '__main__':
    app.run(debug=True)
