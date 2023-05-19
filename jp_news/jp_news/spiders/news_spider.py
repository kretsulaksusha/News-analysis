import scrapy


class JpSpider(scrapy.Spider):
    """
    Spider for crawling and scraping data from japantime website.
    """
    name = 'jp'
    start_urls = ['https://www.japantimes.co.jp/news/world/page/1/']

    def start_requests(self):
        for i in range(1, 259):
            yield scrapy.Request(url=f'https://www.japantimes.co.jp/news/world/page/{i}/', callback=self.parse)

    def parse(self, response, **kwargs):
        """
        Parse response from website.
        """
        for article in  response.css('div.content_col'):
            yield {
                'title': article.css('hgroup p a::text').get(),
                'date': article.css('span.right.date::text').get(),
                'text': article.css('p::text').get().strip()
            }
