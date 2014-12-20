from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(
        default=timezone.now)
    modified = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.title
