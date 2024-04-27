import scrapy
from ..items import FaculteConseilEtab


class FaculteConseiletabSpider(scrapy.Spider):
    name = "faculte_conseilEtab"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/conseil-de-letablissement/",
                  "https://fstt.ac.ma/Portail2023/commission-scientifique/",
                  "https://fstt.ac.ma/Portail2023/commission-recherche-scientifique-cooperation/",
                  "https://fstt.ac.ma/Portail2023/commission-pedagogique/",
                  "https://fstt.ac.ma/Portail2023/commission-activites-culturelles-et-sportives/",
                  "https://fstt.ac.ma/Portail2023/commission-suivi-du-budget/"
                  ]

    def parse(self, response):
        item = FaculteConseilEtab()
        item["Title"] = response.css('h2.elementor-heading-title::text').extract_first()
        brief_elements = response.css('div.elementor-widget-container div.elementor-text-editor').xpath('string()').extract()
        item["Brief"] = ' '.join(brief_elements).strip().replace('\n', '').replace('\t', '').replace('\xA0', ' ')

        table_rows = response.css('.eael-data-table tbody tr')
        for row in table_rows:
            # Extracting name and responsibility
            item["Name"] = row.css('.td-content::text').get()
            item["Responsabilite"] = row.css('.td-content::text').getall()[1]  # Assuming the second .td-content contains the responsibility

            yield item
