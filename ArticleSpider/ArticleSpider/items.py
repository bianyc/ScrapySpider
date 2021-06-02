# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EbRunArticleItem(scrapy.Item):
    """亿邦"""
    img_url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    media = scrapy.Field()
    pubdate = scrapy.Field()
    tag = scrapy.Field()
    content = scrapy.Field()
