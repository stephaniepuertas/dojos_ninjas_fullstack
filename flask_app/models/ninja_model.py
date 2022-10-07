from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojo_and_ninjas_schema_text'


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.field1 = data['field1']
        self.field2 = data['field2']
        self.field3 = data['field3']
        self.field4 = data['field4']
        self.field5 = data['field5']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def __repr__(self):
        return f'<Ninja: {self.field1}>'

    # create a ninja
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO ninjas (field1, field2, field3, field4, field5) VALUES (%(field1)s, %(field2)s, %(field3)s, %(field4)s, %(field5)s);'
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id

    # find all ninjas (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from ninjas;'
        results = connectToMySQL(DATABASE).query_db(query)
        ninjas = []
        for result in results:
            ninjas.append(Ninja(result))
        return ninjas

    # find one ninja by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from ninjas WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        ninja = Ninja(results[0])
        return ninja

    # update one ninja by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE ninjas SET field1 = %(field1)s, field2 = %(field2)s, field3 = %(field3)s, field4 = %(field4)s, field5 = %(field5)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one ninja by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM ninjas WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True