from ast import parse
from cgi import test
import scrapy
import re
import w3lib.html
from scrapy.linkextractors import LinkExtractor


class APSSpider(scrapy.Spider):
    name = "posts"

    def __init__(self):
        self.links = []
        self.start_urls = ["https://myanimelist.net/profile/LucasVaz97",
                           "https://myanimelist.net/anime/49721/Karakai_Jouzu_no_Takagi-san_3"]

    def parse(self, response):
        self.links.append(response.url)
        for href in response.css('a::attr(href)'):
            if href.get() is not None:
                yield response.follow(href.get(), callback=self.parse_data)

    def parse_data(self, response):
        data = response.body.decode("utf-8")
        clean_data = re.sub("(<img.*?>)", "", data, 0,
                            re.IGNORECASE | re.DOTALL | re.MULTILINE)
        yield {
            "url": response.url
        }
