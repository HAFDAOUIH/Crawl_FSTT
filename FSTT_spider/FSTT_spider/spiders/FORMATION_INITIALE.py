import scrapy


class FormationInitialeSpider(scrapy.Spider):
    name = "FORMATION-INITIALE"
    start_urls = ["https://fstt.ac.ma/Portail2023/formation-initiale/"]

    def parse(self, response):
        Content = response.css('div.elementor-text-editor').xpath('string()').get().strip()
        yield print(Content)
