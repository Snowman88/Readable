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


class Comment(models.Model):
    author = models.ForeignKey('auth.User')
    post = models.ForeignKey('Post')
    text = models.TextField()
    craeted = models.DateTimeField(
        default=timezone.now)
    modified = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.text


class Tag(models.Model):
    post = models.ForeignKey('Post')
    tag = models.CharField(max_length=20)

    class Meta:
        unique_together = ('post', 'tag',)


    def __str__(self):
        return self.tag
