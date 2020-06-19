import pymysql
import urllib.request
import re
import urllib.error





headers = ("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

url = "https://p.3.cn/prices/mgets?callback=jQuery2227984&type=1&area=19_1601_50258_51885&pdtk=&pduid=681742069&pdpin=&pin=null&pdbp=0&skuIds=J_100005171461%2CJ_65991639970%2CJ_64612902240%2CJ_69709170058%2CJ_61192828749%2CJ_598827%2CJ_2606374%2CJ_100004918074%2CJ_5155905%2CJ_6772447%2CJ_854803&ext=11100000&source=item-pc"
data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat = '"l":"(.*?)",'
price = re.compile(pat).findall(data)
conn = pymysql.connect("localhost", "root", "root", "jd")
cursor = conn.cursor()
# for i in range(0,len(price)):
#     sql = 'insert into price(price) values("' + price[0] + '")'
#     cursor.execute(sql)
#     conn.commit()
#     print(price[0])
sql = 'insert into price(price) values("' + price[0] + '")'
cursor.execute(sql)
conn.commit()
print(price[0])
cursor.close()
conn.close()

# id = ["43173008309","53609155374","/45253458632","/45253458632","/49453991984"]
# for i in range(0, len(id)):
#     url = "https://c.3.cn/recommend?callback=jQuery8551615&sku=" + id[i] + "&cat=9987%2C653%2C655&area=19_1601_50258_51885&methods=suitv2&count=6&_=1589373156507"
#     try:
#         data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
#         pat = '6000,"finalPrice":(.*?),'
#         price = re.compile(pat).findall(data)
#         print(data)
#
#         for i in range(0, len(price)):
#             print(price[i])
#
#     except urllib.error.URLError as e:
#         if hasattr(e, "code"):
#             print(e.code)
#         if hasattr(e, "reason"):
#             print(e.reason)

# conn = pymysql.connect("localhost", "root", "root", "jd")
# cursor = conn.cursor()
#
# title = "sfbsgsfdb,","sdfbsdfbdsbfdsfb","fndbmfmhhf"
# price = "fadbgbgfrbgb","jsfbgebgav","sdfbdsbbsvcvc"
# product_url = "sdfbsdbdb","afvcvxzcvzvc","fndbmfmhhf"
# shopname = "sfbsdfbsdfb","zcvvafdfabv","fndbmfmhhf"
# shoplink = "sdfbdsbfdsfd","afdvcbsvcbds",""
#
# for i in range(0,len(title)):
#     title1 = title[i]
#     price1 = price[i]
#     product_url1 = product_url[i]
#     shopname1 = shopname[i]
#     shoplink1 = shoplink[i]
#     if(len(title1) and len(price1) and len(product_url1) and len(shopname1) and len(shoplink1)):
#         sql = 'insert into jdd(title,price,product_url,shopname,shoplink) values("'+title1+'","'+price1+'","'+product_url1+'","'+shopname1+'","'+shoplink1+'")'
#         cursor.execute(sql)
#         conn.commit()
#         print(sql)
#
#     else:
#         print("有信息不全的商品未写入")
#
# cursor.close()
# conn.close()


