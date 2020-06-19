# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item["content"])): #把爬取的东西，从数组里面循环打印出来
            print(item["content"][i])
            print(item["link"][i])
            return item
