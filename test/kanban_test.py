import requests
from flask import Flask
from flask_testing import LiveServerTestCase
from flask_login import LoginManager, login_user, logout_user, current_user

class MyTest(LiveServerTestCase):

    def create_app(self):
        from app import app
        return app

    def test_server_is_up_and_running(self):
        r = requests.get(self.get_server_url())
        self.assertEqual(r.status_code, 200)

    # This part is still buggy - having trouble going through logging phase with python
    # Keeping it as it is for now
    def test_login(self):
        s = requests.session()
        login_data = dict(username='admin', password='admin')
        s.post(self.get_server_url() + '/login', data=login_data)
        r = s.get(self.get_server_url())
        self.assertEqual(r.status_code, 200)