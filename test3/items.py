# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class MyItem(scrapy.Item):
    order=scrapy.Field()#用来保证爬取数据的顺序
    class_name=scrapy.Field()
    class_teacher=scrapy.Field()
    class_school=scrapy.Field()
    class_sum=scrapy.Field()

class Test3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
