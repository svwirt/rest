from db import db
from flask import jsonify, render_template, request
from string import Template

class ShipModel(db.Model):
    __tablename__ = 'ships'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    type = db.Column(db.String(80))
    length = db.Column(db.Float)
    self_ship = db.Column(db.String(80))

    def __init__(self, id, name, type, length, self_ship):
        self.id = id
        self.name = name
        self.type = type
        self.length = length
        self.self_ship = self_ship

    def json(self):
        return {'id': self.id, 'name': self.name, 'type': self.type, 'length': self.length, 'self': self.self_ship}

    def html(self):
        my_template = Template("""<h1>Ship</h1>
            <ul>
                <li>id: ${ship_id}</li>
                <li>name: ${ship_name}</li>
                <li>type: ${ship_type}</li>
                <li>length: ${ship_length}</li>
                <li>self: ${ship_self}</li>
            </ul>""")
        return (my_template.substitute(ship_id=self.id, ship_name=self.name, ship_type=self.type, ship_length=self.length, ship_self=self.self_ship))


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
