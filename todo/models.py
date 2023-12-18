from django.db import models
from django.contrib.auth.models import User


class todo(models.Model):
    taskname = models.CharField(max_length=300)
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    done = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.taskname + " - " + str(self.done)