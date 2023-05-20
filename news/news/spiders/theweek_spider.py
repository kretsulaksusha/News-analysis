"""
Module for scraping information
"""

import scrapy

class TheweekSpider(scrapy.Spider):
    """
    Spider for scraping data from theweek.co.uk
    """
    name = "theweek"

    def start_requests(self):
        urls = [
            "https://www.theweek.co.uk/world-news",
            *[f"https://www.theweek.co.uk/world-news?page={i}" for i in range(1, 42)]
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Parses response from website
        """

        for article in response.css('.polaris__article-card--content'):
            yield {
                'header': article.css("h2.polaris__article-card--title span::text").get(),
                'date': article.css("span.polaris__date::text").get(),
            }
