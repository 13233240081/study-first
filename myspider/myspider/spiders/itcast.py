# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    # 爬虫名字
    name = 'itcast'
    # 允许爬取的范围，防止爬虫爬取别的网站
    allowed_domains = ['itcast.cn']
    # 开始爬取的url地址
    start_urls = ['http://itcast.cn/channel/teacher.shtml']

    # 数据提取的方法，接受下载中间件传过来的response
    def parse(self, response):
#         scrapy的response对象可以直接进行xpath
        names = response.xpath('//div[@class="tea_con"]//li/div/h3/text()')
        print(names)

#     获取具体数据文本的方式如下
#         分组
        li_list = response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
#             创建一个数据字典
            item = {}
#           利用scrapy封装好的xpath选择器定位元素，并通过extract（）或extract_first()来获得结果
            item['name'] = li.xpath('.//h3/text()').extract_first()
            item['level'] = li.xpath('.//h4/text()').extract_first()
            item['text'] = li.xpath('.//p/text()').extract_first()
            print(item)
            yield item
