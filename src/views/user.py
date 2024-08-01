from src.app2 import ma
from src.views.role import RoleSchema
from marshmallow import fields
from src.models.user import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    role = ma.Nested(RoleSchema)

class CreateUserSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    role_id = fields.Integer(required=True, strict=True)