import re
import urllib.request


url = "https://passport.csdn.net/login?code=public"
header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
opener = urllib.request.build_opener()
opener.addheaders = [header]
urllib.request.install_opener(opener)

data = urllib.request.urlopen(url)





