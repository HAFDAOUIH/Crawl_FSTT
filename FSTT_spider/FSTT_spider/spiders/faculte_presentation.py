import scrapy
from ..items import FacultePresentation

class FacultePresentationSpider(scrapy.Spider):
    name = "faculte_presentation"
    start_urls = ["https://fstt.ac.ma/Portail2023/presentation/"]

    def parse(self, response):
        item = FacultePresentation()
        item["title"] = response.css('h2.elementor-heading-title::text').extract_first()
        content_elements = response.css('div.elementor-widget-container div.elementor-text-editor').xpath('string()').extract()
        item["content"] = ' '.join(content_elements).strip().replace('\n', '').replace('\t', '').replace('\xA0', ' ')

        yield item

