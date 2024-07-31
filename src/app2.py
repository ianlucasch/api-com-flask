import os
from src.models import db
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

migrate = Migrate()
jwt = JWTManager()

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

    # register blueprints
    from src.controllers import user_controller
    from src.controllers import post_controller
    from src.controllers import auth_controller
    from src.controllers import role_controller

    app.register_blueprint(user_controller.app)
    app.register_blueprint(auth_controller.app)
    app.register_blueprint(role_controller.app)

    return app