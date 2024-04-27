import scrapy
from ..items import FaculteFormationContinueInfo


class FormationContinueInformationsSpider(scrapy.Spider):
    name = 'FORMATION_CONTINUE_informations'
    start_urls = ['http://formation-continue.ma/index.php/formation-continue/dcess/',
                  'http://formation-continue.ma/index.php/formation-continue/dca']

    def parse(self, response):
        links = response.css('span.lead a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_content)
    def parse_content(self, response):
        item = FaculteFormationContinueInfo()
        item["Formation"] = response.css('h3.ja-masshead-title span::text').get()
        item["Filiere"] = response.css('div.SPDetailEntry h1::text').get()
        Responsable_raw = response.css('div.field_responsable').xpath('string()').get().strip()
        Responsable = Responsable_raw.split(':')
        item["Responsable"] = Responsable[1].replace('\n', '').strip()
        item["Objectif"] = response.xpath('//label[@for="Objectif de la formation"]/following-sibling::div[@class="contenu"]').xpath('string()').get().replace('\n', '').replace('\r', '').replace('\xa0', '').strip()
        item["Public_concerne"] = response.xpath('//label[@for="Public concerné"]/following-sibling::div[@class="contenu"]').xpath('string()').get().replace('\n', '').replace('\r', '').replace('\xa0', '').strip()
        item["debouche"] = response.xpath('//label[@for="Débouchés"]/following-sibling::div[@class="contenu"]').xpath('string()').extract()


        yield item



