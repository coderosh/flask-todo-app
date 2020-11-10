import os


class BaseConfig:
    SQLALCHEMY_ECHO = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_ECHO = True
    SECRET_KEY = "3b12aeba14e88"


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///prod.db"


configs = {
    'dev': DevConfig,
    'prod': ProdConfig
}
