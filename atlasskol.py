import scrapy


class AtlasskolSpider(scrapy.Spider):
    name = "atlasskol"
    allowed_domains = ["atlasskolstvi.cz"]
    start_urls = ["https://atlasskolstvi.cz"]

    def parse(self, response):
        pass
