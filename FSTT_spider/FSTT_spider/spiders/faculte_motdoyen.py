import scrapy
from ..items import FaculteMotDoyen


class FaculteMotdoyenSpider(scrapy.Spider):
    name = "faculte_motdoyen"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/mot-du-doyen/"]

    def parse(self, response):
        item = FaculteMotDoyen()
        item["title"]= response.css('h2.elementor-heading-title::text').extract_first()
        content_elements = response.css('div.elementor-widget-container div.elementor-text-editor').xpath(
            'string()').extract()
        item["content"] = ' '.join(content_elements).strip().replace('\n', '').replace('\t', '').replace('\xA0', ' ')

        yield item
