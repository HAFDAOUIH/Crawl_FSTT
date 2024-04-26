# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EspaceEntrep(scrapy.Item):
    title = scrapy.Field()
    qui_sommes_nous = scrapy.Field()
    objectif = scrapy.Field()
    Comment = scrapy.Field()
    activite_service = scrapy.Field()
