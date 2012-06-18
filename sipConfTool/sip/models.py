from django.db import models


class sipUser(models.Model):
    username = models.CharField(max_length=200)
    context = models.CharField(max_length=200)
    secret = models.CharField(max_length=200)
    callerid = models.CharField(max_length=200)
    host = models.CharField(max_length=200)
    canreinvite = models.CharField(max_length=200)
    qualify = models.CharField(max_length=200)
    pickupgroup = models.CharField(max_length=200)
    callgroup = models.CharField(max_length=200)

