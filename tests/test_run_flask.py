from flask import Flask
import urllib.request
from flask_testing import LiveServerTestCase


class RunTest(LiveServerTestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        return app

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

