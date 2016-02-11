__author__ = 'casey'

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class CityPagesSpider(scrapy.Spider):

    name = 'citypages'

    start_url = 'http://www.citypages.com'

    # body = '<html><body><section>latestNews</section></body></html>'
    #
    # Selector(text=body).xpath('//section/text()').extract()


    def parse(self, response):
        print response.css('#latestNews')

    def parse_headline(self, response):
        pass