from django.shortcuts import render
from scapy.layers.inet import *
from scapy.all import *
from login import models


user_list=[]

def index(request):
        pkt = sniff(filter="dst 36.155.132.31", count=3)
        for o in pkt:
                a=o[IP].version
                b=o[IP].ihl
                c=o[IP].tos
                d=o[IP].len
                e=o[IP].id
                f=o[IP].frag
                g=o[IP].ttl
                h=o[IP].proto
                i=o[IP].chksum
                j=o[IP].src
                k=o[IP].dst
                models.User.objects.create(version=a,ihl=b,tos=c,len=d,uid=e,frag=f,ttl=g,proto=h,chksum=i,src=j,dst=k)
        user_list = models.User.objects.all()
        print(user_list)
        return render(request, 'index.html', {'data': user_list})