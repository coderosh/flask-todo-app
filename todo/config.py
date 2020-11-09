class BaseConfig:
    DEBUG = False
    SQLALCHEMY_ECHO = False
    WTF_CSRF_ENABLED = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "sqlite:///prod.db"
    pass


configs = {
    'dev': DevConfig,
    'prod': ProdConfig
}
