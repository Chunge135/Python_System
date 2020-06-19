# -*- coding: utf-8 -*-
import scrapy


class NdbSpider(scrapy.Spider):
    name = 'ndb'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/']
    ua = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q = 0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}

    def parse(self, response):
        data={
            "name":"13126491706",
            "password":"li13126491706",
            "redir":"https://www.douban.com/people/216583360/"
        }

        yield scrapy.FormRequest.from_response(response,
                                               formdata=data,
                                               callback=self.__next__
                                               )

    def __next__(self,response):
        title = response.xpath("/html/head/title/text()").extract()
        print(title[0])




