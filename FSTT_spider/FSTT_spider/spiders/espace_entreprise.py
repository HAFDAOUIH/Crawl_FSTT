import scrapy
from ..items import EspaceEntrep


class EspaceEntrepriseSpider(scrapy.Spider):
    name = 'espace-entreprise'
    start_urls = ['https://fstt.ac.ma/Portail2023/centre-dincubation-de-techno-entrepreneuriat-yabda/']

    def parse(self, response):
        item = EspaceEntrep()
        item["url"] = response.url
        item['title'] = response.css('h2.elementor-heading-title::text').extract_first()
        item['qui_sommes_nous'] = response.css('div#elementor-tab-content-2301').xpath('string()').extract()
        item['objectif']= response.css('div#elementor-tab-content-2302').xpath('string()').extract()
        item['Comment'] = response.css('div#elementor-tab-content-2303').xpath('string()').extract()
        item['activite_service'] = response.css('div#elementor-tab-content-2304').xpath('string()').extract()

        yield item
