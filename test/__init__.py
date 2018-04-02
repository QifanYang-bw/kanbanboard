

from test.kanban_test import *

if __name__ == '__main__':
    unittest.main()

# import unittest
# import requests
# from .app import User, Task

# class IntergrationTest(unittest.TestCase):

#     def test_add_user(self):
#         username = 'test',
#         email = 'test@minerva.edu.com'.
#         password = 'test'
#         r = requests.post(
#             'http://localhost:5000/register', 
#             data = {
#                 'username':username,
#                 'email':email,
#                 'password':password
#             }
#         )
#         self.assertEqual(r.status_code, 200)

#         inserted = User.query.filter(username=username).first()
#         self.assertEqual(inserted.email, email)

#     def test_login(self):
#         username = 'test',
#         password = 'test'
#         r = requests.post(
#             'http://localhost:5000/login', 
#             data = {
#                 'username':username,
#                 'email':email,
#                 'password':password
#             }
#         )
#         self.assertEqual(r.status_code, 200)
#         inserted = User.query.filter(username=username).first()

#         self.assertEqual(inserted.email, email)
