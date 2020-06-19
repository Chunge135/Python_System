# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem #导入容器
from scrapy.http import Request #导入scrapy的请求包

class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com'] #爬取的域名允许范围
    # start_urls = ['http://https://www.qiushibaike.com//'] 这是首次爬取地址，由于我们要伪装成浏览器，所以需要修改。

    def start_requests(self): #首次爬取的函数
        #ua就是伪装浏览器对象4
        ua = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

        #返回浏览器伪装的头部
        yield Request("https://www.qiushibaike.com/", headers = ua)

    def parse(self, response): #爬虫正文部分
        it = FirstItem()
        it["content"] = response.xpath("//a[@class='recmd-content']/text()").extract() #利用xpath来筛选文本信息。
        it["link"] = response.xpath("//a[@class='recmd-content']/@href").extract() #利用xpath来筛选链接信息。
        yield it
