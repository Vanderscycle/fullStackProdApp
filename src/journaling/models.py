from django.db import models
from django.urls import reverse
# Create your models here.
class GratefulFor(models.Model):
    # should work but we have to see if that's the right way to do so. 
    # (if it actually save a timestamp)
    dayOf = models.DateField(auto_now_add=True) 
    # name but eventually we want the user to be logged 
    # (which means we must create users app)
    # https://stackoverflow.com/questions/10991460/django-get-current-user-in-model-save
    user = models.CharField(max_length=120)
    # for now one thing to be grateful for but eventually we will want a few
    gratefulOf = models.TextField(blank=True,null=True)
    
class SmallVictory(models.Model):
    # date (see class GratefulFor)
    # name but eventually we want the user to be logged
    dayOf = models.DateField(auto_now_add=True) 
    user = models.CharField(max_length=120)
    dailyWin = models.TextField(blank=True,null=True)
