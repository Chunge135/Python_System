# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from jingdong.items import JingdongItem
import urllib.request
import urllib.error
import pymysql



class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']



    # def start_requests(self):
    #     headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    #
    #     yield Request("http://jd.com/", headers=headers)

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_item', follow=True),
    )

    def parse_item(self, response):


                item = JingdongItem()
                #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
                #item['name'] = response.xpath('//div[@id="name"]').get()
                #item['description'] = response.xpath('//div[@id="description"]').get()

                #获取请求到的链接
                thisurl = response.url
                #配置正则表达式，帅选商品链接
                pat = "item.jd.com/(.*?).html"
                x = re.search(pat, thisurl)
                conn = pymysql.connect("localhost", "root", "root", "jd")
                cursor = conn.cursor()

                #判断是否存在链接
                if(x):

                    #获取商品的ID
                    thisid = re.compile(pat).findall(thisurl)[0]
                    # print(thisid)

                    #筛选出商品名字
                    # item["title"] = response.xpath("//html/head/title/text()").extract()
                    # print(item["title"][0])
                    title = response.xpath("//html/head/title/text()").extract()
                    # print(title[0])

                    #商店的名字
                    # item["shopname"] = response.xpath("//div[@class='name']/a/text()").extract()
                    # print(item["shopname"][0])
                    shopname = response.xpath("//div[@class='name']/a/text()").extract()
                    # print(shopname[0])

                    #商店的链接
                    # item["shoplink"] = response.xpath("//div[@class='name']/a/@href").extract()
                    # print(item["shoplink"][0])
                    shoplink = response.xpath("//div[@class='name']/a/@href").extract()
                    # print(shoplink[0])

                    #商品的价格
                    price_url = "https://c.3.cn/recommend?callback=jQuery8551615&sku=" + str(thisid) +"&cat=9987%2C653%2C655&area=19_1601_50258_51885&methods=suitv2&count=6&_=1589373156507"
                    price_data = urllib.request.urlopen(price_url).read().decode("utf-8", "ignore")
                    price_pat = '6000,"finalPrice":(.*?),'
                    # item["price"] = re.compile(pat).findall(price_data)
                    # print(item["price"][0])
                    price = re.compile(price_pat).findall(price_data)
                    # print(price[0])

                    #商品链接
                    # item["product_url"] = response.xpath("//div[@class='p-img']/a/@href").extract()
                    # print(item["product_url"][0])
                    product_url = response.xpath("//div[@class='p-img']/a/@href").extract()
                    # print(product_url[0])

                    print("-------------------------------------------------------")

                    #商品的评论

                    if (len(title) and len(shopname) and len(shoplink) and len(price) and len(product_url)):  #and len(price)
                        # sql = 'insert into jdd(title,price,product_url,shopname,shoplink) values("'+title[0]+'","'+price[0]+'","'+product_url[0]+'","'+shopname[0]+'","'+shoplink[0]+'")'
                        # cursor.execute(sql)
                        # conn.commit()
                        print(title)
                        print(price[0])
                        print(product_url)
                        print(shopname)
                        print(shoplink)
                        print("数据库写入部分-----------------------------------------------------------------------")
                    else:
                        print("有商品的信息不全，不给予记录。")

                    # sql = 'insert into jdd(title,price,product_url,shopname,shoplink) values("'+title[0]+'","'+price[0]+'","'+product_url[0]+'","'+shopname[0]+'","'+shoplink[0]+'")'
                    # cursor.execute(sql)
                    # conn.commit()
                    # print(title[0])
                    # print(price[0])
                    # print(product_url[0])
                    # print(shopname[0])
                    # print(shoplink[0])

                    cursor.close()
                    conn.close()

                else:
                    pass
                return item


