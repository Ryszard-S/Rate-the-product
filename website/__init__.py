from flask import Flask
from flask_login import LoginManager
from .extenctions import db

# db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "asdkhfQWER324SDFaxcawewEWcaHTAe34etgfDSA"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/rate-the-product"
    db.init_app(app)

    # path to store files
    app.config['IMAGE_UPLOADS'] = 'C:/Users/Ryszard/OneDrive/Rate-the-product/website/static/assets'
    app.config['ALLOWED_FILE_EXTENTIONS'] = ['PNG', 'JPG', 'JPEG', 'GIF']

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import Login

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Login.query.get(int(id))

    return app
