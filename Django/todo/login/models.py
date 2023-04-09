from django.db import models

class Users(models.Model):
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  address = models.CharField(max_length=255)