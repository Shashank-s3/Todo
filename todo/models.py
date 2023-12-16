from django.db import models

class todo(models.Model):
    taskname = models.CharField(max_length=300)
    done = models.BooleanField(default = False)
    def __str__(self) -> str:
        return self.taskname + " - " + str(self.done)