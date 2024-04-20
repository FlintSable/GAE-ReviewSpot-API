from google.cloud import datastore

client = datastore.Client()

class Business:
    @staticmethod
    def list_by_owner(owner_id):
        query = client.query(kind='Business')
        query.add_filter('owner_id', '=', owner_id)
        results = list(query.fetch())
        if not results:
            return None
        return [{ "id": entity.key.id,
                  "owner_id": entity["owner_id"],
                  "name": entity["name"],
                  "street_address": entity["street_address"],
                  "city": entity["city"],
                  "state": entity["state"],
                  "zip_code": entity["zip_code"]
                } for entity in results]

    @staticmethod
    def create(data):
        key = client.key('Business')
        entity = datastore.Entity(key=key)
        entity.update(data)
        client.put(entity)
        return entity.key.id, entity
    
    @staticmethod
    def get(business_id):
        key = client.key('Business', business_id)
        entity = client.get(key)
        if entity is None:
            return None
        return {
            'id': entity.key.id,
            'owner_id': entity['owner_id'],
            'name': entity['name'],
            'street_address': entity['street_address'],
            'city': entity['city'],
            'state': entity['state'],
            'zip_code': entity['zip_code']            
        }

    @staticmethod
    def list():
        query = client.query(kind='Business')
        return list(query.fetch())

    @staticmethod
    def update(business_id, data):
        key = client.key('Business', business_id)
        entity = client.get(key)
        if not entity:
            return None
        entity.update(data)
        client.put(entity)
        return entity

    @staticmethod
    def delete(business_id):
        key = client.key('Business', business_id)
        entity = client.get(key)
        if not entity:
            return False
        client.delete(key)
        return True

    @staticmethod
    def exists(business_id):
        key = client.key('Business', business_id)
        entity = client.get(key)
        return entity is not None

class Review:
    @staticmethod
    def create(data):
        key = client.key('Review')
        entity = datastore.Entity(key=key)
        entity.update(data)
        client.put(entity)
        return entity.key.id

    @staticmethod
    def exists(user_id, business_id):
        key = client.query(kind='Review')
        key.add_filter('user_id', '=', user_id)
        key.add_filter('business_id', '=', business_id)
        results = list(query.fetch())
        return len(results) > 0

    @staticmethod
    def get(review_id):
        key = client.key('Review', int(review_id))
        entity = client.get(key)
        if not entity:
            return None
        return entity

    @staticmethod
    def list_by_user(user_id):
        query = client.query(kind='Review')
        query.add_filter('user_id', '=', int(user_id))
        return list(query.fetch())

    @staticmethod
    def update(review_id, data):
        key = client.key('Review', int(review_id))
        entity = client.get(key)
        if not entity:
            return None
        entity.update(data)
        client.put(entity)
        return entity

    @staticmethod
    def delete(review_id):
        client = datastore.Client()
        key = client.key('Review', review_id)
        try:
            entity = client.get(key)
            if not entity:
                return False  # No entity found, return False
            client.delete(key)
            return True  # Successfully deleted
        except Exception as e:
            print(f"Failed to delete review: {e}")
            return False  # In case of any exception, return False