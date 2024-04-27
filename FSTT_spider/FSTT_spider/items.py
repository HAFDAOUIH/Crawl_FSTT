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
class EspaceEtuBiblio(scrapy.Item):
    title_biblio = scrapy.Field()
    info_biblio = scrapy.Field()
class EspaceEtuClub(scrapy.Item):
    title_club = scrapy.Field()
    info_club = scrapy.Field()
class FaculteConseilEtab(scrapy.Item):
    Title = scrapy.Field()
    Brief = scrapy.Field()
    Name = scrapy.Field()
    Responsabilite = scrapy.Field()


