mport unittest

from server import app


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        app.config.from_object("web.config.TestingConfig")
        cls.app = app.test_client()

