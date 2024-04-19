from flask import request, jsonify
from models import Business, Review

def register_routes(app):
    @app.route('/businesses', methods=['POST'])
    def create_business():
        required_fields = ['owner_id', 'name', 'street_address', 'city', 'state', 'zip_code']
        data = request.get_json()

        if not data or not all(field in data for field in required_fields):
            return jsonify({"Error": "Missing required fields"}), 400
        
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
        if not business:
            return jsonify({'Error': 'No business found'}), 404
        return jsonify(business), 200

    @app.route('/businesses', methods=['GET'])
    def list_businesses():
        businesses = Business.list()
        return jsonify(businesses), 200

    @app.route('/businesses/<int:business_id>', methods=['PUT'])
    def update_business(business_id):
        data = request.json
        business = Business.update(business_id, data)
        if not business:
            return jsonify({'Error': 'No business found'}), 404
        return jsonify(business), 200

    @app.route('/businesses/<int:business_id>', methods=['DELETE'])
    def delete_business(business_id):
        Business.delete(business_id)
        return '', 204

    @app.route('/reviews', methods=['POST'])
    def create_review():
        data = request.json
        review_id = Review.create(data)
        return jsonify({'id': review_id}), 201

    @app.route('/reviews/<int:review_id>', methods=['GET'])
    def get_review(review_id):
        review = Review.get(review_id)
        if not review:
            return jsonify({'Error': 'No review found'}), 404
        return jsonify(review), 200

    @app.route('/reviews/<int:review_id>', methods=['PUT'])
    def update_review(review_id):
        data = request.json
        review = Review.update(review_id, data)
        if not review:
            return jsonify({'Error': 'No review found'}), 404
        return jsonify(review), 200

    @app.route('/reviews/<int:review_id>', methods=['DELETE'])
    def delete_review(review_id):
        Review.delete(review_id)
        return '', 204

    @app.route('/users/<int:user_id>/reviews', methods=['GET'])
    def list_reviews_by_user(user_id):
        reviews = Review.list_by_user(user_id)
        return jsonify(reviews), 200
