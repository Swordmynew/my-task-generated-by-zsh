from django.db import models

# Create your models here.
class User(models.Model):
    icmp_cou=models.CharField(max_length=128)
    tcp_cou=models.CharField(max_length=128)
    udp_cou=models.CharField(max_length=128)
