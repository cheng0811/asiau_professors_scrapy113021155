import scrapy


class AsiauSpiderSpider(scrapy.Spider):
    name = "asiau_spider"
    allowed_domains = ["csie.asia.edu.tw"]
    start_urls = ["https://csie.asia.edu.tw"]

    def parse(self, response):
        pass
