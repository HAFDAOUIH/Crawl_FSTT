import scrapy
from ..items import FaculteFormationInitialInfo
class FormationInitialeLstSpider(scrapy.Spider):
    name = "FORMATION-INITIALE-informations"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = [
        "https://fstt.ac.ma/Portail2023/cycle-licence/",
        "https://fstt.ac.ma/Portail2023/deust/",
        "https://fstt.ac.ma/Portail2023/cycle-master/"
    ]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        links = response.css('div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element::attr(data-wts-url)').getall()

        for link in links:
            # Check if 'a' tag exists within the div
            a_tags = response.css(f'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element[data-wts-url="{link}"] li.elementor-icon-list-item a::attr(href)').getall()
            if a_tags:
                for a_tag in a_tags:
                    yield response.follow(a_tag, callback=self.parse_content, meta={'title': title})
            else:
                yield response.follow(link, callback=self.parse_content, meta={'title': title})

    def parse_content(self, response):
        item = FaculteFormationInitialInfo()
        item["title"] = response.meta['title']
        item["Formation"] = response.css('h2.elementor-heading-title::text').extract_first()
        item["Objectifs"]= response.css('div.eael-tabs-content div#objectifs--tab').xpath('string()').get().strip()
        item["Programme"] = response.css('div.eael-tabs-content div#programme-tab').xpath('string()').get().strip()
        coordinator_raw = response.css('div.eael-tabs-content div#coordinateur-tab').xpath('string()').get().strip()

        # Splitting the coordinator information into parts
        parts = coordinator_raw.split(':')

        # Extracting relevant information
        item["coordinator_name"] = parts[1].strip() if len(parts) > 1 else None
        item["coordinator_email"] = parts[2].strip() if len(parts) > 2 else None

        yield item
