"""
Retrieving information from various news websites of South Africa
and creating a dataset containing title, url, and date.
"""
import scrapy


class News24Spider(scrapy.Spider):
    """
    Spider for crawling and scraping data from news 24 website.
    """
    name = 'news_24'
    start_urls = ['https://www.news24.com/api/article/loadmore/news24/_SmallThumbItem/_\
/mobile/false/homepage/false/page/1/1106/news24/politics']

    def parse(self, response, **kwargs):
        yield response.json()
