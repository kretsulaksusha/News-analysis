import scrapy

class NewsDANSpider(scrapy.Spider):
    name = "news_dan"
    start_urls = ['https://dan-news.ru/world/']

    def start_requests(self):
        for page in range(1, 280):  # Start from the second page
            url = f'https://dan-news.ru/world/?p={page}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # div = response.css("div.news-item.news-item--list")
        # body_div = div.css("div.news-item__body")
        # titles = body_div.css('div.news-item__title a::text').getall()
        # for title in titles:
        #     yield {
        #         "title": title.strip(),
        #         # 'date': response.css('div.news-item__meta div.news-item__date time::text').get().strip()
        #     }
        for div in response.css('div.news-item__body'):
            title = div.css('div.news-item__title a::text').get()
            date = div.css('div.news-item__meta div.news-item__date time::text').get()
            yield {
                "title": title.strip() if title else None,
                'date': date.strip() if date else None,
            }
