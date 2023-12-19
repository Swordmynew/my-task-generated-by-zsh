from django.shortcuts import render
from scapy.layers.inet import *
from scapy.all import *
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Line

def index(request):
    number_tcp = 0
    number_udp = 0
    number_icmp = 0
    pkt = sniff(filter="ip",timeout=5)
    for package in pkt:
        if package.haslayer(ICMP):
            number_icmp += 1
        elif package.haslayer(UDP):
            number_udp += 1
        elif package.haslayer(TCP):
            number_tcp += 1

    pie = Pie()
    data_pair = [("UDP", number_udp), ("ICMP", number_icmp), ("TCP", number_tcp)]
    pie.add("", data_pair,radius=[75,100])
    pie.set_global_opts(title_opts=opts.TitleOpts(title="统计：饼图"))
    chart_options1 = pie.dump_options()

    bar = Bar()
    bar.add_xaxis(["ICMP", "UDP","TCP"])
    bar.add_yaxis("", [number_icmp, number_udp,number_tcp],
                  category_gap="50%", itemstyle_opts=opts.ItemStyleOpts(color="#00CD96"))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="统计：柱形图"))
    bar.reversal_axis()
    chart_options2 = bar.dump_options()

    line = Line()
    line.add_xaxis(["ICMP", "UDP", "TCP"])
    line.add_yaxis("", [number_icmp, number_udp,number_tcp], is_smooth=True,itemstyle_opts=opts.ItemStyleOpts(color="#00CD96"))
    line.set_global_opts(title_opts=opts.TitleOpts(title="统计：折线图"))
    chart_options3 = line.dump_options()

    line1=Line()
    line1.add_xaxis(["0-3","3-6","6-9","9-12","12-15"])
    tuple=[]
    for i in range(1,6):
        number_tcp1 = 0
        number_udp1 = 0
        number_icmp1 = 0
        pkt1= sniff(filter="ip", timeout=3)
        for package in pkt1:
            if package.haslayer(ICMP):
                number_icmp1 += 1
            elif package.haslayer(UDP):
                number_udp1 += 1
            elif package.haslayer(TCP):
                number_tcp1 += 1
        tuple.append(number_udp1+number_icmp1+number_tcp1)
    line1.add_yaxis("", tuple, is_smooth=a)
    line1.set_global_opts(title_opts=opts.TitleOpts(title="时间统计"))
    chart_options4 = line1.dump_options()

    context = {
        'chart_options1': chart_options1,
        'chart_options2': chart_options2,
        'chart_options3': chart_options3,
        'chart_options4': chart_options4,
    }
    return render(request, 'index.html', context)