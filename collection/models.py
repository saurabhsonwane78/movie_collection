# collection/models.py
from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genres = models.CharField(max_length=100)
    uuid = models.UUIDField()

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    movies = models.ManyToManyField(Movie)
