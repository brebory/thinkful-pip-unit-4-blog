import os
import unittest
import multiprocessing
import time
from urlparse import urlparse

from werkzeug.security import generate_password_hash
from splinter import Browser

# Configure our app to use the testing database
os.environ["CONFIG_PATH"] = "blog.config.TestingConfig"

from blog import app
from blog import models
from blog.database import Base, engine, session

class TestViews(unittest.TestCase):
    def setUp(self):
        """Test setup"""
        self.browser = Browser("phantomjs")

        Base.metadata.create_all(engine)

        self.user = models.User(name="Alice", email="alice@example.com",
                    password=generate_password_hash("test"))

        session.add(self.user)
        session.commit()

        self.process = multiprocessing.Process(target=app.run, kwargs={"host":\
            '0.0.0.0', "port": 8000})
        self.process.start()
        time.sleep(1)

    def tearDown(self):
        """Test teardown"""
        # Remove the tables and their data from the database
        self.process.terminate()
        Base.metadata.drop_all(engine)
        self.browser.quit()

    def testLoginCorrect(self):
        self.browser.visit("http://localhost:8000/login")
        self.browser.fill("email", "alice@example.com")
        self.browser.fill("password", "test")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://localhost:8000/")

    def testLoginIncorrect(self):
        self.browser.visit("http://localhost:8000/login")
        self.browser.fill("email", "incorrect@example.com")
        self.browser.fill("password", "incorrect")
        button = self.browser.find_by_css("button[type=submit]")
        button.click()
        self.assertEqual(self.browser.url, "http://localhost:8000/login")

if __name__ == "__main__":
    unittest.main()

