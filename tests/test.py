try:
    from app import create_app, db, app
    from flask import Flask
    from config import Config
    from sqlalchemy import create_engine
    import unittest
except Exception as e:
    print("Some modules are missing {}".format(e))


class MyTestCase(unittest.TestCase):
    def setUp(self):

        app = create_app()
        self.app = app.test_client()
        app.config['TESTING'] = True

        engine = create_engine('sqlite://')
        app.config['SQLALCHEMY_DATABASE_URI'] = engine.url

        db.init_app(app)
        with app.app_context():
            db.create_all()

    def tearDown(self):
        pass

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 302)

    def test_department(self):
        tester = app.test_client(self)
        response = tester.get('/department')
        self.assertEqual(response.status, "200 OK")

    def test_employee(self):
        tester = app.test_client(self)
        response = tester.get('/employee')
        self.assertEqual(response.status, "200 OK")


if __name__ == '__main__':
    unittest.main()
