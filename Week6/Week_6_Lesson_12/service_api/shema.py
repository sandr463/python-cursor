from service_api.app_database import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name', 'age', 'address')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class NameSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'name')


name_schema = NameSchema()
names_schema = NameSchema(many=True)


class PersonSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'age', 'name_id')


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)