# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.item import Field


class BookspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class DdPipeline(scrapy.Item):
    '''定义小说字段'''
    book_name = Field()
    book_url = Field()
    book_author = Field()
    book_id = Field()
    book_number = Field()
    book_state = Field()
    book_type = Field()
