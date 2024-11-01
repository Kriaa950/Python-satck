from mysqlconnection import connectToMySQL
class  Friend:
    DB = "first_flask"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod 
    def save(cls, data):
        query = """"INSERT INTO friends (first_name, last_name, email, created_at, updated_at)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append(cls(friend))
        return friends
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        data = {"id": friend_id} 
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query ="""UPDATE friends
                SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s, 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    @classmethod
    def delete(cls, friend_id):
        query  = "DELETE FROM friends WHERE id = %(id)s;"
        data = {"id": friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)
