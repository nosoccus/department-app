from flask_testing.utils import TestCase
from flask import Flask


class ViewTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        return app

    def test_dep(self):
        response = self.client.get('/department')
        self.assert_template_used('departments_index.html')
        self.assert_status(response, 200)

    def test_emp(self):
        response = self.client.get('/employee')
        self.assert_template_used('employees_index.html')
        self.assert_status(response, 200)

