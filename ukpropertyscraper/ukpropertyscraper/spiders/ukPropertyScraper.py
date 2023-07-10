import scrapy


class UkpropertyscraperSpider(scrapy.Spider):
    name = 'ukPropertyScraper'
    allowed_domains = ['www.onthemarket.com']
    start_urls = ['http://www.onthemarket.com/']

    def parse(self, response):
        pass
