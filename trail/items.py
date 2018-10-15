# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class TrailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    PostTitle = Field()
    PostUser = Field()
    PostTime = Field()
    PostID = Field()
    
    Year = Field()
    Season = Field()
    Source = Field()
    
    JobFunction = Field()
    JobType = Field()
    
    Degree = Field()
    Experience = Field()
    ExperienceLevel = Field()
    Group = Field()
    InterestPoint = Field()

    Title = Field()
    Level = Field()
    PositionType = Field()
    CompanyName = Field()
    CompanyAltName = Field()
    Area = Field()

    BaseSalary = Field()
    Equity = Field()
    EquitySchedule = Field()
    SignBonus = Field()
    YearlyBonus = Field()

    RelocationFee = Field()
    OtherOffer = Field()
    GreenCard = Field()
    Satisfaction = Field()
    PromotionPkg = Field()
    AnnualRefresh = Field()
    
    URL = Field()
    SpiderTime = Field()


class AjaxItem(scrapy.Item):
    PostID = Field()
    Data = Field()
    DataType = Field()