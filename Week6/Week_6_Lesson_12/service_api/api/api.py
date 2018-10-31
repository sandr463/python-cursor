from flask import Blueprint, request
from flask.views import MethodView

from service_api.app_database import db

from service_api.shema import user_schema, users_schema
from service_api.model import UserTable

user_api = Blueprint('user_api', __name__, static_folder='../../static', template_folder='../../template')


class UserView(MethodView):
    """
    CRUD User View
    """

    def get(self):
        user = UserTable.query.order_by(UserTable.id).all()
        return users_schema.jsonify(user)

    def post(self):
        data = request.get_json()
        new_user = UserTable(**data)

        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)

    def put(self, id):
        data = request.get_json()
        address = data.get("address")

        row = UserTable.query.filter_by(id=id).first()
        row.address = address

        db.session.commit()
        return user_schema.jsonify(row)

    def delete(self, id):
        row = UserTable.query.filter_by(id=id).first()

        db.session.delete(row)
        db.session.commit()
        return user_schema.jsonify(row)


user_api.add_url_rule('/user', view_func=UserView.as_view('user_api'))
user_api.add_url_rule('/user/<id>', view_func=UserView.as_view('user_change'))
