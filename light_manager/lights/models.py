from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser


UserModel = get_user_model()

class Home(models.Model):
    user = models.ForeignKey(UserModel, models.CASCADE)

class Room(models.Model):
    home = models.ForeignKey(Home, models.CASCADE)

class Light(models.Model):
    room = models.ForeignKey(Room, models.CASCADE)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    brightness = models.IntegerField()
    status = models.BooleanField(default=True)


class LightHistory(models.Model):
    light = models.ForeignKey(Light, models.CASCADE)
    created = models.DateTimeField()
