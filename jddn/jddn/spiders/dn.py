# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
import urllib.request
import re
import pymysql


class DnSpider(CrawlSpider):
    name = 'dn'
    allowed_domains = ['jd.com']
    # start_urls = ['http://jd.com/']

    def start_requests(self):  # 首次爬取的函数
        # ua就是伪装浏览器对象4
        ua = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

        # 返回浏览器伪装的头部
        yield Request("https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%20%E8%BD%BB%E8%96%84%E6%9C%AC&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%20%E8%BD%BB%E8%96%84%E6%9C%AC&page=2&s=100&click=1", headers=ua)

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        product_url = response.xpath('//div[@class="p-img"]/a/@href').extract()
        product_id = response.xpath('//li[@class="gl-item"]/@data-sku').extract()

        conn = pymysql.connect("localhost", "root", "root", "jd")
        cursor = conn.cursor()

        for i in range(0, len(product_url)):
            print(product_url[i])
            print(product_id[i])
            # print(price[i])
            pro_price_url = "https://p.3.cn/prices/mgets?callback=jQuery2227984&type=1&area=19_1601_50258_51885&pdtk=&pduid=681742069&pdpin=&pin=null&pdbp=0&skuIds=J_" + product_id[i]
            data = urllib.request.urlopen(pro_price_url).read().decode("utf-8", "ignore")
            pat = '"p":"(.*?)"}'
            price = re.compile(pat).findall(data)
            print(price)
            print("-------------------------------------------------------------------")
            sql = "insert into jddn(product_url,product_id,price) values('"+product_url[i]+"','"+product_id[i]+"','"+price[i]+"')"
            cursor.execute(sql)
            conn.commit()
        cursor.close()
        conn.close()
        return item
