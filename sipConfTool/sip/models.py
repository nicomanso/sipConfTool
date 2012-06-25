from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    
    def getUsers(self):
        return '%s' % (self.username)

    def __unicode__(self):
        return self.name

class SipUser(models.Model):
    username = models.ForeignKey(Users)
    context = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    callerid = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    canreinvite = models.CharField(max_length=200)
    qualify = models.CharField(max_length=200)
    pickupgroup = models.CharField(max_length=200)
    callgroup = models.CharField(max_length=200)
