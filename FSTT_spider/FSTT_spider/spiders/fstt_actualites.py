import scrapy
from ..items import FaculteActualite


class FsttActualitesSpider(scrapy.Spider):
    name = "fstt_actualites"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/category/articles/actualites/"]

    def parse(self, response):
        pages = response.css('h3.elementor-post__title a::attr(href)').extract()
        for page in pages:
            yield response.follow(page, callback=self.parse_link)
        next_page_link = response.css('div.pgntn-page-pagination-block a::attr(href)').extract()
        for link in next_page_link:
            yield response.follow(link, callback=self.parse)
    def parse_link(self, response):
        item = FaculteActualite()
        item["url"] = response.url
        item["title"] = response.css('h2.elementor-heading-title::text').extract_first()
        item["content"] = response.css('div.elementor-element-faf7450 div.elementor-widget-container').xpath('string()').get().strip()

        yield item
