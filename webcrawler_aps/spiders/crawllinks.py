from turtle import title
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
import re


class someSpider(CrawlSpider):
    name = 'linkscrawl'
    item = []
    start_urls = ['https://myanimelist.net/profile/LucasVaz97']

    # this rule follow all the links extrated from LinkExtractor and call parse_obj method
    rules = (Rule(LinkExtractor(), callback="parse_obj", follow=True),
             )

    # get the response link from someSpider removes images and store domain url and content
    def parse_obj(self, response):
        item = response.url
        parsed_uri = urlparse(response.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
        data = response.body.decode("utf-8")
        clean_data = re.sub("(<img.*?>)", "", data, 0,
                            re.IGNORECASE | re.DOTALL | re.MULTILINE)
        yield {
            "domain": domain,
            "url": item,
            "content": clean_data
        }
