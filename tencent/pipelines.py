# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json





# Whole爬虫的管道
class WholePipeline:

    def open_spider(self, spider):
        if spider.name == 'whole':
            self.file = open('Whole.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'whole':
            item = dict(item)
            str_data = json.dumps(item, ensure_ascii=False) + '\n,'
            self.file.write(str_data)

        # 必须要有return item(且在条件判断之外),不然下一个管道获得的值为None
        return item

    def close_spider(self, spider):
        if spider.name == 'whole':
            self.file.close()




#simple爬虫的管道
class SimplePipeline:

    def open_spider(self, spider):
        if spider.name == 'simple':
            self.file = open('tencent.json', 'w')

    def process_item(self, item, spider):
        if spider.name == 'simple':
            item = dict(item)
            str_data = json.dumps(item, ensure_ascii=False) + '\n,'
            self.file.write(str_data)
        # 必须要有return item(且在条件判断之外),不然下一个管道获得的值为None
        return item

    def close_spider(self, spider):
        if spider.name == 'simple':
            self.file.close()



