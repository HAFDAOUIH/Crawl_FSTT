import scrapy
from ..items import FaculteService

class FsttServiceSpider(scrapy.Spider):
    name = "fstt_service"
    start_urls = ["https://fstt.ac.ma/Portail2023/"]

    def parse(self, response):
        section = response.css('section[data-id="68b4d04"]')
        links = section.css('h4.elementor-heading-title a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.pars_link)
    def pars_link(self, response):
        item = FaculteService()
        item["url"] = response.url
        item["service"] = response.css('h2.elementor-heading-title::text').extract_first()
        Brief = response.css('div.elementor-text-editor ::text').extract()
        item["Brief"] = ' '.join(Brief).strip()
        accordion_items = response.css('div.elementor-accordion-item')
        for items in accordion_items:
            item["title"] = items.css('.elementor-accordion-title::text').get().strip()
            item["content"] = items.css('div.elementor-tab-content').xpath('string()').get()

        yield item


