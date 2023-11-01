import scrapy


class GlassdorSpider(scrapy.Spider):
    name = "glassdor"
    allowed_domains = ["glassdoor.com.br"]
    start_urls = ["https://glassdoor.com.br"]

    def parse(self, response):
        pass
