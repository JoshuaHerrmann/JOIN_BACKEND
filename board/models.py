from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Task (models.Model):
    created_at = models.DateField(default=datetime.date.today)
    title = models.CharField(default="title", max_length=40)
    description = models.CharField(default="description", max_length=200,)
    #category = models.ManyToManyField()
    #priority = models.ManyToManyField()
    user = models.ForeignKey( User,on_delete=models.CASCADE)
    #subtasks =
    