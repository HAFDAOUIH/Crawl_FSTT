import scrapy


class FormationContinueInformationsSpider(scrapy.Spider):
    name = 'FORMATION_CONTINUE_informations'
    start_urls = ['http://formation-continue.ma/index.php/formation-continue/dcess/',
                  'http://formation-continue.ma/index.php/formation-continue/dca']

    def parse(self, response):
        links = response.css('span.lead a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_content)
    def parse_content(self, response):
        Formation = response.css('h3.ja-masshead-title span::text').get()
        Filiere = response.css('div.SPDetailEntry h1::text').get()
        Responsable_raw = response.css('div.field_responsable').xpath('string()').get().strip()
        Responsable = Responsable_raw.split(':')
        Responsable = Responsable[1].replace('\n', '').strip()
        Objectif = response.xpath('//label[@for="Objectif de la formation"]/following-sibling::div[@class="contenu"]').xpath('string()').get().replace('\n', '').replace('\r', '').replace('\xa0', '').strip()
        Public_concerne = response.xpath('//label[@for="Public concerné"]/following-sibling::div[@class="contenu"]').xpath('string()').get().replace('\n', '').replace('\r', '').replace('\xa0', '').strip()
        debouche = response.xpath('//label[@for="Débouchés"]/following-sibling::div[@class="contenu"]').xpath('string()').extract()


        yield {
            print('Fomation: ',Formation),
            print('Filiere :', Filiere),
            print('Responsable :', Responsable),
            print('Objectif de la formation :', Objectif),
            print('Public concerné :', Public_concerne),
            print('Débouchés :', debouche)
        }



