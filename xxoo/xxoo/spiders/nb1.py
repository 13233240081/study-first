import scrapy

# 继承下方这个类
class nb1(scrapy.Spider):
    name = "nb1"
    def start_requests(self):
        #   定义爬取的链接
        urls = [
            'http://lab.scrapyd.cn/page/1/',
            'http://lab.scrapyd.cn/page/2/',
       ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'mingyan-%s.html' % page
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('保存文件：%s'%filename)