import scrapy


class EspaceEtudiantBiblioSpider(scrapy.Spider):
    name = 'espace-etudiant-biblio'
    start_urls = ['https://fstt.ac.ma/Portail2023/la-bibliotheque-numerique-cairn-sciences-et-techniques-est-a-votre-service/']

    def parse(self, response):
        title_biblio = response.css('h2.elementor-heading-title::text').extract_first()
        info_biblio = response.css('div.elementor-element-populated div.elementor-widget-container p').xpath('string()').extract()
        yield {
            'BIBLIOTHÈQUE ': title_biblio,
            'Les informations de BIBLIOTHÈQUE ': info_biblio
        }
        print(title_biblio, info_biblio,"################################################\n")
