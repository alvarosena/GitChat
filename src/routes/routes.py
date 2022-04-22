from controllers.authenticate_user_controller import authentication
from controllers.employers_controllers import employers

def routes(app):
    app.register_blueprint(authentication, url_prefix='/api/v1')
    app.register_blueprint(employers, url_prefix='/api/v1')
