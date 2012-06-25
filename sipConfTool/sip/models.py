from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    
    def getUsers(self):
        return '%s' % (self.username)

    def __unicode__(self):
        return self.name

class SipUser(models.Model):
    callerid = models.ForeignKey(Users)
    context = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    username = models.IntegerField()
    host = models.CharField(max_length=200)
    canreinvite = models.CharField(max_length=200)
    qualify = models.BooleanField()
    pickupgroup = models.CharField(max_length=200)
    callgroup = models.CharField(max_length=200)


