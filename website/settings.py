import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
SECRET_KEY = os.environ.get('SECRET_KEY')
IMAGE_UPLOADS = os.environ.get('IMAGE_UPLOADS_PATH')