from src.app2 import ma

class RoleSchema(ma.Schema):
    class Meta:
        fields = ("id", "name")