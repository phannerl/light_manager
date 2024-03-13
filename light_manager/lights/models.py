from django.db import models


class User(models.Model):
    id = models.CharField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255)
