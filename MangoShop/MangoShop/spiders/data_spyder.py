import scrapy

class DataSpider(scrapy.Spider):
    name = "data"
    start_urls =['https://shop.mango.com/bg-en/women/skirts-midi/midi-satin-skirt_17042020.html?c=99',]

    def parse(self, response, **kwargs):
        name = response.css('.product-name::text').get()
        price = response.css('.product-sale::text').get()
        color = response.css('.colors-info-name::text').get()
        size = response.css('.selector-trigger::text').get()

        yield {
            'name': name,
            'price': price,
            'color': color,
            'size': size
               }