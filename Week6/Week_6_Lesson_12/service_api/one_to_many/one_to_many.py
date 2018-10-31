from flask import Blueprint
from flask.views import MethodView

from service_api.model import Name
from service_api.shema import names_schema, name_schema

one_to_many_api = Blueprint('one_to_many', __name__, static_folder='../../static', template_folder='../../template')


class NamesView(MethodView):
    """
    Create database tables
    """

    def get(self):
        names = Name.query.first()
        print(names.persons[0].age)
        return name_schema.jsonify(names)


one_to_many_api.add_url_rule('/one_to_many_names', view_func=NamesView.as_view('one_to_many_names'))