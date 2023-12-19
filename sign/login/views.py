from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from scapy.layers.inet import *
from scapy.all import *


def index(request):
    pass
    pkt = IP(dst="192.168.2.46") / TCP(dport=3306, flags="S")
    ans = sr1(pkt)
    ans.show()
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:  # 确保用户名和密码都不为空
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, 'login/logout.html')
            if user.password == password:
                return redirect('/index/')
    return render(request, 'login/login.html')



def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return render(request,'login/logout.html')