from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField()
    jwt = models.CharField(max_length=255)


#User Model
# 1. email
# 2. jwt
# 3. team(optional)



