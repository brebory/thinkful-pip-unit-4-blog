class DevelopmentConfig(object):
    import os
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-development.db"
    DEBUG = True
    SECRET_KEY = os.environ.get("FLASK_APPLICATION_SECRET_KEY", "")

class TestingConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog-testing.db"
    DEBUG = False
    SECRET_KEY = "Not secret"

