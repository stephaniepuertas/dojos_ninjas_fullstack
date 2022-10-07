from flask_app.config.mysqlconnection import connectToMySQL

DATABASE = 'dojo_and_ninjas_schema_text'


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<Dojo: {self.name}>'

    # create a dojo
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, %(created_at)s, %(updated_at)s;'
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id

    # find all dojos (no data needed)
    @classmethod
    def find_all(cls):
        query = 'SELECT * from dojos;'
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for result in results:
            dojos.append(Dojo(result))
        return dojos

    # find one dojo by id
    @classmethod
    def find_by_id(cls, data):
        query = 'SELECT * from dojos WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])
        return dojo

    # find one make by id with models
    @classmethod
    def find_by_id_with_models(cls, data):
        query = 'SELECT * from makes LEFT JOIN models ON makes.id = models.make_id WHERE makes.id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        make = Make(results[0])
        if results[0]['make_id']:
            for result in results:
                data = {
                    'id': result['models.id'],
                    'name': result['models.name'],
                    'created_at': result['created_at'],
                    'updated_at': result['updated_at'],
                    'make_id': result['make_id']
                }
                make.models.append(Model(data))
        return make

    # update one dojo by id
    @classmethod
    def find_by_id_and_update(cls, data):
        query = 'UPDATE dojos SET field1 = %(field1)s, field2 = %(field2)s, field3 = %(field3)s, field4 = %(field4)s, field5 = %(field5)s WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True

    # delete one dojo by id
    @classmethod
    def find_by_id_and_delete(cls, data):
        query = 'DELETE FROM dojos WHERE id = %(id)s;'
        connectToMySQL(DATABASE).query_db(query, data)
        return True