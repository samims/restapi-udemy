import json

from django.contrib.auth.models import User
from django.db import models


class BookQuerySet(models.QuerySet):
    def serialize(self):
        list_values = list(self.values("id", "title", "isbn"))
        return json.dumps(list_values)


class BookModelManager(models.Manager):
    def get_queryset(self):
        return BookQuerySet(self.model, self._db)

    def serialize(self):
        return self.get_queryset().serialize()


class Book(models.Model):
    title = models.CharField(max_length=500, null=True)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50, null=True)

    objects = BookModelManager()

    def __str__(self):
        return self.title

    def serialize(self):
        data = {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn
        }
        return json.dumps(data)
