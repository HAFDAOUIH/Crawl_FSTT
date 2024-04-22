import scrapy


class EspaceEntrepriseSpider(scrapy.Spider):
    name = 'espace-entreprise'
    allowed_domains = ['https://fstt.ac.ma/Portail2023/centre-dincubation-de-techno-entrepreneuriat-yabda/']
    start_urls = ['https://fstt.ac.ma/Portail2023/centre-dincubation-de-techno-entrepreneuriat-yabda//']

    def parse(self, response):
        title = response.css('h2.elementor-heading-title::text').extract_first()
        qui_sommes_nous = response.css('div#elementor-tab-content-2301').xpath('string()').extract()
        objectif = response.css('div#elementor-tab-content-2302').xpath('string()').extract()
        Comment = response.css('div#elementor-tab-content-2303').xpath('string()').extract()
        activite_service = response.css('div#elementor-tab-content-2304').xpath('string()').extract()
        yield {
            'title': title,
            'Qui sommes-nous ?': qui_sommes_nous,
            'Objectifs': objectif,
            'Comment ?' : Comment,
            'Activités et services': activite_service,
        }
        yield {
            print('title:', title),
            print('Qui sommes-nous :', qui_sommes_nous),
            print('Objectifs :', objectif),
            print('Comment :', Comment),
            print('Activités et services :', activite_service)
        }
