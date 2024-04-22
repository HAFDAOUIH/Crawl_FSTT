import scrapy


class RechercheStructSpider(scrapy.Spider):
    name = "recherche_struct"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/laboratoires-de-recherche/",
                  "https://fstt.ac.ma/Portail2023/equipes-de-recherche/"]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        links = response.css(
            'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element::attr(data-wts-url)').getall()

        for link in links:
            # Check if 'a' tag exists within the div
            a_tags = response.css(
                f'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element[data-wts-url="{link}"] li.elementor-icon-list-item a::attr(href)').getall()
            if a_tags:
                for a_tag in a_tags:
                    yield response.follow(a_tag, callback=self.parse_content, meta={'title': title})
            else:
                yield response.follow(link, callback=self.parse_content, meta={'title': title})

    def parse_content(self, response):
        title = response.meta['title']
        Laboratoire = response.css('h2.elementor-heading-title::text').extract_first()

        directeur_div = response.css('div#elementor-tab-content-1671').xpath('string()').get().replace('\xa0', ' ')
        directeur_infos = directeur_div.xpath('.//p')

        equipes_div = response.css('div#elementor-tab-content-1672')
        equipes_recherche = equipes_div.xpath('.//strong')

        axes_div = response.css('div#elementor-tab-content-1673')
        axes_recherche = axes_div.xpath('.//strong')

        projets_recherche_link = response.css('div#elementor-tab-content-1674 a::attr(href)').get()

        Programme = response.css('div.eael-tabs-content div#programme-tab').xpath('string()').get().strip()
        coordinator_raw = response.css('div.eael-tabs-content div#coordinateur-tab').xpath('string()').get().strip()

        # Splitting the coordinator information into parts
        parts = coordinator_raw.split(':')

        # Extracting relevant information
        coordinator_name = parts[1].strip() if len(parts) > 1 else None
        coordinator_email = parts[2].strip() if len(parts) > 2 else None

        yield {
            'Title': title,
            'Formation': Formation,
            'OBJECTIFS': Objectifs,
            'PROGRAMME': Programme,
            'Coordinateur pédagogique': coordinator_name,
            'Coordinator email': coordinator_email
        }