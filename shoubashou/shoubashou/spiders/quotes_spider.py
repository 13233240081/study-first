# import scrapy
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/3/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url,callback=self.parse)
#     def parse(self, response):
#         for quote in response.css('div.quote'):
#             yield{
#                 'text':quote.css('span.text::text').extract_first(),
#                 'author':quote.css('small.author::text').extract_first(),
#                 'tags':quote.css('div.tags a.tag::text').extract(),
#             }
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename,'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)

from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.http import Request,FormRequest
from shoubashou.items import ShoubashouItem
