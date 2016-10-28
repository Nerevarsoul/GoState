import os


class Config(object):

    DEBUG = True

    # config db
    # DB_USER_NAME = os.environ['DB_USER_NAME']
    # DB_PASSWORD = os.environ['DB_PASSWORD']
    # DB_HOST = "localhost"
    # DB_BASE_NAME = os.environ['DB_BASE_NAME']
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False

