from django.db import models
from testApp.models import User

class IndvTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=288)
    prog = models.IntegerField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Tasks"