from pprint import pprint
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

DATABASE = 'dojo_and_ninjas_schemas'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas=[]

    def __repr__(self):
        return f'<Dojo: {self.name}>'

    # create a dojo
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    # find all dojos (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for result in results:
            dojos.append(Dojo(result))
        return dojos

    # find one dojo by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        return dojo

    # find one make by id with models
    @classmethod
    def find_by_id_with_models(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        print('hello world')
        pprint(results)
        dojo = Dojo(results[0])
        if results[0]['dojo_id']:
            for result in results:
                data = {
                    'id': result['id'],
                    'first_name': result['first_name'],
                    'last_name': result['last_name'],
                    'age': result['age'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at'],
                    'dojo_id': result['dojo_id']
                }
                dojo.ninjas.append(Ninja(data))
                # print (dojo.ninjas)
        return dojo


    # update one dojo by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE dojos SET name = %(name)s, created_at = %(created_at)s, updated_at = %(updated_at)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one dojo by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True