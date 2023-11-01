# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    origin = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    company_name = scrapy.Field()
