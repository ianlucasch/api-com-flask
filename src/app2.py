import os
from src.models import db
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask import json
from werkzeug.exceptions import HTTPException
from flask_marshmallow import Marshmallow
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()
spec = APISpec(
    title="API com Flask",
    version="1.0.0",
    openapi_version="3.0.3",
    info=dict(description="Estudando o framework Flask"),
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

def create_app(environment=os.environ["ENVIRONMENT"]):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f"src.config.{environment.title()}Config")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)
    ma.init_app(app)

    # register blueprints
    from src.controllers import user_controller
    from src.controllers import post_controller
    from src.controllers import auth_controller
    from src.controllers import role_controller

    app.register_blueprint(user_controller.app)
    app.register_blueprint(auth_controller.app)
    app.register_blueprint(role_controller.app)

    @app.route("/docs")
    def docs():
        return spec.path(view=user_controller.delete_user).path(view=user_controller.get_user).to_dict()

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description
            }
        )
        response.content_type = "application/json"
        return response

    return app