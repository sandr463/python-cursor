from flask import Blueprint
from flask.views import MethodView

from service_api.app_database import db

create_db_api = Blueprint('create_db', __name__, static_folder='../../static', template_folder='../../template')


class CreateDatabaseView(MethodView):
    """
    Create database tables
    """

    def post(self):
        db.create_all()
        db.session.commit()
        return "Successfully created all tables"


create_db_api.add_url_rule('/keyspaces', view_func=CreateDatabaseView.as_view('create_db_api'))