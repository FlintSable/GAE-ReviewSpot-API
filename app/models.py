from google.cloud import datastore

client = datastore.Client()

class Business:
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
        return client.get(key)

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
        client.delete(key)

class Review:
    @staticmethod
    def create(data):
        key = client.key('Review')
        entity = datastore.Entity(key=key)
        entity.update(data)
        client.put(entity)
        return entity.key.id_or_name

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
        key = client.key('Review', int(review_id))
        client.delete(key)