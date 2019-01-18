import json
from django.conf import settings
from django.db import models

from .utils import upload_update_image


class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values("id", "user", "content", "image"))
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)

    def serialize(self):
        return self.get_queryset().serialize()


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        try:
            image = self.image.url
        except ValueError:
            image = ""

        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image
        }
        return json.dumps(data)
