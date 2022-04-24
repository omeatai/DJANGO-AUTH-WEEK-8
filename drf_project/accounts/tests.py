from rest_framework.test import APITestCase
from knox import models
from knox.models import User

# class TestModel(APITestCase):
    
#     def test_user(self):
#         obj = User(username='abbey', password='abbeypassword')
#         obj.save()
#         response = User.objects.get(username='abbey')
#         self.assertTrue(response)
#         self.assertEqual(response.username, 'abbey')

    # def test_creates_user(self):
    #     user = User.objects.create_user(
    #         'ifeanyio', 'ifeanyio@gmail.com', 'password123!@')
    #     self.assertIsInstance(user, User)
    #     self.assertFalse(user.is_staff)
    #     self.assertEqual(user.email, 'ifeanyio@gmail.com')

    # def test_raises_error_when_no_username_is_supplied(self):
    #     self.assertRaises(ValueError, User.objects.create_user, username="",
    #                         email='ifeanyio@gmail.com', password='password123!@')

    # def test_raises_error_with_message_when_no_username_is_supplied(self):
    #     with self.assertRaisesMessage(ValueError, 'The given username must be set'):
    #         User.objects.create_user(
    #             username='', email='ifeanyio@gmail.com', password='password123!@')

    # def test_raises_error_when_no_email_is_supplied(self):
    #     self.assertRaises(ValueError, User.objects.create_user,
    #                         username="username", email='', password='password123!@')

    # def test_raises_error_with_message_when_no_email_is_supplied(self):
    #     with self.assertRaisesMessage(ValueError, 'The given email must be set'):
    #         User.objects.create_user(
    #             username='username', email='', password='password123!@')



