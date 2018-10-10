# -*- coding: utf-8 -*-
import scrapy
import datetime
import logging

from trail.items import TrailItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.http import Request, FormRequest


class EasySpider(CrawlSpider):
    name = 'login'
    allowed_domains = ['www.1point3acres.com']
    # start_urls = ['http://www.1point3acres.com/bbs/forum-237-1.html']

    def start_requests(self):
        return [
            Request(
                'http://www.1point3acres.com/bbs/forum-237-1.html',
                callback=self.parse_welcome)
        ]

    def parse_welcome(self, response):
        return FormRequest.from_response(
            response,
            formdata={'username': '', 'password': ''}
        )

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//a[@class = "nxt"]')),
        Rule(LinkExtractor(restrict_xpaths='//a[@class = "s xst"]'),callback='parse_item'),
    )
 

    def parse_item(self, response):
        item = TrailItem()

        item['PostTitle'] = response.xpath('//*[@id="thread_subject"]/text()').extract()
        item['PostUser'] = response.xpath('//*[@class="authi"]/a/text()').extract_first()
        item['PostTime'] = response.xpath('//*[@class="authi"]//span/@title').extract_first()
        
        item['URL'] = response.url
        item['SpiderTime'] = datetime.datetime.now()
        
        table =  response.xpath('//table[@class="cgtl mbm"]//td/text()').extract()
        
        if len(table) == 27:
            item['Year'] = table[0].strip()
            item['Season'] = table[1].strip()
            item['Source'] = table[2].strip()
            
            item['JobFunction'] = table[3].strip()
            item['JobType'] = table[4].strip()
            
            item['Degree'] = table[5].strip()
            item['Experience'] = table[6].strip()
            item['ExperienceLevel'] = table[7].strip()
            item['Group'] = table[8].strip()
            item['InterestPoint'] = table[9].strip()
            item['Title'] = table[10].strip()
            item['Level'] = table[11].strip()
            item['PositionType'] = table[12].strip()
            item['CompanyName'] = table[13].strip()
            item['CompanyAltName'] = table[14].strip()
            item['Area'] = table[15].strip()
            item['BaseSalary'] = table[16].strip()
            item['Equity'] = table[17].strip()
            item['EquitySchedule'] = table[18].strip()
            item['SignBonus'] = table[19].strip()
            item['YearlyBonus'] = table[20].strip()
            item['RelocationFee'] = table[21].strip()
            item['OtherOffer'] = table[22].strip()
            item['GreenCard'] = table[23].strip()
            item['Satisfaction'] = table[24].strip()
            item['PromotionPkg'] = table[25].strip()
            item['AnnualRefresh'] = table[26].strip()
            return item
        else:
            logging.warning(response.body)
            return item