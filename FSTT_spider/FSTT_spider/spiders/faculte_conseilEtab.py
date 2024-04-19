import scrapy


class FaculteConseiletabSpider(scrapy.Spider):
    name = "faculte_conseilEtab"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/conseil-de-letablissement/"]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        brief_elements = response.css('div.elementor-widget-container div.elementor-text-editor').xpath('string()').extract()
        brief = ' '.join(brief_elements).strip().replace('\n', '').replace('\t', '').replace('\xA0', ' ')

        table_rows = response.css('table tr')
        yield{

        }
