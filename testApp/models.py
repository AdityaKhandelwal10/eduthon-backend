from django.db import models

from django.contrib.auth.models import AbstractUser
from group.models import TeamModel


class User(AbstractUser):
    email = models.EmailField()
    jwt = models.CharField(max_length=255)
    team = models.ForeignKey(TeamModel, on_delete = models.CASCADE, blank = True, null = True)





