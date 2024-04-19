import scrapy


class FormationInitialeSpider(scrapy.Spider):
    name = "FORMATION-INITIALE"
    start_urls = ["https://fstt.ac.ma/Portail2023/formation-initiale/"]

    def parse(self, response):
        title = response.css('div.elementor-widget-container h2.elementor-heading-title').xpath('string()').extract_first()
        Content = response.css('div.elementor-text-editor').xpath('string()').get().strip()
        yield {
            print('Title: ', title),
            print('Content: ', Content)
        }