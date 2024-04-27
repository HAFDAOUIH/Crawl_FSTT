import scrapy
from ..items import EspaceEtuClub

class EspaceEtudiantClubsSpider(scrapy.Spider):
    name = 'espace-etudiant-clubs'
    start_urls = ['https://fstt.ac.ma/Portail2023/clubs//']

    def parse(self, response):
        links = response.css('div.has_eae_slider.elementor-column.elementor-col-50::attr(data-wts-url)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_content)
    def parse_content(self, response):
        item = EspaceEtuClub()
        item["title_club"] = response.css('h2.elementor-heading-title::text').extract_first()
        item["info_club"] = response.css('div.elementor-element-populated div.elementor-widget-container p').xpath('string()').extract()
        yield item


