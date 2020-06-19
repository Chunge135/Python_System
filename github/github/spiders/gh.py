# -*- coding: utf-8 -*-
import scrapy

class GhSpider(scrapy.Spider):
    name = 'gh'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        data={"login":"1018519231@qq.com",
              "password":"li13126491706"
              }

        yield scrapy.FormRequest.from_response(response,
                                               formdata=data,
                                               callback=self.__next__
                                               )


    def __next__(self,response):
        title = response.xpath("/html/head/title/text()").extract()
        print(title[0])
