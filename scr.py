import scrapy


class ScrSpider(scrapy.Spider):
    name = "scr"
    allowed_domains = ["www.screener.in"]
    start_urls = ["https://www.screener.in/screens/355766/highest-return-in-1-year/?utm_source=email"]

    def parse(self, response):
        pass
