import scrapy
from ..items import FaculteRechercheStruct


class RechercheStructSpider(scrapy.Spider):
    name = "recherche_struct"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/laboratoires-de-recherche/"]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        links = response.css(
            'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element::attr(data-wts-url)').getall()

        for link in links:
            yield response.follow(link, callback=self.parse_content, meta={'title': title})

    def parse_content(self, response):
        item = FaculteRechercheStruct()
        item["url"] = response.url
        item["title"] = response.meta['title']
        # Extract name of Lab
        item["laboratoire"] = response.css('h2.elementor-heading-title::text').extract_first()
        # Extract nom Directeur du lab
        item["directeur_infos"] = response.css('div#elementor-tab-content-1671').xpath('string()').get()
        # Extract les equipes de recherche
        item["equipes_recherche"] = response.css('div#elementor-tab-content-1672').xpath('.//strong').xpath('string()').getall()
        # Extract axes de recherche
        item["axes_recherche"] = response.css('div#elementor-tab-content-1673').xpath('.//strong').xpath('string()').getall()
        # Extract projets de recherche
        item["projets_recherche_link"] = response.css('div#elementor-tab-content-1674 a::attr(href)').getall()
        # Extract these et habilitations soutenues
        item["these_habil_soutenues_link"] = response.css('div#elementor-tab-content-1675 a::attr(href)').get()



        yield item