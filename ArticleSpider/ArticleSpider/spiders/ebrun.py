import scrapy

from ArticleSpider.items import EbRunArticleItem


class EbrunSpider(scrapy.Spider):
    name = 'ebrun'
    allowed_domains = ['www.ebrun.com']
    start_urls = []

    for i in range(1, 2):
        url = "https://www.ebrun.com/information/retail/more/{}".format(i)
        start_urls.append(url)

    def parse(self, response):
        url_links = response.xpath('//div[@class="eb-main__tab-content__item"]/div[1]/a/@href').extract()
        img_url = response.xpath('//div[@class="eb-main__tab-content__item"]/div[1]/a/img/@src').extract()
        for a in range(len(url_links)):
            url = url_links[a]
            img = img_url[a]
            yield scrapy.Request(url, callback=self.article_details, meta={"img": img})

    def article_details(self, response):
        item = EbRunArticleItem()

        item["img_url"] = response.meta.get("img", "")
        item["title"] = response.xpath('//h1/text()').extract()[0]
        item["author"] = response.xpath('//p[@class="info"]/span[1]/text()').extract()[0].split("：")[1]
        item["media"] = response.xpath('//p[@class="info"]/span[2]/text()').extract()[0].split("：")[1]
        item["pubdate"] = response.xpath('//p[@class="date-time"]/text()').extract()[0]
        item["tag"] = " ".join(response.xpath('//dd/a/text()').extract())
        item["content"] = response.xpath('//div[@class="post-text"]').extract()[0]

        yield item
