import os
from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT


from resources.ship import Ship, Ships


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

# @api.resource('/foo')
# class Ship(Resource):
#     def get(self):
#         return 'Hello, World!'


api.add_resource(Ship, '/ship/<string:id>')
api.add_resource(Ships, '/ships')



# if __name__ == '__main__':
#     from db import db
#     db.init_app(app)
#
#     if app.config['DEBUG']:
#         @app.before_first_request
#         def create_tables():
#             db.create_all()
#
#     app.run(port=5000)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)





# https://www.udemy.com/rest-api-flask-and-python/learn/v4/content
