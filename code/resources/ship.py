from flask_restful import Resource, reqparse
from flask_accept import accept
from models.ship import ShipModel


class Ship(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        # required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('type',
                        type=str,
                        # required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('length',
                        type=float,
                        # required=True,
                        help="This field cannot be left blank!"
                       )
    parser.add_argument('self_ship',
                        type=str,
                        # required=True,
                        help="This field cannot be left blank!"
                       )

    @accept('application/json')
    def get(self, id):
        ship = ShipModel.find_by_id(id)
        if ship:
            return ship.json()
        return {'message': 'Ship not found - no content'}, 204

    @accept('text/html')
    def get(self, id):
        ship = ShipModel.find_by_id(id)
        if ship:
            return ship.html()
        return {'message': 'Ship not found - no content'}, 204


    def post(self, id):
        if ShipModel.find_by_id(id):
            return {'message': "An ship with id '{}' already exists.".format(id)}, 400

        data = Ship.parser.parse_args()

        ship = ShipModel(id, **data)

        try:
            ship.save_to_db()
        except:
            return {"message": "An error occurred inserting the ship."}, 500

        return ship.json(), 201

    def delete(self, id):
        ship = ShipModel.find_by_id(id)
        if ship:
            ship.delete_from_db()
            return {'message': 'Ship deleted.'}, 204
        return {'message': 'Ship not found.'}, 405

    def put(self, id):
        data = Ship.parser.parse_args()

        ship = ShipModel.find_by_id(id)

        if ship:
            ship.name = data['name']
            ship.type = data['type']
            ship.length = data['length']
            ship.self_ship = data['self_ship']
            ship.save_to_db()
            return ship.json(), 303
        else:
            ship = ShipModel(id, **data)
            ship.save_to_db()
            return ship.json(), 201




class Ships(Resource):
    def get(self):
        return {'ships': list(map(lambda x: x.json(), ShipModel.query.all()))}, 200
