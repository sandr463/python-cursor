from service_api.app_database import db


class UserTable(db.Model):
    __tablename__ = 'user_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.INTEGER)
    address = db.Column(db.String(120))

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class TestTable(db.Model):
    __tablename__ = 'test_table'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    field = db.Column(db.String)


# One to many relation Example

class Name(db.Model):
    __tablename__ = 'name'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    persons = db.relationship('Person', backref='carrier')

    def __init__(self, name):
        self.name = name


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    age = db.Column(db.Integer)
    carrier_id = db.Column(db.Integer, db.ForeignKey('name.id'))

    def __init__(self, age, name_id):
        self.age = age
        self.name_id = name_id
