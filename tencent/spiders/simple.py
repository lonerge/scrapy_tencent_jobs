import scrapy
from tencent import items
import json
import time


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['tencent.com']
    # start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1644993808468&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + str(int(time.time() * 1000)) + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=' + '2' + '&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        # pass
        item = items.TencentItem()
        res_dict = json.loads(response.text)
        target = res_dict['Data']['Posts']
        for i in range(len(target)):
            item['name'] = target[i]['RecruitPostName']
            item['link'] = target[i]['PostURL']
            item['date'] = target[i]['LastUpdateTime']
            item['city'] = target[i]['LocationName']
            item['resp'] = target[i]['Responsibility'].strip().replace('\xa0', ' ').replace('\n', '')
            print(item)
            yield item

        # print(response.status, type(response.status))
        # 翻页
            num = 3

            if response.status == 200:
                timestamp = str(int(time.time()*1000))
                url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=' + timestamp + '&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=' + str(num) + '&pageSize=10&language=zh-cn&area=cn'
                num += 1
                yield scrapy.Request(url=url, callback=self.parse)
            else:
                break





