# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FishyItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    scientific_name = scrapy.Field()
    size = scrapy.Field()
    difficulty = scrapy.Field()
    min_tank_size = scrapy.Field()
    specific_gravity = scrapy.Field()
    ph = scrapy.Field()
    temperature = scrapy.Field()
    water_hardness = scrapy.Field()
    stocking_ratio = scrapy.Field()
    diet = scrapy.Field()
    life_span = scrapy.Field()
    origin =  scrapy.Field()
    family = scrapy.Field()
 
