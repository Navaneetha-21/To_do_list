from django.db import models

class To_do_model(models.Model):
    task = models.CharField(max_length=100,null=True,blank=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.task
