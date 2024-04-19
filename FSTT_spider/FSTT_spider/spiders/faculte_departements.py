import scrapy


class FaculteDepartementsSpider(scrapy.Spider):
    name = "faculte_departements"
    allowed_domains = ["fstt.ac.ma"]
    start_urls = ["https://fstt.ac.ma/Portail2023/les-departement/"]

    def parse(self, response):
        cta_contents = response.css('div.elementor-cta__content')

        for cta_content in cta_contents:
            # Extracting title (h3) and content (div)
            title = cta_content.css('h3.elementor-cta__title::text').get()
            content_elements = cta_content.css('div.elementor-cta__description').xpath('.//text()').getall()
            content = ' '.join(content_elements).strip()

            # Extracting chef and email from content
            chef = None
            email = None
            for line in content.split('\n'):
                if 'Chef' in line:
                    chef = line.split(':')[1].strip()
                elif 'Email' in line:
                    email = line.split(':')[1].strip()

            yield {
                'title': title.strip() if title else None,
                'chef': chef,
                'email': email
            }
