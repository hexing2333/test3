# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
class Mypipeline(object):
    def __init__(self):
        self.file = open('MyData.csv', 'a', newline='',encoding='utf-8') #由于有的老师名字里有大黑点。将encoding设为utf-8
        self.fieldnames = ["order","class_name", "class_teacher", "class_school", "class_sum"]
        self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在__init__里面
        self.writer.writeheader()
        self.items=[]

    def process_item(self, item, spider):
        item_1=item.copy()
        print("item")
        print(item_1)
        self.items.append(item_1) #这里不可以直接进行append(item)，会使得之前元素被覆盖，需要深拷贝后赋值
        print("items")
        for each in self.items:
            print(each)
        return item

    def close_spider(self,spider):
        self.items.sort(key=lambda i:i['order'])
        for it in self.items:
            self.writer.writerow(it)
        self.file.close()
