from django.db import models
from django.contrib.auth.models import User

class To_do_model(models.Model):
    task = models.CharField(max_length=100,null=True,blank=True)
    completed = models.BooleanField(default=False)
    user =models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.task
