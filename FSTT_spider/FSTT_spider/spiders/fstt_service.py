import scrapy


class FsttServiceSpider(scrapy.Spider):
    name = "fstt_service"
    start_urls = ["https://fstt.ac.ma/Portail2023/"]

    def parse(self, response):
        section = response.css('section[data-id="68b4d04"]')
        links = section.css('h4.elementor-heading-title a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback=self.pars_link)
    def pars_link(self, response):
        service = response.css('h2.elementor-heading-title::text').extract_first()
        Brief = response.css('div.elementor-text-editor ::text').extract()
        Brief = ' '.join(Brief).strip()
        accordion_items = response.css('div.elementor-accordion-item')
        print('Service:',service)
        print('Brief',Brief)
        for item in accordion_items:
            title = item.css('.elementor-accordion-title::text').get().strip()
            content = item.css('div.elementor-tab-content').xpath('string()').get()
        print('Title:',title)
        print('Content:',content)


