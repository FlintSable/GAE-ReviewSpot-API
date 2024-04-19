from flask import request, jsonify
from models import Business, Review

@app.route('/businesses', methods=['POST'])
def create_business():
    data = request.json
    business = Business.create(data)
    return jsonify(business), 201

@app.route('/businesses/<int:business_id>', methods=['GET'])
def get_business(business_id):
    business = Business.get(business_id)
    if business:
        return jsonify(business), 200
    else:
        return jsonify({'Error': 'No business with this business_id exists'}), 404

@app.route('/businesses', methods=['GET'])
def list_businesses():
    businesses = Business.list()
    return jsonify(businesses), 200

@app.route('/businesses/<int:business_id>', methods=['PUT'])
def update_business(business_id):
    data = request.json
    business = Business.update(business_id, data)
    if business:
        return jsonify(business), 200
    else:
        return jsonify({'Error': 'No business with this business_id exists'}), 404

@app.route('/businesses/<int:business_id>', methods=['DELETE'])
def delete_business(business_id):
    Business.delete(business_id)
    return '', 204

# Implement routes for reviews similarly
