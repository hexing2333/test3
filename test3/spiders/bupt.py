import scrapy
import json
from test3.items import MyItem
class bupt(scrapy.spiders.Spider):
    name = "bupt"
    allowed_domains=["xuetangx.com"]
    start_urls=["https://www.xuetangx.com/search?query=&org=&classify=1&type=&status=&page=1"]
    def parse(self,response):
        request_url="https://www.xuetangx.com/api/v1/lms/get_product_list/?page=1"
        cookies={
            'provider=xuetang; django_language=zh;'
        }
        headers={
            'accept': 'application/json, text/plain, */*',
            'accept-Encoding': 'gzip, deflate, br',
            'accept-Language': 'zh',
            'x-client': 'web',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
            'xtbz': 'xt',
            'content-type': 'application/json',
        }
        post_data={"query":"","chief_org":[],"classify":["1"],"selling_type":[],"status":[],"appid":"10000"}
        k=1
        while k<38:
            request_url="https://www.xuetangx.com/api/v1/lms/get_product_list/?page="+str(k)
            yield scrapy.Request(
                url=request_url,
                method='POST',
                body=json.dumps(post_data),
                headers=headers,
                meta={'order':k},
                callback=self.parse_after
            #cookies=cookies
            )
            k+=1

    def parse_after(self,response):
        item=MyItem()
        print(response.body.decode())
        hjson=json.loads(response.body)
        numbers=len(hjson['data']['product_list'])
        print(numbers)
        for i in range(numbers):
            teacher=""
            item['class_name']=hjson['data']['product_list'][i]['name']
            print(item['class_name'])
            for j in range(len(hjson['data']['product_list'][i]['teacher'])):
                teacher+=hjson['data']['product_list'][i]['teacher'][j]['name']+" "
            item['order']=response.meta['order']
            print(item['order'])
            item['class_teacher'] = teacher
            print(item['class_teacher'])
            item['class_school'] = hjson['data']['product_list'][i]['org']['name']
            print(item['class_school'])
            item['class_sum'] = hjson['data']['product_list'][i]['count']
            print(item['class_sum'])
            yield(item)
        #print(response.body.decode())