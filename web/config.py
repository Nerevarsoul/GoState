import logging
import os


class Config(object):

    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://gostate_user:{}@localhost/gostate".format(os.environ['DATABASE_PASS'])
    # CELERY_BROKER_URL = 'redis://localhost:6379/0'
    # CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SESSION_TYPE = 'memcached'
    SECRET_KEY = 'super secret key'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/flask.log'
    LOGGING_LEVEL = logging.DEBUG
