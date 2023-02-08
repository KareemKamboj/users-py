from Flask_app.config.mysqlconnection import connectToMySQL
DATABASE = 'users_db'

class Users:
    def __init__(self, data):
        self.id = data['id'] 
        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 
        self.email = data['email'] 
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at'] 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM Users;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for user_row in results:
            user_instance = cls(user_row)
            all_users.append(user_instance)
        return all_users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO Users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM Users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) > 0:
            user_instance = cls(results[0])
            return user_instance
        return False

    @classmethod
    def update(cls,data):
            query = "UPDATE Users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
            return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM Users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


