import scrapy


class FaculteContactSpider(scrapy.Spider):
    name = "faculte_contact"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/contact/"]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        content_elements = response.css('li.elementor-icon-list-item')
        content = ' '.join(content_elements).strip().replace('\n', '').replace('\t', '').replace('\xA0', ' ')

        yield {
            'title:': title,
            'content: ': content,
        }
