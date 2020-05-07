from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_default.jpg',
                              upload_to='profile_pics')
    newsletter = models.BooleanField(null=False, default=False)

    # Add here more field (added on top of User's model)
    # to appear in profile e.g. Bio, City, langage, etc

    def __str__(self):
        return f'{self.user.username} Profile'
