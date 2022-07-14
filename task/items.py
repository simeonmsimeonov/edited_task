from scrapy import Item, Field


class ProductItem(Item):
    name = Field()
    price = Field()
    color = Field()
    size = Field()