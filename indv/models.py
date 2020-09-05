from django.db import models
from testApp.models import User
from group.models import GroupTasks

class IndvTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=288)
    desc = models.TextField(null = True)
    prog = models.IntegerField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Tasks"

class ProgressModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    task = models.ForeignKey(GroupTasks, on_delete =models.CASCADE)
    progress = models.IntegerField()

    def __str__(self):
        return self.User

    class Meta:
        verbose_name_plural = "Progress"
