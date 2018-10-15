# -*- coding: utf-8 -*-
import scrapy
import datetime
import logging

import pandas as pd

from trail.items import TrailItem, AjaxItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.http import Request, FormRequest


class EasySpider(CrawlSpider):
    name = 'loginAjaxCsv'
    allowed_domains = ['www.1point3acres.com']

    def start_requests(self):
        return [
            Request(
                'https://www.1point3acres.com/bbs/forum-237-1.html',
                callback=self.parse_welcome)
        ]

    def parse_welcome(self, response):
        return FormRequest.from_response(
            response,
            formdata={'username': '7874364@gmail.com', 'password': ''}
        )

    # rules = (
    #     Rule(LinkExtractor(restrict_xpaths='//a[@class = "nxt"]')),
    # )
 
    def parse(self, response):
        queryOptions = [('Title', 3124), ('BaseSalary',3121), ('Equity',3122), ('SignBonus',3125), ('YearlyBonus',3123)]
        ajax_url = "https://www.1point3acres.com/bbs/forum.php?mod=misc&action=protectsort&tid={0}&optionid={1}&inajax=1"

        df = pd.read_csv('./log/item.csv')
        for PostID in df.PostID.values:
            for i in queryOptions:
                # logging.warning(ajax_url.format(PostID,i[1]))
                yield Request(ajax_url.format(PostID,i[1]),meta={'RequestType':i[0], 'PostID':PostID}, callback=self.parse_ajax_request)

    def parse_ajax_request(self, response):
        ajax_item = AjaxItem()
        ajax_item['PostID'] = response.meta['PostID']
        ajax_item['DataType'] = response.meta['RequestType']
        ajax_item['Data'] = response.xpath('/root/text()').extract()
        yield ajax_item

