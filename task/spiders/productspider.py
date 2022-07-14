import scrapy.spiders as spiders
from scrapy_selenium import SeleniumRequest
from ..items import ProductItem


class productSpider(spiders.CrawlSpider):
    name = 'productspider'

    def start_requests(self):
        yield SeleniumRequest(
            url="https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=99",
            wait_time=3,
            screenshot=False,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response, **kwargs):
        product_name = response.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[1]/h1/text()').get()
        product_color = response.xpath('//*[@id="app"]/main/div/div[3]/div[2]/div[2]/span/text()').get()
        product_price = response.xpath('//*[@id="app"]/main/div/div[3]/div[1]/div[2]/span[4]/text()').get()
        product_price = float(product_price.strip("£"))
        product_sizes = response.css('span.size-unavailable::attr(data-size)').getall()

        item = ProductItem()
        item["name"] = product_name
        item["price"] = product_price
        item["color"] = product_color
        item["size"] = product_sizes
        yield item
