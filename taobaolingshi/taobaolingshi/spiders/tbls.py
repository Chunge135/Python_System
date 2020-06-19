# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request


class TblsSpider(scrapy.Spider):
    name = 'tbls'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']

    def parse(self, response):
        pass
