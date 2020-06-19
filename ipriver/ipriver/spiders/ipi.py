# -*- coding: utf-8 -*-
import scrapy
import urllib.request
from scrapy.http import Request
import pymysql
import re
import urllib.error

class IpiSpider(scrapy.Spider):
    name = 'ipi'
    allowed_domains = ['89ip.cn']
    #start_urls = ['http://89ip.cn/']

    #改变初始遍历的网址
    def start_requests(self):
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

        yield Request("http://www.89ip.cn/index_1.html", headers=headers)

    # def use_proxy(self,url1, proxy_addr):
    #     try:
    #         proxy = urllib.request.ProxyHandler({"http": proxy_addr})
    #         opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    #         urllib.request.install_opener(opener)
    #         data1 = urllib.request.urlopen(url1).read().decode("utf-8", "ignore")
    #         return data1
    #
    #     except urllib.error.URLError as e:
    #         print(e)
    #         pass

    #开始处理获取的数据
    def parse(self, response):

        #建立数据库连接
        conn = pymysql.connect("localhost", "root", "root", "ip")
        cursor = conn.cursor()

        #创建IP地址的空列表
        iplist = []

        #创建端口的空列表
        duankou = []

        #创建最终的IP+端口的列表
        ipaddress = []

        #循环开始获取
        for i in range(0,1):
            #编写免费代理IP地址的网页URL
            url = "http://www.89ip.cn/index_" + str(i) + ".html"
            data = urllib.request.urlopen(url).read().decode("utf-8","ignore")

            #利用正则筛选出IP地址的信息
            pat = "<td>\n\t\t\t(.*?)\t\t</td>"
            ip = re.compile(pat).findall(data)

            #遍历出IP地址
            for j in range(0, len(ip),4):
                iplist.append(ip[j])

            #遍历出端口
            for k in range(1, len(ip),4):
                duankou.append(ip[k])

            #制作出IP+端口的形式，然后写入到数据库中
            for o in range(0,len(iplist)):
                ipaddress.append(iplist[o] + ":" + duankou[o])
                print("开始测试地址：" + ipaddress[o])

                # headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0")
                # opener = urllib.request.build_opener()
                # opener.addheaders = [headers]
                # urllib.request.install_opener(opener)
                #
                # proxy_addr = ipaddress[0]
                # url1 = "http://www.baidu.com"
                #
                # data2 = self.use_proxy(url1, proxy_addr)
                # last = any(data2)
                # if len(data2):
                #     pat = "<title>(.*?)</title>"
                #     baidu_data = re.compile(pat).findall(data2)
                #     print(baidu_data[0])
                #     print("这个IP地址可用：" + ipaddress[0])
                #
                # else:
                #     print(ipaddress[0] + "这个地址不可用。")
                #     pass
                #     continue




                sql = 'insert into ipaddress(ip) values("'+ipaddress[o]+'")'
                cursor.execute(sql)
                conn.commit()

        cursor.close()
        conn.close()




