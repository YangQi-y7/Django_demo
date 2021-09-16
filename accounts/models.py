from django.db import models
import datetime


class User(models.Model):
    gender = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('None', 'Others'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="无")
    create_time = models.DateTimeField(auto_now_add=True)
    time = models.DateTimeField(default=datetime.datetime.now())
    image = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name
