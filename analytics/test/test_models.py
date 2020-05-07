from django.test import TestCase, Client
from analytics.models import ObjectViewed, object_viewed_receiver
from django.contrib.auth.models import User
from snacks.models import Product
from datetime import datetime


class TestModels(TestCase):
    """Class Testing Models in Analytics App"""

    def setUp(self):
        """Set Up variables used in this test"""

        # Setup User
        self.user_1 = User.objects.create_user(
            username='testuser', password='12345',
            email='boggusmail@boggusmail.net'
        )

        # Setup Product
        self.prod_1 = Product.objects.create(
            pk=1,
            ean='3350033118072',
            name='test prod 1',
            category='cat 1',
            image='product_default.png',
            nutriscore='u'
        )

        # Setup Object Viewed Object
        self.objectviewed1 = ObjectViewed(
            username=self.user_1.username,
            ip_address="127.0.0.1",  # IP instance
            object_id=self.prod_1.pk,  # User_id, Product_id
            timestamp=datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
        )

    def test_ObjectViewed(self):
        """Testing the ObjectViewed class' object"""
        self.assertEquals(self.objectviewed1.username, 'testuser')
        self.assertEquals(self.objectviewed1.ip_address, '127.0.0.1')
        self.assertEquals(self.objectviewed1.object_id, 1)
        self.assertEquals(self.objectviewed1.timestamp,
                          datetime.fromisoformat('2011-11-04 00:05:23.283+00:00'))

    # def test_object_viewed_receiver(self):
    #     """Testing the ObjectViewed class' object"""
