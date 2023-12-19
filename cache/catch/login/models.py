from django.db import models

class User(models.Model):
    version=models.CharField(max_length=128)
    ihl=models.CharField(max_length=128)
    tos=models.CharField(max_length=256)
    len=models.CharField(max_length=256)
    uid=models.CharField(max_length=128)
    frag=models.CharField(max_length=256)
    ttl=models.CharField(max_length=128)
    proto=models.CharField(max_length=256)
    chksum=models.CharField(max_length=128)
    src=models.CharField(max_length=64)
    dst=models.CharField(max_length=64)