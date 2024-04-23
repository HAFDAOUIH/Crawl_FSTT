import scrapy


class EquipesRechercheSpider(scrapy.Spider):
    name = "equipes_recherche"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/equipes-de-recherche/"]

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        div_links = response.css(
            'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element::attr(data-wts-url)').getall()
        for link in div_links:
            yield response.follow(link, callback=self.parse_content, meta={'title': title})

        # Extract links from a tag if present
        for link in div_links:
            a_tags = response.css(
                f'div.has_eae_slider.elementor-column.elementor-col-100.elementor-top-column.elementor-element[data-wts-url="{link}"] a::attr(href)').getall()
            for a_tag in a_tags:
                yield response.follow(a_tag, callback=self.parse_content, meta={'title': title})


    def parse_content(self, response):
        title = response.meta['title']

        # Extract name of Lab
        laboratoire = response.css('h2.elementor-heading-title::text').extract_first()

        # Extract nom Directeur du lab
        directeur_infos = response.css('div#elementor-tab-content-1671').xpath('string()').get()

        # Extract axes de recherche
        if response.css('div#elementor-tab-content-1672 strong'):
            axes_recherche = response.css('div#elementor-tab-content-1672').xpath('.//strong').xpath(
                'string()').getall()
        else:
            axes_recherche = response.css('div#elementor-tab-content-1672 ul li::text').getall()
        # Extract projets de recherche
        projets_recherche_link = response.css('div#elementor-tab-content-1673 a::attr(href)').getall()

        # Extract these et habilitations soutenues
        these_habil_soutenues_link = response.css('div#elementor-tab-content-1674 a::attr(href)').getall()

        prod_scientifique = response.css('div#elementor-tab-content-1675 a::attr(href)').getall()

        rows = response.xpath('//table[@class="blueTable"]/tbody/tr[position() > 1]')

        membres = []

        for row in rows:
            # Extract data from each row
            nom = row.xpath('td[1]/text()').get()
            prenom = row.xpath('td[2]/em/text()').get()
            email = row.xpath('td[3]/text()').get()

            # Create an item and populate its fields
            membre = {
                'nom': nom,
                'prenom': prenom,
                'email': email
            }
            membres.append(membre)


        yield {
            'Title': title,
            'Nom Laboratoire': laboratoire,
            'Infos sur Directeur': directeur_infos,
            'Axes de Recherche': axes_recherche,
            'Projets de Recherche': projets_recherche_link,
            'Theses et Habilitations soutenues': these_habil_soutenues_link,
            'Production Scientifique': prod_scientifique,
            'Membres': membres
        }