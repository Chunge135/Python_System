# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    # start_urls = ['http://douban.com/']

    def start_requests(self): #首次爬取的函数
        #返回浏览器伪装的头部
        return [Request("https://accounts.douban.com/j/mobile/login/basic",
                        headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'},
                        callback = self.parse,
                        meta = {"cookiejar" : 1}
                        )]


    def parse(self, response):
        captcha = response.xpath("//img[@id = 'captcha_image']/@src").extract()

        if len(captcha) > 0:
            print("此时有验证码")
            localpath = "F:/pythontext/captcha.png"
            urllib.request.urlretrieve(captcha[0], filename = localpath)
            print("请查看本地的验证码图片，并输入验证码：")
            captcha_value = input()
            data = {
                "username": "13126491706",
                "password": "li13126491706",
                "captcha-solution" : captcha_value,
            }

            print("登陆中……")

        else:
            url = "https://accounts.douban.com/j/mobile/login/basic"
            print("此时没有验证码")
            data = {
                "username" : "13126491706",
                "password" : "li13126491706",
            }
        print("登陆中……")

        return [FormRequest.from_response(response,
                                            meta = {"cookiejar":response.meta["cookiejar"]},
                                            headers = self.header,
                                            formdata=data,
                                            callback=self.next,
                                            )]


    def next(self, response):
        print("此时已经登陆完成，并爬取了信息")
        title = response.xpath("/html/head/title/text()").extract()
        note = response.xpath("//div[@class='content']/text()").extract()

        print(title[0])
        print(note[0])

