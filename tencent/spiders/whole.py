import scrapy
from tencent import items
import json
import time
import re


class WholeSpider(scrapy.Spider):
    name = 'whole'
    allowed_domains = ['tencent.com']
    # timestamp = str(int(time.time() * 1000))
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1645007626057&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        # pass
        res_dict = json.loads(response.text)
        target = res_dict['Data']['Posts']
        # for i in range(len(target)):
        #     # time.sleep(1)
        #     item['name'] = target[i]['RecruitPostName']
        #     item['link'] = target[i]['PostURL']
        #     item['date'] = target[i]['LastUpdateTime']
        #     item['city'] = target[i]['LocationName']
        #     item['resp'] = target[i]['Responsibility'].strip().replace('\xa0', ' ').replace('\n', '')
        #     postid = target[i]['PostId']
            # 含有目标的详情页的地址为:https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp='十三位时间戳''&postId='item['link']可以提取到'&language=zh-cn
        name = re.findall(r'"RecruitPostName":"(.*?)"', response.text)
        link = re.findall(r'"PostURL":"(.*?)"', response.text)
        date = re.findall(r'"LastUpdateTime":"(.*?)"', response.text)
        city = re.findall(r'"LocationName":"(.*?)"', response.text)
        resp = re.findall(r'"Responsibility":"(.*?)"', response.text)
        postid = re.findall(r'"PostId":"(\d*?)"', response.text)
        print(postid)
        num = len(postid)
        # time.sleep(0.5)
        for i in range(num):
            item = items.WholeItem()
            item['postid'] = postid[i]
            item['name'] = name[i]
            item['link'] = link[i]
            item['date'] = date[i]
            item['city'] = city[i]
            item['resp'] = resp[i].strip().replace('\xa0', ' ').replace('\\n', '').replace('\\r', '').replace('\\t', '')
            url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1645007626057&postId=' + postid[i] + '&language=zh-cn'
            print(url)
            # time.sleep(2)
            yield scrapy.Request(url=url, callback=self.require_parse, meta={'item': item})
        # self.num += 1
        # # 接下来翻页
        # time.sleep(1)
            for num in range(2, 1000):
                if response.status == 200:
                    # timestamp =
                    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1645007626057&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=' + str(
                        num) + '&pageSize=10&language=zh-cn&area=cn'
                    yield scrapy.Request(url=url, callback=self.parse)
                else:
                    break

    def require_parse(self, response):
        # time.sleep(0.5)
        # 解析详情页面
        item = response.meta['item']
        # res_dict = json.loads(response.text)
        # target =
        # item['require'] = res_dict['Data']['Requirement'].replace('\n', '')
        item['require'] = re.search(r'"Requirement":"(.*?)"', response.text).group(1).strip().replace('\\n', '').replace('\\r', '').replace('\\t', '')
        print(item)
        yield item






