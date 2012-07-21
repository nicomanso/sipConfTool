from django.db import models
from django import forms

class Users(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    
    def getUsers(self):
        return '%s' % (self.username)

    def __unicode__(self):
        return self.name

class SipUser(models.Model):
    callerid = models.OneToOneField(Users)
    context = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    username = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=200)
    canreinvite = models.CharField(max_length=4)
    qualify = models.CharField(max_length=4)
    pickupgroup = models.IntegerField(max_length=200)
    callgroup = models.IntegerField(max_length=200)
    
    def __unicode__(self):
        return self.callerid.name

