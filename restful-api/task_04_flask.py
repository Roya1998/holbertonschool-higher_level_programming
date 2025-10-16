#!/usr/bin/python3
"""A simple RESTful API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage
users = {}


@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    """Status check endpoint."""
    return "OK"


@app.route('/data')
def get_usernames():
    """Return a list of all usernames."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/users/<username>')
def get_user(username):
    """Return user data by username."""
    if username in users:
        return jsonify(users[username])
    else:
        response = jsonify({"error": "User not found"})
        response.status_code = 404
        return response


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user from JSON data."""
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Invalid JSON")
    except Exception:
        response = jsonify({"error": "Invalid JSON"})
        response.status_code = 400
        return response

    username = data.get("username")

    if not username:
        response = jsonify({"error": "Username is required"})
        response.status_code = 400
        return response

    if username in users:
        response = jsonify({"error": "Username already exists"})
        response.status_code = 409
        return response

    # Store user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    response = jsonify({
        "message": "User added",
        "user": users[username]
    })
    response.status_code = 201
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)