# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JingdongPipeline:
    def process_item(self, item, spider):
        # pass
        #连接数据库
        # conn = pymysql.connect("localhost", "root", "root", "jd")
        # cursor = conn.cursor()
        #
        # for i in range(0, len(item["title"])):
        #     #遍历获取的信息
        #     title = item["title"][i]
        #     shopname = item["shopname"][i]
        #     price = item["price"][i]
        #     shoplink = item["shoplink"][i]
        #     product_url = item["product_url"][i]
        #
        #     # 判断商品信息是否完整，不完整不存入数据库
        #     if (len(title) and len(shopname) and len(shoplink) and len(price) and len(product_url)):
        #         sql = 'insert into jdd(title,price,product_url,shopname,shoplink) values("'+title+'","'+price+'","'+product_url+'","'+shopname+'","'+shoplink+'")'
        #         cursor.execute(sql)
        #         conn.commit()
        #         print(title)
        #         print(price)
        #         print(product_url)
        #         print(shopname)
        #         print(shoplink)
        #     else:
        #         print("有商品的信息不全，不给予记录。")
        # cursor.close()
        # conn.close()

        return item

