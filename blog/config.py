class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-development.db"
    Debug = True

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-testing.db"
    DEBUG = False
    FLASK_APPLICATION_SECRET_KEY = "Not secret"

