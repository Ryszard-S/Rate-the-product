from flask import Flask
from .extenctions import db, login_manager


# db = SQLAlchemy()


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    db.init_app(app)

    # path to store files
    app.config['ALLOWED_FILE_EXTENTIONS'] = ['PNG', 'JPG', 'JPEG', 'GIF']
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import Login

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Login.query.get(int(id))

    return app
