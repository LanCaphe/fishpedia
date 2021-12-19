import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AquariumFishingSpider(CrawlSpider):
    name = 'aquarium_fishing'
    allowed_domains = ['www.theaquariumwiki.com']
    start_urls = ['http://www.theaquariumwiki.com/wiki/Category:Fish_-_Common_names_(Freshwater)']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='(//div[@id="mw-pages"])[1]/a'), follow = True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class= 'mw-category-group']//a[@class='mw-redirect']"), callback = 'parse_item', follow = True)
        )
    

    def parse_item(self, response):
        item = {}
        item['name'] = response.xpath('//h1/text()').get()
        item['scientific name'] = response.xpath('//h1/i/text()').get()
        item['size'] = response.xpath("(//div[@class='right'])[3]/p/text()").get()
        item['difficulty'] = response.xpath('//div[@class="right"]//a[1]/text()').get()
        item['min. Tank size'] = response.xpath("(//div[@class='right'])[2]/p/text()").get()
        item['specific gravity'] = response.xpath("(//div[@class='right'])[4]/p/text()").get()
        item['PH'] = response.xpath("(//div[@class='right'])[5]/p/text()").get()
        item['temperature'] = response.xpath("(//div[@class='right'])[6]/p/text()").get()
        item['water hardness'] = response.xpath("(//div[@class='right'])[7]/p/text()").get()
        item['stocking ratio'] = response.xpath("(//div[@class='right'])[8]/p/text()").get()
        item['diet'] = response.xpath("(//div[@class='right'])[10]//a/text()").get()
        item['life span'] = response.xpath("(//div[@class='right'])[11]//p/text()").get()
        item['origin'] = response.xpath("(//div[@class='right'])[12]//a/text()").get()
        item['family'] = response.xpath("(//div[@class='right'])[13]//p/text()").get()

        return item
