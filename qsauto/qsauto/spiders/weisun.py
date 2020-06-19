# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from qsauto.items import QsautoItem #导入容器
from scrapy.http import Request #导入scrapy的请求包


class WeisunSpider(CrawlSpider):
    name = 'weisun'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['http://qiushibaike.com/']

    def start_requests(self): #首次爬取的函数
        #ua就是伪装浏览器对象4
        ua = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

        #返回浏览器伪装的头部
        yield Request("https://www.qiushibaike.com/", headers = ua)

    rules = (
        Rule(LinkExtractor(allow='article/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        i["content"] = response.xpath("//a[@class='recmd-content']/text()").extract()  # 利用xpath来筛选文本信息。
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()  # 利用xpath来筛选链接信息。
        print(i["content"])
        print(i["link"])
        print("---------------------------")
        return i
