from django.db import models
import uuid


class Searched(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    entry = models.CharField(max_length=40)

    class Meta:
        app_label = 'gathering'

    def __str__(self):
        return f'{self.entry}'


# data is inserted in parser.py
class Package(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=30)
    pubDate = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    email = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    version = models.CharField(max_length=5)
    keywords = models.CharField(max_length=75)

    class Meta:
        app_label = 'gathering'

    def __str__(self):
        return f'{self.title}'
