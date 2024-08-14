""" endpoints """
from flask import Flask, Response
from flask_swagger_ui import get_swaggerui_blueprint
from toolkit.exceptions import ValidationError, DuplicatedError
from .hello import hello_bp
from .create_workflow import new_workflow_bp
from .migrate import migration_bp


def map_endpoints(app: Flask, prefix: str):
    """ Map endpoints based on blueprints """

    app.register_blueprint(blueprint=new_workflow_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=migration_bp, url_prefix=prefix)

    app.register_blueprint(blueprint=hello_bp, url_prefix=prefix)

    app.register_blueprint(
        get_swaggerui_blueprint(
            "/swagger",
            "/static/swagger.json",
            config={
                'app_name': 'PYRULE - A Python Rule Engine API'
            }
        ),
        url_prefix="/swagger"
    )

    app.register_error_handler(
        ValidationError,
        lambda error: Response(
            response=error.description, status=400)
    )

    app.register_error_handler(
        DuplicatedError,
        lambda error: Response(
            response=error.description, status=409)
    )

    @app.after_request
    def after_request_func(response: Response):
        response.content_type = 'application/json'
        return response
