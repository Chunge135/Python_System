# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DangdangPipeline:
    def process_item(self, item, spider):
        conn = pymysql.connect("localhost", "root", "root", "dangdang")
        cursor = conn.cursor()
        #cursor.execute(sql)
        # conn.commit()
        for i in range(0, len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            sql = 'insert into books(title,link,comment) values("'+title+'","'+link+'","'+comment+'")'
            cursor.execute(sql)
            #conn.commit()
        #cursor.close()
        conn.close()
        return item
