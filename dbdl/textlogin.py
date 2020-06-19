from urllib import response

import requests
import re

class login(object):
    def __init__(self):
        self.headers={"Referer": "https://accounts.douban.com/passport/login_popup?login_source=anony",
                      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
                      "Host": "accounts.douban.com"}

        self.login_url="https://accounts.douban.com/passport/login"
        self.post_url="https://accounts.douban.com/j/mobile/login/basic"
        self.logined_url="https://www.douban.com/people/216583360/"
        self.session=requests.Session()

    def login(self):
        post_dat={"ck":"",
                  "name": "13126491706",
                  "password": "li13126491706",
                  "remember": "false",
                  "ticket":""
                      }
        response=self.session.post(self.post_url,data=post_dat,headers=self.headers)
        if response.status_code == 200:
            print("成功登陆")
            self.dynamics(response.text)

        response=self.session.get(self.logined_url,headers=self.headers)
        if response.status_code == 200:
            print("个人页面获取成功")
            self.dynamics(response.text)


    def dynamics(self,html):
        pat = '<title>(.*?)</title>'
        title = re.compile(pat).findall(html)
        for i in range(0,len(title)):
            print(title[i])