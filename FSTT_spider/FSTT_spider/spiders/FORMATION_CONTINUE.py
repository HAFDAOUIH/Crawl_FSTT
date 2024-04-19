import scrapy
import re

class FormationContinueSpider(scrapy.Spider):
    name = "FORMATION-CONTINUE"
    allowed_domains = ["formation-continue.ma"]
    start_urls = ["http://formation-continue.ma/"]

    def parse(self, response):
        title = response.css('h3.ja-masshead-title::text').extract_first()
        content = response.css('div.item-page').xpath('string()').get().strip()
        # Remove HTML tags and unwanted characters using regex
        cleaned_content = re.sub(r'<[^>]*>', '', content)
        cleaned_content = re.sub(r'\xa0', ' ', cleaned_content)  # Replace non-breaking spaces with regular spaces
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content)  # Remove extra whitespaces

        yield {
            print("title :" ,title),
            print("content :" ,cleaned_content)
        }