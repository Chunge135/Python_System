# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline:
    def __init__(self):
        self.fh = open("F:/pythontext/1.txt","a")

    def process_item(self, item, spider):
        print(item["title"])

        print(item["link"])
        print(item["stu"])
        print("-----------------------------------")
        self.fh.write(item["title"][0] + "\n" + item["link"][0] + "\n" + item["stu"][0] + "\n" + "-----------------------------------" + "\n")
        return item

    def close_spider(self):
        self.fh.close()





