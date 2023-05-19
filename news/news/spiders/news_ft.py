import scrapy


class NewsFTSpider(scrapy.Spider):
    name = "news_ft"
    urls_dct = {'2022-02-28': 'https://web.archive.org/web/20220227233905/https://www.ft.com/world',
                '2022-03-09': 'https://web.archive.org/web/20220306115846/https://www.ft.com/world',
                '2022-04-15': 'https://web.archive.org/web/20220415182232/https://www.ft.com/world',
                '2022-07-14': 'https://web.archive.org/web/20220714002245/https://www.ft.com/world',
                '2022-09-08': 'https://web.archive.org/web/20220908201457/https://www.ft.com/world',
                '2022-09-11': 'https://web.archive.org/web/20220911060914/https://www.ft.com/world',
                '2022-11-11': 'https://web.archive.org/web/20221111200310/https://www.ft.com/world',
                '2023-01-16': 'https://web.archive.org/web/20230111162834/https://www.ft.com/world',
                '2023-05-18': "https://www.ft.com/world"}

    def start_requests(self):
        for url in self.urls_dct.keys():
            yield scrapy.Request(url=self.urls_dct[url], callback=self.parse, meta={'date': url})


    def parse(self, response):
        for article in response.css("a.js-teaser-heading-link::text").getall():
            yield {
                "title": article.strip(),
                'date': response.meta['date']
            }
