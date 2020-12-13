try:
    from app import app
    import unittest
except Exception as e:
    print("Some modules are missing {}".format(e))


class MyTestCase(unittest.TestCase):
    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass

    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 302)

    def test_department(self):
        tester = app.test_client(self)
        response = tester.get('/department')
        self.assertEqual(response.status_code, 200)

    def test_employee(self):
        tester = app.test_client(self)
        response = tester.get('/employee')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
