import scrapy
from ..items import FaculteFormationInitial


class FormationInitialeSpider(scrapy.Spider):
    name = "FORMATION-INITIALE"
    start_urls = ["https://fstt.ac.ma/Portail2023/formation-initiale/"]

    def parse(self, response):
        item = FaculteFormationInitial()
        item["url"] = response.url
        item["title"] = response.css('div.elementor-widget-container h2.elementor-heading-title').xpath('string()').extract_first()
        item["Content"] = response.css('div.elementor-text-editor').xpath('string()').get().strip()
        yield item