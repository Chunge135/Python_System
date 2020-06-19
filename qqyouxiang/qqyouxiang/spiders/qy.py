# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class QySpider(scrapy.Spider):
    name = 'qy'
    allowed_domains = ['mail.qq.com']
    # start_urls = ['http://mail.qq.com/']
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    def start_requests(self):
        return [Request("https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&appid=522005705&daid=4&s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input_for_xmail440503.css",
                        callback=self.parse,
                        meta={"cookiejar": 1}
                        )]

    def parse(self, response):
        url = "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?target=self&appid=522005705&daid=4&s_url=https://mail.qq.com/cgi-bin/readtemplate?check=false%26t=loginpage_new_jump%26vt=passport%26vm=wpt%26ft=loginpage%26target=&style=25&low_login=1&proxy_url=https://mail.qq.com/proxy.html&need_qr=0&hide_border=1&border_radius=0&self_regurl=http://zc.qq.com/chs/index.html?type=1&app_id=11005?t=regist&pt_feedback_link=http://support.qq.com/discuss/350_1.shtml&css=https://res.mail.qq.com/zh_CN/htmledition/style/ptlogin_input_for_xmail440503.css"
        print("此时没有验证码")
        data = {
            "u": "1018519231",
            "p": "lichunlin1328",

        }
        print("登陆中……")

        return [FormRequest.from_response(response,
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          headers=self.header,
                                          formdata=data,
                                          callback=self.__next__
                                          )]
        print("准备调用next函数")

    def __next__(self, response):
        print("开始调用")
        print("此时已经登陆完成，并爬取了信息")
        title = response.xpath("/html/head/title").extract()

        print(title)

