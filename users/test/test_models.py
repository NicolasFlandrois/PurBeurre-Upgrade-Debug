from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from users.models import Profile


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

        # Setup User
        client_1 = Client()
        client_1.login(username='testuser', password='12345')
        # Setup Profile
        profile_1 = Profile()
        profile_2 = Profile(image='profile_not_default.jpg', newsletter=True)

        # Testing User
        self.assertEquals(self.user_1.username, 'testuser')
        self.assertTrue(check_password('12345', self.user_1.password))
        self.assertEquals(self.user_1.email,
                          'boggusmail@boggusmail.net')

        # Testing Profile Default @ Creation
        self.assertEquals(profile_1.image, 'profile_default.jpg')
        self.assertFalse(profile_1.newsletter)
        # Testing Profile Non Default
        self.assertEquals(profile_2.image, 'profile_not_default.jpg')
        self.assertTrue(profile_2.newsletter)
