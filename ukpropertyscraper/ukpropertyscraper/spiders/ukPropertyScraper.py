import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import json


class UkpropertyscraperSpider(scrapy.Spider):
    name = 'onTheMarketUKPropertyScraper'
    allowed_domains = ['www.onthemarket.com']
    start_urls = ['http://www.onthemarket.com/']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'onthemarket.csv',
        'LOG_FILE': 'onthemarket.log'
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://www.onthemarket.com/for-sale/property/london/'
        # https://www.onthemarket.com/for-sale/flats-apartments/goodge-street-station/?auction=false&max-bedrooms=3&max-price=500000&min-bedrooms=2&min-price=250000&retirement=false&shared-ownership=false&travel-duration=60&travel-type=public-transport
        for page in range(0, 4):
            next_page = url + '?page=' + str(page)
            yield scrapy.Request(url=next_page, headers=self.headers, callback=self.parse)    

    def parse(self, response):
        self.log('status: ' + str(response.status))
        # extract data
        for card in response.css('li.property-result'):
            items = {
            	'title': card.css('span.title').css('a::text').get(),
                'address': card.css('span.address').css('a::text').get(),
                'description': card.css('p.description::text').get(),
                'price': card.css('p.price-text').css('a::text').get().encode('ascii', 'ignore').decode('utf-8').strip(),
                'agency': card.css('p.marketed-by').css('a::text').get(),
                'phone': card.css('span.marketed-by-contact').css('strong::text').get(),
                'image_url': card.css('picture').css('img::attr(src)').get()
            }
            
            yield items

# run spider
process = CrawlerProcess()
process.crawl(Onthemarket)
process.start()
