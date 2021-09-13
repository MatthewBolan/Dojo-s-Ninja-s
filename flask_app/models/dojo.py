from flask_app.config.mysqlconnection import connectToMySQL

from .ninja import Ninja

class Dojo:

    def __init__(self, data):

        self.id = data ['id']

        self.name = data ['name']

        self.created_at = data ['created_at']

        self.updated_at = data ['updated_at']

        self.ninjas = []






    @classmethod

    def display_all_dojos(cls):

            query = "SELECT * FROM dojos;"

            results = connectToMySQL('dojos&ninjas_schema').query_db(query)

            dojos = []

            for x in results:

                dojos.append(cls(x))

            return dojos




    @classmethod

    def save_dojo(cls, data):

        query = "INSERT INTO dojos (name) VALUES (%(name)s)"

        result = connectToMySQL('dojos&ninjas_schema').query_db(query, data)

        return result




    @classmethod

    def get_one_dojo_ninjas(cls,data):

        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL('dojos&ninjas_schema').query_db(query,data)

        print (results)

        dojos = cls(results[0])

        for ninja in results:

            x = {

                'id': ninja['ninjas.id'],

                'first_name': ninja['first_name'],

                'last_name': ninja['last_name'],

                'age': ninja['age'],

                'created_at': ninja['ninjas.created_at'],

                'updated_at': ninja['ninjas.updated_at']

            }

            dojos.ninjas.append(Ninja(x))

        return dojos
