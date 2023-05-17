"""
Retrieving information from various news websites of South Africa
and creating a dataset containing title, url, and date.
"""
from datetime import datetime
import scrapy


class SANewsSpider(scrapy.Spider):
    """
    Spider for crawling and scraping data from sa news website.
    """
    name = 'sa_news'
    start_urls = ["https://www.sanews.gov.za/south-africa"]

    def parse(self, response, **kwargs):
        # we are using re:test method to specify and test our regular expression
        # on the class attribute div
        articles = response.xpath('//div[re:test(@class, "^views-row views-row-\d+ \
views-row-(odd|even).*$")]')[:15]

        for article in articles:
            date = article.css('div div div.field.field-name-post-date.field-type-ds.\
field-label-hidden div div::text').get()
            yield {
                'title': article.css('h2 a::text').get(),
                'date': date,
                'url': "https://www.sanews.gov.za" + article.css('h2 a').attrib['href']
            }

        if datetime.strptime(date, "%d %b %Y") > datetime(2022, 2, 24):
            next_page = "https://www.sanews.gov.za" + response.css('li.pager-next a').attrib['href']
            yield response.follow(next_page, callback=self.parse)
