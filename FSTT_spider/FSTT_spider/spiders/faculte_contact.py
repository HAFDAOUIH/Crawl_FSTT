import scrapy


class FaculteContactSpider(scrapy.Spider):
    name = "faculte_contact"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/contact/"]

    def parse(self, response):
        # Extracting the items
        items_elements = response.css('div[data-id="d03fd3c"]').xpath('string()').extract()
        items = ' '.join(items_elements).strip().replace('\t', '').replace('\xA0', '')

        localisation = None
        num = None
        fax = None
        email = None
        for line in items.split('\n'):
            if 'Tanger' in line:
                localisation = line.split('\n')[0].strip()
            elif '55' in line:
                num = line.split('\n')[0].strip()
            elif '53' in line:
                fax = line.split('\n')[0].strip()
            elif 'fstt' in line:
                email = line.split('\n')[0].strip()
        yield{
            'localisation: ': localisation ,
            'numero telephone: ': num,
            'fax: ': fax,
            'email: ': email
        }