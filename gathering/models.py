from django.db import models


class Searched(models.Model):
    entry = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.entry}'

class Package(models.Model):
    title = models.CharField(max_length=20)
    link = models.CharField(max_length=30)
    pubDate = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}'