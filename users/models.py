from django.db import models
from django.contrib.auth.models import User

class custom_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pais = models.CharField(max_length=100)


