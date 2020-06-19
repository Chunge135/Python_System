# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class CsSpider(scrapy.Spider):
    name = 'cs'
    allowed_domains = ['csdn.net']
    # start_urls = ['http://csdn.net/']

    def start_requests(self):

        return [Request("https://passport.csdn.net/login?code=public",
                        meta={'cookiejar' : 1},
                        callback=self.parse,
                        method="POST"
                        )]

    def parse(self, response):
        pass
