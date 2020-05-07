from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


class TestModels(TestCase):
    """Class Testing Models in Users App"""

    def setUp(self):
        """Set Up variables used in this test"""

        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

    def test_Profile(self):
        """Testing the Profile class' object"""
        client = Client()
        client.login(username='testuser', password='12345')
        self.assertEquals(self.user_1.username, 'testuser')
        self.assertTrue(check_password('12345', self.user_1.password))
        self.assertEquals(self.user_1.email,
                          'boggusmail@boggusmail.net')
