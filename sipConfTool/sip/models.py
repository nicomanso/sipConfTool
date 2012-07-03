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
    callerid = models.ForeignKey(Users, unique=True)
    context = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    username = models.IntegerField()
    host = models.CharField(max_length=200)
    canreinvite = models.BooleanField(max_length=200)
    qualify = models.BooleanField()
    pickupgroup = models.IntegerField(max_length=200)
    callgroup = models.IntegerField(max_length=200)
    
    def __unicode__(self):
        return self.callerid.name

