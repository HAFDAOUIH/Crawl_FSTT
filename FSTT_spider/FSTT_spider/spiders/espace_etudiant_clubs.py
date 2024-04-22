import scrapy


class EspaceEtudiantClubsSpider(scrapy.Spider):
    name = 'espace-etudiant-clubs'
    start_urls = ['https://fstt.ac.ma/Portail2023/clubs//']

    def parse(self, response):
        links = response.css('div.has_eae_slider.elementor-column.elementor-col-50::attr(data-wts-url)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_content)
    def parse_content(self, response):
        title_club = response.css('h2.elementor-heading-title::text').extract_first()
        info_club = response.css('div.elementor-element-populated div.elementor-widget-container p').xpath('string()').extract()
        yield {
            'Club :': title_club,
            'Les informations de Club': info_club
        }
        print(title_club, info_club,"################################################\n")


