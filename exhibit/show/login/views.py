from django.shortcuts import render
from scapy.all import *
import json
from django.views.decorators.csrf import csrf_exempt




data= {}
# Create your views here.
icmp_cou = 0
tcp_cou = 0
udp_cou = 0
@csrf_exempt
def index(request):
     if(request.method == "POST"):
         url=request.POST.get('url')
         if(url=='YES'):
             def count_pkt(pkt):
                 global icmp_cou, tcp_cou, udp_cou
                 for p in pkt:
                     if (p.haslayer('IP')):
                         if (p.haslayer('TCP')):
                             tcp_cou += 1
                         if (p.haslayer('UDP')):
                             udp_cou += 1
                         if (p.haslayer('ICMP')):
                             icmp_cou += 1


             pkt = sniff(filter='ip', timeout=5, prn=count_pkt)
             print(pkt)
             print("udp总数 %d" % (udp_cou))
             print("tcp总数 %d" % (tcp_cou))
             print("icmp总数 %d" % (icmp_cou))

             data={
                 'udp_cou':udp_cou,
                 'tcp_cou':tcp_cou,
                 'icmp_cou':icmp_cou
             }
             json_data=json.dumps(data)
             return render(request,'index.html',{'json_data':json_data})
     return render(request,'index.html')