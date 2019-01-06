from django.conf import settings
from django.db import models

from .utils import upload_update_image


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""
