# -*- coding: utf-8 -*-
import scrapy
import datetime


from trail.items import TrailItem

from scrapy.loader import ItemLoader
from scrapy.http import Request

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['www.1point3acres.com']
    start_urls = ['http://www.1point3acres.com/bbs/forum-237-1.html']

    def parse(self, response):
        next_url = response.xpath('//a[@class = "nxt"]/@href').extract_first()
        self.log(next_url)
        yield Request(next_url)
        
        for blog_post in response.xpath('//table[@summary]/tbody[not(@class = "emptb")]/tr'):
            item = TrailItem()
            item['title'] = blog_post.xpath('./th/a[@class = "s xst"]/text()').extract()
            item['url'] = blog_post.xpath('./th/a[@class = "s xst"]/@href').extract()
            yield item