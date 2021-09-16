from django.db import models
from accounts.models import User
import datetime


class Media(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Article(Media):
    part_1 = models.TextField()
    part_2 = models.TextField()
    part_3 = models.TextField()


class Video(Media):
    url = models.CharField(max_length=128)
