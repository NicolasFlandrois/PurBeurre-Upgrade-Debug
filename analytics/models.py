from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from .utils import get_client_ip


User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    """Tracking analytics of browsing Activities - Models"""
    username = models.CharField(
        max_length=20, blank=True, null=True)
    ip_address = models.CharField(
        max_length=220, blank=True, null=True)  # IP instance
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE)  # Product
    object_id = models.PositiveIntegerField()  # User_id, Product_id
    content_object = GenericForeignKey(
        'content_type', 'object_id')  # Product instance
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.content_object} viewed on {self.timestamp}'

    class Meta:
        ordering = ['-timestamp']  # Most recent saved show up first.
        verbose_name = 'Object viewed'
        verbose_name_plural = 'Objects viewed'


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)
    ip_address = None
    try:
        ip_address = get_client_ip(request)
    except:
        pass

    new_view_instance = ObjectViewed.objects.create(
        username=request.user.username,
        content_type=c_type,
        object_id=instance.id,
        ip_address=ip_address
    )


object_viewed_signal.connect(object_viewed_receiver)
