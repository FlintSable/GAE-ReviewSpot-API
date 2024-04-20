from flask import request, jsonify
from models import Business, Review

def register_routes(app):

    @app.route('/owners/<int:owner_id>/businesses', methods=['GET'])
    def list_businesses_for_owner(owner_id):
        businesses = Business.list_by_owner(owner_id)
        if businesses is None:
            return jsonify({"Error": "No businesses found for this owner"}), 404
        return jsonify(businesses), 200

    @app.route('/businesses', methods=['POST'])
    def create_business():
        required_fields = ['owner_id', 'name', 'street_address', 'city', 'state', 'zip_code']
        data = request.get_json()

        if not data or not all(field in data for field in required_fields):
            return jsonify({"Error": "The request body is missing at least one of the required attributes"}), 400
        
        business_id, new_business = Business.create(data)
        response_data = {
            'id': business_id,
            'owner_id': new_business['owner_id'],
            'name': new_business['name'],
            'street_address': new_business['street_address'],
            'city': new_business['city'],
            'state': new_business['state'],
            'zip_code': new_business['zip_code']
        }
        return jsonify(response_data), 201

    @app.route('/businesses/<int:business_id>', methods=['GET'])
    def get_business(business_id):
        business = Business.get(business_id)
        if business is None:
            return jsonify({'Error': 'No business with this business_id exists'}), 404
        return jsonify(business), 200

    @app.route('/businesses', methods=['GET'])
    def list_businesses():
        businesses = Business.list()
        return jsonify(businesses), 200

    @app.route('/businesses/<int:business_id>', methods=['PUT'])
    def update_business(business_id):
        required_fields = ['owner_id', 'name', 'street_address', 'city', 'state', 'zip_code']
        data = request.json

        if not all(field in data for field in required_fields):
            return jsonify({"Error": "The request body is missing at least one of the required attributes"}), 400

        # Assuming there is a function in models.py to handle the update
        success = Business.update(business_id, data)
        if not success:
            return jsonify({"Error": "No business with this business_id exists"}), 404

        return jsonify(data), 200

    @app.route('/businesses/<int:business_id>', methods=['DELETE'])
    def delete_business(business_id):
        success = Business.delete(business_id)
        if not success:
            # Business not found, return 404
            return jsonify({"Error": "No business with this business_id exists"}), 404
        # Business found and deleted, return 204
        return '', 204

    @app.route('/reviews', methods=['POST'])
    def create_review():
        data = request.get_json()
        required_fields = ['user_id', 'business_id', 'stars']

        if not all(field in data for field in required_fields):
            return jsonify({"Error": "The request body is missing at least one of the required attributes"}), 400
        
        if not Business.exists(data['business_id']):
            return jsonify({"Error": "No business with this business_id exists"}), 404

        # Additional validation to check if a review already exists
        if Review.exists(data['user_id'], data['business_id']):
            return jsonify({"Error": "You have already submitted a review for this business. You can update your previous review, or delete it and submit a new review"}), 409

        review_id = Review.create(data)
        return jsonify({
            "id": review_id,
            "user_id": data['user_id'],
            "business_id": data['business_id'],
            "stars": data['stars'],
            "review_text": data.get("review_text", "")  # Optional field
        }), 201

    @app.route('/reviews/<int:review_id>', methods=['GET'])
    def get_review(review_id):
        review = Review.get(review_id)
        if review is None:
            return jsonify({"Error": "No review with this review_id exists"}), 404
        return jsonify(review), 200

    @app.route('/reviews/<int:review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.get_json()
        required_fields = ['stars']  # Adjust based on actual requirements

        if not all(field in data for field in required_fields):
            return jsonify({"Error": "The request body is missing at least one of the required attributes"}), 400

        review = Review.update(review_id, data)
        if review is None:
            return jsonify({"Error": "No review with this review_id exists"}), 404

        return jsonify(review), 200

    @app.route('/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review(review_id):
        try:
            if not Review.exists(review_id):
                return jsonify({"Error": "No review with this review_id exists"}), 404

            # If it exists, proceed to delete it
            if Review.delete(review_id):
                return '', 204  # Return 204 No Content if deletion is successful
            else:
                return jsonify({"Error": "Failed to delete review"}), 500  # In case deletion fails
        except Exception as e:
            # Capture any unexpected errors and log them
            print(f"An error occurred: {e}")
            return jsonify({"Error": "Internal Server Error"}), 500

    @app.route('/users/<int:user_id>/reviews', methods=['GET'])
    def list_reviews_by_user(user_id):
        reviews = Review.list_by_user(user_id)
        return jsonify(reviews), 200