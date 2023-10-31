import scrapy

from src.items import SchoolItem
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from loguru import logger


class AtlasskolSpider(scrapy.Spider):
    name = "atlasskol"
    allowed_domains = ["atlasskolstvi.cz"]
    start_urls = ["https://atlasskolstvi.cz/stredni-skoly/"]

    #this link extractor will find all links on the page
    page_link_extractor = LinkExtractor(restrict_css='.pagination .next')

    #this link extractor will find all links to other pages
    detail_link_extractor = LinkExtractor(restrict_css='.schoollist li a')
    
    def parse(self, response):
        """
        Default parsing function for response object, all responses will be passed here first
        """
        for link in self.page_link_extractor.extract_links(response):
            logger.info(f'Found a next page link: {link.url}')
            yield Request(link.url, callback=self.parse)

        for link in self.detail_link_extractor.extract_links(response):
            logger.info(f'Found a school link: {link.url}')
            yield Request(link.url, callback=self.parse_detail)

    def parse_detail(self, response):
        """
        Parsing function for detail page    
        """
        i = SchoolItem()

        i['name'] = response.css('div.maininfo strong.title::text').get()

        i['identifier'] = response.xpath('//strong[text()="IČ:"]/following-sibling::text()[1]').get()
        i['address'] = response.css('div.maininfo ul li.address::text').get()
        i['email'] = response.css('div.maininfo ul li.mail a::text').get()
        i['phone'] = response.css('div.maininfo ul li.phone a::text').get()
        i['website'] = response.css('div.maininfo ul li.www a::text').get()

        yield i

