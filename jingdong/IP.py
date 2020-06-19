import urllib.request
import urllib.error
import re


def use_proxy(url, proxy_addr):
        try:
                proxy = urllib.request.ProxyHandler({"http": proxy_addr})
                opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
                urllib.request.install_opener(opener)
                data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
                return data

        except urllib.error.URLError as e :
                print(e)
                pass

headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

proxy_addr = "223.241.2.247:4216"
url = "http://www.baidu.com"

data = use_proxy(url, proxy_addr)
print(any(data))


#有些代理IP是无效的，自行更换就好了