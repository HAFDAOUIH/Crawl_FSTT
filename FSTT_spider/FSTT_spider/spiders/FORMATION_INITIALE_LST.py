import scrapy


class FormationInitialeLstSpider(scrapy.Spider):
    name = "FORMATION-INITIALE-LST"
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
            yield response.follow(link, callback=self.parse_content, meta={'title': title})

    def parse_content(self, response):
        title = response.meta['title']
        Formation = response.css('h2.elementor-heading-title::text').extract_first()
        Objectifs = response.css('div.eael-tabs-content div#objectifs--tab').xpath('string()').get().strip()
        Programme = response.css('div.eael-tabs-content div#programme-tab').xpath('string()').get().strip()
        coordinator_raw = response.css('div.eael-tabs-content div#coordinateur-tab').xpath('string()').get().strip()


        # Splitting the coordinator information into parts
        parts = coordinator_raw.split(':')

        # Extracting relevant information
        coordinator_name = parts[1].strip() if len(parts) > 1 else None
        coordinator_email = parts[2].strip() if len(parts) > 2 else None
        Competences_Debouches = response.css('div.eael-tabs-content div#competences-visees-et-debouches-tab').xpath('string()').get().strip()

        yield {
            'title': title,
            'Formation': Formation,
            'OBJECTIFS': Objectifs,
            'PROGRAMME': Programme,
            'Coordinateur pédagogique': coordinator_name,
            'Coordinator email': coordinator_email,
            'COMPETENCES VISEES ET DEBOUCHES': Competences_Debouches
        }
